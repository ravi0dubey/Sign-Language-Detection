
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