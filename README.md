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

## How project was build?
1. Write template.py which create a folder structure of our project. Within each folders, it will create the filenames where we will be writing our code. </br>
2. Clone yolov5 github repo from git  using "clone https://github.com/ultralytics/yolov5.git" and delete its .git and .gitignore folder </br>
3. From YOLOV5 requirements.txt, copy its content into our project requirements.txt  and on top of it add addtional modules required for your project and at last add -e . which will be used by setup.py </br>
4. setup.py file is created where we write statement so that signLanguage folder will behave as libraries </br>
5. Exception and Logger module will handle exception and write log activities respectively</br>
6. All common functionality like encode-decode image, reading/writing of yaml files are written in utils>main.py  </br>
7.  ss </br>
8.   </br>




## How to run?  
1. conda create -n signLanguage python=3.7 -y  </br>
2. conda activate signLanguage </br>
3. pip install -r requirements.txt </br>
4. python main.py </br>
5. open in browser: http://localhost:8080/ </br>

## Data Collections
![image](https://github.com/ravi0dubey/Sensor-Fault-Detection/assets/38419795/fb8bb7d5-e34d-44dd-908e-0f9b429f94f8)

## Project Architecture
![image](https://github.com/ravi0dubey/Sensor-Fault-Detection/assets/38419795/e6776a8e-27b9-419e-ab7a-f435beee4e01)

## Deployment Architecture
![image](https://github.com/ravi0dubey/Sensor-Fault-Detection/assets/38419795/637987ee-f192-4968-86b1-9bbc0ff7ddb0)


## Approach while doing the coding
![image](https://user-images.githubusercontent.com/38419795/226114307-71505cd5-8bb4-44fb-b0e1-1e28a5b045ec.png)
1. Define all constants used which will be used under constants folder
2. In Entity folder we declare configuration and artifact of the component
3. Train Pipeline uses both configuration and artifact of the component
4. Components like data ingestion, data validation etc. will be declared which will be used by pipeline


## Training Pipeline
![image](https://user-images.githubusercontent.com/38419795/225762823-2756c612-b41e-4418-9e86-b94c81f10252.png)

## Data Ingestion pipeline
![image](https://user-images.githubusercontent.com/38419795/225761627-e7bb0f6f-724d-4b94-a181-06136365932d.png)

## Folder structure of Artifact which gets created on running Training Pipeline
#### Data Ingestion
![image](https://user-images.githubusercontent.com/38419795/226071961-d9678667-cf9e-4410-a9d4-6a4293f4ae1e.png)\n
#### Data Validation 
![image](https://user-images.githubusercontent.com/38419795/226494010-ac475551-5159-46ce-84c2-a3e2904e249b.png)

![image](https://user-images.githubusercontent.com/38419795/226127381-6ddfd989-76e2-4087-86e8-c1cd0daa846b.png)

#### Data Transformation
![image](https://user-images.githubusercontent.com/38419795/227364255-1657eb48-628a-4c22-a073-1d21fa3c37c9.png)

#### Model Trainer
![image](https://user-images.githubusercontent.com/38419795/228225084-3daabd37-dc7d-41c5-89a7-362516e59108.png)


#### Model Evaluation
Models will be stored in timestamp folder \n
![image](https://user-images.githubusercontent.com/38419795/227789015-c9e7434a-5a76-4977-b53a-9929721f8231.png)

#### Model Pusher
![image](https://user-images.githubusercontent.com/38419795/228396989-a72568fa-f190-4694-aa3e-6579f29ccb71.png)

#### Saved Model Path
![image](https://user-images.githubusercontent.com/38419795/228519585-222ceb72-cb9f-4929-bc50-9169bb4ed4b3.png)


## Data Drift Detection
![image](https://user-images.githubusercontent.com/38419795/226199171-c98ae16f-5007-484e-b5f9-5b3d3e73cc92.png)

## Concept Drift Detection
![image](https://user-images.githubusercontent.com/38419795/226199601-27d1bf75-0556-4275-9c53-21bef8891f66.png)

## Target Drift Detection
![image](https://user-images.githubusercontent.com/38419795/226200126-e31f41e5-c791-43f7-8a57-4df7700a3cce.png)



## CI-CD Pipeline
![image](https://user-images.githubusercontent.com/38419795/229185395-bbe50ebc-f0e2-4ff5-9ad8-6dad2cc4311b.png)

# Image of successful CI-CD pipeline deployment
![image](https://github.com/ravi0dubey/Sensor-Fault-Detection/assets/38419795/56e03363-dcf5-4e7d-9297-571f6df61f75)

![image](https://github.com/ravi0dubey/Sensor-Fault-Detection/assets/38419795/712fc20c-24ff-4d28-952c-7ba492abbe57)




#### Docker image in ECR

![image](https://github.com/ravi0dubey/Sensor-Fault-Detection/assets/38419795/9440c21b-b466-4076-8ef8-2034de278b3f)



