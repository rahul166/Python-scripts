from functools import reduce
m=int(input())
r_s=[int(x) for x in input().split()]
N=int(input())

r_s=reduce(lambda x,y:x*y,r_s)

cards=[i for i in range(1,101)]

piles=[]


# def odeve(num,pno):
#     if num%==0
#Rounds
for i in range(r_s,0,-1):
    # lst=list(filter(lambda x:x%i==0,cards))
    lst=[]
    print(i)
    for x in range(1,len(cards)+1):
        if(x%i==0):
            lst.append(cards[x-1])
    # print(lst)
    cards=[c for c in cards if c not in lst]
    # print(cards)
    piles.append(lst)
# print(piles)
# for i in piles:
#     i.reverse()
cards=[]
for p in range(len(piles)-1,-1,-1):
    cards=cards+piles[p]
    
print(cards)
print(cards[N-1])
# print(piles)






