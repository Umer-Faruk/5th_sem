#3> Python Classes: Write a python class to reverse a sentence (initialized via constructor) word by word.
# Example: I am here should be reversed as here am I. Create instances of this class for each of the
# three strings input by the user and display the reversed string for each, in descending order of number of
# vowels in the string
# class myclass:
#     def __init__(self,x):
#         self.name =x
#     def myname(self,name):
#         print("mty name is "+self.name)
# i=myclass("umer")
# print(i.name)

class reverse_sent:
    def __init__(self,sent):
        self.sent=sent
        sent=sent.split()
        l1=(sent[::-1])
        print(' '.join(l1))
    


i=reverse_sent(input("enter the sent\n"))
print(i.sent)









