""" You are given a string . Suppose a character '' occurs consecutively  times in the string. Replace these consecutive 
occurrences of the character '' with  in the string."""
# Sample Input : 1222311
# Sample Output : (1, 1) (3, 2) (1, 3) (2, 1)

s=input()
i=0
l=[]
k=1
while i<len(s):
    if (i+1<len(s)) and (s[i]==s[i+1]):
        k+=1
        i+=1
    else:
        l.append(tuple([k,int(s[i])]))
        k=1
        i+=1
for x in l:
    print(x,end=' ')
