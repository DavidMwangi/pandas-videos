import pandas as pd 

headers = ["user_id", "age", "gender", "occupation","zip_code"]

data = pd.read_csv('data/u.user', sep = '|', names = headers)

data.set_index('user_id', inplace=True)#sets user_id as the index

#SLICING DATA FRAMES 

print(data[5:10])#Carrying out slicing operation just like on other data types

ofinterest = ['age','gender','occupation']#Speciffy the columns you are interested in

print(data[ofinterest].head())#head function prints the first 5 entities of the interested fileds in the dataframe

print(data[data.age>30].tail(15))
"""

The concept of boolean indexation. 
Data can be manipulated to make queries of specific interest.
In the example above the last 15 entries whose age are over 30 years will be printed out.
The head and tail functions can take parameters specifying the number needed.

Multiples queries can be made in a single statement.
See below

"""

print(data[(data.gender == 'M') & (data.age>30)].head())#the first 5 male users over 30 years of age

#We would also want to know just their occupations

print(data['occupation'][(data.gender == 'M') & (data.age>30)].head())#Occupations of the first 5 male users over 30 years of age

#The count function.

#1. List all male and female occupations and count number of people in each

print("All male occupations and number of people in each\n")

print(data['occupation'][data.gender == 'M'].value_counts())

print("All female occupations and number of people in each\n")

print(data['occupation'][data.gender == 'F'].value_counts())

#Gender comparison

print("Gender Count: \n")

print(data.gender.value_counts())