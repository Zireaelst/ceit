personalDataDict = {
    'Joe': {
        'height': 73,
        'weight': 200,
        'sex': 'M',
        'age': 35,
        'allergies': ['tree pollen', 'carrots', 'onions']
    },
    'Sally': {
        'height': 58,
        'weight': 100,
        'sex': 'F',
        'age': 32,
        'allergies': ['bee stings']
    },
    'John': {
        'height': 36,
        'weight': 75,
        'sex': 'M',
        'age': 8,
        'allergies': ['peanuts']
    },
    'Mary': {
        'height': 35,
        'weight': 60,
        'sex': 'F',
        'age': 7,
        'allergies': []
    }
}

for personName in personalDataDict:
    onePersonDict = personalDataDict[personName]
    age = onePersonDict['age']
    sex = onePersonDict['sex']
    height = onePersonDict['height']
    weight = onePersonDict['weight']
    allergyList = onePersonDict['allergies']

    print(f"Name: {personName}")
    print(f"Age: {age}")
    print(f"sex: {sex}")
    print(f"Height: {height}")
    print(f"Weight: {weight}")

    if not allergyList:
        print(personName, 'is not allergic to anything')
    else:
        print(personName, 'is allergic to the following:')
        for allergy in allergyList:
            print(f"    *{allergy}*")
