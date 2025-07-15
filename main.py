from network_security.components.data_ingestion import DataIngestion
from network_security.components.data_validation import DataValidation
from network_security.components.data_transformation import DataTransformation
from network_security.components.model_trainer import ModelTrainer

from network_security.exceptions.exception import NetworkSecurityException
from network_security.logging.logger import logging
from network_security.entities.config_entity import DataIngestionConfig
from network_security.entities.config_entity import DataValidationConfig
from network_security.entities.config_entity import DataTransformationConfig
from network_security.entities.config_entity import TrainingPipelineConfig
from network_security.entities.config_entity import ModelTrainerConfig


import sys

if __name__=='__main__':
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation completed")
        print(dataingestionartifact)
        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        data_validation = DataValidation(dataingestionartifact,data_validation_config)
        logging.info("Initiate the data validation")
        data_validation_artifact = data_validation.initiate_data_validation()
        print(data_validation_artifact)
        logging.info("Data Validation complete")
        data_transformation_config = DataTransformationConfig(trainingpipelineconfig)
        logging.info("data transformation started")
        data_transformation = DataTransformation(data_validation_artifact, data_transformation_config)
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("data transformation completed")
        logging.info("Model Training started")
        logging.info("Model Training started")
        model_trainer_config = ModelTrainerConfig(trainingpipelineconfig)
        model_trainer=ModelTrainer(model_trainer_config=model_trainer_config,data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact=model_trainer.initiate_model_trainer()

        logging.info("Model Training artifact created")
        
    except Exception as e:
        raise NetworkSecurityException(e,sys)
