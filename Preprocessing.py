import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing


class ETL(object):

    """
    Owner: Jens Ponnet
    Date: 15/07/2016
    Functionality: This class offers methods for extracting, transforming and loading data
    Included methods:
        - extractFromCSV: extracts data from a CSV file and returns it into a pandas data frame
    """
    def extractFromCSV(self, filepath):
        if type(filepath) == str:
            df = pd.read_csv(filepath, delimiter=",")
            return df
        else:
            return "filepath is not a string"

    def splitXY(self,inputselection,outputselection,filepath):
        df = self.extractFromCSV(filepath)
        list1 = np.array(inputselection)
        list2 = np.array(outputselection)
        x = df.as_matrix(columns=list1.tolist())
        y = df.as_matrix(columns=list2.tolist())
        # Y = np.reshape(np.array(df[outputselection]),(-1,1))
        return x, y

    def normalize(self,dataset):
        min_max_scaler = preprocessing.MinMaxScaler()
        dataset = min_max_scaler.fit_transform(dataset)
        return dataset

    def scaleback(self,dataset):
        min_max_scaler = preprocessing.MinMaxScaler()
        dataset = min_max_scaler.inverse_transform(dataset)
        return dataset

    def takeOutValidationData(self, dataset, number):
            total_rows = len(dataset)
            dataset_holdin = dataset[:(total_rows-1-number)]
            dataset_holdout = dataset[(total_rows-number):]
            return dataset_holdin, dataset_holdout
