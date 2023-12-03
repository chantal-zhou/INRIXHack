import math

def getCoordinates(resp):
    coordinates = {}
    for spot in resp["result"]:
        coordinates.update({spot["name"] : spot["point"]["coordinates"]})
    return coordinates

def getDistances(resp, point):
    distances = getCoordinates(resp)
    for spot in distances:
        distances.update({spot : math.dist(distances.get(spot), point)})
    return distances

def getCostIndex(resp):
    costs = {}
    for spot in resp["result"]:
        costs.update({spot["name"] : spot["costIndex"]})
    return costs

def getPrices(resp):
    prices = {}
    for spot in resp["result"]:
        prices.update({spot["name"] : spot["rateCard"]})
    return prices

def getAvailabilities(resp):
    available = {}
    for spot in resp["result"]:
        available.update({spot["name"] : spot["occupancy"]["available"]})
    return available

def isOpen(resp):
    open = {}
    for spot in resp["result"]:
        open.update({spot["name"] : spot["isOpen"]})
    return open