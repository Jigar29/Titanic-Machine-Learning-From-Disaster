import tensorflow as tf
import pandas as pd

class Datapreparation(object):

    def __init__(self, filepath):
        self.filepath = filepath
        self.dataframe = pd.DataFrame()
        return

    '''Fuction to create the pandas dataframe from CSV File'''
    def createDataFrameFromCSVFile(self):
        if (self.dataframe.empty):
            self.dataframe = pd.read_csv(self.filepath)
        else:
            print("The DataFrame is already created")

        return

    '''Fuction to create the pandas dataframe from Excel File'''
    def createDataFrameFromExcelFile(self):
        if(self.dataframe.empty):
            self.dataframe = pd.read_excel(self.filepath)
        else:
            print("The DataFrame is already created")

        return

    '''Fuction to create the tensor object from Excel File'''
    def createTensorObjectFromCSVFile(self):
        self.tensor = tf.read_file(self.filepath, "Data_Tensor")
        return

    def createTensorObjectFromExcelFile(self):
        self.tensor = tf.read_file(self.filepath, "Data_Tensor")
        return

''' Singleton Class for Titanic Problem'''
''' Inherits DataPreparation Class'''
class Titanic(Datapreparation):

    ##copy of the class instance
    class_instance = None

    def __init__(self, train_filepath, test_filepath):
        if(Titanic.class_instance != None):
            raise Exception("The Class is Singlton, can not create more than one objects")
        else:
            Titanic.class_instance = self
            self.training_object = Datapreparation(train_filepath)
            self.test_object = Datapreparation(test_filepath)
            self.training_object.createDataFrameFromCSVFile()
            self.test_object.createDataFrameFromCSVFile()
        return

    @classmethod
    def getInstance(cls, train_filepath, test_filepath):
        if(cls.class_instance == None):
            cls(train_filepath, test_filepath)

        return Titanic.class_instance
