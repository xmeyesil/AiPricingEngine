import random
import time


class RoomTypes:

    def __init__(self, roomType, pax):
        self.roomType = roomType
        self.pax = pax

    def toString(self):
        return (self.roomType, self.pax)

    def tipBaz(self):

        economic = {
            "pax": self.pax,
            "id": 7 if self.pax == 1 else (4 if self.pax == 2 else 0),
            "basePrice": 70 if self.pax == 1 else (80 if self.pax == 2 else 100),
            "maxPrice": 350 if self.pax == 1 else (400 if self.pax == 2 else 500),
            "minPrice": 35 if self.pax == 1 else (40 if self.pax == 2 else 50),
            "totalRoomCount": 25 if self.pax == 1 else (60 if self.pax == 2 else 80)
        }

        standard = {
            "pax": self.pax,
            "id": 8 if self.pax == 1 else (5 if self.pax == 2 else 1),
            "basePrice": 140 if self.pax == 1 else (170 if self.pax == 2 else 200),
            "maxPrice": 560 if self.pax == 1 else (680 if self.pax == 2 else 800),
            "minPrice": 70 if self.pax == 1 else (85 if self.pax == 2 else 100),
            "totalRoomCount": 25 if self.pax == 1 else (80 if self.pax == 2 else 110)
        }

        self.else_ = {
            "pax": self.pax,
            "id": 6 if self.pax == 2 else 2,
            "basePrice": 250 if self.pax == 2 else 300,
            "maxPrice": 1000 if self.pax == 2 else 1200,
            "minPrice": 125 if self.pax == 2 else 150,
            "totalRoomCount": 40 if self.pax == 2 else 80
        }
        deluxe = self.else_

        suit = {
            "pax": 3,
            "id": 3,
            "basePrice": 400,
            "maxPrice": 1700,
            "minPrice": 200,
            "totalRoomCount": 40
        }

        if (self.roomType == "economic"):
            return 'Kisi Sayisi: {} Id: {} Max Fiyat: {} Max Fiyat: {} Min Fiyat: {} Oda Adedi: {} '.format(
                economic['pax'], economic['id'], economic['basePrice'], economic['maxPrice'],
                economic['minPrice'], economic['totalRoomCount'])

        if (self.roomType == "standard"):
            return 'Kisi Sayisi: {} Id: {} Max Fiyat: {} Max Fiyat: {} Min Fiyat: {} Oda Adedi: {}'.format(
                standard['pax'], standard['id'], standard['basePrice'], standard['maxPrice'],
                standard['minPrice'], standard['totalRoomCount'])

        if (self.roomType == "deluxe"):
            return 'Kisi Sayisi: {} Id: {} Max Fiyat: {} Max Fiyat: {} Min Fiyat: {} Oda Adedi: {}'.format(
                deluxe['pax'], deluxe['id'], deluxe['basePrice'], deluxe['maxPrice'], deluxe['minPrice'],
                deluxe['totalRoomCount'])

        if (self.roomType == "suit"):
            return 'Kisi Sayisi: {} Id: {} Max Fiyat: {} Max Fiyat: {} Min Fiyat: {} Oda Adedi: {}'.format(
                suit['pax'], suit['id'], suit['basePrice'], suit['maxPrice'], suit['minPrice'], suit['totalRoomCount'])
