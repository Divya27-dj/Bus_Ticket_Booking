import csv

class Passenger_Registration():
    def __init__(self):
        self.passengerName = None
        self.noOfPass = None
        self.departLoc = None
        self.destLoc = None
        self.ddmmyy = None
        self.seatNO = None
        self.totalAmount = None
        self.autoInc = 1
        self.countSeat = 0
        self.seatType = None

    def getPassengerInfo(self):
        self.passengerName = input("Enter Passenger Name : ")
        self.noOfPass = int(input("Please enter total number of Passengers : "))
        departureLocations = ["Ahmedabad", "Surat", "Delhi", "Mumbai"]
        locations_list = ", ".join(departureLocations)
        destinationLocations = ["Jaipur", "Haryana", "Gandhinagar", "Chandigarh"]
        locations_list2 = ", ".join(destinationLocations)

        while True:
            self.dl = input(f"Enter Departure Location from {locations_list}: ")
            if self.dl in departureLocations:
                self.departLoc = self.dl
                break  
            else:
                print("Please enter a correct Departure location!")

        while True:
            self.dl2 = input(f"Enter destination location from {locations_list2}: ")
            if self.dl2 in destinationLocations:
                self.destLoc = self.dl2
                break  # Exit the loop if the input is valid
            else:
                print("Please enter a correct Destination Location!")
            

        self.ddmmyy = input("Enter date of journey like 01-01-2025 : ")

        seatNoList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
        self.bookingList = []
        while True:
            try:
                self.seatNO = int(input("Choose seat number you want to book from [1-25] : "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if 1 <= self.seatNO <= 25:
                 
                if self.seatNO in seatNoList:
                    self.bookingList.append(self.seatNO)
                    seatNoList.remove(self.seatNO)
                    print(f"Seat {self.seatNO} successfully booked.")
                    print(f"Available seats: {seatNoList}")
                    count = len(seatNoList)
                else:
                    print("Seat already Booked. Please choose different seat number!")
        
                y = input("Do you want to book one more seat? (Yes/No) : ").strip().lower()
                if y != "yes":  
                    break
                else:
                    print("Kindly choose a valid seat number from 1 to 25!")
            
            else:
                print(f"All booked seats: {self.bookingList}")

        print("1. AC BUS     = Rs. 500")
        print("2. NON-AC BUS = Rs. 300")
        self.busType = int(input("Choose bus type (either 1 or 2) : "))
        if self.busType == 1:
            self.seatType = "AC BUS"
            self.totalAmount = self.noOfPass * 500
        if self.busType == 2:
            self.seatType = "NON-AC BUS"
            self.totalAmount = self.noOfPass * 300


class PassengerDataSaveCSV(Passenger_Registration):
    def saveData(self):

        try:
            with open("passengerData.csv", 'r+', newline="") as f:
                r = csv.reader(f)
                data = list(r)
                for i in data:
                    self.autoInc += 1
                    for j in i:
                        self.countSeat += 1
                    print()
                print(f"Number of records are found in Database : ", self.autoInc)
        
        except:
            print("File not Found")
        
        finally:
            with open("passengerData.csv", 'a+', newline="") as f:
                w = csv.writer(f)
                w.writerow([self.autoInc, self.passengerName, self.noOfPass, self.departLoc, self.destLoc, self.ddmmyy, self.seatType, self.bookingList, self.totalAmount])
                print("Data Saved Successfully!")
                print()

"""obj = PassengerDataSaveCSV()
obj.getPassengerInfo()
obj.saveData()"""

class TicketShow():

    def ticketShow(self):
        bln = []
        with open("passengerData.csv", 'r+', newline="") as f:
            r = csv.reader(f)
            data = list(r)
            id = int(input("Enter your Booking Id : "))
            for i in data:
                if id == int(i[0]):
                    for j in i:
                        bln.append(j)
                    break

        print("---------------------------------------------------------------------")
        print(" e_ticket :", "Delhi Address                 : Karol Bagh, Delhi     ")
        print("          :", "PhoneNo / MobNo               : 9999999999, 8888888888")
        print()
        print("", bln[3],"-------->", bln[4], "     ","      Passenger ID : ", bln[0])
        print(" Passenger Name : ", bln[1], "       "," Number of Passenger :",bln[2])
        print("_____________________________________________________________________")
        print("Date OF Booking : ",bln[5],"         ","            Seat No : ",bln[7])
        print(" Bus Type :         ",bln[6],"                                       ")
        print(" Bus Total Amount : ",bln[8],"                                       ")
        print("---------------------------------------------------------------------")

        