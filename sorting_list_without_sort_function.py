s = [-5, -23, 5, 0, 23, -6, 23, 67]
nl = []
for i in range(len(s)):
    a = min(s)
    nl.append(a)
    s.remove(a)

print nl
