Tata Steel AI Customer Satisfaction Prediction
Overview

This is an advanced AI-driven full-stack web application designed to predict customer satisfaction (CSF) for Tata Steel based on key operational factors. The system integrates a CatBoost AI model simulation, dynamic dashboards, and a professional user interface for enterprise-level demonstration.

The platform helps evaluate operational efficiency, raw material security, customer-centricity, and sustainability, providing actionable insights through interactive analytics.

Features

User Authentication: Signup and Login system with email and password.

Session Management: Secure session-based login.

Dashboard: Creative, interactive KPI dashboard with animated cards and AI model status.

Analytics: AI-driven customer satisfaction prediction panel with dynamic results and confidence display.

Dark Mode: Toggle light/dark theme for professional visualization.

Responsive UI: Clean and modern interface using HTML, CSS, and Flask templates.

SQLite Database: Lightweight storage for user credentials.

Technologies Used

Backend: Python, Flask

Frontend: HTML, CSS, JavaScript

Database: SQLite

AI Simulation: CatBoost (simulation of predictions; can integrate full model)

Libraries: Flask, SQLite3

Installation & Setup

Clone the repository

git clone <your-repo-url>
cd tata_steel_prediction


Install dependencies

pip install flask


Run the application

python app.py


Open in browser

http://127.0.0.1:5000

Folder Structure
tata_steel_prediction/
│
├── app.py             # Main Flask application
├── database.db        # SQLite database (auto-created)
├── templates/         # HTML templates
│   ├── base.html
│   ├── login.html
│   ├── signup.html
│   ├── dashboard.html
│   └── analytics.html
└── static/
    └── css/
        └── style.css

Usage

Signup using email and password.

Login to access the dashboard.

View KPI metrics and AI model status.

Navigate to Analytics to simulate customer satisfaction predictions.

Toggle dark mode for better visualization.

Future Enhancements

Integrate actual CatBoost AI model for real predictions.

Add charts and graphs for historical data visualization.

Implement admin panel and role-based access.

Enable report generation in PDF or Excel format.

Deploy on cloud platforms for enterprise access.

License

This project is open-source and free to use for educational purposes.
