#Alex Thayn 1/29/2019
#Sum of all multiples of 3 or 5 less than 1000
#Answer = 233168

def SumMultiplesOf3And5LessThan1000():
    sum = 0
    for i in range(1000):
        #check if number is a multiple of 3 or 5
        if i % 5 == 0 or i % 3 == 0:
            sum += i
    return sum

print(SumMultiplesOf3And5LessThan1000())