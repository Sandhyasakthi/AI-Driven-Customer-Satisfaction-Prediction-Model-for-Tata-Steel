🚀 AI-Driven Customer Satisfaction Prediction System

A full-stack machine learning web application that predicts customer satisfaction using CatBoost and stores prediction history with authentication.

📌 Features

🔐 User Registration & Login (JWT Authentication)

🤖 Customer Satisfaction Prediction (CatBoost Model)

📊 Prediction Probability Output

🗂️ User-wise Prediction History

💾 SQLite Database

🌐 Flask Backend + HTML/CSS/JS Frontend

🛠️ Tech Stack

Backend

Flask

Flask-SQLAlchemy

Flask-JWT-Extended

CatBoost

SQLite

Frontend

HTML

JavaScript (Fetch API)

ML

CatBoost Classifier

Pandas

Scikit-learn
⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/yourusername/AI_Customer_Satisfaction_Advanced.git
cd AI_Customer_Satisfaction_Advanced

2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows

3️⃣ Install Dependencies
pip install flask flask-sqlalchemy flask-jwt-extended catboost pandas scikit-learn joblib

4️⃣ Train the Model
cd backend
python train.py


This creates model.pkl.

5️⃣ Run the Application
python app.py

6️⃣ Open in Browser
http://127.0.0.1:5000/

🧠 Dataset Format

The dataset must contain:

Quality,Delivery,Support,Price,Satisfaction


Where:

Quality → Service/Product Quality (1–10)

Delivery → Delivery Experience (1–10)

Support → Customer Support Rating (1–10)

Price → Pricing Satisfaction (1–10)

Satisfaction → 0 (Not Satisfied) / 1 (Satisfied)

🔄 How It Works

User registers and logs in.

JWT token is generated.

User enters rating values.

CatBoost model predicts satisfaction.

Prediction + probability stored in database.

User can load their prediction history.

📸 Future Improvements

Add Charts & Visualization

Deploy on Render/Heroku

Use PostgreSQL instead of SQLite

Add Model Accuracy Display

Improve UI with Bootstrap or React

👩‍💻 Author

Sandhya

📜 License

This project is for educational and academic purposes.
