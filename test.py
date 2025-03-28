from classes import Room, SuiteRoom, Guest, LoyalGuest, Booking, Payment, Hotel, Invoice


def test_guest_creation():
    print("\n--- Guest Account Creation Test ---")
    guest_id = input("Enter Guest ID: ")
    name = input("Enter Guest Name: ")
    contact = input("Enter Contact Info: ")
    guest = Guest(guest_id, name, contact, [])  # Fixed: Added empty reservation history
    print("✅ Guest Created Successfully:")
    print(guest)


def test_loyal_guest():
    print("\n--- Loyal Guest Creation Test ---")
    guest_id = input("Enter Guest ID: ")
    name = input("Enter Guest Name: ")
    contact = input("Enter Contact Info: ")

    while True:
        try:
            points = int(input("Enter Loyalty Points: "))  # Ensures integer input
            break
        except ValueError:
            print("❌ Invalid input. Please enter a valid number for loyalty points.")

    level = input("Enter Membership Level: ")

    while True:
        try:
            discount = float(input("Enter Discount Rate: "))  # Ensures float input
            break
        except ValueError:
            print("❌ Invalid input. Please enter a valid number for discount rate.")

    loyal_guest = LoyalGuest(guest_id, name, contact, [], points, level, discount)
    print("✅ Loyal Guest Created Successfully:")
    print(loyal_guest)


def test_room_availability():
    print("\n--- Room Availability Test ---")
    room_number = input("Enter Room Number: ")
    room_type = input("Enter Room Type: ")
    amenities = input("Enter Amenities (comma-separated): ").split(',')
    price = float(input("Enter Price Per Night: "))
    status = input("Is the room available? (yes/no): ").lower() == "yes"

    room = Room(room_number, room_type, amenities, price, status)
    print("✅ Room Details:")
    print(room)
    print("Availability Status:", "🟢 Available" if room.is_available() else "🔴 Not Available")


def test_booking():
    print("\n--- Booking Test ---")
    booking_id = input("Enter Booking ID: ")
    guest_id = input("Enter Guest ID: ")
    room_number = input("Enter Room Number: ")
    checkin = input("Enter Check-in Date (YYYY-MM-DD): ")
    checkout = input("Enter Check-out Date (YYYY-MM-DD): ")
    status = input("Enter Booking Status (Confirmed/Pending/Canceled): ")

    booking = Booking(booking_id, guest_id, room_number, checkin, checkout, status)
    print("✅ Booking Created Successfully:")
    print(booking)


def test_payment():
    print("\n--- Payment Processing Test ---")
    payment_id = input("Enter Payment ID: ")
    booking_id = input("Enter Booking ID: ")
    method = input("Enter Payment Method (Card/Cash/Wallet): ")

    while True:
        try:
            amount = float(input("Enter Payment Amount: "))  # Ensures float input
            break
        except ValueError:
            print("❌ Invalid input. Please enter a valid number for payment amount.")

    date = input("Enter Payment Date (YYYY-MM-DD): ")

    payment = Payment(payment_id, booking_id, method, amount, date)
    print("✅ Payment Processed Successfully:")
    print(payment)
    print("Payment Status:", "Success" if payment.process_payment() else "Failed")


def test_invoice():
    print("\n--- Invoice Generation Test ---")
    invoice_id = input("Enter Invoice ID: ")

    # Create a Booking object first
    booking = Booking(input("Enter Booking ID: "), input("Enter Guest ID: "), input("Enter Room Number: "),
                      input("Enter Check-in Date (YYYY-MM-DD): "), input("Enter Check-out Date (YYYY-MM-DD): "),
                      input("Enter Booking Status: "))

    guest_id = input("Enter Guest ID: ")
    charges = float(input("Enter Room Charges: "))

    # Use the get_booking_id() method to retrieve the booking ID
    invoice = Invoice(invoice_id, booking.get_booking_id(), guest_id, charges)
    discount = float(input("Enter Discount Amount: "))

    total = invoice.calculate_total(discount)
    print("Invoice Generated Successfully:")
    print(invoice)
    print(f"Total Amount after Discount: {total}")


def run_tests():
    test_guest_creation()
    test_loyal_guest()
    test_room_availability()
    test_booking()
    test_payment()
    test_invoice()


if __name__ == "__main__":
    run_tests()
