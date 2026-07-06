# 📝 Jotly — Django Notes Application

Jotly is a full-stack notes application built with Django where users can securely create, manage, and organize their personal notes. It includes authentication, search functionality, and a clean UI designed for productivity.

---

## 🚀 Live Demo
https://jotly-gus5.onrender.com

---

## ✨ Features

- 🔐 User authentication (Sign up / Login / Logout)
- 📝 Create, edit, and delete notes
- 📌 Pin important notes
- 🔍 Search notes by title or content
- 👤 User-specific notes (each user sees only their own data)
- 📄 Dedicated note detail page
- 📱 Clean and responsive UI

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Django Templates
- **Database:** PostgreSQL (Neon)
- **Deployment:** Render
- **Auth:** Django built-in authentication system

---

## 🧠 What I Learned

While building Jotly, I worked through:

- Django models, views, templates architecture
- Authentication and session handling
- Query filtering and search logic
- PostgreSQL integration with Django
- Environment variables and secure config handling
- Static file management in production
- Deployment debugging (Render + Neon DB)

---

## 📂 Project Structure


notesProject/
│
├── notes/ # Main app
│ ├── templates/
│ ├── static/
│ ├── models.py
│ ├── views.py
│ └── urls.py
│
├── notesProject/ # Project settings
│ ├── settings.py
│ ├── wsgi.py
│
├── requirements.txt
├── build.sh
└── manage.py


---

## 🔮 Future Improvements

- Rich text editor for notes
- Tags / categories
- Dark mode
- Note sharing
- Mobile-first UI improvements
- Search highlight feature
