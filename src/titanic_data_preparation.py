from src.legacy.data_preparation import Datapreparation

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