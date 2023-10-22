from .firebase import bucket
import os


def uploadBase64String(base64String: str, filepath: str):
    blob = bucket.blob(filepath)
    blob.upload_from_string()


def uploadFile(sourceFilePath: str, destination_dir: str = "images"):
    file_name = os.path.basename(sourceFilePath)
    path = f"{destination_dir}/{file_name}"
    blob = bucket.blob(path)
    blob.upload_from_filename(sourceFilePath)
    blob.make_public()
    return blob.public_url
