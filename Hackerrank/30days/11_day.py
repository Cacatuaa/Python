def main():
    arr = []
    """
    1 1 1 0 0 0
    0 1 0 0 0 0
    1 1 1 0 0 0
    0 0 2 4 4 0
    0 0 0 2 0 0
    0 0 1 2 4 0
    """
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    sumHourglasses = []

    for i in range(0, len(arr)-2):
        for j in range(0, len(arr)-2):
            total = arr[i][j] + arr[i][j+1] + arr[i][j+2] #first line of the hoursglass
            total += arr[i+1][j+1] #middle of the hourglass
            total += arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2] #last line of the hourglass
            sumHourglasses.append(total)

    print(max(sumHourglasses))

if __name__ == "__main__":
    main()