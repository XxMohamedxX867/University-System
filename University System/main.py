kerollos = {"Name": "kerollos ashraf wadia",
            "ID": "202102360",
            "age": "19",
            "college": "IT",
            "email": "k.gerges2360@su.edu.eg",
            "GPA": "4"
            }
osama = {"Name": "Osama ahmed mahmoud",
         "ID": "202102355",
         "age": "18",
         "college": "IT",
         "email": "o.ahmed2355@su.edu.eg",
         "GPA": "4"
         }
gebaly = {"Name": "Mohamed adel gebaly",
          "ID": "202102357",
          "age": "19",
          "college": "IT",
          "email": "m.oraby2357@su.edu.eg",
          "GPA": "4"
          }
ahmed = {"Name": "Ahmed mohamed reda",
         "ID": "202103084",
         "age": "19",
         "college": "IT",
         "email": "a.saleh3084@su.edu.eg",
         "GPA": "4"
         }
students_list = []
def add():
    name = input("type your name>>")
    while True:
        try:
            ID = int(input("type your ID>>"))
        except:
            print("Please enter a number!")
            continue
        else:
            break
    while True:
        try:
            age = int(input("type your age>>"))
        except:
            print("Please enter a number!")
            continue
        else:
            break
    college = input("type your college>>")
    email = input("type your email>>")
    while True:
        try:
            GPA = float(input("type your GPA>>"))
        except:
            print("Please enter a number!")
            continue
        else:
            break
    new_password = input("Enter your new password>>")
    new = {"Name": name,
           "ID": ID,
           "age": age,
           "college": college,
           "email": email,
           "GPA": GPA
           }

    students_list.append(new)
    print(students_list)

def update(u):
    while True:
        print("(Name | ID | Age | College | E-mail | GPA)")
        o = input("choose what to change or type 'exit': ")
        if o == "name" or o == "Name":
            students_list[0]["Name"] = input("Enter new name>>")
            print("Name changed")
            print(students_list[0].items())
            continue
        elif o == "ID" or o == "id":
            students_list[0]["ID"] = input("Enter new ID>>")
            print("ID changed")
            print(students_list[0].items())
            continue
        elif o == "age" or o == "AGE":
            students_list[0]["age"] = input("Enter new age>>")
            print("age changed")
            print(students_list[0].items())
            continue
        elif o == "COLLEGE" or o == "college":
            students_list[0]["college"] = input("enter new college>>")
            print("college changed")
            print(students_list[0].items())
            continue
        elif o == "email" or o == "EMAIL":
            students_list[0]["email"] = input("Enter new Email>>")
            print("email changed")
            print(students_list[0].items())
            continue
        elif o == "gpa" or o == "GPA":
            students_list[0]["GPA"] = input("Enter new GPA>>")
            print("GPA changed")
            print(students_list[0].items())
            continue
        elif o == "exit" or o == "EXIT":
            break
        else:
            print("wrong type!!")
            continue


def checker(username, password):
    try:
        if (username == "kerollos" and password == "1234") or (username == "osama" and password == "1234") or (
                username == "gebaly" and password == "1234") or (username == "ahmed" and password == "1234") or (
                username == new["Name"] and password == new_password):
            print("successful login")
            return True
    except:
        print("Please enter your username and password again!")
        return False


def user(x):
    while True:
        print("1.view your information")
        print("2.Exit")
        student_menu = int(input("Enter the number>>"))
        try:
            if student_menu == 1:
                print(eval("{}.items()".format(x)))
        except:
            print(new)
        if student_menu == 2:
            break
        if (student_menu < 1) and (student_menu > 2):
            print("please enter a number from menu!")
            continue


while True:
    print("1.admin")
    print("2.student")
    print("3.Exit")
    main_menu = input("Enter the number>>")

    if main_menu == "1":
        print("(admin)")
        while True:
            admin_name = input("Enter user name>>")
            admin_password = input("Enter password>>")
            if admin_name == "mazen" and admin_password == "1234":
                print("successful login")
                break
            else:
                print("invalid! Please enter user name and password again")
                continue
        while True:
            print("1.add student")
            print("2.update on student information")
            print("3.delete student")
            print("4.exit")
            admin_menu = input("Enter the number>>")
            if admin_menu == "1":
                add()

            elif admin_menu == "2":
                print("1.kerollos")
                print("2.osama")
                print("3.gebaly")
                print("4.ahmed")
                try:
                    print("5.",students_list[0]["Name"],sep="")
                except:
                    print("")
                try:
                    print("6.",students_list[1]["Name"],sep="")
                except:
                    print("")
                try:
                    print("7.",students_list[2]["Name"],sep="")
                except:
                    print("")
                update_menu = input("type a number of name you want to change>>")
                if update_menu == "1":
                    u = "kerollos"
                    update(u)
                elif update_menu == "2":
                    u = "osama"
                    update(u)
                elif update_menu == "3":
                    u = "gebaly"
                    update(u)
                elif update_menu == "4":
                    u = "ahmed"
                    update(u)
                elif update_menu == "5":
                    l = students_list[0]
                    u = str(l["Name"])
                    update(u)
                elif update_menu == "6":
                    u = students_list[1]["Name"]
                    update(u)
                elif update_menu == "7":
                    u = students_list[2]["Name"]
                    update(u)
            elif admin_menu == "3":
                print("1.kerollos")
                print("2.osama")
                print("3.gebaly")
                print("4.ahmed")
                try:
                    print("5." + str(new['Name']))
                except:
                    print("")
                delete_menu = input("Enter the number of name you want to delete>> ")
                if delete_menu == "1":
                    kerollos.clear()
                    print("deleting kerollos..")
                    print("kerollos deleted")
                elif delete_menu == "2":
                    osama.clear()
                    print("deleting osama..")
                    print("osama deleted")
                elif delete_menu == "3":
                    gebaly.clear()
                    print("deleting gebaly..")
                    print("gebaly deleted")
                elif delete_menu == "4":
                    ahmed.clear()
                    print("deleting ahmed..")
                    print("ahmed deleted")
                elif delete_menu == "5":
                    try:
                        print("deleting " + new["Name"] + "..")
                        print(new["Name"] + " deleted")
                        new.clear()
                    except:
                        print("Nothing to delete!")
            elif admin_menu == "4":
                break
            else:
                print("please enter a number from the menu!")
                continue
    if main_menu == "2":
        while True:
            student_name = input("Enter your username>>")
            student_password = input("Enter your password>>")
            if checker(student_name, student_password):
                break
        user(student_name)
    if main_menu == "3":
        break
    else:
        print("please enter a number from the list!")
        continue