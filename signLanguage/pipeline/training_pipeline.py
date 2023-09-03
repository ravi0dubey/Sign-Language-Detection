# This is the core pipeline which drives all phases of sign language detection

import sys, os
from signLanguage.logger import logging
from signLanguage.exception import SignException
from signLanguage.components.data_ingestion import DataIngestion
from signLanguage.components.data_validation import DataValidation
from signLanguage.components.model_trainer import ModelTrainer
from signLanguage.entity.config_entity import (DataIngestionConfig, DataValidationConfig,ModelTrainerConfig)
from signLanguage.entity.artifact_entity import (DataIngestionArtifact,DataValidationArtifact,ModelTrainerArtifact)



class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config  = DataIngestionConfig()
        self.data_validation_config = DataValidationConfig()
        self.model_trainer_config   = ModelTrainerConfig()

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
    
    # data validation class takes data ingestion artifact and data validation configuration and data validation function will get initiated 
    def start_data_validation(self,data_ingestion_artifact:DataIngestionArtifact)-> DataValidationArtifact:
        try: 
            logging.info("Entered the start_data_validation method of TrainPipeline class")
            data_validation = DataValidation(data_ingestion_artifact = data_ingestion_artifact, data_validation_config = self.data_validation_config)
            data_validation_artifact = data_validation.initiate_data_validation()
            logging.info("Performed the data validation operations")
            logging.info("Exited the start_data_validation method of TrainPipeline class")
            return data_validation_artifact
        except Exception as e:
            raise SignException(e, sys)

    
    def start_model_trainer(self) -> ModelTrainerArtifact:
        try:
            logging.info("Entered the start_model_trainer method of TrainPipeline class")
            model_trainer = ModelTrainer(model_trainer_config=self.model_trainer_config,)
            model_trainer_artifact = model_trainer.initiate_model_trainer()
            logging.info("Performed the model training operations")
            logging.info("Exited the start_model_trainer method of TrainPipeline class")
            return model_trainer_artifact

        except Exception as e:
            raise SignException(e, sys)







    # main run pipeline which gets called from app.py
    # it calls all phases of the project one after another
    def run_pipeline(self) -> None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact= data_ingestion_artifact)
            if data_validation_artifact.validation_status == True:
                model_trainer_artifact = self.start_model_trainer()
        except Exception as e:
            raise SignException(e, sys)

