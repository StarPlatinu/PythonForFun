
# n = 5
# while n > 0 :
#     print(n)
#     n = n - 1
# print('Blastoff')
# print(n)

# while True:
#     line = input('> ')
#     if(line[0] =="#"):
#         continue
#     if line == 'done':
#         break
#     print(line)
# print('Done')

#Simple loop
for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blastoff!')

#Loop with String

friends = ['HdUONG','bA cUONG','mINH aNH']
for friend in friends:
    print('Happy new year: ',friend)
print('Done!')

#Finding The largest value 
larget_so_far = -1 
print("Before",larget_so_far)
for the_num in [9,41,12,3,74,15] :
     if the_num > larget_so_far :
         larget_so_far = the_num
     print(larget_so_far,the_num)
print('After',larget_so_far)

#Finding the average in loop

count = 0
sum = 0 
print('Before',count,sum)
for value in [9,12,3,74,14] :
    count = count + 1
    sum = sum + value
    print(count,sum,value)
print('After',count,sum,sum/count)

#is and is not Operators
smallest =None
print('Before')
for value in [3,41,12,9,74,15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
        print(smallest,value)
print('After',smallest)