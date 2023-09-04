# End to End Sign Language Detection

## Problem Statement

We need to build Sign language detection model where hand signs are detected by the model and it will tell if its "Please", "Thanks", "Help", "I love You, "Yes" or "No".


## Solution Proposed

In this project, the focus is to correctly detect the hand sign using YOLOV5 model


## Tech Stack Used
Python </br>
FastAPI </br>
Yolov5 algorithms </br>
Docker </br>


## Infrastructure Required.
AWS S3 </br>
AWS EC2 </br>
AWS ECR </br>
Git Actions </br>
Terraform </br>


## How to run  
1. conda create -n signLanguage python=3.7 -y  </br>
2. conda activate signLanguage </br>
3. pip install -r requirements.txt </br>
4. python main.py </br>
5. open in browser: http://localhost:8080/ </br>
6. To do the object detection for a static image upload the image and it will predict the sign language </br>
7. To do the sign language prediction, live, change the url in the browser to : http://localhost:8080/train/live </br>
6. To the train the model change the url in the browser to : http://localhost:8080/train </br>

## Input Data for training the model

Sign language annotated data is kept in github repository: https://github.com/ravi0dubey/Dataset/raw/main/Sign_language_data.zip

## Project Architecture
![image](https://github.com/ravi0dubey/Sensor-Fault-Detection/assets/38419795/e6776a8e-27b9-419e-ab7a-f435beee4e01)

## Deployment Architecture
![deployment](https://github.com/ravi0dubey/Sign-Language-Detection/assets/38419795/19351f34-e3d7-4e98-967c-656075a9a87a)


## How project was designed and build
1. Write **template.p**y which create a folder structure of our project. Within each folders, it will create the filenames where we will be writing our code. </br>
2. Clone **YOLOV5** github repo from git  using "clone https://github.com/ultralytics/yolov5.git" and delete its .git and .gitignore folder </br>
3. From YOLOV5 requirements.txt, copy its content into our project **requirements.txt**  and on top of it add addtional modules required for your project and at last add -e . which will be used by setup.py </br>
4. **setup.py** file is created where we write statement so that signLanguage folder will behave as libraries </br>
5. **Exception** and **Logger** module will handle exception and write log activities respectively</br>
6. All common functionality like encode-decode image, reading/writing of yaml files are written in utils>main.py  </br>
7. Steps to create the project. We will write code in following order for better structure </br>
  a. **Constants ->** We will first declare all constants variable to be used by each individual components in constant->training_pipeline->__init__.py  </br> </br>
  b. **entity ->**  </br>
              i. We will declare dataclass for each components in entity->config_entity.py </br>
              ii. We will declare artifacts which each components will be generating in  entity->artifact_entity.py </br> </br>
  c. **configurations->s3_operations.py ->** It has **upload_file** method to push the model to s3 bucket based on the s3-bucket name declared in the project  </br> </br>
  d. **components ->**  </br>
          i. **data_ingestion.py ->**  will fetch input sign language data from github repo, unzip it and divide images into train and test folder </br>
            It will return data_zile_file_path and feature_store_path as its artifact. Feature_store_path contains train(folder), test(folder) and data.yaml file  </br>
         ii. **data_validation.py ->** which will read the artifacts of data_ingestion and validate that it has 3 necessary components received from data_ingestion(train, test and data.yaml file) </br>.
            It will return validation_status as its artifact </br>
        iii. **model_trainer.py ->** If validation status from data_validation.py is True then it will download the modelweights from YOLOV5S and it will train the model on the sign language data using the number of epochs mentioned. I have trained using 300 epochs</br>
         iv. **model_pusher.py ->** If validation status from data_validation.py is True then it will call upload_file method of configurations-> s3_operations.py to push the trained model best.pt to **S3 bucket** for future usage  </br> </br>
         
   e. **pipeline ->** </br>
      i. **application.py** -> it stores the configuration of host and port number on which the project will run </br></br>
     ii. **training_pipeline.py ->** will call each components of the project(mentioned above) in sequence </br> </br>
   
   f. **app.py ->**  It is the main driver part of the application which calls the pipeline for training and prediction </br>





## Training Pipeline

#### Data Ingestion pipeline
![Data Ingestion](https://github.com/ravi0dubey/Sign-Language-Detection/assets/38419795/b9ba1b27-9268-4f20-95f3-2b38dc4f6154)

#### Folder structure of Artifact which gets created on running Training Pipeline for Data Ingestion
![image](https://github.com/ravi0dubey/Sign-Language-Detection/assets/38419795/143f79e9-3fe8-489a-adb1-c00bde7f4ea5)

#### Data Validation 

![Data validation](https://github.com/ravi0dubey/Sign-Language-Detection/assets/38419795/0b4b4daa-55f8-42ac-a01c-54bc2aa7c238)

#### Folder structure of Artifact which gets created on running Training Pipeline for Data Validation
![image](https://github.com/ravi0dubey/Sign-Language-Detection/assets/38419795/d98cf223-0508-43f1-98a2-808800288301)


#### Model Trainer
![Model trainer](https://github.com/ravi0dubey/Sign-Language-Detection/assets/38419795/b56eabbe-4b6e-42d4-b613-0229ddbf2b56)

#### Folder structure of Artifact which gets created on running Training Pipeline for Model Trainer
![image](https://github.com/ravi0dubey/Sign-Language-Detection/assets/38419795/09617b89-05bb-4ea7-b6a0-0c23278e7ec3)


#### Model Pusher
![Model Pusher](https://github.com/ravi0dubey/Sign-Language-Detection/assets/38419795/213ee1e0-00ce-4a06-8370-e1411b05aab1)

#### Model best.pt getting saved in S3 bucket
![image](https://github.com/ravi0dubey/Sign-Language-Detection/assets/38419795/8a218159-1f54-4e39-99b5-7e0f88b62fe2)





## CI-CD Pipeline
![image](https://user-images.githubusercontent.com/38419795/229185395-bbe50ebc-f0e2-4ff5-9ad8-6dad2cc4311b.png)

# Image of successful CI-CD pipeline deployment
![image](https://github.com/ravi0dubey/Sensor-Fault-Detection/assets/38419795/56e03363-dcf5-4e7d-9297-571f6df61f75)

![image](https://github.com/ravi0dubey/Sensor-Fault-Detection/assets/38419795/712fc20c-24ff-4d28-952c-7ba492abbe57)




#### Docker image in ECR

![image](https://github.com/ravi0dubey/Sign-Language-Detection/assets/38419795/4ed95417-642b-410a-b8a8-005522f932e3)




