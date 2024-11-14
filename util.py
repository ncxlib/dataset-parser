import pickle
import boto3
import gzip
from dotenv import load_dotenv
import os

load_dotenv()

parent_dir = "data"
lib_name = "ncxlib"
postfix = "data.gz"
raw = "raw"
bucket = "ncxlib"

session = None

def connect_aws():
    global session
    if not session:
        session = boto3.Session(
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        )
    return session

def prefix(name):
    return f"{parent_dir}/{name}/{raw}/"

def new():
    return {
        "split": True,
        "X_train": [],
        "X_test": [],
        "y_train": [],
        "y_test": [],
    }

def build_path(name):
    return f"{parent_dir}/{name}/{lib_name}.{name}.{postfix}"

def save_data(data, name):
    file_path = build_path(name)
    with gzip.open(file_path, "wb") as f:
        pickle.dump(data, f)

    session = connect_aws()
    s3 = session.resource('s3')

    print("Uploading compressed data file to S3 bucket...")
    s3.Bucket(bucket).upload_file(file_path, file_path)

    print("Upload successful!")

def load_data(name):
    file_path = build_path(name)

    session = connect_aws()
    s3 = session.resource('s3')

    print("Downloading compressed data from S3...")
    s3.Bucket(bucket).download_file(file_path, file_path)
    print("Download successful!")
    
    with gzip.open(file_path, "rb") as f: 
        data = pickle.load(f)
    
    return data
