data = "Zylar,25,Dj Bujumbura, 7, Bern"
pieces = data.split(",")
name = pieces[0]
age = pieces = pieces[1]

try:
    age = int(age)
    if age >= 18:
        print(name + " is an adult")
    else:
        print(name + "is a minor")
except:
    print("Invalid age data")