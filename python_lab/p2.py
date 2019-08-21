# Write a temperature converter python program, which is menu
# driven. Each such conversion logic should be defined in separate functions. The program should call the
# respective function based on the users requirement. The program should run as long as the user wishes
# so. Provide an option to view the conversions stored as list of tuples with attributes - from unit value, to
# unit value sorted by the users choice (from-value or to-value).
def CTOK(C):
    return c+273.15
def CTOF(c):
    return (c*1.8)+32
def FTOC(f):
    return (f-32)/1.8
def FTOK(f):
    return (f+459.67)*5/9
def KTOC(k):
    return (k-273.15)
def KTOF(k):
    return (k*9/5)-459.67

while True:
    
    temp=int(input("\nenter \n 1 for Celsius to Kelvin converter \n 2 for Celsius to Fahrenheit conversion \n 3 for Fahrenheit to Celsius conversion \n 4 Fahrenheit to Kelvin conversion \n 5  for Kelvin to Celsius conversion \n 6 Kelvin to Fahrenheit conversion \n 9 for quit\n"))
#print(type(temp))
    if temp == 1:
            c=float(input("celsius :"))
            print("kelvin :"+str(CTOK(c))+" °K" )


    elif temp == 2:
            c=float(input("celsius :"))
            print("fahrenheit :"+str(CTOF(c))+" °F")
            
           
    elif temp == 3:
          f=float(input("Fahrenheit :"))
          print("celsius : "+str(FTOC(f))+"°C")
    elif temp == 4:
            f=float(input("Fahrenheit :"))
            print("kelvin : "+str(FTOK(f))+" °K")

    elif temp == 5:
         k=float(input("kelvin :"))
         print("celsius : "+str(KTOC(k))+" °C")

    elif temp == 6:
         k=float(input("kelvin :"))
         print("fahrenheit:" +str(KTOF(k))+" °F")
    elif temp == 9:
        exit()
    else :
            print("enter right choise")




