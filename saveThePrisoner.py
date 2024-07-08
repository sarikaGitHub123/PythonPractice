

def saveThePrisoner(n, m, s):
    rCandies  = 0
    k=5
    if(m>n):
        rCandies = m%n
        if(m%n!=0):
          print('this con1')
          x=(s-1)+rCandies
          if x>n:
              k=x-n
          else:
              k=x
        else:
            c=(s+n)-1
            if (c<=n):
                print('con1', c)
                k=c
            else:
                print('con2',c)
                k=c-n
    if(m<n):
        a = m+s
        if(a>n):
            if(a-n>1):
               k=(a-n)-1
            else:
                k=n
        else:
            k=a-1
    if(m==n):
         if(s>1):
           k=s-1
         else:
            k=n        
    return k        


if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        s = int(first_multiple_input[2])

        result = saveThePrisoner(n, m, s)
        
        print('result',result)
