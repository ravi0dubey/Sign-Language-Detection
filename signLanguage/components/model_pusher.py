import sys
from signLanguage.configuration.s3_operations import S3Operation
from signLanguage.entity.artifact_entity import (ModelPusherArtifacts,ModelTrainerArtifact)
from signLanguage.entity.config_entity import ModelPusherConfig
from signLanguage.exception import SignException
from signLanguage.logger import logging



class ModelPusher:
    def __init__(self,model_pusher_config: ModelPusherConfig,model_trainer_artifact: ModelTrainerArtifact, s3: S3Operation):
        try:
            self.model_pusher_config = model_pusher_config
            self.model_trainer_artifacts = model_trainer_artifact
            self.s3 = s3
        except Exception as e:
           raise SignException(e, sys)
    

    #  Once model is trained method then it needs to be pushed to S3 bucket. 
    def initiate_model_pusher(self) -> ModelPusherArtifacts:               
        logging.info("Entered initiate_model_pusher method of Modelpusher class")
        try:
            # Calling upload_file function from Configuration-> s3_operations.py which will Upload best.pt model to s3 bucket
            self.s3.upload_file(
                self.model_trainer_artifacts.trained_model_file_path,
                self.model_pusher_config.S3_MODEL_KEY_PATH,
                self.model_pusher_config.BUCKET_NAME,
                remove=False,
            )
            logging.info("Uploaded best model to s3 bucket")
            logging.info("Exited initiate_model_pusher method of ModelTrainer class")

            # Saving the model pusher artifacts  which is s3 bucket name and model name.    
            model_pusher_artifact = ModelPusherArtifacts(bucket_name=self.model_pusher_config.BUCKET_NAME,s3_model_path=self.model_pusher_config.S3_MODEL_KEY_PATH,)
            return model_pusher_artifact

        except Exception as e:
            raise SignException(e, sys) from e

