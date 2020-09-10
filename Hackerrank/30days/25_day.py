import math
def Prime(number):
    if number < 2:
        return False
    elif number > 10000: # for big numbers, time complexity = O(sqrt(n))
        for i in range(2, math.ceil(math.sqrt(number))):
            if number % i == 0:
                return False
        return True
    else:
        for i in range(2, number): #for small number, time complexity = O(n)
            if number % i == 0:
                return False
        return True

def main():
    n = int(input(""))
    for _ in range(n):
        number = int(input())
        isprime = Prime(number)
        if isprime:
            print("Prime")
        else:
            print("Not prime")

if __name__ == "__main__":
    main()