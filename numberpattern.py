n=int(raw_input('enter number between 1 to 9'))
#     1
#    121
#   12321
#  1234321
# 123454321
#12345654321
for i in range(1,n+1):
    s=' '
    for l in range(n-i):
        print s,
    for j in range(1,i+1):
        print j,
    for k in range(i-1,0,-1):
        print k,
    print
for i in range(n-1,0,-1):
    s=' '
    for l in range(n-i):
        print s,
    for j in range(1,i+1):
        print j,
    for k in range(i-1,0,-1):
        print k,
    print
n1=int(raw_input('enter 1 for even, 2 for odd'))
if n1==1:
    print "All even numbers gone!!"
    for i in range(1,n+1):
        s=' '
        for l in range(n-i):
            print s,
        for j in range(1,i+1):
            if j%2==0:
                print s,
            else:
                print j,
        for k in range(i-1,0,-1):
            if k%2==0:
                print s,
            else:
                print k,
        print
    for i in range(n-1,0,-1):
        s=' '
        for l in range(n-i):
            print s,
        for j in range(1,i+1):
            if j%2==0:
                print s,
            else:
                print j,
        for k in range(i-1,0,-1):
            if k%2==0:
                print s,
            else:
                print k,
        print
elif n1==2:
    print "All odd numbers gone!!"
    for i in range(1,n+1):
        s=' '
        for l in range(n-i):
            print s,
        for j in range(1,i+1):
            if j%2!=0:
                print s,
            else:
                print j,
        for k in range(i-1,0,-1):
            if k%2!=0:
                print s,
            else:
                print k,
        print
    for i in range(n-1,0,-1):
        s=' '
        for l in range(n-i):
            print s,
        for j in range(1,i+1):
            if j%2!=0:
                print s,
            else:
                print j,
        for k in range(i-1,0,-1):
            if k%2!=0:
                print s,
            else:
                print k,
        print
print "AND THE LAST PATTERN"
print
for i in range(1,n+1):
    s=' '
    for l in range(n-i):
        print s,
    for j in range(1,i+1):
        if j==i or i==n:
            print s,
        else:
            print j,
    for k in range(i-1,0,-1):
        if k==i or i==n:
            print s,
        else:
            print k,
    print
for i in range(n-1,0,-1):
    s=' '
    for l in range(n-i):
        print s,
    for j in range(1,i+1):
        if j==i or i==n:
            print s,
        else:
            print j,
    for k in range(i-1,0,-1):
        if k==i or i==n:
            print s,
        else:
            print k,
    print
print "THANK YOU"


    
