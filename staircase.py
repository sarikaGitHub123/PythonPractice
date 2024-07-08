


def staircase(n):
    string=''
    for i in range(1,n+1):
        for j in range(n-i):
               string+=''
        for k in range(i):
               string+='*'  
        string+="\n"
    print(string)


    

if __name__ == '__main__':
    n = int(input().strip())
    staircase(n)

