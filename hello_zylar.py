score = 0

answer1 = input("What's the capital of burundi ? ")
if answer1 == "bujumbura":
    score = score + 1

answer2 = input("What's the capital of switzerland? ")
if answer2 == "bern":
    score = score + 1

print("you got "  + str(score) + " out of 2 correct")