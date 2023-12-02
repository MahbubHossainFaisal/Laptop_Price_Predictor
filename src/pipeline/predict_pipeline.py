import sys
import os
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)

class CustomData:
    def __init__(self,
                Company:str,
                TypeName:str,
                Ram: int,
                Weight:float,
                Touchscreen:bool,
                IPS:bool,
                Screen_Resolution:str,
                size:float,
                Cpu_Brand:str,
                HDD:int,
                SSD:int,
                Hybrid:int,
                Flash_Storage:int,
                Gpu_Brand:str,
                Os:str):

        
        self.Company = Company

        self.TypeName = TypeName

        self.Ram = Ram

        self.Weight = Weight

        self.Touchscreen = Touchscreen

        self.IPS = IPS
         	                
        self.PPI = ((int(Screen_Resolution.split('x')[0]))**2 + (int(Screen_Resolution.split('x')[1]))**2)**.5 / float(size)

        self.Cpu_Brand = Cpu_Brand

        self.HDD = HDD

        self.SSD = SSD

        self.Hybrid = Hybrid

        self.Flash_Storage = Flash_Storage

        self.Gpu_Brand = Gpu_Brand

        self.Os = Os



    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "Company": [self.Company],
                "TypeName": [self.TypeName],
                "Ram(GB)": [self.Ram],
                "Weight(kg)": [self.Weight],
                "Touchscreen": [self.Touchscreen],
                "IPS": [self.IPS],
                "PPI": [self.PPI],
                "Cpu_Brand": [self.Cpu_Brand],
                "HDD(GB)": [self.HDD],
                "SSD(GB)": [self.SSD],
                "Hybrid(GB)": [self.Hybrid],
                "Flash_Storage(GB)": [self.Flash_Storage],
                "Gpu_Brand": [self.Gpu_Brand],
                "Os": [self.Os]

            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)