print("welcome to interactive personal data collector created by ahmed")
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in metres: "))
fav_num= int(input("Please enter your favourite number: "))

print("Thank you for providing your information!", " Here is what you entered")
print("Name: ", name,"type: " ,(type(name)),"memory address: ", (id(name)))
print("Age: ", age,"type: " ,(type(age)),"memory address: ", (id(age)))
print("Height: ", height,"type: " ,(type(height)),"memory address: ", (id(height)))
print("Favourite Number: ", fav_num,"type: " ,(type(fav_num)),"memory address: ", (id(fav_num)))

print("your birth year is: ", 2025 - age)
print("thank you for using ahmed data collector")

