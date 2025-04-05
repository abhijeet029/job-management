from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os
import json

# Set root directory path (2 levels up from current DAG file)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from app.core.database import SessionLocal
from app.services.user_job_status import updateUserJobStatus


# Default arguments for the DAG
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 4, 1),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    "process_resume",  # This should match the API call
    default_args=default_args,
    description="DAG to process uploaded files from MinIO",
    schedule_interval=None,  # Only triggered manually or via API
    catchup=False,
)

# Function to process file
def process_file(**kwargs):
    """Reads the uploaded file from MinIO and processes it."""
    conf = kwargs.get("dag_run").conf or {}  # Get parameters from API call
    resume_id = conf.get("resume_id")
    db = SessionLocal()
    updateUserJobStatus(db, resume_id)

# Task to process file
process_task = PythonOperator(
    task_id="process_file",
    python_callable=process_file,
    provide_context=True,
    dag=dag,
)

process_task  # Only one task, so no dependencies needed

