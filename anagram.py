'''Anagram program'''
lst=input("Enter space separated words to group anagrams ").split()
d={}
for word in lst:
    KEY=''.join(sorted(word))
    #check if key exists in dictionary
    if KEY in d.keys():
        d[KEY].append(word)
    else:
        d[KEY]=[]
        d[KEY].append(word)
for k,v in d.items():
    print(v)
