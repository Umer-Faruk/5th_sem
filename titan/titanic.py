'''Python for Data Science: Load Titanic Dataset into one of the data structures (NumPy or Pandas). Perform data pre-processing on this dataset. Create dataframes, perform computations and visualize the results appropriately.'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#reading or inporint the data file using '.read_csv() ' method of pandas
tita_data =pd.read_csv('data.csv')
print(tita_data)

#we can view the only some number of rows using '.head()' method of pandas
print(tita_data.head(5))

#we can get the breef details of input file using '.info()' method of pandas
tita_data.info()
#tita_data.describe()

#altering the data replacing values 
#replacing the SexCode value 0 ,1 with F and M using '.map()' method

tita_data['SexCode']=tita_data['SexCode'].map({0:'F',1:'M'})

print(tita_data.head(5))


#droping the columns
#droping unwanted columns

tita_data.drop(['SexCode','PassengerID','Name'],axis=1,inplace=True)

tita_data.info()
print(tita_data.head(10))


#fill all null values with S in Name column setting the defult value
#tita_data['Name']=tita_data['Name'].fillna("S")

#ploing the graph and visualizing the data 
print("\n\n\n**** DATA VISUALIZATIONS****\n\n")

#ax=sns.countplot(x='Sex', hue='Survived',palette='Set1',data=tita_data)

#ax.set(title='testing',xlabel='Sex',ylabel='ser')
#plt.show()

print(pd.crosstab(tita_data["Sex"],tita_data.Survived))


# # We look at Age column and set Intevals on the ages and the map them to their categories as
# # (Children, Teen, Adult, Old)

print(pd.crosstab(tita_data["Sex"],tita_data.Age))

#to reduse the columns we are grouping the age

agp=(0,18,35,60,120)
cg=['children','teen','adult','old']
tita_data['Age']=pd.cut(tita_data.Age,agp,labels=cg)
print(pd.crosstab(tita_data["Sex"],tita_data.Age))

#age and sex
ax=sns.countplot(x='Age',hue='Sex',data=tita_data)
plt.show()

#age and survival rate
print(pd.crosstab(tita_data['Survived'],tita_data.Age))

ax=sns.countplot(x='Age',hue='Survived',data=tita_data)
plt.show()









