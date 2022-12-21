name ="kpufanyrqqmtgxhyycltlnusyeyyqygwupcaagtkuqkwamvdsi"
typed ="kpuufaanyrqqqmttggxxhyyyycclttllnusyeyqqyggwuuppccaaaggtkkuuqkwwamvvddsii"
 
def isin(first, sec):

    f = set(first)
    s = set(sec)
    if f == s:
        for l in f:
            if first.count(l) > sec.count(l):
                return False
        else: return True   
    else: return False

def takeOutDup(sen):
    s = list(sen)
    indexes =  [i for i in range(len(s)-1) if s[i] == s[i+1]]
    
    c = 0
    for i in indexes:
        s.pop(i-c)
        c += 1
    else: return "".join(s)
    
if name == typed:
    print(True)
else:
    if takeOutDup(name) == takeOutDup(typed):
        if isin(name, typed):
            if any(x*2 in typed for x in name):
                print(True)
            else: print(False)
        else: print(False)
    else: print(False) 
    
