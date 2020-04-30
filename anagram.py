lst=input("Enter space separated words to group anagrams ").split()
d={}
for word in lst:
    key=''.join(sorted(word))
    #check if key exists in dictionary
    if key in d.keys():
        d[key].append(word)
    else:
        d[key]=[]
        d[key].append(word)
for k,v in d.items():
    print(v)
