def sentence_reversal(mystr):
    nlist = []
    newstr = ""
    nstr = ""
    mystr = mystr.strip()
    for i in range(len(mystr)):
        if mystr[i] == " " and mystr[i] == mystr[i + 1]:
            continue
        else:
            nstr = nstr + mystr[i]

    for i in range(len(nstr)):
        sp = nstr.count(" ")
        
        if i == len(nstr) - 1:
            newstr += nstr[i]
            nlist.append(newstr)
            
        if nstr[i] != " ":
            newstr += nstr[i]

        else:
            nlist.append(newstr)
            newstr = ""
            
    nstr = " ".join(nlist[::-1])
            

    return nstr


print(sentence_reversal("   This    is  a  boy    "))
