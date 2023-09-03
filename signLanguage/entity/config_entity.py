
# config entity of all components of sign language detection are declared here
import os
from dataclasses import dataclass
from datetime import datetime
from signLanguage.constant.training_pipeline import *

TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

# In TrainingPipelineConfig, within artifacts folder, timestamp folder will get created on each run
@dataclass
class TrainingPipelineConfig:
    artifacts_dir: str = os.path.join(ARTIFACTS_DIR,TIMESTAMP)

training_pipeline_config:TrainingPipelineConfig = TrainingPipelineConfig() 


# In DataingestionConfig class we are setting up path of dataingestion directory, feature store and download url.
@dataclass
class DataIngestionConfig:
    data_ingestion_dir: str = os.path.join(training_pipeline_config.artifacts_dir, DATA_INGESTION_DIR_NAME)
    feature_store_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR)
    data_download_url: str = DATA_DOWNLOAD_URL


# In DataValidationConfig class we are setting up path of datavalidation directory, valid_status_file directory and required_file_list.
@dataclass
class DataValidationConfig:
    data_validation_dir: str = os.path.join(training_pipeline_config.artifacts_dir, DATA_VALIDATION_DIR_NAME)
    valid_status_file_dir: str = os.path.join(data_validation_dir, DATA_VALIDATION_STATUS_FILE)
    required_file_list = DATA_VALIDATION_ALL_REQUIRED_FILES


# In ModelTrainerConfig class we are setting up path of trained model directory. Weight name is declared which will be used for training. 
# Number of epochs and batch size for the training are declared
@dataclass
class ModelTrainerConfig:
    model_trainer_dir: str = os.path.join(training_pipeline_config.artifacts_dir, MODEL_TRAINER_DIR_NAME)
    weight_name = MODEL_TRAINER_PRETRAINED_WEIGHT_NAME
    no_epochs = MODEL_TRAINER_NO_EPOCHS
    batch_size = MODEL_TRAINER_BATCH_SIZE