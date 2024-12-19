
seats = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
booked_seats = []


def book_seat(seat):
    if seat in booked_seats:
        print(f"Seat {seat} is already booked.")
    elif seat not in seats:
        print(f"Seat {seat} does not exist.")
    else:
        booked_seats.append(seat)
        print(f"Seat {seat} booked successfully.")
    show_available_seats()


def remove_seat(seat):
    if seat in booked_seats:
        booked_seats.remove(seat)
        print(f"Seat {seat} removed successfully.")
    else:
        print(f"Seat {seat} is not booked.")
    show_available_seats()


def show_available_seats():
    available_seats = [seat for seat in seats if seat not in booked_seats]
    print(f"Available seats: {available_seats}")

show_available_seats()  
book_seat(3)            
remove_seat(5)          
book_seat(5)           
book_seat(3)            
remove_seat(7)          
