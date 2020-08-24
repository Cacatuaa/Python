#!/bin/python3
#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    if s[-2] == "P":
        list_string = list(s)
        time = list_string[0] + list_string[1]
        time = int(time)

        if time != 12:
            time += 12
            time_str = str(time)
            list_string[0] = time_str[0]
            list_string[1] = time_str[1]
        list_string.pop()
        list_string.pop()
        new_str = "".join(list_string)

    elif s[-2] == "A":
        list_string = list(s)
        if list_string[0] == "1" and list_string[1] == "2":
            list_string[0] = "0"
            list_string[1] = "0"
        
        list_string.pop()
        list_string.pop()
        new_str = "".join(list_string)

    return new_str

if __name__ == '__main__':
    s = input()

    result = timeConversion(s)
    print(result)