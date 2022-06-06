s = int(input('Size--> '))
#CREATING THE LIST OF ELEMENTS
l = []
d = []
for i in range(s*s):
    i = str(i)
    l.append(i)

# DEFINING PRINTING MATRIX
def printaid(s) :
    if s == 3:
        for j in range(s):
            c = []
            for i in range(j * s, (j + 1) * s):
                c.append(l[i])
                if i == ((j+1) * s)-1:
                    print('',l[i])
                else:
                    print('',l[i],end = ' ')
            d.append(c)

    elif s > 3:
        for j in range(s):
            c = []
            for i in range(j * s, (j + 1) * s):
                c.append(l[i])
                if l[i]  in ('0','O','1','2','3','4','5','6','7','8','9','X'):
                    if i == j * s :
                        print('',l[i],end = ' ')
                    elif i == ((j+1) *s) - 1:
                        print('',l[i])
                    else:
                        print('',l[i],end = ' ')
                else:
                    if i == (j * s) :
                        print(l[i],end = ' ')
                    elif i ==((j+1) *s) - 1:
                        print(l[i])
                    else:
                        print(l[i],end = ' ')

            d.append(c)

printaid(s)

#----------GAME STARTS-------------
#only checking rows and columns right now
def judgement(s):
    for i in range(s):
        if d[i].count('O')== s :
            print('Winner: O')
            exit()
        elif d[i].count('X')== s :
            print('Winner: X')
            exit()
    for i in range(s):
        m = []
        for j in range(s):
            o = d[j][i]
            m.append(o)
        if m.count('O') == len(m):
            print('Winner: O')
            exit()
        elif m.count('X') ==len(m):
            print('Winner: X')
            exit()
    alpha = []
    for i in range(s):
        alpha.append(d[i][i])
        if alpha.count('O') == s:
            print('Winner: O')
            exit()
        elif alpha.count('X') == s:
            print('Winner: X')
            exit()
    beta = []
    for j in range(s):
        beta.append(d[j ][s - 1 - j])
        if beta.count('O') == s:
            print('Winner: O')
            exit()
        elif beta.count('X') == s:
            print('Winner: X')
            exit()
#none
    x = 0
    for i in range(s):
        for j in range (s):
            if d[i][j] == 'O' or d[i][j] == 'X':
                x += 1
                if x == (s * s) :
                    print('Winner: None')

#--------GAME STARTS----------

while True:
    a = int(input('X--> '))
    l[a] = 'X'
    d = []
    printaid(s)
    judgement(s)
    a = int(input('O--> '))
    l[a] = 'O'
    d = []
    printaid(s)
    judgement(s)
