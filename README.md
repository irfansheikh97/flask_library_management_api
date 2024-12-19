# Flask Library Management API

This project implements a RESTful API for managing books and members. It includes endpoints for CRUD operations on books and members, as well as search functionality with pagination and authentication for secure routes.

---

## **How to Run the Project**

### **1. Prerequisites**
- Python 3.8+
- Virtual environment tool (optional but recommended)
- `pip` (Python package installer)

### **2. Setup Instructions**

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Create a Virtual Environment:** (Optional)
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate    # Windows
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables:**
   - Create a `.env` file in the project root.
   - Add the following line:
     ```
     SECRET_KEY=your-secret-key
     ```

5. **Run the Application:**
   ```bash
   python app.py
   ```

6. **Access the API:**
   - The API will be available at `http://127.0.0.1:5000/`.

7. **Run Tests:**
   ```bash
   python -m unittest discover -s tests
   ```

---

## **Design Choices Made**

### **1. Modular Structure**
- **`app.py`**:
  - Acts as the entry point and registers blueprints for modular organization.
- **`routes.py`**:
  - Contains route logic for books, members, and search functionality.
- **`auth.py`**:
  - Handles token-based authentication and secure routes.
- **`models.py`**:
  - Defines data models for `Book` and `Member` and manages in-memory storage.

### **2. Authentication**
- A token-based approach is used for secure routes.
- A secret key is required to access protected endpoints.

### **3. Pagination**
- Pagination is implemented in search and book listing endpoints using `page` and `limit` query parameters.
- This ensures efficient data retrieval for large datasets.

### **4. Error Handling**
- Proper HTTP status codes and messages are returned for various scenarios:
  - `404`: Resource not found.
  - `400`: Bad request.
  - `403`: Unauthorized access.

### **5. In-Memory Data Storage**
- The application uses in-memory lists (`books` and `members`) for simplicity.
- Each entity (book/member) has a unique ID assigned incrementally.

---

## **Assumptions and Limitations**

### **Assumptions**
1. **Unique Titles and Authors:**
   - Titles and authors are considered case-insensitive for searching and filtering.
2. **Simplified Authentication:**
   - No database is used for user credentials; a hardcoded username and password validate the login.

### **Limitations**
1. **No Persistent Storage:**
   - The project uses in-memory storage, so all data is lost when the server restarts.
   - A database (e.g., SQLite, PostgreSQL) would be ideal for real-world usage.

2. **Single User Authentication:**
   - The system only supports a single hardcoded user for authentication.

3. **Scalability:**
   - With in-memory data storage, the project is not suitable for handling large datasets.

4. **Search Functionality:**
   - Search queries must match substrings of the title or author.
   - No advanced search capabilities like fuzzy matching are implemented.

---

## **Future Improvements**
- Integrate a database for persistent data storage.
- Implement advanced search features (e.g., fuzzy matching).
- Add support for multiple users and role-based access control.
- Use a framework like Flask-RESTful or Flask-SQLAlchemy for better scalability and maintainability.

