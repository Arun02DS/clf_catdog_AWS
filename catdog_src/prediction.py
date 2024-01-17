from catdog_src.logger import logging
from catdog_src.exception import CatDogException
import os,sys



class CatDog:
    def __init__(self,filename):
        try:
            logging.info(f"{'||||'*5} Prediction {'||||'*5}" )
            self.filename = filename
        except Exception as e:
            raise CatDogException(e,sys)

    def predictioncatdog(self)->int:
        
        """
        Description: This function loads model and predict outcome.

        Return: Interger output (0,1)

        """

        try:
            
        except Exception as e:
            raise CatDogException(e,sys)

    