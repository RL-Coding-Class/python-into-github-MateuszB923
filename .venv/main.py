# https://ufkapano.github.io/algorytmy/lekcja02/zadania.html


    # dokonczyc zadania

    # ZADANIE 2.4
#     >> > len("napis")
#     5
#     >> > len(str(2 ** 10000))
#     3011
#     >> > len("abc", 'abc')
#     Traceback(most
#     recent
#     call
#     last):
#     File
#     "<stdin>", line
#     1, in < module >
# TypeError: len()
# takes
# exactly
# one
# argument(2
# given)
# >> > S = "ab"   'cd'
# >> > S
# 'abcd'
# >> > S = "abrakadabra"
# >> > S
# 'abrakadabra'
# >> > S[2], S[-3], S[3:5], S[3:], S[:4]
# ('r', 'b', 'ak', 'akadabra', 'abra')
# >> > L = ["a", "b", "c"]
# >> > L[0] + L[1] + L[2]
# 'abc'
# >> > L[0] + "=" + L[1] + "=" + L[2]
# 'a=b=c'
# >> > "".join(L)
# 'abc'
# >> > "".join(L)
# 'abc'
# >> >  # S.join([S1,S2,S3]) daje S1+S+S2+S+S3
# >> > S
# 'abrakadabra'


# ZADANIE 2.5

# Długość listy (len()): len(L) zwraca liczbę elementów w liście L.
#
# Indeksowanie: Można uzyskać dostęp do elementów listy przez podanie indeksu, np. L[1] zwraca "xyz". Dla zagnieżdżonych elementów używamy kolejnych indeksów, np. L[1][0] zwróci pierwszą literę "xyz", czyli "x", a L[2][1] zwróci 20.
#
# Wycinki: Wycinki (slicing) pozwalają na pobranie fragmentu listy. Na przykład L[0:2] zwróci listę [3, "xyz"].
#
# Konkatenacja i powtórzenie: Można dodawać listy za pomocą operatora +, np. [1, 2] + [3, 4] da [1, 2, 3, 4]. Powtórzenie uzyskamy przez *, np. [1, 2] * 2 zwróci [1, 2, 1, 2].
#
# Podstawianie pod element lub wycinek: Podstawiając wartość pod element, zmieniasz go, np. L[1] = 5 zamienia "xyz" na 5. Podobnie można podmieniać fragmenty listy, np. L[0:2] = [7, 8].
#
# Generowanie list funkcją range(): range() tworzy sekwencję liczb. Na przykład list(range(5)) daje [0, 1, 2, 3, 4].
#
# Kopiowanie list: Listę można kopiować przez przypisanie, ale głęboka kopia (dla zagnieżdżonych list) wymaga funkcji copy.deepcopy().
#
# Sortowanie list: Listy można posortować przy pomocy L.sort() lub sorted(L).
#
# Listy składane: Listy składane umożliwiają wygodne tworzenie list za pomocą wyrażeń, np. [x**2 for x in range(5)] zwróci [0, 1, 4, 9, 16].

# ZADANIE 2.8

# list = [1, 2, 3, 2, 4, 3, 5]
# unique_elements = list(set(list))
# print(unique_elements)
# #[1, 2, 3, 4, 5]

# ZADANIE 2.9

# def copy_without_comments(in_file, out_file):
#     with open(in_file, 'r') as input_file, open(out_file, 'w') as output_file:
#         for line in input_file:
#             if not line.strip().startswith('#'):
#                 output_file.write(line)
#
# copy_without_comments("plik_wejscia.txt", "plik_wyjscia.txt")

# ZADANIE 2.10

# def how_many_words(line):
#     words = line.split()
#     return len(words)
#
# line = "Jakiś napis do policzenia wyrazów"
#
# print(how_many_words(line))

# ZADANIE 2.11

# word = "MateuszBochenek"
# result = "_".join(word)
# print(result)

# ZADANIE 2.12

# def first_and_last(line):
#
#     words = line.split()
#
#     first_letters = "".join([word[0] for word in words])
#     last_letters = "".join([word[-1] for word in words])
#
#     return first_letters, last_letters
#
# line = "Prawdopodobnie yeti to himalajska okropna niewiemjakieslowozebypasowalo"
#
# made_from_first_letters, made_from_last_letters = first_and_last(line)
# print(made_from_first_letters, made_from_last_letters)

# ZADANIE 2.13

# def sum_lengths(line):
#     words = line.split()
#     return sum(len(word) for word in words)
#
# line = "Takich dwóch jak nas trzech, to nie ma ani jednego"
#
# sum = sum_lengths(line)
# print(sum)

# ZADANIE 2.14

# def find_the_longest(line):
#     words = line.split()
#
#     the_longest = max(words, key=len)
#     the_longest_length = len(the_longest)
#
#     return the_longest, the_longest_length
#
#
# phrase = "To by nic nie dało, nawet gdybym ja był pierwszy w kulach."
# the_longest, the_longest_length = find_the_longest(phrase)
#
# print("Najdłuższy: " + the_longest)
# print("Jego długość " + str(the_longest_length))

# ZADANIE 2.15

# def make_phrase(list):
#     return ''.join(str(i) for i in list)
#
# list = [1, 23, 456, 7, 89, 2137]
#
# phrase = make_phrase(list)
#
# print(phrase)

# ZADANIE 2.16

# line = "GvR to twórca języka Python."
# replaced = line.replace("GvR", "Guido van Rossum")
#
# print("Zmieniony tekst:", replaced)

# ZADANIE 2.17

# phrase = "Młody powiem krótko, 12 złotych od metra, w ciągu godziny zrobisz metr maks półtora. Matematykę pozostawiam Tobie"
#
# words = phrase.split()
#
# sorted_alphabetically = sorted(words)
# print("Alfabetycznie:", sorted_alphabetically)
#
# sorted_by_length = sorted(words, key=len)
# print("Według długości:", sorted_by_length)

# ZADANIE 2.18

# number = 10000023012054078
#
# number_string = str(number)
#
# number_of_zeros = number_string.count('0')
#
# print(number_of_zeros)

# ZADANIE 2.19

# list = [1, 12, 123, 21, 37, 500, 6]
#
# phrase = ''.join(str(number).zfill(3) for number in list)
#
# print(phrase)

print("polska gurommmm")