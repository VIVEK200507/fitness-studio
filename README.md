# 🏋️ Fitness Studio API

A backend REST API built using **FastAPI** for managing a fitness studio. The system supports **user authentication**, **class creation**, **class booking**, and **viewing bookings**, secured with **JWT-based authentication**.

---

## 📌 Project Overview

This project provides APIs for:

* User signup and login
* JWT authentication & authorization
* Creating fitness classes (admin / authenticated users)
* Viewing available fitness classes
* Booking fitness classes
* Viewing user bookings

It demonstrates real-world backend concepts such as authentication, database relationships, and RESTful API design.

---

## 🛠 Tech Stack

* **Python 3.10+**
* **FastAPI**
* **SQLAlchemy** (ORM)
* **SQLite** (Database)
* **JWT (JSON Web Tokens)**
* **Passlib (bcrypt)** for password hashing
* **Uvicorn** (ASGI server)

---

## ✨ Features

* 🔐 Secure user authentication with JWT
* 👤 User registration & login
* 📅 Create fitness classes
* 🏃 Book available fitness classes
* 📄 View all classes
* 📋 View user-specific bookings
* ⏱ Timezone handling (IST)

---

## 📂 Project Structure

```text
fitness/
│── app/
│   ├── main.py          # FastAPI app & routes
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic schemas
│   ├── auth.py          # Password hashing & JWT
│   ├── deps.py          # Dependencies (DB, auth)
│   ├── database.py      # Database connection
│── requirements.txt
│── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone <repository-url>
cd fitness
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
uvicorn app.main:app --reload
```

The API will be available at:

👉 **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

## 📘 API Documentation

FastAPI provides automatic Swagger documentation:

* **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🔐 Authentication Flow (JWT)

1. User signs up using `/signup`
2. User logs in using `/login`
3. API returns an **access token**
4. Click **Authorize** in Swagger UI
5. Paste token as:

```text
Bearer <your_access_token>
```

6. Authenticated routes can now be accessed

---

## 🔗 API Endpoints

### 🔑 Authentication

| Method | Endpoint | Description           |
| ------ | -------- | --------------------- |
| POST   | /signup  | Register a new user   |
| POST   | /login   | Login & get JWT token |

---

### 🏋️ Classes

| Method | Endpoint | Description                            |
| ------ | -------- | -------------------------------------- |
| POST   | /classes | Create a fitness class (Auth required) |
| GET    | /classes | View all classes                       |

#### Sample Request (Create Class)

```json
{
  "name": "Morning Yoga",
  "dateTime": "2026-01-25T06:30:00",
  "instructor": "Vicky",
  "availableSlots": 20
}
```

---

### 📅 Bookings

| Method | Endpoint  | Description                  |
| ------ | --------- | ---------------------------- |
| POST   | /book     | Book a class (Auth required) |
| GET    | /bookings | View user bookings           |

---

## 🗄 Database Models

### User

* id
* name
* email
* password

### FitnessClass

* id
* name
* date_time
* instructor
* available_slots

### Booking

* id
* user_id
* class_id

---

## 🧪 Testing

* Tested using **Swagger UI**
* Authentication tested with JWT
* Class creation & booking tested with valid tokens

---

## 🚀 Future Improvements

* Role-based access (Admin/User)
* Pagination for classes
* Email notifications
* Docker support
* Deployment to cloud

---

## 👨‍💻 Author

**Vivek Dharmwan**
Backend Developer (FastAPI, Python)

---

## 📄 License

This project is created for learning and assignment purposes.
