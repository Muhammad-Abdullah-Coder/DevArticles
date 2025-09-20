# DevArticles 📝  

> ⚡ Previously known as **4ixsquad Solution**  
> 🎥 Watch the full project demo video here: [Project Video](https://drive.google.com/file/d/1w1TFIQF8vqY6Atv3rD78XVHiLHbe_jAj/view?usp=drive_link)  

---

## 📖 About the Project  

**DevArticles** is a Django-based web application where users can:  

- Sign up and log in  
- Write their own articles  
- Update or delete only their own articles  
- Comment on other users’ articles  

This project demonstrates **full-stack functionality** using Django’s backend and a clean frontend interface.  

---

## 🚀 Features  

- 🔑 User Authentication (Login, Signup, Logout)  
- 📝 Full CRUD for Articles (Create, Read, Update, Delete)  
- 🔒 Only the author can delete their own posts  
- 💬 Comment system for interaction  
- 🎨 Simple and responsive UI  

---

## ⚙️ Technologies Used  

- **Python 3**  
- **Django**  
- **SQLite** (default database)  
- **HTML, CSS, Bootstrap**  

---

## 📦 Installation  

Run this project locally in a few steps:  

```bash
# 1. Clone the repository
git clone https://github.com/Muhammad-Abdullah-Coder/DevArticles.git

# 2. Go inside the project
cd DevArticles

# 3. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate   # On Windows
# source venv/bin/activate   # On Mac/Linux

# 4. Install dependencies
pip install -r requirements.txt

# 5. Apply migrations
python manage.py migrate

# 6. Start the server
python manage.py runserver
