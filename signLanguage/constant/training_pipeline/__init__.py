import os

# Purpose is to create artifacts folder
ARTIFACTS_DIR: str = "artifacts"


# Data Ingestion related constant start with DATA_INGESTION variable name. 
# Within artifacts folder data_ingestion/feature_Store folder will be created which will store sign language annotated data pulled from github repo in train and test folders.

DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_DOWNLOAD_URL: str = "https://github.com/ravi0dubey/Dataset/raw/main/Sign_language_data.zip"



# Data Valiation related constant start with DATA_VALIDATION variable name. 
# Within artifacts folder data_validation folder will be created which will use train,test and data.yaml files of data ingestion phase.
# It will perform validation of train data and store validation results in status.txt file.

DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_STATUS_FILE: str = "status.txt"
DATA_VALIDATION_ALL_REQUIRED_FILES = ["train","test","data.yaml"]


# Model Trainer related constant start with MODEL_TRAINER var name
# It will perform the training of the model using pretrained weights of YOLOV5 architecture

MODEL_TRAINER_DIR_NAME: str = "model_trainer"
MODEL_TRAINER_PRETRAINED_WEIGHT_NAME: str = "yolov5s.pt"
MODEL_TRAINER_NO_EPOCHS: int = 1
MODEL_TRAINER_BATCH_SIZE: int = 16

# MODEL PUSHER related constant start with MODEL_PUSHER var name
# It will push the model to s3 bucket with name best.pt

BUCKET_NAME = "sign-lang23-bucket"
S3_MODEL_NAME = "best.pt"
