N = int(input())
R = []
while not N == 1:
    R.append(int(N))
    if N % 2 == 0:
        N /= 2
    else:
        N = N * 3 + 1
if not len(R) or R[-1] != 1:
    R.append(1)
R = [str(x) for x in R]
print(' '.join(R))
