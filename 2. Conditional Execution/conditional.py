x = 5
if x < 10:
    print('Smaller')
if x > 20:
    print('Bigger')
    
print('Finis')

#Comparison Operators
#Boolean expressions < <= == >= > !=
#Remember: "=" is used for assignment

#Think about begin/end Blocks

x = 5
if x > 2:
    print('Bigger Than 2')
    print('Still bigger')
print('Done with 2')

for i in range(5) :
    print(i)
    if i > 2 :
        print('Bigger than 2')
    print('Done with i', i)
print('All Done')

#Nested Decisions
x  = 42

if(x>1):
    print('More than 1')
    if(x<100): 
        print('Less than 100')
print('All Done')

#Two-way Decisions
x = 4 
if(x>2): #or if x > 2
    print('Bigger')
else:
    print('Not Bigger')
print('All Done')

x = 0
#Multi-way
if x < 2 :
    print('Small')
elif x < 10 :
    print('Medium')
else:
    print('LARGE')
print('All DOne')

#Multi-way use elif

#No Else
x = 5
if x < 2 :
    print('small')
elif x < 10 :
    print('Medium')
    
print('All done')

#The Try / except Structure
# Surround a dangerous section of code with try and except

astr = 'Hello ThanhVu'
try:
    istr = int(astr)
except:
    istr = -1

print('First',istr)

astr = '123'

try:
    istr = int(astr)
except:
    istr = -1
    
print('Second',istr)

#Try/except

astr = 'Bob'
try:
    print('Hello')
    istr = int(astr)
    print('There')
except:
    istr = -1

print('Done',istr)

#Sample try / except

rawstr = input('Enter a number:')
try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0 :
    print('Nice work')
else:
    print('Not a number')
    
#Exercise

while True:
   try:
        hour = int(input("Enter Hours: "))
        rate = int(input("Enter Rate:"))
        print("Pay: ",hour*rate)
        break
   except:
       print("Eorror, please enter numeric input")