

#zadanie 2.10
print('------ZADANIE 2.10------')

line = """Przykladowy
tekst z kilkoma     wyrazami
na wielu liniach."""

num_words = len(line.split())
print(num_words)

#zadanie 2.11
print('------ZADANIE 2.11------')
word = "word"
word_ = "_".join(word)
print(word_) 

#zadanie 2.12
print('------ZADANIE 2.12------')
line = "jakis przykladowy tekst"

words = line.split()

first = "".join(w[0] for w in words)
last = "".join(w[-1] for w in words)

print("Pierwsze litery:", first)
print("Ostatnie litery:", last)

#zadanie 2.13
print('------ZADANIE 2.13------')
line = "jakis przykladowy tekst"
words = line.split()
total_length = sum(len(w) for w in words)
print("Laczna dlugosc:",total_length)

#zadanie 2.14
print('------ZADANIE 2.14------')
line = "jakis przykladowy tekst"
words = line.split()
longest_word = max(words, key=len)
longest_word_len = len(longest_word)

print("Najdłuższy wyraz:", longest_word)
print("Długość:", longest_word_len)

#zadanie 2.15
print('------ZADANIE 2.15------')
L = [12, 3, 456, 78]
result = "".join(str(x) for x in L)
print(result)

#zadanie 2.16
print('------ZADANIE 2.16------')
line = "Jednym z moich ulubionych holenderskich programistow jest GvR dalsze slowa w stringu."

new_line = line.replace("GvR", "Guido van Rossum")
print(new_line)

#zadanie 2.17
print('------ZADANIE 2.17------')
line = "Ten przykladowy tekst zawiera wiecej wyrazow zeby bylo co sortowac"
words = line.split()

sorted_alpha = sorted(words)

sorted_length = sorted(words, key=len)

print("Alfabetycznie:", sorted_alpha)
print("Według długości:", sorted_length)

#zadanie 2.18
print('------ZADANIE 2.18------')
number = 1002030450006007 #9

num_zeros = str(number).count('0')
print(num_zeros)

#zadanie 2.19
print('------ZADANIE 2.19------')
L = [7, 24, 356, 4, 89]
blocks = [str(x).zfill(3) for x in L]
result = "".join(blocks)

print(result)