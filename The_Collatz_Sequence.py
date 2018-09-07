def collatz(num):
    if num % 2 == 0:
        print (num // 2)
        return num //2
    elif num % 2 == 1:
        result = 3 * num + 1 
        print(result)
        return result

try:
    n = int(input('Give me a number other than 1:- '))
    while n != 1:
        n = collatz(n)
except ValueError:
    print('Sorry, you must enter an integer')
