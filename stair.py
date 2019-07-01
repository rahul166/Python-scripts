#stair problems 

#number of steps
N=int(input())

#possible steps that could be taken
lst=[1,3,5]


dp=[[0 for i in range(5)] for  j in range(len(lst))]
# print(dp)
def count(step,n):
    ans=0
    #base conditions
    if n<0:
        return 0
    if n==0:
        # print(dp)
        return 1
    
    if dp[step-1][n]:
        return dp[step-1][n]

    # print(dp)
    #main rec call
    ct=0
    for st in lst:
        # print(st)
        ct=count(st,n-st)
        ans+=ct
        # print(st,"::",dp,"::",n)
        if n-st>0:
            dp[st-1][n-st]+=ct
        print(st,"::",dp,"::",n)
    
    return ans

# print(dp)
ways=0
for st in lst:
    ways+=count(st,N-st)

#ways in which we can reach the top stair using given steps
print("WAYS:::"," ",ways)    
# print(count(3,1))

