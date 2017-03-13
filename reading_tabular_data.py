import pandas as pd

orders = pd.read_table('data/chipotle.tsv')

#read_table assumes that your data is tab seperated
#Assumes that the first row is the header
#Works perfectly with this dataset

#Delimeter to use if data is not tab is 'sep='
#Without a header use argument 'header = None'

headers = ['user_id','age','gender','occupation','zip_code']

movieUsers =  pd.read_table('data/u.user', sep = '|', header = None, names = headers)

