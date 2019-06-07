def rle(s):
    encoded = [] #empty list
    while len(s)>1: #lenth of string is grater than 1
        runlen = 1 #instilzqtion
        runchar = s[0] #instialization
        while runlen < len(s) and s[runlen]==runchar:
            runlen = runlen + 1
        #2
        if runlen>1:
            encoded.append(runlen)
            encoded.append(runchar)
        s=s[runlen:] 
    return encoded


s = "aavbbbbbccdddddd"
print(s)
print(rle(s))
print(s)