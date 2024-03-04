class Parking_garage():
    def __init__(self, tickets, parkingSpaces):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = {}

    def takeTicket(self):
        self.tickets -= 1
        self.parkingSpaces -= 1
        license_plate = input('Enter your license plate: ')
        self.currentTicket[license_plate] = False
        print(f'Car licensed: {license_plate} just took a ticket')

    def payForParking(self):
        license_plate = input('Enter your license plate: ')
        print(f'{license_plate} has not paid for the ticket yet. The total amount is $10')
        while True:
            amount = int(input('Insert card or cash to pay for the ticket: Amount: '))
            if amount >= 10:
                print("Paid. you have 15 minutes to exit")
                self.currentTicket[license_plate] = True
                break

    def leaveGarage(self):
        license_plate = input('Enter your license plate: ')
        if self.currentTicket[license_plate] == True:
            print('Thank you, have a nice day')
            self.tickets +=1
            self.parkingSpaces += 1
        else:
            while True:  
                paid_amount = int(input(f'License plate "{license_plate}" Not paid yet, please enter amount to pay: '))
                if paid_amount >= 10:
                    print('Paid. Have a nice day!')
                    self.tickets +=1
                    self.parkingSpaces += 1
                    self.currentTicket[license_plate] = True
                    break
    
    def show_history(self):
        print('History of the garage on this day: ')
        for k,v in self.currentTicket.items():
            print(f'License plate: {k}: paid?: {v}')
    
    def check_spaces(self):
        print(f'Currently, the garage has {self.parkingSpaces} open spaces ')



def main():
    garage1 = Parking_garage(10,10)
    while True:
        print("\nParking Garage Menu:")
        print("1. Take Ticket")
        print("2. Pay for Parking")
        print("3. Leave Garage")
        print("4, Check Spaces")
        print("5, Show history of the garage on the day")
        print("6. Quit")
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            garage1.takeTicket()
        elif choice == '2':
            garage1.payForParking()
        elif choice == '3':
            garage1.leaveGarage()
        elif choice == '4':
            garage1.check_spaces()
        elif choice == '5':
            garage1.show_history()
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

main()


#Test
# garage1 = Parking_garage(10,10)
# garage1.takeTicket('9zpo')
# garage1.takeTicket('912')
# garage1.check_spaces()
# garage1.leaveGarage('9zpo')
# garage1.takeTicket('9890')
# garage1.payForParking('912')
# garage1.leaveGarage('912')
# garage1.show_history()
# garage1.check_spaces()


            







