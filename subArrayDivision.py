

def listSum(li):
    sum=0
    for i in li:
     sum+=i

    return sum   


def birthday(s, d, m):
    print('segments',s)
    print('birthDay',d,'birthMonth',m)
    segments = len(s)
    pairs = []
    result = []
    finalList = []

    

    for i in range(segments+1):
        newarr = s[i:]
        other=s[:i]
        newlist = newarr
        sum=0
        sortedlist = []
        data=newlist[0:m]
        if(listSum(data)==d):
            print('ressss',data)
            sortedlist=data
        
        if(len(sortedlist)>0):
        #    sortedlist.sort()
           result.append(sortedlist)
        #    result.append(sortedlist)
        if(len(result)>0):
          for k in result:
            #   print('k...',k)
              if k not in finalList:
                finalList.append(k)

    print('pairs..',finalList)
    print('result is',len(finalList))

    return len(finalList)         
        



if __name__ == '__main__':

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    print('result is',result)

