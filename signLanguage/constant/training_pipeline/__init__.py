import os

# Purpose is to create artifacts folder
ARTIFACTS_DIR: str = "artifacts"

"""
Data Ingestion related constant start with DATA_INGESTION variable name. 
Within artifacts folder data_ingestion/feature_Store folder will be created which will store sign language annotated data pulled from github repo in train and test folders.
"""
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_DOWNLOAD_URL: str = "https://github.com/ravi0dubey/Dataset/raw/main/Sign_language_data.zip"


"""
Data Valiation related constant start with DATA_VALIDATION variable name. 
Within artifacts folder data_validation folder will be created which will use train,test and data.yaml files of data ingestion phase.
It will perform validation of train data and store validation results in status.txt file.
"""
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_STATUS_FILE: str = "status.txt"
DATA_VALIDATION_ALL_REQUIRED_FILES = ["train","test","data.yaml"]

