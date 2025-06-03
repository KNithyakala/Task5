#Question - 1
#Create a list of dictionary with name and age

person=[{'name':'Nithya','age':42},{'name':'Harrshit','age':7},{'name':'Rithesh','age':12},
        {'name':'Bala','age':42},{'name':'Saraswathy','age':68},{'name':'Kavya','age':18}]


under18=list(filter(lambda x:x['age']<18,person))

print("Person under 18:",under18)
print("\n")
adult=[x['name'] for x in person if x not in (list(filter(lambda x:x['age']<18,person)))]
print("Adult in the list:",adult)

