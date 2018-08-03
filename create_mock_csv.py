'''
This is a script for generaing mock data/dataset as a csv file

you have to pass the file name with a .csv extension for example test.csv

You can add columns of your choice so you have to change both DictWriter and writerow

Currently it is genrating a csv file with 3 cols BrnadID,ID(userID),Tran_date(transaction Date) which I needed for some Machine Learning stuff

Variables:
    faker {[Module]} -- [Genrates fake data you can check the official documentation for more info]
'''



import sys
import os
from faker import Factory
import csv
from datetime import datetime
import random
from random import randint 

faker=Factory.create()
def randomEnumerator():
    howManyRows = 1000000
    for currentRowNumber in range(0, howManyRows):
        yield currentRowNumber

# def date_between(d1, d2):
#     f = '%b%d-%Y'
#     return faker.date_time_between_dates(datetime.strptime(d1, f), datetime.strptime(d2, f))

# year = random.randint(2016, 2017)
# month = random.randint(1, 12)
# day = random.randint(1, 30)    

def main(filename):
    '''It is the main function whhich does the main task :p
    
    Arguments:
        filename {[string]} -- [filname -> filename.csv]
    '''
    filename=str(filename)
    f = open(filename, 'w' )
    fieldnames=['BrandID','ID','Tran_date']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    
    for current in randomEnumerator():
        writer.writerow(  dict(
        	BrandID=str(randint(1,2000)),
        	ID=str(random.choice([1,2])),
        	Tran_date=str(faker.date_between(datetime(2016,3,4),datetime(2017,3,4))),
        	))
    f.close()

    df=pd.read_csv(filename)
    df.columns= fieldnames
    df.to_csv(filename)

main(filename)