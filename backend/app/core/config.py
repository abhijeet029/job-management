from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    MINIO_ENDPOINT: str
    MINIO_ACCESS_KEY: str
    MINIO_SECRET_KEY: str
    MINIO_BUCKET_NAME: str
    AIRFLOW_URL: str
    AIRFLOW_USERNAME: str
    AIRFLOW_PASS: str

    class Config:
        env_file = ".env"

# Create a global instance of settings
settings = Settings()
