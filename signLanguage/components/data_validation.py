# Data Valiation will read train,test and data.yaml files from data ingestion phase.
# It will perform validation of data and store results of validation in status.txt file.

import os
import sys
import shutil
from signLanguage.logger import logging
from signLanguage.exception import SignException
from signLanguage.entity.config_entity import DataValidationConfig
from signLanguage.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact


class DataValidation:
    def __init__(
        self,
        data_ingestion_artifact: DataIngestionArtifact = DataIngestionArtifact(),
        data_validation_config: DataValidationConfig = DataValidationConfig(),
        ) :
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
        except Exception as e:
           raise SignException(e, sys)
        
    
    def validate_all_files_exist(self)->bool:
        try:
            # once data_ingestion phase completes, data validation will fetch the artifiacts from data_ingestion and will validate
            # it has required file list which are  "train","test" and "data.yaml" based on the validation status returned it will pass the artifact i.e validation_Status to next phase
            # it will pass False if we do not have anyone of the files from the mentioned file list
            # it will pass True  if we have all files from the mentioned file list
            validation_status = None
            all_files = os.list_dir(self.data_ingestion_artifact.feature_store_path)
            for file in all_files:
                if file not in self.data_validation_config.required_file_list:
                    validation_status = False
                else:
                    validation_status = True                
        
                os.makedirs(self.data_validation_config.data_validation_dir,exist_ok=True)
                with open(self.data_validation_config.valid_status_file_dir,'w') as f:
                    f.write(f"Validation status : {validation_status} ")
            return validation_status
        
        except Exception as e:
            raise SignException(e, sys)   

    
    def initiate_data_validation(self)-> DataValidationArtifact:
        logging.info("Entered initiate_data_validation method of Data_Validation class")
        try: 
            # it calls function  validate_all_files_exist to verify the files and return validation status as the artifact  
            status = self.validate_all_files_exist()
            data_validation_artifact = DataValidationArtifact( validation_status = status,   )
            logging.info("Exited initiate_data_validation method of Data_Validation class")
            logging.info(f"Data validation artifact: {data_validation_artifact}")
             # 
            if status:
                shutil.copy(self.data_ingestion_artifact.data_zip_file_path,os.getcwd())
            return data_validation_artifact
        except Exception as e:
            raise SignException(e, sys)   