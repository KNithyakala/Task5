#Question - 6
#variable term - get input from prompt
#create fibonacci function with lambda and reduce function
#import reduce from functools
#reduce function with arguments lambda function, iterate upto n-2(n->term),initializer [0,1]
#lambda function is with one ignored variable using _ which will take iterable value(based "term" value
#(eg) for term=4--> n=4--->range 2--->x=[0,1]+[0+1]-->[0,1,1]+[1+1]-->[0,1,1,2]
#x[-1]+x[-2] will add the last two numbers in the series and then add this value to the series


from functools import reduce

term = int(input("Enter Terms for fibonacci series:"))

fibonacci = lambda n: reduce(lambda x,_:x+[x[-1]+x[-2]],range(n-2),[0,1])

print("Fibonacci series of",term,":",fibonacci(term))


