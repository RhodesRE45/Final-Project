# Define max row and col
MAX_ROW = 8
MAX_COL = 80

# Define a class to represent the seat booking application
class SeatBookingApp: 
    def __init__(self):
        # Initialize a list to represent the seat status
        self.seat_status = [['F' for _ in range(MAX_COL + 1)] for _ in range(MAX_ROW)]  # F: Free, R: Reserved
        self.menu_options = {
            '1': self.check_availability,
            '2': self.book_seat,
            '3': self.free_seat,
            '4': self.show_booking_state,
            '5': self.exit_program
        }
        # Consider storage and isles
        for i in range(MAX_COL + 1):
            self.seat_status[4][i] = 'X'
        self.seat_status[5][76] = 'S'
        self.seat_status[5][77] = 'S'
        self.seat_status[6][76] = 'S'
        self.seat_status[6][77] = 'S'
        self.seat_status[7][76] = 'S'
        self.seat_status[7][77] = 'S'

    # Function to check the availability of a seat
    def check_availability(self):
        row = int(input(f"Enter row number (1-{MAX_ROW}): "))
        column = int(input(f"Enter column number (1-{MAX_COL}): "))
        if self.seat_status[row][column] == 'F':
            print("Seat is available.")
        else:
            print("Seat is already booked.")

    # Function to book a seat
    def book_seat(self):
        row = int(input(f"Enter row number (1-{MAX_ROW}): "))
        column = int(input(f"Enter column number (1-{MAX_COL}): "))
        if self.seat_status[row][column] == 'F':
            self.seat_status[row][column] = 'R'
            print("Seat booked successfully.")
        elif self.seat_status[row][column] == 'S':
            print("Place is storage area")
        elif self.seat_status[row][column] == 'X':
            print("Place is isles")
        else:
            print("Seat is already booked.")

    # Function to free a seat
    def free_seat(self):
        row = int(input(f"Enter row number (1-{MAX_ROW}): "))
        column = int(input(f"Enter column number (1-{MAX_COL}): "))
        if self.seat_status[row][column] == 'R':
            self.seat_status[row][column] = 'F'
            print("Seat freed successfully.")
        else:
            print("Seat is already free.")

    # Function to show the current booking state
    def show_booking_state(self):
        for row_num, row in enumerate(self.seat_status, start=1):
            for col_num, status in enumerate(row, start=1):
                print(f"Row {row_num}, Seat {col_num}: {status}")

    # Function to exit the program
    def exit_program(self):
        print("Exiting the program.")
        exit()

    # Function to display the menu options and handle user input
    def display_menu(self):
        while True:
            print("\nMenu:")
            print("1. Check availability of seat")
            print("2. Book a seat")
            print("3. Free a seat")
            print("4. Show booking state")
            print("5. Exit program")
            choice = input("Enter your choice: ")
            if choice in self.menu_options:
                self.menu_options[choice]()
            else:
                print("Invalid choice. Please try again.")


# Main function to run the seat booking application
def main():
    # Create an instance of the SeatBookingApp class
    seat_booking_app = SeatBookingApp()
    # Display the menu and handle user input
    seat_booking_app.display_menu()


# Entry point of the program
if __name__ == "__main__":
    main()
