def main():
    n = int(input())
    binary = str(bin(n)).replace("0b", "").split("0")
    biggest = 0
    for i in binary:
        if len(i) > biggest:
            biggest = len(i)

    print(biggest)

if __name__ == '__main__':
    main()