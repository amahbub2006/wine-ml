from wineml.logging.logger import logger
from wineml.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

from wineml.config.configuration import ConfigurationManager

config = ConfigurationManager()
data_ingestion_config = config.get_data_ingestion_config()


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