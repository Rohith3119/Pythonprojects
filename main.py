lower= int(input("Enter the lower number in range: "))
upper= int(input("Enter the upper number in range: "))

for i in range(lower,upper+1):
    if(i%2 !=0):
        print(i)