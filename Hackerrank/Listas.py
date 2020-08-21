"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.
teste
"""
def list_insert(lista, index, number):
    lista.insert(index, number)
    return lista

def list_print(lista):
    print(lista)

def list_remove(lista, number):
    lista.remove(number)
    return lista

def list_append(lista, number):
    lista.append(number)
    return lista

def list_sort(lista):
    lista.sort()
    return lista

def list_pop(lista):
    lista.pop()
    return lista

def list_reverse(lista):
    lista.reverse()
    return lista

if __name__ == '__main__':
    lista = []
    N = int(input())
    for i in range(0, N):
        command = input("").split()
        if command[0] == "insert":
            list_insert(lista, int(command[1]), int(command[2]))

        elif command[0] == "print":
            list_print(lista)

        elif command[0] == "print":
            list_print(lista)

        elif command[0] == "remove":
            list_remove(lista, int(command[1]))

        elif command[0] == "append":
            list_append(lista, int(command[1]))

        elif command[0] == "sort":
            list_sort(lista)

        elif command[0] == "pop":
            list_pop(lista)

        elif command[0] == "reverse":
            list_reverse(lista)