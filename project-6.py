class journalmanager:
    # also use exception handling for file not found
    def write_new_file(self, file_name,user_input):
        try:
            file = open(file_name, "a")
            file.write(user_input+"\n")
            file.close()
        except FileNotFoundError:
            print("Error: File not found.")


    def show_entry(self, file_name):
        try:
            file = open(file_name, "r")
            print(file.read())
            file.close()
        except FileNotFoundError:
            print("Error: File not found.")
    
    def search_entry(self, file_name,find):
        try:
            found = False
            line = 0
            file = open(file_name, "r")
            while True:
                data = file.readline()
                if not data:  
                    break
                line += 1
                if find in data:
                    print(f"Entry found on line {line}: {data.strip()}")
                    found = True
            file.close()
            if not found:
                print("Entry not found")
        except FileNotFoundError:
            print("Error: File not found.")
    def delete_entry(self, file_name):
        try:
            # First, try to open in read mode to verify file exists
            with open(file_name, "r") as f:
                pass
            # If file exists, now delete its contents
            with open(file_name, "w") as f:
                f.write("")
            print("all entries deleted successfully")
        except FileNotFoundError:
            print("Error: File not found.")

j1=journalmanager()


print("welcome to personal journal manager")
print("please select an option")
while True:
    print("1.add a new entry")
    print("2.view all entries")
    print("3.search an entry")
    print("4.delete all entries")
    print("5.exit")


    choice=int(input("enter your choice: "))
    if choice==1:
        file_name=input("enter the file name: ")
        user_input=input("enter the text: ")
        j1.write_new_file(file_name,user_input)
        print("entry saved successfully")
    elif choice==2:
        file_name=input("enter the file name: ")
        j1.show_entry(file_name)
    elif choice==3:
        file_name=input("enter the file name: ")
        find=input("enter the text to search: ")
        j1.search_entry(file_name,find)
    elif choice==4:
        file_name=input("enter the file name: ")
        j1.delete_entry(file_name)
    elif choice==5:
        print("thank you for using personal journal manager")
        break
    else:
        print("invalid choice")





