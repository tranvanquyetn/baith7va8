k=open('c:test7_2.txt', 'r')
char, wc, lc=0,0,0
for line in k:
    for k in range(0,len(line)):
        char +=1
        if (line[k]==''):
            wc+=1

        if (line[k]=='\n'):
            wc,lc=wc+1,lc+1

print("the no,of chars is %d\n the no.of words is %d\n the no.of line is %d"%(char, wc, lc))

