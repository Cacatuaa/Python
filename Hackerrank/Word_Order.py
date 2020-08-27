from collections import Counter

def main():
    n = int(input(""))
    words = []
    for i in range(0, n):
        words.append(input(""))
    distinct = set(words)
    print(len(distinct))

    total = []
    counter = 0
    for i in distinct:
        for j in words:
            if i == j:
                counter += 1
        total.append(str(counter))
        counter = 0    
    total.sort(reverse=True)
    print(" ".join(total))

if __name__ == "__main__":
    main()