

#zadanie 3.1
print('\n------ZADANIE 3.1------\n')

x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;
#kod wyżej jest poprawny składniowo i się wykona, ale nie jest to zgodny z dobrym stylem, lepiej:

x = 2
y = 3
if x > y:
    result = x
else:
    result = y

#for i in "axby": if ord(i) < 100: print (i) #błąd, nie można pisać instrukcji if bezpośrednio po : .



for i in "axby": print (ord(i) if ord(i) < 100 else i)#poprawne składniowo


#zadanie 3.2
print('\n------ZADANIE 3.2------\n')
L = [3, 5, 4] ; L = L.sort()    #list.sort() sortuje listę w miejscu i zwraca None więc po tej linii L jest None.
print(L)

#x, y = 1, 2, 3     #Liczba wartości po prawej jest różna od liczby zmiennych po lewej.

#X = 1, 2, 3 ; X[1] = 4     #to krotka (tuple) – jest niemodyfikowalna.

#X = [1, 2, 3] ; X[3] = 4   #Indeks 3 nie istnieje (lista ma indeksy 0–2)

#X = "abc" ; X.append("d")  #string nie ma metody .append().

#L = list(map(pow, range(8)))   #pow() wymaga dwóch argumentów (podstawa, wykładnik).


#zadanie 3.3
print('\n------ZADANIE 3.3------\n')
for i in range(31):
    if i % 3 != 0:
        print(i, end=", ")


#zadanie 3.4
print('\n------ZADANIE 3.4------\n')
print('------Zadanie wymaga wprowadzenia danych ------\n')
while True:
    x = input("Podaj liczbę lub 'stop': ")
    if x.lower() == "stop":
        break
    try:
        x=x.replace(',','.')
        x = float(x)
        print(f"{x} ^ 3 = {x ** 3}")
    except ValueError:
        print("Błąd: to nie jest liczba.")

#zadanie 3.5
print('\n------ZADANIE 3.5------\n')
n = 21

miarka = "|"
for i in range(n):
    miarka += "....|"

liczby = "0"
for i in range(1, n + 1):
    liczby += f"{str(i):>5}"

print(miarka)
print(liczby)

#zadanie 3.6
print('\n------ZADANIE 3.6------\n')
def prostokat(wiersze, kolumny):
    poziom = "+---" * kolumny + "+"
    pion = "|   " * kolumny + "|"
    result = ""
    for _ in range(wiersze):
        result += poziom + "\n" + pion + "\n"
    result += poziom
    print(result)

prostokat(3, 4)

#zadanie 3.8
print('\n------ZADANIE 3.8------\n')

a = [1, 2, 3, 4, 1]
b = [3, 4, 5, 6, 1, 7]
# a)
common = list(set(a) & set(b))

# b)
all_unique = list(set(a) | set(b))

print("Wspólne:", common)
print("Wszystkie:", all_unique)

#zadanie 3.9
print('\n------ZADANIE 3.9------\n')

seq = [[], [4], (1, 2), [3, 4], (5, 6, 7)]

sums = [sum(x) for x in seq]
print(sums)

#zadanie 3.10
print('\n------ZADANIE 3.10------\n')
# 1.
roman = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
# 2.

roman = dict([
    ('I', 1),
    ('V', 5),
    ('X', 10),
    ('L', 50),
    ('C', 100),
    ('D', 500),
    ('M', 1000)
])
# 3.
keys = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
values = [1, 5, 10, 50, 100, 500, 1000]

roman = dict(zip(keys, values))

def roman2int(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
             'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev = 0
    for ch in reversed(s):
        value = roman[ch]
        if value < prev:
            total -= value
        else:
            total += value
        prev = value
    return total

print(roman2int("XIV"))  
print(roman2int("MCMXC")) # 1990