import os,sys
import yaml
from signLanguage.utils.main_utils import read_yaml_file
from signLanguage.logger import logging
from signLanguage.exception import SignException
from signLanguage.entity.config_entity import ModelTrainerConfig
from signLanguage.entity.artifact_entity import ModelTrainerArtifact

class ModelTrainer:
    def __init__(self,model_trainer_config: ModelTrainerConfig,):
        try:
            self.model_trainer_config = model_trainer_config
        except Exception as e:
           raise SignException(e, sys)

    # model training folder which performs the training of the model
    def initiate_model_trainer(self,) -> ModelTrainerArtifact:
        logging.info("Entered initiate_model_trainer method of ModelTrainer class")
        try:
            # unzipping of sign language data 
            logging.info("Unzipping data")
            os.system("unzip Sign_language_data.zip")
            os.system("rm Sign_language_data.zip")

            # data.yaml is read to figure out the number of classes we have in sign language daga    
            with open("data.yaml", 'r') as stream:
                num_classes = str(yaml.safe_load(stream)['nc'])
            
            # YOLOV5 (*model's).yaml file is read and a new custom_(*model's).yaml will be created
            # this custom_(*model's).yaml  will store all .yaml configuration of the model chosen 
            # but number of classes will be changed to number of classes we have in our sign language data
            model_config_file_name = self.model_trainer_config.weight_name.split(".")[0]
            print(model_config_file_name)
            config = read_yaml_file(f"yolov5/models/{model_config_file_name}.yaml")
            config['nc'] = int(num_classes)

            # a new custom_*.yaml is created which will contain all configuration of existing model's.yaml file excpet the number of class which is of our sign language data
            with open(f'yolov5/models/custom_{model_config_file_name}.yaml', 'w') as f:
                yaml.dump(config, f)
            
            # Next, we'll fire off training!Here, we are able to pass a number of arguments:
            # img: define input image size = 416
            # batch: determine batch size = 16  
            # epochs: define the number of training epochs. (Note: often, 3000+ are common here!) = 300
            # data: set the path to our yaml file
            # cfg: specify our model configuration choosing custom_yolov5s.yaml file
            # weights: specify a custom path to weights. (Note: you can download weights from the Ultralytics Google Drive folder) = yolov5s.pt
            # name: result names
            # nosave: only save the final checkpoint
            # cache: cache images for faster training
            os.system(f"cd yolov5/ && python train.py --img 416 --batch {self.model_trainer_config.batch_size} --epochs {self.model_trainer_config.no_epochs} --data ../data.yaml --cfg ./models/custom_yolov5s.yaml --weights {self.model_trainer_config.weight_name} --name yolov5s_results  --cache")
            os.system("cp yolov5/runs/train/yolov5s_results/weights/best.pt yolov5/")
            os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)
            os.system(f"cp yolov5/runs/train/yolov5s_results/weights/best.pt {self.model_trainer_config.model_trainer_dir}/")         
            
            # After training is done we will delete runs,train,test directory and data.yaml file  its contents recursively generated from above run without prompting for confirmation. 
            os.system("rm -rf yolov5/runs")
            os.system("rm -rf train")
            os.system("rm -rf test")
            os.system("rm -rf data.yaml")
            
            # model best.pt will get generated whose path will be stored in model_trainer_Artifact
            model_trainer_artifact = ModelTrainerArtifact(trained_model_file_path="yolov5/best.pt",)
            logging.info("Exited initiate_model_trainer method of ModelTrainer class")
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")
            return model_trainer_artifact
        except Exception as e:
            raise SignException(e, sys)