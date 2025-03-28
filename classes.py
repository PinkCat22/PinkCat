# Room class representing a hotel room
class Room:
    """
    Represents a hotel room with details such as room number, type, amenities, price per night, and availability.
    """

    def __init__(self, room_number: str, room_type: str, amenities: list[str], price_per_night: float,
                 availability_status: bool):
        # Protected attributes
        self._room_number = room_number
        self._room_type = room_type
        self._amenities = amenities
        self._price_per_night = price_per_night
        self._availability_status = availability_status

    # Getter and setter methods for protected attributes
    def get_room_number(self):
        """Returns the room number."""
        return self._room_number

    def set_room_number(self, room_number: str):
        """Sets the room number."""
        self._room_number = room_number

    def get_room_type(self):
        """Returns the room type."""
        return self._room_type

    def set_room_type(self, room_type: str):
        """Sets the room type."""
        self._room_type = room_type

    def get_amenities(self):
        """Returns the list of amenities."""
        return self._amenities

    def set_amenities(self, amenities: list[str]):
        """Sets the list of amenities."""
        self._amenities = amenities

    def get_price_per_night(self):
        """Returns the price per night."""
        return self._price_per_night

    def set_price_per_night(self, price: float):
        """Sets the price per night."""
        self._price_per_night = price

    def get_availability_status(self):
        """Returns the availability status."""
        return self._availability_status

    def set_availability_status(self, status: bool):
        """Sets the availability status."""
        self._availability_status = status

    def is_available(self):
        """Checks if the room is available."""
        return self._availability_status

    def __str__(self):
        """Returns a string representation of the room."""
        return f"Room {self._room_number}: {self._room_type}, Price: {self._price_per_night}, Available: {self._availability_status}"


# SuiteRoom class, inheriting from Room
class SuiteRoom(Room):
    """
    Represents a suite room with additional luxury features.
    """

    def __init__(self, room_number: str, room_type: str, amenities: list[str], price_per_night: float,
                 availability_status: bool, has_private_lounge: bool, complimentary_service: list[str],
                 suite_size: int):
        super().__init__(room_number, room_type, amenities, price_per_night, availability_status)
        # Private attributes
        self.__has_private_lounge = has_private_lounge
        self.__complimentary_service = complimentary_service
        self.__suite_size = suite_size

    # Getter and setter methods for private attributes
    def get_has_private_lounge(self):
        """Returns if the suite has a private lounge."""
        return self.__has_private_lounge

    def set_has_private_lounge(self, lounge: bool):
        """Sets the private lounge availability."""
        self.__has_private_lounge = lounge

    def get_complimentary_service(self):
        """Returns the list of complimentary services."""
        return self.__complimentary_service

    def set_complimentary_service(self, service: list[str]):
        """Sets the list of complimentary services."""
        self.__complimentary_service = service

    def get_suite_size(self):
        """Returns the suite size in square meters."""
        return self.__suite_size

    def set_suite_size(self, size: int):
        """Sets the suite size."""
        self.__suite_size = size

    def __str__(self):
        """Returns a string representation of the suite room."""
        return super().__str__() + f", Lounge: {self.__has_private_lounge}, Suite Size: {self.__suite_size} sqm"


# Guest class representing a hotel guest
class Guest:
    """
    Represents a guest with personal details and reservation history.
    """

    def __init__(self, guest_id: str, name: str, contact_info: str, reservation_history: list[str]):
        # Protected attributes
        self._guest_id = guest_id
        self._name = name
        self._contact_info = contact_info
        self._reservation_history = reservation_history

    # Getter and setter methods for protected attributes
    def get_guest_id(self):
        """Returns the guest ID."""
        return self._guest_id

    def set_guest_id(self, guest_id: str):
        """Sets the guest ID."""
        self._guest_id = guest_id

    def get_name(self):
        """Returns the guest name."""
        return self._name

    def set_name(self, name: str):
        """Sets the guest name."""
        self._name = name

    def get_contact_info(self):
        """Returns the contact information."""
        return self._contact_info

    def set_contact_info(self, contact_info: str):
        """Sets the contact information."""
        self._contact_info = contact_info

    def get_reservation_history(self):
        """Returns the reservation history."""
        return self._reservation_history

    def set_reservation_history(self, history: list[str]):
        """Sets the reservation history."""
        self._reservation_history = history

    def __str__(self):
        """Returns a string representation of the guest."""
        return f"Guest {self._guest_id}: {self._name}, Contact: {self._contact_info}"


# LoyalGuest class, inheriting from Guest
class LoyalGuest(Guest):
    """
    Represents a loyal guest with additional benefits such as loyalty points and membership level.
    """

    def __init__(self, guest_id: str, name: str, contact_info: str, reservation_history: list[str], loyalty_points: int,
                 membership_level: str, discount_rate: float):
        super().__init__(guest_id, name, contact_info, reservation_history)
        # Private attributes
        self.__loyalty_points = loyalty_points
        self.__membership_level = membership_level
        self.__discount_rate = discount_rate

    # Getter and setter methods for private attributes
    def get_loyalty_points(self):
        """Returns the loyalty points."""
        return self.__loyalty_points

    def set_loyalty_points(self, points: int):
        """Sets the loyalty points."""
        self.__loyalty_points = points

    def get_membership_level(self):
        """Returns the membership level."""
        return self.__membership_level

    def set_membership_level(self, level: str):
        """Sets the membership level."""
        self.__membership_level = level

    def get_discount_rate(self):
        """Returns the discount rate."""
        return self.__discount_rate

    def set_discount_rate(self, rate: float):
        """Sets the discount rate."""
        self.__discount_rate = rate

    def add_loyalty_points(self, points: int):
        """Adds loyalty points to the guest's account."""
        self.__loyalty_points += points

    def redeem_loyalty_points(self, points: int):
        """Redeems loyalty points if available."""
        if points <= self.__loyalty_points:
            self.__loyalty_points -= points
        else:
            print("Insufficient loyalty points.")

    def __str__(self):
        """Returns a string representation of the loyal guest."""
        return super().__str__() + f", Membership: {self.__membership_level}, Points: {self.__loyalty_points}"



class Hotel:
    """
    Represents a hotel with attributes such as name, location, total rooms, and rating.
    """
    def __init__(self, hotel_name: str, location: str, total_rooms: int, rating: float):
        self.__hotel_name = hotel_name  # Private attribute
        self.__location = location  # Private attribute
        self.__total_rooms = total_rooms  # Private attribute
        self.__rating = rating  # Private attribute

    # Getters and setters
    def get_hotel_name(self):
        return self.__hotel_name

    def set_hotel_name(self, hotel_name: str):
        self.__hotel_name = hotel_name

    def get_location(self):
        return self.__location

    def set_location(self, location: str):
        self.__location = location

    def get_total_rooms(self):
        return self.__total_rooms

    def set_total_rooms(self, total_rooms: int):
        self.__total_rooms = total_rooms

    def get_rating(self):
        return self.__rating

    def set_rating(self, rating: float):
        self.__rating = rating

    def __str__(self):
        return f"Hotel: {self.__hotel_name}, Location: {self.__location}, Rooms: {self.__total_rooms}, Rating: {self.__rating}"


class Booking:
    """
    Represents a hotel booking with attributes such as booking ID, guest ID, room number, check-in and check-out dates, and booking status.
    """
    def __init__(self, booking_id: str, guest_id: str, room_number: str, check_in_date: str, check_out_date: str, booking_status: str):
        self.__booking_id = booking_id  # Private attribute
        self.__guest_id = guest_id  # Private attribute
        self.__room_number = room_number  # Private attribute
        self.__check_in_date = check_in_date  # Private attribute
        self.__check_out_date = check_out_date  # Private attribute
        self.__booking_status = booking_status  # Private attribute

    # Getters and setters
    def get_booking_id(self):
        return self.__booking_id

    def set_booking_id(self, booking_id: str):
        self.__booking_id = booking_id

    def get_guest_id(self):
        return self.__guest_id

    def set_guest_id(self, guest_id: str):
        self.__guest_id = guest_id

    def get_room_number(self):
        return self.__room_number

    def set_room_number(self, room_number: str):
        self.__room_number = room_number

    def get_check_in_date(self):
        return self.__check_in_date

    def set_check_in_date(self, check_in_date: str):
        self.__check_in_date = check_in_date

    def get_check_out_date(self):
        return self.__check_out_date

    def set_check_out_date(self, check_out_date: str):
        self.__check_out_date = check_out_date

    def get_booking_status(self):
        return self.__booking_status

    def set_booking_status(self, booking_status: str):
        self.__booking_status = booking_status

    def __str__(self):
        return f"Booking ID: {self.__booking_id}, Guest ID: {self.__guest_id}, Room: {self.__room_number}, Check-in: {self.__check_in_date}, Check-out: {self.__check_out_date}, Status: {self.__booking_status}"



class Payment:
    """
    Represents a payment transaction for a booking, including payment method and amount.
    """

    def __init__(self, payment_id: str, booking: Booking, amount: float, payment_method: str, payment_status: str):
        # Private attributes
        self.__payment_id = payment_id
        self.__booking = booking
        self.__amount = amount
        self.__payment_method = payment_method  # "Credit Card", "Cash", "Online"
        self.__payment_status = payment_status  # "Pending", "Completed", "Failed"

    # Getter and setter methods for private attributes
    def get_payment_id(self):
        """Returns the payment ID."""
        return self.__payment_id

    def get_booking(self):
        """Returns the booking associated with this payment."""
        return self.__booking

    def set_booking(self, booking: Booking):
        """Sets the booking for this payment."""
        self.__booking = booking

    def get_amount(self):
        """Returns the payment amount."""
        return self.__amount

    def set_amount(self, amount: float):
        """Sets the payment amount."""
        self.__amount = amount

    def get_payment_method(self):
        """Returns the payment method."""
        return self.__payment_method

    def set_payment_method(self, method: str):
        """Sets the payment method."""
        self.__payment_method = method

    def get_payment_status(self):
        """Returns the payment status."""
        return self.__payment_status

    def set_payment_status(self, status: str):
        """Sets the payment status."""
        self.__payment_status = status

    def process_payment(self):
        """Simulates processing a payment."""
        if self.__payment_status != "Completed":
            self.__payment_status = "Completed"

    def __str__(self):
        """Returns a string representation of the payment."""
        return f"Payment {self.__payment_id}: {self.__amount} via {self.__payment_method}, Status: {self.__payment_status}"



class Invoice:
    """
    Represents an invoice linked to a booking, including invoice ID, guest ID, room charges, and the ability to calculate total charges.
    """
    def __init__(self, invoice_id: str, booking_id: str, guest_id: str, room_charges: float):
        self.__invoice_id = invoice_id  # Private attribute
        self.__booking_id = booking_id  # Private attribute
        self.__guest_id = guest_id  # Private attribute
        self.__room_charges = room_charges  # Private attribute

    # Getters and setters
    def get_invoice_id(self):
        return self.__invoice_id

    def set_invoice_id(self, invoice_id: str):
        self.__invoice_id = invoice_id

    def get_booking_id(self):
        return self.__booking_id

    def set_booking_id(self, booking_id: str):
        self.__booking_id = booking_id

    def get_guest_id(self):
        return self.__guest_id

    def set_guest_id(self, guest_id: str):
        self.__guest_id = guest_id

    def get_room_charges(self):
        return self.__room_charges

    def set_room_charges(self, room_charges: float):
        self.__room_charges = room_charges

    def calculate_total(self, discounts: float):
        """Calculates the total cost after applying discounts."""
        return max(0, self.__room_charges - discounts)

    def __str__(self):
        return f"Invoice ID: {self.__invoice_id}, Booking ID: {self.__booking_id}, Guest ID: {self.__guest_id}, Room Charges: {self.__room_charges}"

