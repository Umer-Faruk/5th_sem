#Read a list of elements.
#print("reading the elements ")

# l1=[]
# noe=int(input("enter the number of elements"))
# for i in range(0,noe):
# 	l1.append(input("enter the element "+ str(i)))
# print("elements inhe list are:")
# print(l1)

#list having all the elements minus the duplicates (Use functions).
#l2=[1,3,4,2,5,6,3,4,1,5,3,2,5,]

#print(set(l2)) we can use set to remove duplicates

# def removeduplicates(l2):
# 	newlist=[]
# 	for num in l2:
# 		if num not in newlist:
# 			newlist.append(num)
# 	return newlist

# print("list with dduplicate")
# print(l2)
# l2=removeduplicates(l2)
# print("after removing duplicates")
# print(l2)

#Use one-line comprehensions of create a new list of even numbers.
# l3=even=[i for i in l2 if i%2==0]
# print("even list")
# print(l3)

#Create another list reversing the elements.
# l2.reverse()
# print(l2)


#b) Write a python program to count the frequency of words in a given file.


#fname=open(input("enter the file name"))
l1=[2,4,5,3,2,56,3,6,2,56,7,5,3]
#l2=[]
# for i in fname:
# 	i=i.rstrip()
# 	l1=i.split()
# 	print(l1)
# for i in l1:
# 	if i not in l2:
# 		l2.append(i)
# for j in range(0,len(l2)):
# 	print(l2[j]+":"+ str(l1.count(l2[j])))

#print(l1[1:])
#c
def Max(l1):
    if len(l1) == 1:
        return l1[0]
    else:
        m = Max(l1[1:])
		
        return m if m > l1[0] else l1[0]
	
print(Max(l1))