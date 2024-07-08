


def countingValleys(steps, path):
    # Write your code here
    # lists = {}
    particular_value = ' '
    result = []
    temp_list = []
    for i in path:
        if i == particular_value:
            temp_list.append(i)
            result.append(temp_list)
            # temp_list = []
        else:
            temp_list.append(i)
    result.append(temp_list)
                
        #   count.append(path[i])
    print('list is',result)
    return None

if __name__ == '__main__':

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)
   
    print('result',result)
