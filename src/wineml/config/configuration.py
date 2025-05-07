from pathlib import Path
from box import ConfigBox
from wineml.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH, SCHEMA_FILE_PATH
from wineml.utils.common import read_yaml, create_directories
from wineml.entity.config_entity import (DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig)


class ConfigurationManager:
    def __init__(
        self,
        config_filepath: Path = CONFIG_FILE_PATH,
        params_filepath: Path = PARAMS_FILE_PATH,
        schema_filepath: Path = SCHEMA_FILE_PATH
    ):
        self.config: ConfigBox = read_yaml(config_filepath)
        self.params: ConfigBox = read_yaml(params_filepath)

        # Optional schema loading
        self.schema: ConfigBox | None = None
        if schema_filepath.exists():
            self.schema = read_yaml(schema_filepath)

        create_directories([Path(self.config.artifacts_root)])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([Path(config.root_dir)])

        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(config.root_dir),
            source_URL=config.source_URL,
            local_data_file=Path(config.local_data_file),
            unzip_dir=Path(config.unzip_dir)
        )

        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS if self.schema else {}

        create_directories([Path(config.root_dir)])

        data_validation_config = DataValidationConfig(
            root_dir=Path(config.root_dir),
            STATUS_FILE=Path(config.STATUS_FILE),
            unzip_data_dir=Path(config.unzip_data_dir),
            all_schema=schema  # schema is now a dict
        )
        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path
        )

        return data_transformation_config

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN if self.schema else {}

        create_directories([Path(config.root_dir)])

        return ModelTrainerConfig(
            root_dir=Path(config.root_dir),
            train_data_path=Path(config.train_data_path),
            test_data_path=Path(config.test_data_path),
            model_name=config.model_name,
            alpha=params.alpha,
            l1_ratio=params.l1_ratio,
            target_column=self.params.target_column
    )