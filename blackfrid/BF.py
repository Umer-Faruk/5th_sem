'''6. Python for Data Science: Load Black Friday Dataset into one of the data structures (NumPy or Pandas). Perform data pre-processing on this dataset. Create dataframes, perform computations and visualize the results appropriately.'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

umer = pd.read_csv("blackfri.csv")
print(umer.head(5))
umer.info()
umer.drop(['City_Category','Purchase','Product_ID'],axis=1,inplace=True)
umer.info()


umer['Gender']=umer['Gender'].map({'F': 0,'M':1})
print(umer.head(5))

umer['Wine_Tumblers'] = umer['Wine_Tumblers'].fillna('gandooo')
print(umer.head(5))

umer.rename(columns={'Gender':'Sex'}, inplace=True)
print(umer.head(5))

print(umer.tail(2))

print(pd.crosstab(umer['Sex'],umer.Age))
vinay = sns.countplot(x='Sex',hue='Age',data=umer)
vinay.set(title='my_graph',xlabel='Gender',ylabel='Age range')
plt.show()


