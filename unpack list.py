
'''
name, age, birthday = ['esha', 22, '05-01-1998']
print(age)
print(name)
print(birthday)
'''

def her_characteristics (list):
    name, *chars = list
    print(name)

    for x in chars:
        print(x)

characteristics = ['esha','5\'3"','dark circles','tiny hands','long hair','necklace','rings','loves cats','loves music']

her_characteristics(characteristics)

#### ZIP TOO ####

first = ['Rawson', 'Ragib', "Maisha"]
last = ['Tabassum', 'Shahriar', 'Mahjabin']

names = zip(first, last)

for a, b in names:
    print(a, b)

print('\n',names)



####  LAMBDA  ####

ans = lambda x : x ** x

print(ans(5))