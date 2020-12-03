import datetime
import random


# returns a unique reservation number
def get_reference_number():
    return random.getrandbits(32)


class Reservation:
    def __init__(self, reservation_status, payment_status,
                 room_reservations, main_guest, start_date=datetime.date.today() + datetime.timedelta(days=7),
                 end_date=datetime.date.today() + datetime.timedelta(days=14)):
        self.start_date = start_date
        self.end_date = end_date
        self.reservation_status = reservation_status
        self.payment_status = payment_status
        self.room_reservations = room_reservations
        self.main_guest = main_guest
        self.reference_number = get_reference_number()

    def set_main_guest(self, main_guest):
        if main_guest is None:
            return False
        else:
            self.main_guest = main_guest
            return True

    def cancel(self):
        if self.start_date - datetime.date.today() > datetime.timedelta(2):
            self.reservation_status = 'cancel'
            return True
        else:
            return False
