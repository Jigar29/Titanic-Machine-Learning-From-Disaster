from src.data_preparation import Datapreparation
from src.data_preprocessing import DaraPreprocessing
from src.model import Model
from src.data_representation import DataRepresentation
import pandas as pd

''' Singleton Class for Titanic Problem'''
''' Inherits DataPreparation Class'''
class Titanic(Datapreparation):

    #copy of the class instance
    class_instance = None

    def __init__(self, train_filepath, test_filepath):
        if(Titanic.class_instance != None):
            raise Exception("The Class is Singlton, can not create more than one objects")
        else:
            Titanic.class_instance = self
            self.train_dataset_path = train_filepath;
            self.test_dataset_path  = test_filepath;
            self.training_datafrme = pd.DataFrame.from_dict({});
            self.testing_dataframe = pd.DataFrame.from_dict({});
            self.model = Model();                       #to be fixed
            self.training_object = Datapreparation(self.train_dataset_path);
            self.test_object = Datapreparation(self.test_dataset_path);
        return

    @classmethod
    def getInstance(cls, train_filepath, test_filepath):
        if(cls.class_instance == None):
            cls(train_filepath, test_filepath)
        return cls.class_instance

    def prepareData(self):                  #to be fixed for tensorflow
        self.training_datafrme = self.training_object.createDataFrameFromCSVFile();
        self.testing_dataframe = self.test_object.createDataFrameFromCSVFile();
        return

    def preProcessData(self):                #Tobe fixed for tensorflow
        training_preprocessing_obj = DaraPreprocessing(dataframe=self.training_datafrme);
        testing_preprocessing_obj  = DaraPreprocessing(dataframe=self.testing_dataframe);

        ################################Training Dataset Preprocessing######################################
        self.training_datafrme = training_preprocessing_obj.dropAColumn(col_str=["Fare", "Cabin", "Ticket", "Name", "Embarked"]);
        self.training_datafrme = training_preprocessing_obj.dropNA();
        self.training_datafrme = training_preprocessing_obj.labelEncoding("Sex");
        self.training_datafrme = training_preprocessing_obj.minMaxScaling(y_label="Survived");
        print("[EXIT] Preprocessing Completed");
        return

    def representData(self):
        self.prepareData();
        self.preProcessData();
        representation_obj = DataRepresentation(dataframe=self.training_datafrme);
        representation_obj.printHead(10);
        representation_obj.printStatastic();
        representation_obj.printScatterPlot("Survived");
        return

    def autoRun(self):
        self.prepareData();
        self.preProcessData();
        print(self.training_datafrme);
        return
