import requests

class parkingSpot:
    @staticmethod
    def getCoordinates(resp):
        coordinates = {}
        for spot in resp["result"]:
            coordinates.update({spot["name"] : spot["point"]["coordinates"]})
        return coordinates
    @staticmethod
    def getPrices(resp):
        prices = {}
        for spot in resp["result"]:
            prices.update({spot["name"] : spot["rateCard"]})
        return prices
