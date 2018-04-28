# If

a = 2
b = 4

if a == b:
   print(a)
   
# Exercise 1
   
if a < b:
    print(a)
    
    
if a == b:
   print(a)
else:
   print("Not equal")
   
# Exercise 2

a = 1
b = 2
c = 3

if a > b:
   a = a + b
   print(a)
else:
   print(b)
print(a)

# Elif

if a == b:
   print(a+b)
elif a > b:
   print(a)
else: 
   print(b)

# Exercise 3
   
if a < b:
   print("a is less than b")
elif a < c:
   print("a is less than c")
else:
   print(a)
   

if a < b:
   print("a is less than b")
else:
   print(a)
if a < c:
   print("a is less than c")
else:
   print(a)
   
# In the first block, the if condition is met so 
# the output is generated and the elif and else statements are 
# ignored.
   
# In the second block, both if statements are tested, the outputs
# are generated, and the else statements are ignored.

# For Loops
   
a = [1,2,3,4,5,6]

for i in a:
   print(i)
for i in a:
   print(i + 2)
   
# Exercise 4
   
for i in a[:3]:
    print(i)
    
    
for i in a:
   if i > 2:
      print(i)

b = [4,5]

for i in a:
   if i not in b:
      print(i)
    
# Exercise 5
      
a = [1,2,3,"Hello",4,5,"Hi",6]

for i in a:
    if type(i) == str:
        print(i)
        
# Exercise 6
        
b = []
for i in a:
    if type(i) == str:
        b.append(i)
        a.remove(i)
for i in a:
    print(i)
for i in b:
    print(i)
c = [i for i in a]
print(c)

    
# Exercise 7

b = []
for i in a:
    if type(i) == str:
        b.append(i)
        a.remove(i)
