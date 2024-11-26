

available = True
notAvailable = False

class seats:
    def __init__(self, seatings, availabilty):
        self.seatings = seatings
        self.availabilty = availabilty

    def __str__(self):
        availability_str = "Available" if self.availabilty else "Not Available"
        return f"{self.seatings}: {availability_str}"

class airplane:
    def __init__(self):
        self.seats = [
            seats("1", available),
            seats("2", notAvailable),
            seats("3", available),
            seats("4", available),
            seats("5", available),
            seats("6", notAvailable),
            seats("7", available),
            seats("8", notAvailable),
            seats("9", notAvailable),
            seats("10",notAvailable),
            seats("11", notAvailable),
            seats("12", available),
            seats("13", available),
            seats("14", available),
            seats("15", notAvailable),
            seats("16", available),
            seats("17", notAvailable),
            seats("18", notAvailable),
            seats("19",notAvailable),
            seats("20", available)
        ]
        self.selected_seats = []

    def showSeats(self):
        print("\nList of Seats, Please pick a Seat")
        for seat in self.seats:
            print(seat)

    def SelecSeat(self):
        while True:
            try:
                seatInput = int(input("Select a seat from the list\n"))
                if seatInput < 1 or seatInput > 20:
                    print("Seat not in the list, Please try again")
                    continue

                if  1 <= seatInput <= 8:
                    confirmation = input("You have selected a First Class Seat ($200 fee), confirm or cancel?\n").strip().lower()
                    if confirmation != "confirm":
                        print("First class seat selection canceled.")
                        continue

                if  9 <= seatInput <= 16:
                    confirmation = input("You have selected a Emergency Seat, do you accept responsibility for being able to help in-case of emergency ? yes or no?\n").strip().lower()
                    if confirmation != "yes":
                        print("First class seat selection canceled.")
                        continue


                selected_seat = self.seats[seatInput - 1]
                if not selected_seat.availabilty:
                    print(f'Seat {seatInput} is not available, please select another one')
                    continue

                print(f'Seat {seatInput} Selected.')
                selected_seat.availabilty = False
                self.selected_seats.append(selected_seat.seatings)
                return selected_seat
            except ValueError:
                print('Error. Please enter a number from the list (1-20)')

    def showSelectedSeats(self):
        if self.selected_seats:
            print('\nSeats selected:')
            print(",".join(self.selected_seats))
        else:
            print('\nNo seats selected')

    def cost(self):
        totalCost = 0
        for seat in self.selected_seats:
            if int(seat) <= 10:
                totalCost += 200
            else:
                totalCost += 100
        print(f'\nThe Total cost for your seats is: ${totalCost}')
plane = airplane()

while True:
    plane.showSeats()
    plane.SelecSeat()
    moreSeats = input("Do you want to continue chosing seats? (confirm,cancel)\n")
    if moreSeats != 'confirm':
        print('All seats selected.')
        plane.showSelectedSeats()
        plane.cost()
        break


