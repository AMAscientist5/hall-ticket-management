class Star_Cinema:
    hall_list = []
    def entry_hall(self, hall):
        self.hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, name, rows, cols, hall_no):
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self._seats = {}
        self._show_list = []
        self.name = name
        super().__init__()

    def entry_show(self, id, movie_name, time):
        if id in self._show_list:
            print('already exits show list')
            return
        showInfo = (id, movie_name, time)
        self._show_list.append(showInfo)

        self._seats[id] = {}

    def view_show_list(self):
        # print('_____Shows List______\n')
        for show in self._show_list:
            print(f"Show name {show[1]} - Show id {show[0]} - time {show[2]}")
        print("=========================")

    def booking_seats(self, id,  seat_list,):
        if id not in self._seats:
            print("invalid id")
            return
        for row, col in seat_list:
            if not (0 <= row < self._rows and 0 <= col < self._cols):
                print("invalid seat:", row, col)
                return

            if (row, col) in self._seats[id]:
                print("Already booked:", row, col)
                return

        for row, col in seat_list:
            self._seats[id][(row, col)] = True
        print("Booking successfully")

    def view_available_seats(self, id):
        if id not in self._seats:
            print("invalid id")
            return

        print(f"Seats are available for Show ID {id} (Row, Col):")
        for row in range(self._rows):
            for col in range(self._cols):
                if (row, col) not in self._seats[id]:
                    print(f'({row}, {col})', end=' ')
            print()


class Replica:
    def __init__(self, hall):
        self.hall = hall
    def re_entry_show(self, id, movie_name, time):
        self.hall.entry_show(id, movie_name, time)

    def re_view_show_list(self):
        self.hall.view_show_list()

    def re_view_available_seats(self, id):
        self.hall.view_available_seats(id)

    def re_booking_seats(self, id,  seat_list):
        self.hall.booking_seats(id, seat_list)


defaultHall = Hall(name='jonaki', rows=5, cols=5, hall_no=1000)

replica = Replica(defaultHall)
replica.re_entry_show(100, "kotipoti", 12.00)
replica.re_entry_show(200, "fokinni", 3.00)
replica.re_entry_show(200, "middle class", 6.00)

flag = True
while flag:
    print('1. View All Show List')
    print('2. View Available Seats')
    print('3. Book Seat')
    print('4. Exit')

    option = int(input('Enter your option:'))
    if option == 1:
        replica.re_view_show_list()
    elif option == 2:
        id = int(input('Enter Show ID: '))
        replica.re_view_available_seats(id)

       
    elif option == 3:
        id = int(input('Enter Show ID: '))
        quantity = int(input("Enter seat Quantity: "))
        seat_list = []
        for _ in range(quantity):
            row = int(input('Enter Row Number: '))
            col = int(input('Enter Column Number: '))
            seat_list.append((row, col))
        replica.re_booking_seats(id,  seat_list)
    elif option == 4:
        flag = False
