import sys

n = int(input())

L = 0
#R = 0
#C = 0
for x in input().split():
    L += int(x)
    #C += 1
    #R += C
#R += C + 1
#print(int(R - L))

print(int(n * (n + 1) // 2 - L))
