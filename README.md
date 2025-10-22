# HNGi13 Stage 0 Backend Task – REST API

This project is a simple RESTful API built with **Python (Flask)** for the HNGi13 Backend Track (Stage 0).  
It returns your profile information along with a dynamic cat fact from the **Cat Facts API**.

---

## 📦 Features
- GET `/me` endpoint
- Returns JSON with:
  - `status`: success
  - `user`: name, email, stack
  - `timestamp`: current UTC time (ISO 8601)
  - `fact`: random cat fact (dynamic on each request)

---

## 🧑‍💻 Tech Stack
- Python
- Flask
- Gunicorn
- Render (for deployment)

---

## ⚙️ Installation (Local Setup)

```bash
https://github.com/lemuelmidas/Dynamic_Profile_Endpoint
cd Dynamic_Profile_Endpoint
pip install -r requirements.txt
python app.py
