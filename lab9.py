rowinput=int(input("Enter the Number of Rows: "))
num=1
for row in range(1,rowinput+1):
    for col in range(1,row+1):
        print(num,end=" ")
        num+=1
    print()