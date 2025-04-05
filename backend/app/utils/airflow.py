import requests
from typing import Union
from app.core.config import settings

AIRFLOW_URL = settings.AIRFLOW_URL
AIRFLOW_AUTH = (settings.AIRFLOW_USERNAME, settings.AIRFLOW_PASS) 

def trigger_airflow_dag(resume_id: str) -> dict:
    resume_data = {
        "conf": {
            "resume_id": resume_id
        }
    }

    try:
        response = requests.post(AIRFLOW_URL, json=resume_data, auth=AIRFLOW_AUTH)

        if response.status_code == 200:
            return {"success": True, "message": "✅ Job pushed to Airflow successfully!"}
        else:
            return {
                "success": False,
                "message": f"❌ Failed to push job: {response.status_code}",
                "details": response.text,
            }

    except requests.RequestException as e:
        return {
            "success": False,
            "message": "❌ Exception occurred while calling Airflow",
            "details": str(e),
        }
