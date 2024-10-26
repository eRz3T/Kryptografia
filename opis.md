# 1. Szyfr Monoalfabetyczny

Szyfr monoalfabetyczny jest klasycznym rodzajem szyfru podstawieniowego, w którym każda litera w tekście jawnie (oryginalnym) jest zamieniana na inną, unikalną literę alfabetu. Klucz szyfrujący to permutacja alfabetu, co oznacza, że każda litera alfabetu jest zamieniana na inną literę z tego samego zestawu.
Jak działa szyfr monoalfabetyczny:

#### Krok 1: Klucz szyfrowania – Najpierw ustalamy klucz szyfrowania, czyli zamieniamy wszystkie litery alfabetu na inne litery. Przykładowo, klucz może wyglądać tak:

    a -> q
    b -> w
    c -> e
    d -> r
    ...
    z -> m

Klucz musi zawierać dokładnie 26 liter, aby każda litera alfabetu miała swój odpowiednik w szyfrowaniu.

#### Krok 2: Szyfrowanie – Dla każdej litery w oryginalnym tekście, zamieniamy ją na odpowiadającą literę z klucza. Na przykład, jeśli mamy tekst "hello" i klucz z powyższego przykładu, litery będą zamienione na:

    h -> i
    e -> t
    l -> s
    o -> z

#### Krok 3: Deszyfrowanie – Odszyfrowanie tekstu polega na odwróceniu zamiany, czyli znajdywaniu litery z klucza, która odpowiada danej zaszyfrowanej literze.

Zalety

Łatwy do zrozumienia i implementacji.
Szyfr monoalfabetyczny zamienia litery, co daje różne szyfrogramy dla tego samego tekstu przy różnych kluczach.

Wady:

Łatwo go złamać za pomocą analizy częstotliwości, ponieważ często występujące litery w języku oryginalnym pojawiają się równie często w zaszyfrowanym tekście.
Brak bezpieczeństwa w kontekście współczesnej kryptografii.

Przykład działania:

Dla klucza qwertyuiopasdfghjklzxcvbnm i tekstu "secret":

    s -> l
    e -> t
    c -> o
    r -> p
    e -> t
    t -> z

Zaszyfrowany tekst: "ltoptz"








# 2. Szyfr Transpozycyjny

Szyfr transpozycyjny działa inaczej niż szyfr monoalfabetyczny, ponieważ w tym przypadku nie zmieniamy liter na inne, ale zmieniamy ich kolejność w tekście. Klucz szyfrowania w szyfrze transpozycyjnym określa liczbę kolumn, w jakie układamy tekst przed przestawieniem go.
Jak działa szyfr transpozycyjny:

#### Krok 1: Podział na kolumny – Wyobraźmy sobie, że wpisujemy tekst w tabeli o określonej liczbie kolumn (którą wybieramy jako klucz). Jeśli wybieramy 5 kolumn, tekst „szyfrowanie jest fajne” zostanie wpisany jak poniżej:

s  z  y  f  r
o  w  a  n  i
e  j  e  s  t
f  a  j  n  e

#### Krok 2: Odczytywanie kolumn – Następnie tekst jest odczytywany kolumnami od góry do dołu, co daje zaszyfrowany tekst:

szyfro wyanef jestnje 

Puste miejsca mogą być uzupełnione spacjami lub innymi znakami.

#### Krok 3: Deszyfrowanie – Aby odszyfrować tekst, ponownie wstawiamy litery w kolumny, a następnie odczytujemy je wierszami. Liczba kolumn powinna być znana (jest to klucz szyfrowania).

Zalety:

Bez zmiany samych liter, zmienia tylko ich kolejność.
Bardziej odporny na analizę częstotliwości niż szyfr monoalfabetyczny.

Wady:

Nie tak bezpieczny jak współczesne algorytmy kryptograficzne.
Gdyby napastnik znał liczbę kolumn, mógłby łatwo odczytać tekst.

Przykład działania:

Tekst do zaszyfrowania: „szyfr transpozycyjny”

#### Klucz: 5 (5 kolumn)
Podział tekstu na kolumny:

    s  z  y  f  r
    t  r  a  n  s
    p  o  z  y  c
    j  n  y

Zaszyfrowany tekst: "strpjzonayynfscr"






# 3. Algorytm DES (Data Encryption Standard)

DES to symetryczny algorytm szyfrowania blokowego, zaprojektowany do szyfrowania danych w blokach o długości 64 bitów, przy użyciu 56-bitowego klucza.

Jak działa DES:

#### Krok 1: Podział danych na bloki
Dane są dzielone na bloki o długości 64 bitów, a każdy blok jest przetwarzany osobno.

#### Krok 2: Generowanie kluczy rundowych
Z 56-bitowego klucza głównego generowane jest 16 kluczy rundowych.

#### Krok 3: 16 rund szyfrowania
Każdy blok danych przechodzi przez 16 rund szyfrowania, które obejmują permutacje, zamiany bitów i operacje logiczne z wykorzystaniem kluczy rundowych.

#### Krok 4: Łączenie wyników
Po 16 rundach zaszyfrowany blok jest łączony z kolejnymi blokami, aby uzyskać zaszyfrowany tekst.

**Przykład**:  
Tekst: `123456ABCD132536` (64-bitowy blok)  
Klucz: `A1B2C3D4E5F60708` (56-bitowy)  
Szyfrogram: (po 16 rundach) `C0B7A8D05F3A829C`

**Zalety**: Powszechnie stosowany w kryptografii do szyfrowania danych.

**Wady**: Ze względu na krótki klucz, DES jest podatny na ataki brute-force, dlatego obecnie zaleca się stosowanie bardziej zaawansowanych algorytmów jak AES.







# 4. Algorytm AES (Advanced Encryption Standard)

AES to zaawansowany algorytm szyfrowania blokowego, który został przyjęty jako standard przez NIST. AES działa na blokach danych o długości 128 bitów i obsługuje klucze o długościach 128, 192 lub 256 bitów.

Jak działa AES:

#### Krok 1: Podział danych na bloki
Dane są dzielone na bloki o długości 128 bitów.

#### Krok 2: Generowanie kluczy rundowych
AES wykorzystuje klucz główny, z którego generowane są klucze rundowe dla poszczególnych rund (10, 12 lub 14 rund, w zależności od długości klucza).

#### Krok 3: Operacje szyfrowania
Każda runda szyfrowania składa się z czterech podstawowych operacji:
- **SubBytes**: Zamiana bajtów na podstawie tabeli substytucji.
- **ShiftRows**: Przesunięcie wierszy macierzy.
- **MixColumns**: Mieszanie kolumn macierzy.
- **AddRoundKey**: Dodanie klucza rundowego.

#### Krok 4: Finalizacja
Po ostatniej rundzie otrzymujemy zaszyfrowany blok, który jest łączony z kolejnymi blokami, aby uzyskać zaszyfrowany tekst.

**Przykład**:  
Tekst: `00112233445566778899AABBCCDDEEFF` (128-bitowy blok)  
Klucz: `000102030405060708090A0B0C0D0E0F` (128-bitowy)  
Szyfrogram: `69C4E0D86A7B0430D8CDB78070B4C55A` (po 10 rundach)

**Zalety**: Bardzo bezpieczny algorytm o dużej szybkości działania, wykorzystywany w wielu aplikacjach kryptograficznych.

**Wady**: Wymaga zaawansowanych zasobów obliczeniowych w porównaniu z DES.