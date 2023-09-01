import os

# Purpose is to create artifacts folder
ARTIFACTS_DIR: str = "artifacts"


"""
Data Ingestion related constant start with DATA_INGESTION Variable name. Within artifacts folder dataingestion/feature_Store folder will be created which will store 
sign language annotated data pulled from github repo in train and test folder.
"""
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_DOWNLOAD_URL: str = "https://github.com/ravi0dubey/Dataset/raw/main/Sign_language_data.zip"
