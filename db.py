from models.resort import Resort
from models.room import Room
from models.restaurant import Restaurant
from models.swimming_pool import SwimmingPool
from models.family_member import FamilyMember
from models.main_guest import MainGuest
from models.contact_information import ContactInformation
from models.resevation import Reservation
from models.room_reservation import RoomReservation

import datetime


class DB:
    room1 = Room('room1', 80, 2, 'behind bar', 'Pool', 'regular', 80, False)
    room2 = Room('room2', 110, 3, 'behind bar', 'Pool', 'regular', 100, False)
    room3 = Room('room3', 120, 3, 'behind bar', 'Pool', 'regular', 140, False)
    room4 = Room('room4', 180, 4, 'behind pool', 'Pool', 'regular', 200, False)
    room5 = Room('room5', 200, 4, 'behind bar', 'Pool', 'regular', 230, True)
    room6 = Room('room6', 140, 2, 'behind bar', 'Pool', 'luxury', 100, False)
    room7 = Room('room7', 160, 2, 'behind pool', 'Ocean', 'luxury', 120, False)
    room8 = Room('room8', 90, 2, 'behind bar', 'Pool', 'regular', 110, False)
    room9 = Room('room9', 130, 3, 'behind bar', 'Pool', 'regular', 160, True)
    room10 = Room('room10', 200, 3, 'behind pool', 'Bar', 'luxury', 180, False)
    room11 = Room('room11', 240, 4, 'behind bar', 'Ocean', 'regular', 210, False)
    room12 = Room('room12', 300, 4, 'behind bar', 'Ocean', 'luxury', 320, False)
    room13 = Room('room13', 100, 2, 'behind pool', 'Pool', 'regular', 90, True)
    room14 = Room('room14', 130, 3, 'behind bar', 'Pool', 'regular', 140, True)
    room15 = Room('room15', 180, 4, 'behind bar', 'Pool', 'regular', 160, False)
    room16 = Room('room16', 160, 3, 'behind bar', 'Pool', 'luxury', 200, True)
    room17 = Room('room17', 70, 2, 'behind bar', 'Pool', 'regular', 90, False)
    room18 = Room('room18', 100, 3, 'behind bar', 'Pool', 'regular', 110, False)
    room19 = Room('room19', 140, 2, 'behind bar', 'Pool', 'regular', 140, False)
    room20 = Room('room20', 180, 3, 'behind bar', 'Pool', 'regular', 160, True)

    r1 = Restaurant('sea_food', '0-24', 300)
    r2 = Restaurant('italian', '10-15', 300)
    r3 = Restaurant('mexican', '0-24', 300)
    r4 = Restaurant('sea_food', '16-20', 300)
    r5 = Restaurant('mexican', '16-20', 300)
    r6 = Restaurant('chinese', '0-24', 300)

    s1 = SwimmingPool('adult', '0-24', 'behind_bar', 80, 100)
    s2 = SwimmingPool('family', '0-24', 'behind_bar', 180, 200)
    s3 = SwimmingPool('family', '8-20', 'beach', 110, 120)
    s4 = SwimmingPool('adult', '0-24', 'beach', 180, 120)
    s5 = SwimmingPool('adult', '8-20', 'behind_bar', 110, 140)

    res1 = Resort('Blue Mountain', 'Winter', 'Perfect Location for winter skying',
                  4, [room1, room2, room3], [r1, r2], [s1, s2], 'lobby')
    res2 = Resort('Winter Spa', 'Winter', 'Spa while snowing',
                  5, [room1, room2, room3], [r1, r2], [s1, s2, s4], 'lobby_room')
    res3 = Resort('Hot Tea', 'Winter', 'Affordable bed and breakfast',
                  3, [room4, room5, room6], [r3, r4], [s3, s4, s5], 'lobby_room')
    res4 = Resort('Blue Sea', 'Caribbean', 'Best beach ever seen',
                  4.5, [room7, room8, room9], [r1, r2], [s1, s2, s3], 'no_access')
    res5 = Resort('Marina', 'Caribbean', 'Enjoy the warm weather',
                  4, [room10, room11, room12], [r1, r2], [s1, s2, s4], 'lobby')
    res6 = Resort('Gold Fish', 'Caribbean', 'Paradise of food lovers',
                  5, [room13, room14, room15, room20], [r1, r5, r6], [s1, s2, s3], 'no_access')
    res7 = Resort('Old Castle', 'History', 'Experience the old era',
                  4.5, [room16, room17, room18, room19], [r5, r3, r2], [s1, s4, s5], 'lobby_room')

    resorts = [res1, res2, res3, res4, res5, res6, res7]

    fm1 = FamilyMember('bob', 'smith', datetime.date(1988, 1, 1), 'spouse')
    fm2 = FamilyMember('jack', 'smith', datetime.date(2000, 4, 10), 'child')
    fm3 = FamilyMember('richard', 'black', datetime.date(1985, 9, 17), 'brother')
    fm4 = FamilyMember('ana', 'fisher', datetime.date(1973, 4, 12), 'spouse')

    ci1 = ContactInformation('123 test st', '', '12345', 'Toronto', 'ON', 'CA', '1234567890', 'test1@test.ca')
    ci2 = ContactInformation('123 test st', '', '12345', 'Toronto', 'ON', 'CA', '1234567890', 'test1@test.ca')

    mg1 = MainGuest('Rose', 'white', datetime.date(1993, 6, 2), ci1, [fm1, fm2])
    mg2 = MainGuest('Joe', 'Brown', datetime.date(1956, 2, 14), ci2, [fm3, fm4])

    room_res1 = RoomReservation(None, res1, room1, 80)
    reservation1 = Reservation('active', 'approved',
                               room_res1, mg1, datetime.date(2020, 11, 15), datetime.date(2020, 11, 22))
    room_res1.reservation = reservation1

    room_res2 = RoomReservation(None, res2, room1, 90)
    reservation2 = Reservation('active', 'approved',
                               room_res2, mg1, datetime.date(2020, 11, 15), datetime.date(2020, 11, 22))
    room_res2.reservation = reservation2

    reservations = [reservation1, reservation2]
