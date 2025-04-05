# 🚀 Full Stack Project — FastAPI + Angular

This is a monorepo project combining a **FastAPI backend** with an **Angular frontend**.  
Use this stack to build modern web apps with Python on the server and Angular on the client.

---

## 📁 Project Structure

job-management/
├── backend/        # Python/FastAPI
│   ├── app/
│   ├── .env
│   └── ...
├── frontend/       # Angular
│   ├── src/
│   ├── node_modules/
│   └── ...
├── .gitignore      # Should be here
└── README.md



---

## Backend — FastAPI

### ▶️ Run FastAPI Server

```bash
cd backend
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Run the server
uvicorn app.main:app --reload


#Airflow project
-- airflow db init
-- airflow webserver --port 8088
-- airflow schedule

## Frontend — Angular
cd frontend
npm install
ng serve



