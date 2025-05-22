from books_recommender.components.stage_00_data_ingestion import DataIngestion
from books_recommender.exception.exception_handler import AppException
import sys

class TrainingPipeline:
    def __init__(self):
        self.data_ingestion = DataIngestion()
    
    def start_data_ingestion(self):
        """
        Start the data ingestion process
        """
        try:
            self.data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise AppException(e, sys) from e