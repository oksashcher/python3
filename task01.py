#A = [int(i) for i in input().split()] 
#X = int(input()) 
#print(A.count(X)) 




#a=list(map(int,input().split()))
#b=int(input())
#c=[]
#for i in a:
#    c.append(abs(b-i))
#d=c.index(min(c))
#print(a[d])




s = input()
d = {'[AEIOULNSTR]': '1', '[DG]': '2', '[BCMP]': '3', '[FHVWY]': '4', 'K': '5', '[JX]': '8', '[QZ]': '19'}
for k in d:
    s = re.sub(k, d[k], s)
print(sum(map(int, s)))
