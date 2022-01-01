#* ************************************************************************** *#
#*                                                                            *#
#*                            \\             #`#``                            *#
#*                            ~\o o_       0 0\                               *#
#*                            # \__)      (u  ); _  _                         *#
#*                     # \# \#  #           \  \# \# \                        *#
#*                    #(   . . )            (         )\                      *#
#*                   #  \_____#              \_______#  \                     *#
#*                       []  []               [[] [[]    *.                   *#
#*                       []] []]              [[] [[]                         *#
#*                                                                            *#
#* ****************************************************************** nuo *** *#

from collections import deque
import sys

n, m = [int(x) for x in input().split()]

E = [[] for _ in range(n)]

for _ in range(m):
    a, b = [int(x) for x in input().split()]
    a -= 1
    b -= 1
    E[a].append(b)
    E[b].append(a)

Q = deque()
Q.append(0)

Parent = [None for _ in range(n)]
Seen = [False for _ in range(n)]
Seen[0] = True

while Q:
    print(Parent)
    x = Q.popleft()
    if x == n - 1:
        route = [x]
        while Parent[x] is not None:
            route.append(x)
            x = Parent[x]
        route = [str(x + 1) for x in reversed(route)]
        print(len(route))
        print(' '.join(route))
        sys.exit(0)

    for i in E[x]:
        if Seen[i]:
            continue
        Seen[i] = True
        Parent[i] = x
        Q.append(i)

print('IMPOSSIBLE')
