if __name__ == "__main__":
    words = []
    n = int(input())
    for i in range(0, n):
        words.append(input())
    
    for i in range(0, len(words)):
        word = words[i]
        even_letters = []
        odd_letters = []
        for j in range(0, len(word)):
            if j % 2 == 0:
                even_letters.append(word[j])
            else:
                odd_letters.append(word[j])
        print(f'{"".join(even_letters)} {"".join(odd_letters)}')


