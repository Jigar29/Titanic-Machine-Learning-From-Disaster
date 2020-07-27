import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sbn

class DataRepresentation():
    def __init__(self, dataframe={}):
        if dataframe is {}:
            print("Dataset passed is null. Please provide valid Dataset to create an object of this class");
            raise Exception("Dataframe can not be null for DataRepresentation class")
        else:
            self.dataframe = pd.DataFrame.from_dict(dataframe);

        return

    def printHead(self, num_of_entries=5):
        print("", "********************Dataset Head*********************", self.dataframe.head(num_of_entries), sep='\n');
        return

    def printTail(self, num_of_entries=5):
        print("", "********************Dataset Tail*********************", self.dataframe.tail(num_of_entries), sep='\n');
        return

    def printShape(self):
        print("", "********************Dataset Size*********************", self.dataframe.shape,
              sep='\n');
        return

    def printUniquevalues(self):
        print("", "**************Unique Values per Column***************", sep='\n');
        for i in self.dataframe.columns:
            print(i, self.dataframe[i].unique(), sep='\n')
        return

    def printNumberofUniquevalues(self):
        print("", "**********Num of Unique Values per Column************", self.dataframe.nunique(), sep='\n');
        return

    def printNULLvalueCount(self):
        print("", "************Null value count for Dataset*************", self.dataframe.isnull().sum(), sep='\n');
        return

    def printStatastic(self):
        print("", "******************Dataset Statistics*****************", self.dataframe.describe(), sep='\n');
        return

    def printCorrelationMatrix(self):
        print("", "******************Correlation Matrix*****************", self.dataframe.corr(), sep='\n');
        return

    def printColumns(self):
        print("", "*******************Dataset Columns*******************", self.dataframe.columns, sep='\n');
        return

    def printGlimpse(self, num_of_entries=5):
        print("", "********************************Dataset Birdeye View********************************", sep='\n');
        self.printHead(num_of_entries)
        self.printTail(num_of_entries)
        self.printShape()
        self.printColumns()
        self.printNULLvalueCount()
        self.printNumberofUniquevalues()
        self.printStatastic()
        return

    def plotHeatmap(self, column="NULL"):
        if column == "NULL":
            sbn.heatmap(self.dataframe.isnull(),
                        xticklabels=self.dataframe.columns,
                        yticklabels=False, cmap='viridis');
            plt.title("NaN Heatmap")
        else:
            sbn.heatmap(self.dataframe[column],
                        xticklabels=self.dataframe.columns,
                        yticklabels=self.dataframe.columns,
                        cmap='viridis');
            plt.title("Heatmap")

        plt.show()
        return

    def plotHistogram(self, column='null'):
        if column != 'null':
            for i in column:
              sbn.distplot(self.dataframe[i].dropna(axis=0))
              plt.title("Histogram for " + i)
              plt.show()
        else:
            raise Exception("Column can not be left blank or set to 'NULL' for Histogram")
        return

    def plotBoxplot(self, x_data, y_data):
        sbn.boxplot(data=self.dataframe, x=x_data, y=y_data, palette='winter')
        plt.title("BoxPlot: "+x_data+" vs "+y_data)
        plt.show()
        return

    def plotCorrelationMatrix(self):
        correlation = self.dataframe.corr();
        sbn.heatmap(data=correlation,
                    xticklabels=correlation.columns,
                    yticklabels=correlation.columns,
                    cmap='viridis', annot=True)
        plt.title("Correlation Matrix")
        plt.show()
        return

    def printconfusionMatrix(self, output_label = ''):
        print("Confusion matrix not supported yet");
        pass

    def plotContplot(self, xdata="", hue=""):
        sbn.countplot(data= self.dataframe, x=xdata, hue = hue);
        plt.title("CountPlot: "+xdata+" vs "+hue)
        plt.show()
        return

    def plotPairPlot(self):
        sbn.pairplot(self.dataframe)
        plt.title("Pair Plot")
        plt.show();
        return

    def plotScatterPlot(self, x_data, ydata, hue):
        sbn.relplot(data=self.dataframe.dropna(axis=0),
                    x=x_data,
                    y=ydata,
                    hue=hue);
        plt.title("Scatter Plot:"+x_data+" vs "+ydata+" With Hue: "+hue)
        plt.show();
        return

    def __del__(self):
        del self
        print("Object of DataRepresentation class is freed")
        return

