from itertools import *

def iterPermutations():
    # input = HACK 2
    word, number = input("").split()
    sorted_char = sorted(word)
    sorted_string = "".join(sorted_char)

    perm = list(permutations(sorted_string, int(number)))
    for i in perm:
        print(''.join(i))

def iterProduct():
    # input =   1 2
    #           3 4
    a = list(map(int, input("").split()))
    b = list(map(int, input("").split()))
    print(*product(a,b))

def iterCombinations():
    # input = HACK 2
    word, number = input("").split()
    sorted_char = sorted(word)
    sorted_string = "".join(sorted_char)

    for i in range(1, int(number) + 1):
        comb = list(combinations(sorted_string, i))
        for j in comb:
            print("".join(j))

def iterGroupby():
    string = input("")

    for k, g in groupby(string):
        print(f'({len(list(g))}, {k})', end=' ')
    """
    key = []
    group = []
    for k, g in groupby(string):
        key.append(k)
        group.append(list(g))

    for i in range(len(key)):
        print(f'({len(group[i])}, {key[i]})', end=' ')"""


def main():
    while True:
        print('\n=============== Itertools ===============')
        print("Choose what Itertool function do you want to use: ")
        print("1 - Permutation")
        print("2 - Combination")
        print("3 - Product")
        print("4 - Groupby")
        print("0 - Quit Itertools Functions")
        
        try:
            choice = int(input("Your choice: "))
        
        except ValueError:
            print("Please only input a valid integer!")
        
        except KeyboardInterrupt:
            print("You decided to leave. Bye!")
            break
        
        else:
            if choice == 0:
                print("You decided to leave. Bye!")
                break
            elif choice == 1:
                iterPermutations()
            elif choice == 2:
                iterCombinations()
            elif choice == 3:
                iterProduct()
            elif choice == 4:
                iterGroupby()

if __name__ == "__main__":
    main()