# Recipe Manager

## Overview
The **Recipe Manager** is a web application built with **Django** and **SQL** that allows users to perform **CRUD (Create, Read, Update, Delete) operations** on recipes. Users can add new recipes along with images and details, modify existing recipes, and delete unwanted ones.

## Features
- 📌 **Add new recipes** with images and details
- 📝 **Modify existing recipes**
- 🗑️ **Delete recipes**
- 🔍 **View all recipes in a list format**
- 🖼️ **Upload and display recipe images**
- 🛠️ **User-friendly interface** with Django templates

## Technologies Used
- **Backend:** Django (Python)
- **Database:** SQLite / PostgreSQL / MySQL
- **Frontend:** HTML, CSS, Bootstrap (for UI styling)
- **Storage:** Django Media Files for image uploads

## Installation & Setup

### Prerequisites:
- Python 3.9+
- Django installed (`pip install django`)
- SQLite (default) or any other SQL database

### Steps:
```sh
# Clone the repository
git clone https://github.com/eyekrish/Recipe-Manager.git
cd Recipe-Manager

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Create a superuser for admin panel
python manage.py createsuperuser

# Start the development server
python manage.py runserver
## Usage
- Open `http://127.0.0.1:8000` in your browser.
- Navigate to the application dashboard.
- View **real-time stock market data** from NEPSE.
- Analyze market trends using built-in **technical indicators**.
- Receive **Buy and Sell signals** based on trend analysis.
- Customize alerts for specific stocks or indicators.

## Roadmap
✅ Real-time stock data scraping  
✅ Basic technical indicator implementation  
🔜 User authentication and portfolio tracking  
🔜 Advanced AI-based stock predictions  
🔜 API integration for automated trading  

## Contributing
We welcome contributions from the community! To contribute:
1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Submit a pull request for review.


