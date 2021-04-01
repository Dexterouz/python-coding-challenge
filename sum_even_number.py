'''
    This program accept the length of a list through an input
    and then provide the numbers through an input which is in the range
    in size of the list, after then it calculates the  even numbers provided
    in the list e.g
    list[1,2,3,4,5,6,7,8,9], sum of even numbers = 2+4+6+8 = 20
'''
# declaring and empty number list
numbers = []

# initialzing the even number variable to zero
even_num = 0

# input to specify the size of the numbers list
size = int(input("Enter the size of your list: "))

# looping the input by the size specified
for i in range(0, size):
    number = int(input("Enter your number: "))
    # appending the number in the numbers list
    numbers.append(number) 

# looping through the numbers list 
for number in numbers:
    # check if numbers are even, then add all together
    if (number % 2) == 0:
        even_num += number

print("The total of the even numbers are: " + str(even_num))