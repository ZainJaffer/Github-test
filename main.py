
persons = [ 
    {'Name' : 'Bob', 'Age' : 42, 'Occupation' : 'Student'}, 
    {'Name' : 'Clark', 'Age' : 32, 'Occupation' : 'Bank Clerk'},
    {'Name' : 'John', 'Age' : 22, 'Occupation' : 'Office Manager'}
]


# sum the age of the dictionary elements

ages = 0

for x in persons:
    ages += x['Age']

print("Total age is:", ages)

