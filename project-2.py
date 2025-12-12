print("welcome to pattern generator and number analyzer created by ahmed")
print("select an option")
print("1. Generate a pattern of right angle triangles")
print("2. Analyze numbers in a range")
print("3. Exit")
option=int(input("Enter your choice (1/2/3): "))
if option==1:
    rows=int(input("Enter number of rows for the triangle pattern: "))
    for i in range(1,rows+1):
        for j in range(1,i+1):
            print("*", end=" ")
        print()
if option==2:
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
for i in range(num1,num2+1):
    if i%2==0:
        print(i, "is even")
    else:
        print(i, "is odd")
sum=0
for i in range(num1,num2+1):
    sum=sum+i
print("The sum of all number is:", sum)
if option==3:
    print("thank you for using ahmed pattern generator and number analyzer")
    
