import datetime
import pandas as pd
#from matplotlib import pyplot as plt
#import seaborn as sns
#import numpy as np

def readDataAndfix():
    data1 = pd.read_csv('data.csv', index_col=0, encoding='ISO-8859-1')
    data2 = pd.read_csv('data-2.csv', index_col=0, encoding='ISO-8859-1')
    data3 = pd.read_csv('data-3.csv', index_col=0, encoding='ISO-8859-1')

    yearWeek = data1.loc[:, 'year_week']

    def fixDate(row):
        date = datetime.datetime.strptime(row + '-1', '%Y-W%W-%w')
        return date

    for row in yearWeek:
        fixDate(row)

    data1['formatted_date'] = yearWeek.apply(fixDate)
    print(data1)




