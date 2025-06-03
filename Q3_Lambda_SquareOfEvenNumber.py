#Question - 3
#Create a list of numbers
#Form new list of squares of even number using list comprehension
#Even numbers list - using lambda function

numbers=[3,4,7,8,10]

evennumbers=list(filter(lambda x:x%2==0,numbers))

square_even=[n**2 for n in evennumbers]

print("Squares of even numbers:",square_even)