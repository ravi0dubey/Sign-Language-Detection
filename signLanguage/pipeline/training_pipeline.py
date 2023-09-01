# This is the core pipeline which drives all phases of sign language detection

import sys, os
from signLanguage.logger import logging
from signLanguage.exception import SignException
from signLanguage.components.data_ingestion import DataIngestion
from signLanguage.entity.config_entity import (DataIngestionConfig)
from signLanguage.entity.artifact_entity import (DataIngestionArtifact)


class TrainPipeline:
    # data ingestion configuration declaration
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    # data ingestion class takes data ingestion configuration and data ingestion will get initiated 
    def start_data_ingestion(self)-> DataIngestionArtifact:
        try: 
            logging.info("Entered the start_data_ingestion method of TrainPipeline class")
            logging.info("Getting the data from URL")
            data_ingestion = DataIngestion(data_ingestion_config =  self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got the data from URL")
            logging.info("Exited the start_data_ingestion method of TrainPipeline class")
            return data_ingestion_artifact

        except Exception as e:
            raise SignException(e, sys)
        

    # main run pipeline which gets called from app.py
    # it calls all phases of the project one after another
    def run_pipeline(self) -> None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()
        
        except Exception as e:
            raise SignException(e, sys)
