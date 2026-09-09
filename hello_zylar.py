score = 0

answer1 = input("What's the capital of burundi ? ")
if answer1.lower() == "bujumbura":
    score = score + 1

answer2 = input("What's the capital of switzerland? ")
if answer2.lower() == "bern":
    score = score + 1

answer3 = input("How many continents do we have ?")
try:
    answer3 = int(answer3)
    if answer3 == 7:
        score = score + 1
        print(f"Correct! There are {answer3} continents")
    else:
        print("incorrect answer")

except:
   print("That's not a valid number")
   
print(f"you got  {score}  out of 3 correct")