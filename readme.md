# Instrukcja obsługi

## 1. Update i instalacja niezbędnych paczek
```
sudo apt update
sudo apt install python3 python3-pip python3-venv python3-tk
```
## 2. Utworzenie środowiska wirtualnego
```
python3 -m venv <NAZWA_FOLDERU>
```
### 2.1 Instalacja niezbędnych paczek python
```
pip install pycryptodome cryptography PyPDF2 pikepdf
```
## 3. Uruchomienie środowiska wirtualnego
```
source <NAZWA_FOLDERU>/bin/activate
```
## 4. Uruchomienie projektu
```
cd <NAZWA_FOLDERU>/
```
```
python -m venv venv
```
### windows
```
venv\Scripts\activate
```
### linux
```
source venv/bin/activate
```
```
python gui.py
```
## Testowanie
```
python -m unittest -v Testy."NAZWATESTU"
```
