🚀 AI-Driven Customer Satisfaction Prediction System










An advanced Full-Stack Machine Learning Web Application that predicts customer satisfaction using CatBoost, with authentication and user-wise prediction history.

📌 Features

🔐 User Registration & Login (JWT Authentication)

🤖 Customer Satisfaction Prediction (CatBoost Model)

📊 Probability Confidence Output

🗂️ User-wise Prediction History

💾 SQLite Database

🌐 Flask Backend + HTML/CSS/JS Frontend

🛠️ Tech Stack
Backend

Flask

Flask-SQLAlchemy

Flask-JWT-Extended

CatBoost

Scikit-learn

Joblib

Frontend

HTML5

CSS3

JavaScript (Fetch API)

Database

SQLite


⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/yourusername/AI_Customer_Satisfaction_Advanced.git
cd AI_Customer_Satisfaction_Advanced

2️⃣ Create Virtual Environment

Windows

python -m venv venv
venv\Scripts\activate


Mac/Linux

python -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies
pip install flask flask-sqlalchemy flask-jwt-extended catboost pandas scikit-learn joblib

4️⃣ Train the Model
cd backend
python train.py

5️⃣ Run the Application
python app.py

6️⃣ Open in Browser
http://127.0.0.1:5000/

🧠 Dataset Format
Quality,Delivery,Support,Price,Satisfaction

Feature	Range	Description
Quality	1–10	Product/Service Quality Rating
Delivery	1–10	Delivery Experience
Support	1–10	Customer Support Rating
Price	1–10	Pricing Satisfaction
Satisfaction	0/1	Target Variable
🔍 Model Details

Algorithm: CatBoostClassifier

Type: Binary Classification

Output:

Satisfaction Prediction (0 or 1)

Confidence Probability Score

📜 License

This project is developed for academic purposes only.
