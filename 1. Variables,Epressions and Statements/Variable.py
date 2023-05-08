#Variable => store data
#Expressions => + - * / ** %
#type() => Check type variable
#implicitly converted
#String Conversions
#Ex => int() and float()
#User input => pause and read data from the user 
#Using the input() function
#The input() function return a string
name = input('Who are you? ')
print('Wellcome',name)

inp = input('Europe floor?')
usf = int(inp) + 1
print('US Floor',usf)

#Get the name of the file and open it
name = input('Enter file:')
handle = open(name,'r')

#Count word frequence
counts = dict()
for line in handle:
       worlds = line.split()
       for word in worlds:
           counts[word] = counts.get(word,0)+1
           
#Find the most common word
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
#All donw
print(bigword, bigcount)