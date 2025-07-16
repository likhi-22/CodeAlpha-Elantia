🛒 Elantia – E-commerce Web Application

Elantia is a full-featured e-commerce web application built using the Django web framework. It is designed to deliver a smooth, secure, and user-friendly online shopping experience. Users can browse a catalog of products, manage their shopping cart, and place orders, all within a clean and responsive interface.
 🔑 Features

* User registration, login, and profile management
* Product catalog with images and detailed descriptions
* Shopping cart with add/remove/update functionality
* Order placement and order history tracking
* Modular Django app structure for maintainability and scalability
* Responsive design with Django templates and static assets
* Secure session and user authentication handling

 🧰 Technologies Used

* **Backend**: Python, Django Web Framework
* **Database**: SQLite
* **Frontend**: HTML, CSS, JavaScript
* **Templating**: Django Templates
* **Static Files**: Managed for images, CSS, and JS
 📁 Project Structure

ecommerce/       # Main Django project settings and configuration
│
├── users/       # Handles user accounts and core e-commerce logic
├── static/      # Static assets (CSS, JavaScript, product images)
├── templates/   # HTML templates for all frontend pages
├── db.sqlite3   # SQLite database file
└── manage.py    # Django management script

🚀 Getting Started

1. Clone the repository

     ``` bash
   git clone https://github.com/your-username/elantia.git
   cd elantia
   

2. Install dependencies
   Make sure Python and Django are installed. You can install Django using pip:

     ``` bash
   pip install django


3. **Run database migrations**

   ```bash
   python manage.py migrate
   ```

4. **Start the development server**

   ```bash
   python manage.py runserver
   ```

5. **Visit the app**
   Open your browser and go to:
   [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

📜 License

This project is developed for educational purposes only.

