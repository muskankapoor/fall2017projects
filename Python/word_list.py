def buildWordList(s):
    """function should build and return a dictionary where the
keys are the words in the input strinb. The entry for each key will be a list and the itdm in he list
will be all the words thata follow they key word."""
    #create a dictioanry that will loop throught all the strings
    

def buildWordList(text):
    l = [] #empty list
    d = {} #empty dictionary
    for w in text.split(): 
        w = w.lower()
        word = ''
        for x in w:
            if x.isalpha():
                word += x
        if word != '':
            l.append(word)
    return l

def buildwordphrasedictionary(text):
    pd = {}
    l = buildwordlist(text)
    for i in range(len(l)-1):
        pd.setdefault(l[i],list())
        pd[l[i]].append(l[i+1])
    return pd

def bwpdhuman(text):
    d = buildwordphrasedictionary(text)
    k = list(d.keys())
    v = list(d.values())
    for i in range(len(k)):
        r = print(k[i], ':', v[i])
    return r

print (buildWordList('ooh child things are going to get easier ohh child things will get brighter'))
print 
