from catdog_src.logger import logging
from catdog_src.exception import CatDogException
import os,sys
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np





class CatDog:
    def __init__(self,filename):
        try:
            logging.info(f"{'||||'*5} Prediction {'||||'*5}" )
            self.filename = filename
        except Exception as e:
            raise CatDogException(e,sys)

    def predictioncatdog(self)->str:
        
        """
        Description: This function loads model and predict outcome.

        Return: Interger output (0,1)

        """

        try:
            #loading model
            logging.info(f"loading model")
            model = load_model(os.path.join('model','model_clf.h5'))

            logging.info(f"loading test image")
            imagename=self.filename

            test_image=image.load_img(imagename,target_size=(224,224))
            #test_image=image.load_img(imagename,target_size=(64,64))
            test_image=image.img_to_array(test_image)
            test_image=np.expand_dims(test_image,axis=0)
            result=np.argmax(model.predict(test_image),axis=1)

            logging.info(f"result: {result}")
            print(result)

            if result[0]==1:
                prediction='dog'
                logging.info(f"Image provided is {prediction}")
                return [{"image":prediction}]
            else:
                prediction='cat'
                logging.info(f"Image provided is {prediction}")
                return [{"image":prediction}]

        except Exception as e:
            raise CatDogException(e,sys)

    