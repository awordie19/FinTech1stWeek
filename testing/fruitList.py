favFruits = ["mango", "avocado", "pineapple","grapes", "pomegranate"]

print(favFruits) 

favFruits.append("orange")

print(favFruits) 

enisFav = favFruits[2]

print(enisFav)

# favFruits.pop(2)

# print(favFruits)

favFruits.remove("pineapple")
print(favFruits)

for fruit in favFruits:
    print("I like " + fruit + ".")
    
for x in range(0, len(favFruits)):
    print("I like " + str(x))
    
fruitCriteria = [True, 0.20, True, True, 100, "banana", True]
fruitCriteria = {"is Fresh" : True, "costPerPound": 0.20, "isRipe": True, "inSeason":True, "howMuchILike": 100, "WhatIsIt": "banana", "isAllergic": True}
print(fruitCriteria)

fruitCriteria["specialFeature"] = "GMO"
print(fruitCriteria["isAllergic"])

print(fruitCriteria)


for key in fruitCriteria:
    print("The answer to " + str(key) + " is " + str(fruitCriteria[key]) + "." )
print(fruitCriteria["specialFeature"])

fruitCriteria["Organic"] = "fair"
print(fruitCriteria["Organic"])


