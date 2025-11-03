#zadanie 4.2
print('\n------ZADANIE 4.2------\n')

def make_ruler(n):
    ruler = "|"
    for i in range(n):
        ruler += "....|"

    numbers = "0"
    for i in range(1, n + 1):
        numbers += f"{str(i):>5}"

    return ruler + '\n' + numbers

print(make_ruler(16))
print()
def make_grid(rows, cols):
    horizontal = "+---" * cols + "+"
    vertical = "|   " * cols + "|"
    result = ""
    for _ in range(rows):
        result += horizontal + "\n" + vertical + "\n"
    result += horizontal
    return result

print(make_grid(3, 4))

#zadanie 4.3
print('\n------ZADANIE 4.3------\n')
def factorial(n):
    
    if n < 0:
        raise ValueError("Silnia niezdefiniowana dla liczb ujemnych")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


print("0! =",factorial(0))  
print("5! =",factorial(5))   

#zadanie 4.4
print('\n------ZADANIE 4.4------\n')

def fibonacci(n):
    if n < 0:
        raise ValueError("n musi być >= 0")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print("fib_9 =",fibonacci(9))   
print("fib_10 =",fibonacci(10)) 

#zadanie 4.5
print('\n------ZADANIE 4.5------\n')
def reverse_iter(L, left, right):
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1


def reverse_rec(L, left, right):
    if left >= right:
        return
    L[left], L[right] = L[right], L[left]
    reverse_rec(L, left + 1, right - 1)

L = [1, 2, 3, 4, 5, 6]
reverse_iter(L, 1, 4)
print(L)
reverse_rec(L, 1, 4)
print(L)

#zadanie 4.6
print('\n------ZADANIE 4.6------\n')
def sum_seq(sequence):
    total = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            total += sum_seq(item) 
        else:
            total += item
    return total

print(sum_seq([1, [2, 3], (4, 5, [6])]))  #21

#zadanie 4.7
print('\n------ZADANIE 4.7------\n')

def flatten(sequence):
    result = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            result.extend(flatten(item)) 
        else:
            result.append(item)
    return result

sequence = [1,(2,3),[],[4,(5,6,7)],8,[9]]

print(flatten(sequence))   # [1,2,3,4,5,6,7,8,9]
