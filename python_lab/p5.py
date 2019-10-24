# Python File Handling & List Comprehension: Write a python program to read contents of a file
# (filename as argument) and store number of occurrences of each word in a dictionary. Display the top 10
# words with most number of occurrences in descending order. Store the length of each of these words in a
# list and display the list. Write a one-line reduce function to get the average length and one-line list
# comprehension to display squares of all odd numbers and display both.
import sys
import functools

# print ('Number of arguments:', len(sys.argv), 'arguments.')
# print ('Argument List:', str(sys.argv))
d={}
l1=[] #to store the len of each word
f=open(sys.argv[1])
data=f.read().split()
#data=data.split()
for word in data:
    if word not in d:
        l1.append(len(word))
        d[word]=0
    d[word] += 1 #if word already exist incre

l2=[]
for k,v in d.items():
    l2.append([v,k])
l2.sort(reverse=True)   
print(l2)


for k,v in l2[:10]:
    print(k,v)

print(l1)

    
#Write a one-line reduce function to get the average length
print(sum(l1)/len(l1))
#or
print(functools.reduce(lambda x,y : x+y,l1 )/len(l1))
#one-line list comprehension to display squares of all odd numbers and display both.
print([x**x for x in l1 if x%2!=0])
