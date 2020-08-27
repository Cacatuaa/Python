from collections import Counter

def main():
    n = int(input(""))
    c = Counter()
    for i in range(0, n):
        c[input("")] += 1

    print(len(set(c)))
    number = []
    for word in c:
        number.append(str(c[word]))

    print(" ".join(number))

if __name__ == "__main__":
    main()