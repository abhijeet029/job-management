import uuid
from fastapi import UploadFile
from app.core.minio import minio_client
from app.core.config import settings

BUCKET_NAME = settings.MINIO_BUCKET_NAME

def upload_to_minio(file: UploadFile):
    try:
        ext = file.filename.split('.')[-1]
        object_name = f"{uuid.uuid4().hex}.{ext}"
        minio_client.put_object(
            BUCKET_NAME,
            object_name,
            file.file,
            length=-1,
            part_size=10 * 1024 * 1024,
            content_type=file.content_type
        )

        base_url = f"http://{settings.MINIO_ENDPOINT}/{BUCKET_NAME}"
        return base_url, object_name
    except Exception as e:
        print(f"[MinIO Unexpected Error] {e}")
        raise

def get_minio_obj(filename):
    try:
        response = minio_client.get_object(BUCKET_NAME, filename)
        return response
    except Exception as e:
        print(f"[MinIO Unexpected Error] {e}")
        raise
