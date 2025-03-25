import csv 
class Admin:
    def __init__(self):
        self.username = None
        self.password = None
    
    def adminRegistration(self):
        print()
        with open("admininfo.csv", 'w', newline="") as f:
            w = csv.writer(f)
            self.username = input("Please enter Username  : ")
            self.password = input("Please enter Password  : ")
            w.writerow([self.username, self.password])
            print("Registration Successfully!")
            print()

    def adminLogin(self):
        actlist = []
        with open("admininfo.csv", 'r+', newline="") as f:
            r = csv.reader(f)
            data = list(r)
            for i in data:
                for j in i:
                    actlist.append(j)

        while True:
            self.username = input("Enter Username : ")
            self.password = input("Enter password : ")
            for row in data:
                if self.username == row[0] and self.password == row[1]:
                    print("Login Successfully!")
                    return
                else:
                    print("Please enter correct Username and Password !")

"""obj = Admin()
obj.adminRegistration()
obj.adminLogin()     """ 