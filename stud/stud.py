import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sdata=pd.read_csv('stud.csv')
print(sdata)

sdata.info()
print(sdata.head(5))


#sdata['gender']=sdata['gender'].map({'female':0,'male':1})

print(sdata.head(5))

#droping the columns
#sdata.drop(['lunch','test preparation course'],axis=1,inplace=True)

sdata.info()

print(sdata.head(7))


#seting the defult value

sdata['parental level of education']=sdata['parental level of education'].fillna("not application")
print(sdata.head(9))
print(sdata.tail(9))

##Convert the attribute ‘race/ethnicity’ to have ‘groupA’ to be ‘Asian Students’, ‘groupB’ to be ‘African Students’ ,  ‘groupC’ to be ‘Afro-Asian #Students’, ‘groupD’ to be ‘American Students’ and ‘groupE’ to be ‘European Students#

'''sdata['race/ethnicity'] = sdata['race/ethnicity'].map({'group A':'Asian Students','group B':'African Students','group C':'Afro-Asian','group D':'American Students','group E':'European Students'})'''

print(sdata.head(5))


#  #Tally of the Number of Male & Female students who took up the ‘test preparation course’ and those who did not.

print(pd.crosstab(sdata['gender'],sdata.test_preparation_course))

#ploting the graph
ax=sns.countplot(x='test_preparation_course',hue='gender',data=sdata)
#plt.show()

# #Total Number of Male & Female Students belonging to each student group 


print(pd.crosstab(sdata['race/ethnicity'],sdata.gender))
#ploting graph

ax=sns.countplot('race/ethnicity',hue='gender',data=sdata)
#we cal label the axis
ax.set(title='givinght title',xlabel='groups',ylabel='sex')
#plt.show()

#No of students who ‘failed’(less than 40), ‘second class’(between 40 & 50).
# #'first class’(between 60 & 75) and ‘distinction’(above 75) in ‘Maths’ and ‘Reading’ and ‘Writing’.

r=(0,40,50,60,75)
l=['failed','second class','first class','distinction']

sdata['mathscore']=pd.cut(sdata.mathscore,r,labels=l)
print(pd.crosstab(sdata['mathscore'],sdata.gender))

#plot in math
#palette=Set 1,2,3    .... to giv deff coluer to graph
sns.countplot(x='mathscore',hue='gender',palette='Set3',data=sdata)
plt.show()

#grouping the score
sdata['readingscore']=pd.cut(sdata.readingscore,r,labels=l)
print(pd.crosstab(sdata['readingscore'],sdata.gender))
#plot in reading
sns.countplot('readingscore',hue='gender',data=sdata)
plt.show()

#grouping the score
sdata['writingscore']=pd.cut(sdata.writingscore,r,labels=l)
print(pd.crosstab(sdata['writingscore'],sdata.gender))
#plot writing
sns.countplot('writingscore',hue='gender',data=sdata)
plt.show()




























