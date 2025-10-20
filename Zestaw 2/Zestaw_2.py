

#zadanie 2.10
print('\n------ZADANIE 2.10------\n')

line = """Przykladowy
tekst z kilkoma     wyrazami
na wielu liniach."""

num_words = len(line.split())
print("Liczba slow:",num_words)

#zadanie 2.11
print('\n------ZADANIE 2.11------\n')
word = "word"
word_ = "_".join(word)
print(word_) 

#zadanie 2.12
print('\n------ZADANIE 2.12------\n')
line = "jakis przykladowy tekst"

words = line.split()

first = "".join(w[0] for w in words)
last = "".join(w[-1] for w in words)

print("Pierwsze litery:", first)
print("Ostatnie litery:", last)

#zadanie 2.13
print('\n------ZADANIE 2.13------\n')
line = "jakis przykladowy tekst"
words = line.split()
total_length = sum(len(w) for w in words)
print("Laczna dlugosc:",total_length)

#zadanie 2.14
print('\n------ZADANIE 2.14------\n')
line = "jakis przykladowy tekst"
words = line.split()
longest_word = max(words, key=len)
longest_word_len = len(longest_word)

print("Najdłuzszy wyraz:", longest_word)
print("Długosc:", longest_word_len)

#zadanie 2.15
print('\n------ZADANIE 2.15------\n')
L = [12, 3, 456, 78]
result = "".join(str(x) for x in L)
print(result)

#zadanie 2.16
print('\n------ZADANIE 2.16------\n')
line = "Jednym z moich ulubionych holenderskich programistow jest GvR dalsze slowa w stringu."

new_line = line.replace("GvR", "Guido van Rossum")
print(new_line)

#zadanie 2.17
print('\n------ZADANIE 2.17------\n')
line = "Ten przykladowy tekst zawiera wiecej wyrazow zeby bylo co sortowac"
words = line.split()

sorted_alpha = sorted(words,key=str.lower)

sorted_length = sorted(words, key=len)

print("Alfabetycznie:", sorted_alpha)
print("Według dlugosci:", sorted_length)

#zadanie 2.18
print('\n------ZADANIE 2.18------\n')
number = 1002030450006007 #9

num_zeros = str(number).count('0')
print(num_zeros)

#zadanie 2.19
print('\n------ZADANIE 2.19------\n')
L = [7, 24, 356, 4, 89]
blocks = [str(x).zfill(3) for x in L]
result = "".join(blocks)

print(result)