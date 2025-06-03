# Question - 4
# create lambda function isnum_decimal
# Replacing the decimal point by 1
# and check the string with isnumeric function to verify it is numeric value or not
# create lambda function isnum_sign to ignoring the first place of string to validate negative numbers


isnum_decimal=lambda dec : dec.replace('.','1').isnumeric()

isnum_sign=lambda n: isnum_decimal(n) if n[0]!='-' else isnum_decimal(n[1:])

strlist =['121','-13','1e','12.34','-0.p']

for i in range(len(strlist)):
    print(strlist[i],"is number:",isnum_sign(strlist[i]))


