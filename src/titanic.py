from src.data_preparation import Datapreparation
from src.data_preprocessing import DataPreprocessing
from src.model import Model
from src.data_representation import DataRepresentation
from src.model import Model
from sklearn.preprocessing import LabelEncoder

import pandas as pd

''' Singleton Class for Titanic Problem'''
''' Inherits DataPreparation Class'''
class Titanic(Datapreparation):

    #copy of the class instance
    class_instance = None

    def __init__(self, train_filepath, test_filepath, submission_filepath):
        if(Titanic.class_instance != None):
            raise Exception("The Class is Singlton, can not create more than one objects")
        else:
            Titanic.class_instance = self
            self.train_dataset_path = train_filepath;
            self.test_dataset_path  = test_filepath;
            self.submission_filepath = submission_filepath;
            self.training_dataframe = pd.DataFrame.from_dict({});
            self.testing_dataframe = pd.DataFrame.from_dict({});
            self.submission_dataframe = pd.DataFrame(columns=['PassengerId', 'Survived'], index=None);
            self.model = Model();                       #to be fixed
            self.training_dataPrep_object = Datapreparation(self.train_dataset_path);
            self.test_dataPrep_object = Datapreparation(self.test_dataset_path);
            self.model = Model(model_type='LogisticRegression');
        return

    @classmethod
    def getInstance(cls, train_filepath, test_filepath, submission_filepath):
        if(cls.class_instance == None):
            cls(train_filepath, test_filepath, submission_filepath)
        return cls.class_instance

    def prepareData(self):                  #to be fixed for tensorflow
        self.training_dataframe_const = self.training_dataPrep_object.createDataFrameFromCSVFile();
        self.testing_dataframe_const = self.test_dataPrep_object.createDataFrameFromCSVFile();
        return

    def preProcessData(self):
        training_preprocessing_obj = DataPreprocessing(dataframe=self.training_dataframe_const);
        testing_preprocessing_obj  = DataPreprocessing(dataframe=self.testing_dataframe_const);
        submission_preprocessing_obj = DataPreprocessing(dataframe=self.testing_dataframe_const);

        def replaceNULL(dataframe):
            for index, row in dataframe.iterrows():
                temp = row.isnull()
                if temp['Age']:
                    if row['Pclass'] == 1:
                        dataframe['Age'].loc[index] = 37
                    elif row['Pclass'] == 2:
                        dataframe['Age'].loc[index] = 29
                    elif row['Pclass'] == 3:
                        dataframe['Age'].loc[index] = 24
            return dataframe

        ################################Submission Preprocessing######################################
        temp_df = submission_preprocessing_obj.dropColumns(col_list=["Fare", "Cabin", "Ticket", "Name", "Embarked"]);
        self.submission_dataframe['PassengerId'] = temp_df['PassengerId'];

        ################################Training Dataset Preprocessing######################################
        self.training_dataframe = training_preprocessing_obj.dropColumns(col_list=["PassengerId", 'Name', 'Ticket', 'Cabin'])
        self.training_dataframe = training_preprocessing_obj.oneHotEncoding(['Sex', 'Embarked'])
        self.training_dataframe = replaceNULL(self.training_dataframe)
        self.training_dataframe = training_preprocessing_obj.minMaxScaling(self.training_dataframe);

        ################################Testing Dataset Preprocessing#######################################
        self.testing_dataframe = testing_preprocessing_obj.dropColumns(col_list=["PassengerId", 'Name', 'Ticket', 'Cabin'])
        self.testing_dataframe = testing_preprocessing_obj.oneHotEncoding(['Sex', 'Embarked'])
        self.testing_dataframe = replaceNULL(self.testing_dataframe)
        self.testing_dataframe = testing_preprocessing_obj.minMaxScaling(self.testing_dataframe);
        print("Data Pre-processing Completed");
        return

    def representData(self):
        representation_obj = DataRepresentation(dataframe=self.training_dataframe);
        representation_obj.printGlimpse(num_of_entries=10);
        representation_obj.plotHeatmap(column="NULL");
        representation_obj.plotCorrelationMatrix();
        representation_obj.plotHistogram(column=["Age", "Pclass"])
        representation_obj.plotContplot("Survived", "Sex");
        representation_obj.plotBoxplot(x_data='Pclass', y_data='Age')
        representation_obj.plotBoxplot(x_data='SibSp', y_data='Age')
        representation_obj.plotScatterPlot(x_data='Pclass', ydata='Age', hue="Sex")
        return

    def buildSubmissionFile(self, labels=[]):
        self.submission_dataframe['Survived'] = pd.DataFrame.from_dict({'Survived':labels});
        print("Generating the Submission File...");
        self.submission_dataframe.to_csv(path_or_buf=self.submission_filepath, index=None);
        return

    def autoRun(self):
        self.prepareData();
        self.preProcessData();
        self.model.trainModel(features=self.training_dataframe.drop(labels='Survived', axis=1), labels= self.training_dataframe['Survived']);
        self.predicted_lables = self.model.predictTheModel(self.training_dataframe.drop(labels='Survived', axis=1));
        self.buildSubmissionFile(labels=self.predicted_lables);
        return