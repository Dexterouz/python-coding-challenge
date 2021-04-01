question = [
        ["In which year was python created","1989"],
        ["(1 == 1) is equal to", "true"],
        ["'aaa' * 3 print how many 'a' ","9"],
        ["What keyword is use in defining a python function","def"],
        ["Python is an Interpreted language? True or False","true"],
        ["We can use '{}' in an if statement in python? True or False","false"]
    ]
score = 0
correction = []
for i in range(len(question)):
    answer = str(input(question[i][0]+": "))
    if(question[i][1] == answer):
        score += 5
        print("You got it right!")
    
    if(question[i][1] != answer):
        correction.append(question[i][0]+" = "+question[i][1])
        score += 0
        print("You got it wrong!")

print("\n")
print("Quiz Over! Total score is ",score," point")

print("\n")
if(len(correction) != 0):
    print("Here are your corrections")
    for i in range(len(correction)):
        print(i+1,". "+correction[i])
