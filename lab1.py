print("hello, world!!") #This is a comment

x=5
y="mary"

print(x)
print(y)
print(x,y)

x , y, z = "orange", "banana", "cherry"
print (x,y,z)
print (x+y+z)

print (10>9)
print (10==9)

a=200
b=200

if b > a:
    print ("b is greater than a")
elif b < a:
    print ("b is smaller than a")
else:
    print (" b is equal to a")
 

for r in range(6):
    print(r)

fruits = ["apple", "banana", "cherry", "orange"]
for x in fruits:
    print(x)
    if x == "banana":
        break

students = {"john": 16, "mary": 17, "sam":18}

for name in students: #print key
    print (name)

for name in students: #print value
    print ("age is :", students[name])

for name, age in students.items():
    print (name+"'s age is :", age)




students = {"john":"m", "mary":"f", "sam":"m"}

for name, sex in students.items():
    if sex == "m":
        print (name, "is a boy")
    else:
        print (name, "is a girl")

#john is a boy
#mary is a girl
#sam is a boy

import random
print (random.randint(0,9))


name = input("what is your name? ")
print ("my name is", name)