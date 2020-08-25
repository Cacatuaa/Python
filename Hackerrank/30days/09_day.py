def factorial(n):
    total = 1
    for i in range(n, 0, -1):
        total = total * i
    return total

def main():
    n = int(input())
    print(factorial(n))

if __name__ == "__main__":
    main()