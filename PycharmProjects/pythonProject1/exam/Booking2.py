MAX_ROW = 8
MAX_COL = 80

import random
import string
# Define a struct to store customer info
class CustomerInfo:

    # Initial customer info
    def __init__(self):
        self.firstName = ""
        self.lastName = ""
        self.passport = ""
        self.reference = ""
        self.seatRow = -1
        self.searCol = -1

    def __init__(self, reference, fName, lName, passport, row, col):
        self.reference = reference
        self.firstName = fName
        self.lastName = lName
        self.passport = passport
        self.row = row
        self.col = col

    # Check seat place is the customer
    def is_the_seat(self, row, col):
        if self.row == row and self.col == col:
            return True
        return False

# Define a class to represent the seat booking application
class SeatBookingApp:
    def __init__(self):
        # Initialize a list to represent the seat status
        self.seat_status = [['F' for _ in range(MAX_COL + 1)] for _ in range(MAX_ROW + 1)]  # F: Free, R: Reserved
        self.menu_options = {
            '1': self.check_availability,
            '2': self.book_seat,
            '3': self.free_seat,
            '4': self.show_booking_state,
            '5': self.show_booking_detail,
            '6': self.exit_program
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
        # store customer info
        self.booking_detail = []

    # Function to check the availability of a seat
    def check_availability(self):
        row = int(input(f"Enter row number (1-{MAX_ROW}): "))
        column = int(input(f"Enter column number (1-{MAX_COL}): "))
        if self.seat_status[row][column] == 'F':
            print("Seat is available.")
        else:
            print("Seat is already booked.")

    # Function to generate reference
    def generate_reference(self):
        # Define a set to store generated references
        generated_references = set()

        # Loop until a unique reference is generated
        while True:
            # Generate a random reference with 8 alphanumeric characters
            reference = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

            # Check if the reference is unique
            if reference not in generated_references:
                return reference  # Return the unique reference
            else:
                # If not unique, generate another reference
                continue

    # Function to book a seat
    def book_seat(self):
        row = int(input(f"Enter row number (1-{MAX_ROW}): "))
        column = int(input(f"Enter column number (1-{MAX_COL}): "))
        if self.seat_status[row][column] == 'F':
            self.seat_status[row][column] = 'R'
            self.booking_detail.append(CustomerInfo(self.generate_reference(), "", "", "", row, column))
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
            self.remove_customer(row, column)
            print("Seat freed successfully.")
        else:
            print("Seat is already free.")

    # Function remove customer info
    def remove_customer(self, row, column):
        for i, info in enumerate(self.booking_detail):
            if info.is_the_seat(row, column):
                del self.booking_detail[i]
            
    # Function to show the current booking state
    def show_booking_state(self):
        print("Booking state:")
        for row_num, row in enumerate(self.seat_status, start=1):
            for col_num, status in enumerate(row, start=1):
                print(f"Row {row_num}, Seat {col_num}: {status}")

    # Function to show the detail info
    def show_booking_detail(self):
        if len(self.booking_detail) <= 0:
            print("Booking detail: None")
        else:
            print("Booking detail:")
            for _, info in enumerate(self.booking_detail):
                print(f"Row {info.row}, Seat {info.col}")

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
            print("5. Show booking detail")
            print("6. Exit program")
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
