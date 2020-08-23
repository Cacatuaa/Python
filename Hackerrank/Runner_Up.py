if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    newList = list(arr)
    newList.sort(reverse=True)
    first = newList[0]

    for i in range (1, len(newList)):
        if newList[i] < first:
            print(newList[i])
            break