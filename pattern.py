'''Prints pattern'''
n=int(input()) #takes input from user
l=[str(x) for x in range(n*2) if x%2!=0] #generates list of odd numbers using list comprehension
for _ in range(n):
    print(''.join(l)) # generating the pattern
    x=l[0]
    l.remove(x)
    l.append(x)
