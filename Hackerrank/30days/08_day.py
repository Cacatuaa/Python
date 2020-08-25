if __name__ == "__main__":
    n = int(input(""))
    dictionary = {}
    for i in range(0, n):
        string = input("").split(" ")
        dictionary[string[0]] = string[1]

    while True:
        query = input("")
        if query in dictionary:
            print(f'{query}={dictionary[query]}')
        else:
            print("Not found")
