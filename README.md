# 🛍️ Online Clothing Store

This is a web-based e-commerce platform built with **Flask** and **MySQL** that allows users to browse, register, log in, add clothing items to a cart, and place orders. There is also an admin dashboard for managing users and products.

---

## 📦 Features

### 🧍‍♀️ User Authentication
- Users can **register** and **log in** securely.
- Session-based login system to manage access to profile and cart.

### 📄 Profile Page
- Logged-in users can view their personal details and order history.

### 🛒 Shopping Cart
- Add products to cart from men's and women's categories.
- View items in cart with calculated total price.
- Quantity can be specified for each item.

### 🧾 Order System
- Orders are stored in the database and associated with the user's ID.
- Order history shown in the profile page.

### 🧑‍💼 Admin Panel
- Admins can log in using a separate login page.
- Admin dashboard allows viewing and managing products and users.

### 🧮 Database Integration
- **MySQL** used for all persistent data (users, products, orders, admins).
- Multiple tables: `customers`, `products`, `orders`, `admins`.

### 🖼️ Product Catalog
- Products are separated by gender (`men`, `women`).
- Images and descriptions loaded dynamically from the database.

### 📄 Footer + Popups
- Footer includes links (e.g., **Terms and Conditions**) that trigger popup windows.

---

## 🗃️ Database Structure (Simplified)

```sql
-- Customers Table
CREATE TABLE customers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    email VARCHAR(255) UNIQUE,
    password VARCHAR(255)
);

-- Admins Table
CREATE TABLE admins (
    id INT PRIMARY KEY AUTO_INCREMENT,
    admin_name VARCHAR(255),
    admin_password VARCHAR(255)
);

-- Products Table
CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    price DECIMAL(10, 2),
    image_url VARCHAR(255),
    gender ENUM('men', 'women')
);

-- Orders Table
CREATE TABLE orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    product_id INT,
    quantity INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
