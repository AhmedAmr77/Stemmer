

w="coding"
print "( "+w+" )"

def check(w):
    file1=open('C:\Users\Ahmd Amr\Desktop\wo.txt','r')
    for line in file1:
        if w in line:
            print w+" it'already a root"
            return True
    file1.seek(0)
#----------------------------------------------------
    file3=open('C:\Users\Ahmd Amr\Desktop\e.txt','r')
    cons=('b','c','d','f','g','h','j','k','l','m','n','o','p','q','r','s','t','v','w','y','z')
    vwl=('a','e','i','o','u')
    if w.endswith("ing"):
        suf=w[0:len(w)-3]
        if suf[len(suf)-1]==suf[len(suf)-2]:
            suff=suf[0:len(suf)-1]
            print suff+"    5"
            return True
        elif suf.endswith(cons):
            if suf[len(suf)-2] in vwl:
                suff=suf+"ed"
                for i in file3:
                    if suff==i:
                        print suff[0:len(suff)-1]
                        return True
    elif w.endswith("ed"):
        file3.seek(0)
        for line in file3:
            if w in line:
                suf=w[0:len(w)-1]
            else:
                suf=w[0:len(w)-2]
        print suf
        return True
    elif w.endswith("s"):
        suf=w[0:len(w)-1]
        file4=open('C:\Users\Ahmd Amr\Desktop\ie.txt','r')
        for x in file4:
            if suf in x:
                print suf+"    roooot"
                return True
        if suf.endswith("e"):
            if suf[len(suf)-2]in["o","x","z"]:
                suff=suf[0:len(suf)-1]
                print suff+"    1"
                return True
            elif suf[len(suf)-3:len(suf)-1]in["sh","ch","ss"]:
                suff=suf[0:len(suf)-1]
                print suff+"    2"
                return True
            elif suf[len(suf)-2]in["i"]:
                suff=suf[0:len(suf)-2]+"y"
                print suff+"    3"
                return True
    elif w.endswith("er"):
        suf=w[0:len(w)-2]
        if suf[len(suf)-1]==suf[len(suf)-2]:
            suff=suf[0:len(suf)-1]
            print suff+"    4"
        return True
    elif w.endswith("able"):
        suf=w[0:len(w)-4]
        print suf
    else:
        suf=w
        print suf+"     else"

    for line in file1:
        if suf in line:
            print suf+"     roooooot"
            return True
#----------------------------------------------------
    file2=open('C:\Users\Ahmd Amr\Desktop\un.txt','r')
    for line in file2:
        if suf in line:
            print suf+" it's a root"
            return True
    if w.startswith(("un","re")):
        pre=suf[2:]
    else:
        pre=suf
    print pre+"     LAST"
#----------------------------------------------------



check(w)





'''
def check(w):
    file1=open('C:\Users\Ahmd Amr\Desktop\wo.txt','r')

    for line in file1:
        if w in line:
            print w+" it's a root"
            return True
    file1.seek(0)

    if w.endswith("ing"):
        suf=w[0:len(w)-3]
    else:
        suf=w
    print suf

    for line in file1:
        if suf in line:
            print suf+" is the root"
            return True

    file2=open('C:\Users\Ahmd Amr\Desktop\un.txt','r')
    for line in file2:
        if suf in line:
            print suf+" it's a root"
            return True
    if w.startswith(("un","re")):
        pre=suf[2:]
    else:
        pre=suf
    print pre
'''


'''

def stm(w):
    if(w=="read"):
        print "it's a root"

    def remPre(v):
        if v.startswith(("un","re")):
            pre=w[2:]
        else:
            pre=w
        print pre
        return pre
    pre = remPre(w)

    def remSuf(v):
        if v.endswith("able",""):
            suf=pre[0:4]
        else:
            suf=pre
        print suf
        return suf
    suf=remSuf(w)
'''

'''
def remPre(v):
    if v.startswith("un"|"re"|"be"|"co"|"de"):
        pre=w[2:]
    elif v.startswith("dis"|"mis"|"out"|"pre"|"sub"):
        pre=w[3:]
    elif v.startswith("over"|"fore"):
        pre=w[4:]
    elif v.startswith("inter"|"under"|"trans"):
        pre=w[5:]
    print pre
'''