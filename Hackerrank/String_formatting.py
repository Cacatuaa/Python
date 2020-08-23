def print_formatted(number):
    width = len(bin(number).replace("0b", ""))
    for i in range(0,number+1):
        octal = oct(i)
        octal = octal.replace("0o", "")

        hexadecimal = hex(i)
        hexadecimal = hexadecimal.replace("0x", "")
        hexadecimal = hexadecimal.upper()

        binary = bin(i)
        binary = binary.replace("0b", "")

        print(f'{str(i).rjust(width)} {octal.rjust(width)} {hexadecimal.rjust(width)} {binary.rjust(width)}')
        # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)