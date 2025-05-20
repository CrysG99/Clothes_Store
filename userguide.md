# How to run it yourself
## Requirements

- Python 3.x
- Flask
- PyMySQL
- MySQL server
  
## Setup Instructions
1. Clone the project
```bash
git clone https://github.com/CrysG99/Clothes_Store.git
```

2. Install dependancies
```bash
pip install flask pymysql
```

3. Set up the MySQL database
- Create a MySQL database called `clothes_store`
- Run the SQL schema from above (or from a provided `sql` file)
4. Update database config in `app.py`
```python
db_config = {
    'host': 'your_host (10.2.4.9)',
    'user': 'your_mysql/mariadb_user',
    'password': 'your_mysql/mariadb_password',
    'database': 'clothes_store'
}
```
5. Run the app
```bash
python app.py
```
6. Visit in browser
```arduino
http://localhost:8080
```

## Image hosting notes

Make sure product images are stored in `/static/img/` and their filenames are correctly referenced in the `image_url` column of the database.

### Contact

Made by CrysG [Jonathan]. For questions or contributions, please open an issue or reach out to me! Thanks for checking out my stuff.