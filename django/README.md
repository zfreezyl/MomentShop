# Moment Shop

A fully functional watch e-commerce store built with Django. Registration, login, catalog, shopping cart, admin panel — everything works out of the box.

## 🛠 Tech Stack

- **Backend:** Python 3.x, Django 6.0
- **Database:** MySQL / SQLite
- **Frontend:** HTML, CSS, Bootstrap 5
- **Authentication:** Built-in Django auth system

## 🚀 Features

- Homepage with latest products
- Catalog with category filtering
- Product detail page with description and price
- Shopping cart: add, remove, update quantity, clear
- User registration and login
- About and Social Media pages
- Admin panel for full product management
- Custom space-themed design with animated stars

---

## 📦 Setup & Installation

### 1. Clone the repository

git clone https://github.com/zfreezyl/MomentShop.git
cd MomentShop

### 2. Create a virtual environment

**Windows:**
python -m venv .venv
.venv\Scripts\activate

**Linux / macOS:**
python3 -m venv .venv
source .venv/bin/activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Configure the database

Open `onlineshop/settings.py` and find the `DATABASES` section.

**For quick start (SQLite):**
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

**For MySQL:**
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'momentshop_db',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

### 5. Run migrations

python manage.py migrate

### 6. Create a superuser (for admin panel access)

python manage.py createsuperuser

You'll be prompted to enter:
- **Username** (e.g., `admin`)
- **Email** (optional — press Enter to skip)
- **Password** (create one and remember it)
- **Password confirmation**

### 7. Start the server

python manage.py runserver

Open your browser and go to: **http://127.0.0.1:8000**

---

## 🛒 How to Add Products

### Step 1: Log into the admin panel

Go to: **http://127.0.0.1:8000/admin**

Enter the username and password you created in step 6.

### Step 2: Create categories

In the left sidebar, click **"Categories"** → **"Add category"**

- **Name:** e.g., "Classic", "Sport", "Premium"
- **Slug:** auto-generated from the name
- Click **"Save"**

### Step 3: Add products

In the left sidebar, click **"Products"** → **"Add product"**

Fill in the fields:
- **Name:** name of the watch
- **Slug:** auto-generated
- **Description:** detailed product description
- **Price:** format like `199.99`
- **Category:** select from the ones you created
- **Image:** upload a product photo

Click **"Save"** — the product will appear in the store catalog.

---

## 👤 Author

zfreezyl, Full-Stack Developer

- GitHub: [github.com/zfreezyl](https://github.com/zfreezyl)
