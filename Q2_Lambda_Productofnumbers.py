#Question - 2
#Create list of numbers
#Use reduce function (need import reduce function from functools)
#reduce function - lambda expression and list of numbers(iterable) as arguments
#reduce - returns a single value-->here 10*15=150*12=1800*20=36000

from functools import reduce

numbers=[10,15,12,20]

productofnumbers = reduce(lambda a,b: a*b, numbers)

print("Product of numbers in the list:",productofnumbers)

