#Alex Thayn 2/10/19
# Write a program that outputs all possibilities to put the operator '+', '-', or nothing
# between the numbers 1,2...,9

import itertools

possibleOperators = ['+', '-', '']
numbers = "1%s2%s3%s4%s5%s6%s7%s8%s9"
TOTAL = 100

def allPossiblitiesOf100():
    #find all possible placement of + , - , or nothing by doing a cartesian product
    for i in itertools.product(possibleOperators, possibleOperators, possibleOperators, possibleOperators, possibleOperators, possibleOperators, possibleOperators,possibleOperators):
        #check if the equation evaluates to 100
        if eval(numbers % i) == TOTAL:
            print(numbers % i + " = 100")


if __name__ == "__main__":
    allPossiblitiesOf100()


