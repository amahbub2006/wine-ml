import os 
from wineml.logging.logger import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from wineml.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
    
    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)

        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("training and test set split completed.")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)