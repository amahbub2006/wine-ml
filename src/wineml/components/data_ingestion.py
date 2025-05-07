import os
import urllib.request as request
import zipfile
import pandas as pd
from pathlib import Path
from wineml.logging.logger import logger
from wineml.utils.common import get_size
from wineml.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} downloaded successfully! \nHeaders:\n{headers}")
        else:
            logger.info(f"File already exists — size: {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        """
        Extracts the downloaded zip file into the unzip directory,
        removes 'Id' column from any CSV files found,
        and overwrites them without the column.
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)

        logger.info(f"Data extracted to: {unzip_path}")

        # Drop 'Id' column from any CSVs in the extracted folder
        for file_name in os.listdir(unzip_path):
            if file_name.endswith(".csv"):
                file_path = os.path.join(unzip_path, file_name)
                try:
                    df = pd.read_csv(file_path)
                    if "Id" in df.columns:
                        df.drop("Id", axis=1, inplace=True)
                        df.to_csv(file_path, index=False)
                        logger.info(f"'Id' column dropped and {file_name} saved.")
                    else:
                        logger.info(f"No 'Id' column found in {file_name}, skipping.")
                except Exception as e:
                    logger.error(f"Failed to process {file_name}: {e}")
