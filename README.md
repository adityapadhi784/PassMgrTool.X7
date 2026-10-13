# 🔐 SecureKeyChain

> Flask-based password management tool with role-based access, bcrypt-hashed logins, and Fernet-encrypted credential storage. Built as a cybersecurity learning project.

![Python](https://img.shields.io/badge/python-3.13-blue)
![Flask](https://img.shields.io/badge/flask-3.1-lightgrey)
![Database](https://img.shields.io/badge/database-MySQL%20%7C%20SQLite-orange)
![Category](https://img.shields.io/badge/category-Cybersecurity-red)

---

## 📖 About

**SecureKeyChain** lets users register, log in, and store website credentials in a personal vault. Account passwords are hashed with **bcrypt**, and the credentials saved in the vault are encrypted with **Fernet** (from the `cryptography` library) before they reach the database. An admin role provides a separate dashboard for managing user accounts.

> ⚠️ This is an educational project. For real-world passwords, use an audited manager such as Bitwarden or KeePass. See [Security Considerations](#-security-considerations).

---

## ✨ Features

**For users**
- Register and log in with session management (Flask-Login)
- Add, view, update, and delete saved credentials (site name, username, password)
- Stored passwords are encrypted at rest and decrypted only when the owner requests them
- Personal dashboard

**For admins**
- Separate admin login and dashboard
- View, update, and delete user accounts
- Reset a user's password

**Security**
- bcrypt password hashing for account logins
- Fernet encryption (AES-128-CBC with HMAC authentication) for vault entries
- Role-based route protection (`admin` and `user`)
- Credentials are scoped to the owning user

---

## 🧰 Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask 3.1 |
| Auth | Flask-Login, Flask-Bcrypt |
| Encryption | `cryptography` (Fernet) |
| Database | MySQL (PyMySQL) or SQLite, via Flask-SQLAlchemy |
| Migrations | Flask-Migrate (Alembic) |
| Frontend | HTML, CSS, JavaScript (Jinja2 templates) |

---

## 📁 Project Structure

```
SecureKeyChain/
├── app.py                  # Flask app, routes, encryption helpers
├── models.py               # User model
├── create_admin.py         # Helper script to create an admin account
├── generate_secret_key.py  # Generates the Fernet encryption key
├── requirements.txt
├── database/
│   └── password.sql        # SQL schema (MySQL)
├── migrations/             # Alembic migration scripts
├── templates/              # Jinja2 HTML templates
│   └── includes/           # Header, navbar, footer partials
└── static/                 # CSS and JavaScript
    ├── css/
    └── js/
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/codewithchandan945/SecureKeyChain.git
cd SecureKeyChain
```

### 2. Create a virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # macOS / Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
pip install PyMySQL cryptography python-dotenv
```

### 4. Generate the encryption key
```bash
python generate_secret_key.py
```
This creates `secret.key`. **Back it up and never commit it.** Without this key, saved credentials cannot be decrypted.

### 5. Choose a database
In `app.py`, set `USE_MYSQL`:
- `False` uses SQLite and needs no setup. This is the easiest way to try the project.
- `True` uses MySQL. Create the database first (`database/password.sql`) and set your own connection string.

### 6. Apply migrations
```bash
flask db upgrade
```

### 7. Create an admin user
```bash
python create_admin.py
```

### 8. Run the app
```bash
python app.py
```
Open **http://127.0.0.1:5000** in your browser.

---

## 🗺️ Application Routes

| Route | Access | Purpose |
|-------|--------|---------|
| `/` | Public | Landing page |
| `/register` | Public | Create a user account |
| `/login` | Public | User login |
| `/admin_login` | Public | Admin login |
| `/dashboard` | Logged in | User or admin dashboard |
| `/add_credential` | User | Save a new credential |
| `/view_credentials` | User | List saved credentials |
| `/update_credential/<id>` | User | Edit a credential |
| `/delete_credential/<id>` | User | Remove a credential |
| `/admin_dashboard` | Admin | Manage users |
| `/update/<id>`, `/delete/<id>` | Admin | Edit or remove a user |
| `/reset_password/<id>` | Admin | Reset a user's password |
| `/logout` | Logged in | End the session |

---

## 🛡️ Security Considerations

This project demonstrates core security concepts, but it is **not production ready**. Known limitations and recommended fixes:

- **Configuration secrets.** Keep the Flask `SECRET_KEY` and database credentials out of source code. Load them from environment variables or a `.env` file (`python-dotenv` is already a dependency) and add `.env` to `.gitignore`.
- **Encryption key storage.** The Fernet key lives in a plain `secret.key` file next to the app. Store it outside the project directory or in a secrets manager, and never commit it.
- **Do not commit data files.** `database.db`, `instance/`, `secret.key`, and `.venv/` should all be listed in `.gitignore`.
- **CSRF protection.** State-changing actions such as delete are triggered by GET requests. Switch them to POST and enable CSRF tokens with Flask-WTF.
- **Production mode.** Run without `debug=True` and behind a production WSGI server.
- **Login hardening.** Add rate limiting, account lockout, and optional two-factor authentication.

---

## 🔮 Roadmap

- [ ] Move all secrets and settings to environment variables
- [ ] Add a `.gitignore` and remove committed data files
- [ ] CSRF protection and POST-only delete actions
- [ ] Password generator and strength meter
- [ ] Two-factor authentication (TOTP)
- [ ] Per-user encryption key derived from the master password
- [ ] Rate limiting and audit logging
- [ ] Docker setup

---

## 🤝 Contributing

Suggestions and improvements are welcome. Fork the repo, create a feature branch, and open a pull request.

---

## 📜 License

Released under the MIT License. Add a `LICENSE` file to your repo to enable this.

---

## 👤 Author

**codewithchandan945**
- GitHub: [@codewithchandan945](https://github.com/codewithchandan945)

---

⭐ If you found this project useful, consider giving it a star!
