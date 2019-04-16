import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt

class DataRepresentation():
    def __init__(self, dataframe={}):
        self.dataframe = pd.DataFrame.from_dict(dataframe);
        return

    def printHead(self, num_of_entries=5):
        print(self.dataframe.head(num_of_entries));
        return

    def printStatastic(self):
        print(self.dataframe.describe());
        return

    def printconfusionMatrix(self, output_label = ''):
        pass

    def printScatterPlot(self, output_label =''):
        plt.scatter(x=self.dataframe.drop(labels=output_label, axis=1), y=self.dataframe[output_label], marker = '*');
        plt.show();
        return

    def printConfuionMatrix(self):
        pass


