student = []
while True:
    print("welcome to student recording system")
    print("1. Add student")
    print("2. Delete student")
    print("3. Update student")
    print("4. Display student")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter student name: ")
        sid = input("Enter student id: ")
        age = input("Enter student age: ")
        d0b =input("enter your dob: ")
        subject =input("enter your subject: ")
        student.append({"name": name, "id": sid, "age": age ,"dob":d0b,"subject":subject})
    elif choice == "2":
      sid = input("Enter student id to delete: ")
      for i in range(len(student)):
         if student[i]["student id"] == sid:
            del student[i]
            print("Student deleted successfully")
            break
    elif choice == "3":
       sid = input("Enter roll number of student to update: ")
       for i in range(len(student)):
          if student[i]["student id"] == sid:
             name = input("Enter new name: ")
             sid = input("Enter new student id: ")
             age = input("Enter new age: ")
             dob = input("enter your dob: ")
             subject = input("enter your subject: ")
             student[i]["name"] = name
             student[i]["student id"] = sid
    elif choice == "4":
       for i in range(len(student)):
          print("Name: ", student[i]["name"])
          print("studnet id: ", student[i]["student id"])
          print("Age: ", student[i]["age"])
          print("Dob: ", student[i]["dob"])
          print("Subject: ", student[i]["subject"])
          print("\n")
    elif choice == "5":
       break


