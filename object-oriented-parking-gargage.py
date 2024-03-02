class Parking_garage():
    def __init__(self, tickets, parkingSpaces):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = {}

    def takeTicket(self, license_plate):
        self.tickets -= 1
        self.parkingSpaces -= 1
        self.currentTicket[license_plate] = False

    def payForParking(self, license_plate, amount):
        print(f'{license_plate} has not paid for the ticket yet. The total amount is $10')
        while True:
            amount = int(input('Insert card or cash to pay for the ticket: Amount: '))
            if amount >= 10:
                print("Paid. you have 15 minutes to exit")
                self.currentTicket[license_plate] = True
                break

    def leaveGarage(self, license_plate):
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
    
    def show_parkingSpaces(self):
        print('History of the garage on this day: ')
        for k,v in self.currentTicket.items():
            print(f'License plate: {k}: paid?: {v}')
        print(f'Currently, the garage has {self.parkingSpaces} open spaces ')

garage1 = Parking_garage(10,10)
garage1.takeTicket('9zpo')
garage1.takeTicket('912')
garage1.leaveGarage('9zpo')
garage1.takeTicket('9890')
garage1.payForParking('912', 10)
garage1.leaveGarage('912')
garage1.show_parkingSpaces()


            







