def getPrices():
  result = dict()
  for i in range(0,len(resp["result"])): 
    test = resp["result"][i]
    price = test["rateCard"]
    location = test["name"]
    result.update({location : price})
  print(result)
