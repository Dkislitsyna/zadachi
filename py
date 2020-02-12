N=int(input())
mnk=0
mkr=0
mkr2=0
for i in range(N):
    a=int(input())
    if a%14==0 and a>mkr2:
        mkr=mkr2
        mkr2=a
    elif a>mkr and a<mkr2:
        mkr=a
    else:
        if a>mnk:
            mnk=a
if mnk*mkr2>mkr*mkr2:
    x=mnk*mkr2
else:
    x=mkr*mkr2
print(x)
