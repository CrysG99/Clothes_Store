from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql #type: ignore
from flask import session

app = Flask(__name__)
app.secret_key = 'storekey'
# secret key brukes for session

# Database informasjonen, følger med ip adressen, brukernavnet, passordet og databasen på raspberry pi-en
db_config = {
    'host': '10.2.3.123',
    'user': 'jonathan',
    'password': 'jonathan2007',
    'database': 'clothes_store'
}

@app.route('/profile/<name>')
def profile(name):
    print(session)
    if 'user_id' not in session:
        flash("You need to be logged in to access your profile", "danger")
        return redirect(url_for('login'))
    
    user_id = session['user_id']


    try:
        conn = pymysql.connect(**db_config)
        cur = conn.cursor(pymysql.cursors.DictCursor)

        user_query = "SELECT id, name, email FROM customers WHERE name = %s"
        cur.execute(user_query, (name,))
        user = cur.fetchone()

        if not user:
            flash('User not found', 'danger')
            return redirect(url_for('home'))
        # If the user doesnt exist it uses this code

        cur.execute("SELECT * FROM orders WHERE customer_id = %s ORDER BY created_at DESC", (user_id,))
        orders = cur.fetchall()

        cur.close()
        conn.close()

        return render_template('profile.html', user=user, orders=orders)

    except Exception as e:
        flash(f"Error loading profile: {e}", 'danger')
        return redirect('/')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

    try:
        conn = pymysql.connect(**db_config)
        cur = conn.cursor()
        cur.execute("SELECT * FROM customers WHERE name = %s AND password = %s", (name, password))
        user = cur.fetchone()
        cur.close()
        conn.close()

        if user:
            session['user_id'] = user[0]
            session['name'] = user[1]
            flash('Logged in successfully! Velkommen {user[1]}', 'success')
            return redirect(url_for('profile/<name>'))
        else:
            flash('Invalid name or password', 'danger')
            return redirect(url_for('login'))
        
    except Exception as e:
        flash(f"Error logging in: {e}", 'danger')

    return render_template('login.html')


# admin stuff

@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        admin_name = request.form['admin_name']
        admin_password = request.form['admin_password']

        try:
            conn = pymysql.connect(**db_config)
            cur = conn.cursor()

            query = "SELECT * FROM admins WHERE admin_name = %s AND admin_password = %s"
            cur.execute(query, (admin_name, admin_password))
            admin = cur.fetchone()
            cur.close()
            conn.close()

            if admin:
                session['admin_id'] = admin[0]
                session['admin_name'] = admin[1]
                flash(f'Admin login successful! Welcome {admin[1]}', 'success')
                print("Hello admin!")
                return redirect(url_for('admin_dashboard'))
            else:
                flash('Invalid admin name or password', 'danger')
                return redirect(url_for('admin_login'))
        except Exception as e:
            flash(f"Error during admin login: {e}", 'danger')
            print(f"Login error: {e}")
            return redirect(url_for('admin_login'))

    return render_template('admin_login.html')

@app.route('/admin_dashboard')
def admin_dashboard():
    if 'admin_id' not in session:
        flash('You must be logged in as an admin to access this page', 'danger')
        return redirect(url_for('admin_login'))
    
    return render_template('admin_dashboard.html', admin_name=session.get('admin_name'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        try:
            conn = pymysql.connect(**db_config)
            cursor = conn.cursor()
            query = "INSERT INTO customers (name, email, password) VALUES (%s, %s, %s)"
            cursor.execute(query, (name, email, password))
            conn.commit()
            cursor.close()
            conn.close()
            return redirect(url_for('login'))
        except Exception as e:
            flash('Email already exists or another error occurred.', 'danger')
            print(f"Error: {e}")
            return redirect(url_for('register'))
        


@app.route('/admin_submit', methods=['GET', 'POST'])
def admin_submit():
    if request.method == 'POST':
        admin_name = request.form['admin_name']
        admin_password = request.form['admin_password']

        try:
            conn = pymysql.connect(**db_config)
            cursor = conn.cursor()
            query = "INSERT INTO admins (admin_name, admin_password) VALUES (%s, %s)"
            cursor.execute(query, (admin_name, admin_password))
            conn.commit()
            cursor.close()
            conn.close()
            flash('Admin registered successfully!', 'success')
            return redirect('/admin_login')
        except Exception as e:
            flash('An error occurred while registering admin', 'danger')
            print(f"error: {e}")
            return redirect(url_for('admin_login'))



@app.route('/women')
def women():
    conn = pymysql.connect(**db_config)
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("SELECT * FROM products WHERE gender = 'women'")
    products = cur.fetchall()
    cur.close()
    conn.close
    return render_template('women.html', products=products)

@app.route('/men')
def men():
    conn = pymysql.connect(**db_config)
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("SELECT * FROM products WHERE gender = 'men'")
    products = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('men.html', products=products)

@app.route('/cart')
def cart():
    cart_items = session.get('cart', [])
    total_price = sum(float(item['price']) * int(item['quantity']) for item in cart_items)
    return render_template('cart.html', cart_items=cart_items, total_price = total_price)

@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    quantity = int(request.form.get('quantity', 1))

    try:

        conn = pymysql.connect(**db_config)
        cur = conn.cursor()
        cur.execute("SELECT id, name, price FROM products WHERE id = %s", (product_id,))
        product = cur.fetchone()
        cur.close()
        conn.close()

        if product:
            item = {
                'id': product[0],
                'name': product[1],
                'price': product[2],
                'quantity': quantity
            }

        if 'cart' not in session:
            session['cart'] = []

            session['cart'].append(item)
            session.modified = True
            flash(f"Added {item['name']} to cart.", "success")
        else:
            flash("Product not found.", "danger")
    
    except Exception as e:
        flash(f"Error adding to cart: {e}", "danger")


    return redirect(url_for('cart'))


@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Successfully logged out!', 'info')
    return redirect(url_for('home'))

if __name__== '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)