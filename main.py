from passenger_info import *
from admin import *

global ch

def start():
    print("1. Admin Registration !")
    print("2. Admin Login !")
    adminobj = Admin()
    ch = int(input("Account Login. If not you can Register !"))
    
    if ch == 1:
        adminobj.adminRegistration()

    if ch == 2:
        adminobj.adminLogin()

        print()
        print("1. Passenger Registration !")
        print("2. Show Booked Ticket !")
         
        ch = int(input("Please enter your choice : "))
        if ch == 1:
            pass_obj = PassengerDataSaveCSV()
            pass_obj.getPassengerInfo()
            pass_obj.saveData()
        elif ch == 2:
            obj = TicketShow()
            obj.ticketShow()

start()

