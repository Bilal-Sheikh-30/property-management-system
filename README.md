# 🏡 Propfolio - Property Management Platform

## 📌 Description
**Propfolio** is a property management platform built for showcasing real estate and managing property-related appointments. It provides users with a dashboard where they can monitor and handle appointments, making the property management experience streamlined and professional.

---

## 🚀 Features
- 📋 Showcase property listings
- 🗓️ Appointment scheduling and management
- 🧑‍💼 User dashboard with upcoming appointments
- 💻 Responsive user interface with Bootstrap
- 🔐 Environment variable support for secure database access

---

## 🛠️ Tech Stack

| Layer      | Technologies Used                |
|------------|----------------------------------|
| Frontend   | HTML, CSS, JavaScript, Bootstrap |
| Backend    | Django (Python)                  |
| Database   | MySQL                            |

---

## 📹 Demo

A demo video of the project can be found below:

<!-- Replace with your actual video link -->
<iframe width="560" height="315" src="/workspaces/property-management-system/propfolio demo.mp4" frameborder="0" allowfullscreen></iframe>

---

## 🔧 Installation & Setup

### 📋 Prerequisites
- Python 3.x
- MySQL
- Virtualenv (recommended)

### ⚙️ Steps to Run Locally

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/propfolio.git
   cd propfolio

2. **Create and Activate Virtual Environment**
    ```python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install Project Dependencies**
    ```pip install -r requirements.txt

3. **Configure Environment Variables**
    Create a .env file in the root directory (where manage.py exists) and include the following:
    NAME=your_database_name
    USER=your_database_user
    PASSWORD=your_database_password
    HOST=your_database_host
    PORT=your_database_port

5. **Apply Migrations**
    ```python manage.py migrate

6. **Run the Development Server**
    ```python manage.py runserver