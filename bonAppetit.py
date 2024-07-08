

def circularArrayRotation(a, k, queries):
    # Write your code here
    rotatedList = []
    queryList = []
    for i in range(k+1):
        x=a[i:]+a[:i]
        print('x',x)
        rotatedList=x
    print('rotatedList..',rotatedList, queries)
    for n in queries:
        queryList.append(rotatedList[n])
    return queryList
    

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    q = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)
    
    print('result',result)

