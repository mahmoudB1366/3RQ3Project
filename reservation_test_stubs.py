from models.resevation import Reservation
import datetime

from db import DB

db = DB()


# Requirement 4.3.1.1: Main Guest
def test_main_guest():
    reservation = Reservation('active', 'paid', db.room_res1, db.mg1, 123)
    assert reservation.set_main_guest(None) is False, 'main guest is required for reservation!'


# Requirement 4.3.2 Reservation period
def test_reservation_period_default_dates():
    reservation = Reservation('active', 'paid', db.room_res1, db.mg1)

    assert reservation.start_date == datetime.date.today() + datetime.timedelta(days=7), \
        'default value for reservation start date should be 7 days from the current date!'
    assert reservation.end_date == datetime.date.today() + datetime.timedelta(days=14), \
        'default value for reservation  end date should be 14 days from the current date!'


# Requirement 4.5.2 Reference number
def test_reference_number():
    reservation1 = Reservation('active', 'paid', db.room_res1, db.mg1)
    reservation2 = Reservation('active', 'paid', db.room_res2, db.mg2)

    assert reservation1.reference_number != reservation2.reference_number, 'reservation number should be unique!'


# Requirement 4.7 Cancellation
def test_cancellation():
    reservation1 = Reservation('active', 'paid', db.room_res1, db.mg1,
                               datetime.date.today() + datetime.timedelta(days=1),
                               datetime.date.today() + datetime.timedelta(days=8))
    reservation2 = Reservation('active', 'paid', db.room_res2, db.mg2,
                               datetime.date.today() + datetime.timedelta(days=3),
                               datetime.date.today() + datetime.timedelta(days=10))

    result1 = reservation1.cancel()
    result2 = reservation2.cancel()

    assert result1 is False, 'cancellation is only allowed before 48 hours of arrival!'
    assert result2 is True, 'cancellation is only allowed before 48 hours of arrival!'
    assert reservation2.reservation_status == 'cancel', 'cancelled reservation should have proper status'


if __name__ == '__main__':
    test_main_guest()
    test_reservation_period_default_dates()
    test_reference_number()
    test_cancellation()
