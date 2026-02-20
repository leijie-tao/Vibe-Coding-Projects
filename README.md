# Vibe-Coding-Projects
## Use AI to complete some projects.
## Projet 1: MyEmployeeSystem: Python + Django + MySQL + Bootstrap
A robust, full-stack enterprise administration dashboard built with **Python 3** and **Django**. This project features a complete employee/department data flow, secure authentication, and a dynamic data visualization dashboard to support digital resource management.

### ✨ Key Features

* **🔒 Security & Authentication**
    * **Session-based Authentication**: Secure administrator login system.
    * **Custom Middleware**: Global request interception to redirect unauthorized users, ensuring data integrity and security.
    * **Modern UI**: Features a custom login interface with modern flat design and glassmorphism effects.

* **📊 Data Visualization Dashboard**
    * **Dynamic Rendering**: Decoupled architecture where the frontend fetches data via Ajax and the backend returns structured JSON.
    * **Apache ECharts Integration**: Real-time visualization including:
        * Bar Charts (Department headcount statistics)
        * Line Charts (Monthly employee onboarding trends)
        * Pie Charts (Employee age distribution)

* **👥 Department & Employee Management (CRUD)**
    * **Full CRUD Operations**: Automated form generation and validation using Django `ModelForm`.
    * **Relational Data Handling**: Efficient data querying using Foreign Keys (`ForeignKey`) for Department-Employee relationships.
    * **Advanced Search & Pagination**:
        * Keyword-based fuzzy search filtering.
        * Custom pagination logic that persists search parameters across pages.

### 🛠️ Tech Stack

* **Backend:** Python 3, Django Framework (MVT Architecture)
* **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 3 (Bootswatch Flatly Theme)
* **Database:** MySQL (via `pymysql` driver)

### 📸 Screenshots
1. **Login Interface**
<img width="1497" height="818" alt="image" src="https://github.com/user-attachments/assets/1bf1a661-493a-4f3c-a2f8-2f2be037b4ec" /> 

2. **Department List**
<img width="1497" height="818" alt="image" src="https://github.com/user-attachments/assets/1fa30026-22d7-4079-bdd0-91ad88aefc34" />

3. **Employee List with Search & Pagination**
<img width="1497" height="818" alt="image" src="https://github.com/user-attachments/assets/9f512262-a374-428c-9938-aa794a0f5c79" />

4. **Employee Data Dashboard**
<img width="1497" height="818" alt="image" src="https://github.com/user-attachments/assets/ebfe2eba-2e40-444c-af6c-bad652fcc65f" />





