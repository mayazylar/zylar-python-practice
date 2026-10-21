quiz = {"What's the capital of Canada?": "Ottawa", "What's the capital of Switzerland?": "Bern", "What's the legal age in British Columbia?": "19"}
score = 0
for key in quiz:
    answer = input(key)
    if answer.lower() == quiz[key].lower():
            score = score + 1
print("You have " + str(score) + "out of 3 correct")
