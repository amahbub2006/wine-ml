from wineml.logging.logger import logger
from wineml.config.configuration import ConfigurationManager

from wineml.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from wineml.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from wineml.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from wineml.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline


config = ConfigurationManager()
data_ingestion_config = config.get_data_ingestion_config()

# Stage 1: Data Ingestion
STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx<<<")
    logger.info(f"{'>>'*20} {STAGE_NAME} completed {'<<'*20}")
except Exception as e:
    logger.exception(e)
    raise e

# Stage 2: Data Validation
STAGE_NAME = "Data Validation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    logger.info(f"{'>>'*20} {STAGE_NAME} completed {'<<'*20}")
except Exception as e:
    logger.exception(e)
    raise e

# Stage 3: Data Transformation
STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

# Stage 4: Model Trainer
STAGE_NAME = "Model Trainer stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e