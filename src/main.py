import tensorflow as tf
import pandas as pd

class TrainData():
    def __init__(self, filepath):
        self.filepath = filepath;
        self.dataframe = None;
        return

    def getDataFromCSV(self):
        if (self.dataframe == None):
            self.dataframe = pd.read_csv(self.filepath)
        else:
            print("The data Frame is already created")
        return self.dataframe

    def getDataFromEXCEL(self):
        if(self.dataframe == None):
            self.dataframe = pd.read_excel(self.filepath)
        else:
            print("The data Frame is already created")
        return

    def showHeadOfDataframe(self):
        print(self.dataframe.head())
        return

instance = TrainData("C:/Users/Jigar/Desktop/Titanic-Machine-Learning-From-Disaster/data/train.csv")

instance.showHeadOfDataframe()

