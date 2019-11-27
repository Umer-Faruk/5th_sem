'''Python for Data Science: Load Iris Dataset into one of the data structures (NumPy or Pandas). Perform data pre-processing on this dataset. Create dataframes, perform computations and visualize the results appropriately.'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ddata =pd.read_csv('iris.csv')
print(ddata)

ddata.info()
ddata.describe()

print(ddata.head(5))
print(ddata.tail(6))

#droping the column

ddata.drop(['Sepal_Length'],axis=1,inplace=True)
ddata.info()

#print(data.head(5))

#plt.figure(figsize=[12,6])
print(pd.crosstab([' Sepal_Width'],ddata.Class))
sns.countplot(x=' Sepal_Width',hue='Class',data=ddata)
plt.tight_layout()
#plt.show()


i =(0,1,2,4)
c=['<1','1 to 2','>2']
ddata[' Petal_Length']=pd.cut(ddata[' Petal_Length'],i,labels=c)
print(pd.crosstab([' Petal_Length'],ddata.Class))

sns.countplot(x=' Petal_Length',hue='Class',data=ddata)
#plt.show()


plt.figure(figsize=[12,6])

ax = sns.countplot(data = ddata[ddata['Class'] == 'Iris-setosa'],
                     x = ' Sepal_Width',palette='Set1')


ax.set(title='Iris-setosa',xlabel='Sepal Width',ylabel='No. of flowers')
plt.show()









