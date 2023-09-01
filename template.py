# Purpose of Template.py is to create a folder structure of our project. Rather than manual creation it will create all folders which we will be using in our project.
# Within each folders, it will create the filenames where we will be writing our code.

import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "signLanguage"

# In list_of_files mention all the folders  and filenames within each folders which we want in our project
list_of_files = [
    ".github/workflows/.gitkeep",
    "data/.gitkeep",
    "docs/.gitkeep",
    # Constructor to treat module as package
    f"{project_name}/__init__.py",
    # Different components of the Deep Learning Project 
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_pusher.py",
    # code for S3 bucket
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/s3_operations.py",
    # Code for constant
    f"{project_name}/constant/__init__.py",
    f"{project_name}/constant/training_pipeline/__init__.py",
    f"{project_name}/constant/application.py",
    # Code for entity
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/artifacts_entity.py",
    f"{project_name}/entity/config_entity.py",
    # Code for exception
    f"{project_name}/exception/__init__.py",
    # Code for logger
    f"{project_name}/logger/__init__.py",
    # Code for Pipeline
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    # Code for Utilites
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "template/index.html",
    ".dockerignore",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
]



# For loop to read complete folder list and then create folder struture and respetive file name in the folder
for filepath in list_of_files:
    filepath = Path(filepath)

# it will separate file name from the directory name. Example if we have path = "sign_language/pipeline/training_pipeline.py"
# os.path.split(path) will store filedir and filename as ('sign_language/pipeline', 'training_pipeline.py') respectively.
    filedir, filename = os.path.split(filepath)

# if File directory is not spaces then it will create the directory
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

# if filename does not exists then it will create the filename    
    if(not os.path.exists(filename)) or (os.path.getsize(filename) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filename}")

# Else it will log that file already exists    
    else:
        logging.info(f"{filename} is already created")







