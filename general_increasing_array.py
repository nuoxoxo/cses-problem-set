#* ******************************************** *#
#*                                              *#
#*              \\             #`#``            *#
#*              ~\o o_       0 0\               *#
#*              # \__)      (u  ); _  _         *#
#*       # \# \#  #           \  \# \# \        *#
#*      #(   . . )            (         )\      *#
#*     #  \_____#              \_______#  \     *#
#*         []  []               [[] [[]    *.   *#
#*         []] []]              [[] [[]         *#
#*                                              *#
#* ************************************ nuo *** *#

n = int(input())
G = []
N = 0
for x in input().split():
    G.append(int(x))
for i in range(n - 1):
    #print(G[i], G[i + 1])
    if G[i + 1] < G[i]:
        N += G[i] - G[i + 1]
        G[i + 1] = G[i]
print(N)
