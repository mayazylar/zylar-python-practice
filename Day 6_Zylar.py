people = [ {"name" : "Angie", "age" : "28", "origin": "Guada"}, {"name": "Jiggy", "age" : "28", "origin" : "Nigeria"}, {"name" : "Zylar", "age": "25", "origin" : "Switzerland"}]
for person in people:
    print(person["name" ]  + " is " +  person["age" ])
    if int(person ["age"]) >= 18:
        print("adult")
    else:
        print("minor")