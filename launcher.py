import tkinter as tk
from tkinter import messagebox
from subprocess import Popen
import os

def open_program(path):
    Popen(["python", path])

def open_description(title, description):
    desc_window = tk.Toplevel()
    desc_window.title(title)
    desc_window.geometry("400x200")
    tk.Label(desc_window, text=description, wraplength=380, justify="left").pack(padx=10, pady=10)

# Lista programów i ich opisów
programs = [
    {"name": "AES Blokowy", "path": os.path.join("AES_blokowy", "gui.py"), "description": "AES blokowy to metoda szyfrowania danych, która przetwarza informacje w blokach o stałym rozmiarze (zwykle 128 bitów). Jeśli dane są krótsze niż wymagany rozmiar bloku, są uzupełniane specjalnym wypełnieniem (paddingiem). Działa z wykorzystaniem klucza szyfrującego i zaawansowanych operacji matematycznych, takich jak zamiana, mieszanie i przesunięcia bitowe, co sprawia, że dane stają się trudne do odczytania bez odpowiedniego klucza. "},
    {"name": "AES Strumieniowy", "path": os.path.join("AES_strumieniowy", "gui.py"), "description": "AES strumieniowy to sposób szyfrowania danych, który przekształca dane w czasie rzeczywistym, przetwarzając je kawałek po kawałku (strumieniowo), zamiast całych bloków naraz. Wykorzystuje klucz szyfrujący oraz generator wektora początkowego (IV), by zaszyfrować każdy fragment danych w unikalny sposób, zapewniając bezpieczeństwo. "},
    {"name": "DES Blokowy", "path": os.path.join("DES_blokowy", "gui.py"), "description": "DES blokowy to starszy algorytm szyfrowania, który działa na danych podzielonych na bloki o stałym rozmiarze 64 bitów. Wykorzystuje klucz szyfrujący o długości 56 bitów do przekształcania danych w procesie składającym się z 16 rund złożonych operacji, takich jak permutacje i zamiany bitów. DES blokowy był przez lata popularnym standardem, ale dziś jest uważany za przestarzały ze względu na zbyt krótki klucz, co czyni go podatnym na ataki siłowe."},
    {"name": "DES Strumieniowy", "path": os.path.join("DES_strumieniowy", "gui.py"), "description": "DES strumieniowy to modyfikacja klasycznego algorytmu DES, która przetwarza dane w sposób ciągły, zamiast w blokach. Wykorzystuje klucz szyfrujący i generator wektora początkowego (IV), aby szyfrować dane w czasie rzeczywistym, kawałek po kawałku."},
    {"name": "RSA", "path": os.path.join("RSA_czysty", "gui.py"), "description": "RSA to metoda szyfrowania, która wykorzystuje wyłącznie algorytm RSA do ochrony danych. Klucz prywatny i publiczny są generowane w ramach pary, gdzie klucz publiczny służy do szyfrowania danych, a klucz prywatny do ich odszyfrowywania. W czystym RSA dane są dzielone na małe bloki, ponieważ algorytm może przetwarzać jedynie określoną ilość informacji naraz, zależną od długości klucza."},
    {"name": "RSA + AES", "path": os.path.join("Diffie_Hellman", "RSA", "gui.py"), "description": "RSA to popularny algorytm kryptograficzny oparty na kluczach publicznym i prywatnym, wykorzystywany głównie do zabezpieczania transmisji danych. W połączeniu z AES, RSA pełni rolę w hybrydowym szyfrowaniu, gdzie RSA szyfruje klucz sesyjny AES, a AES jest używany do szyfrowania dużych ilości danych. AES jest szybki i wydajny, co czyni go idealnym do szyfrowania danych, podczas gdy RSA zapewnia bezpieczne przekazanie klucza AES."},
    {"name": "Szyfr Monoalfabetyczny", "path": os.path.join("MonoAlfabetyczny", "gui.py"), "description": "Szyfr monoalfabetyczny to prosty sposób szyfrowania tekstu, w którym każda litera alfabetu zastępowana jest inną literą zgodnie z ustalonym kluczem. Klucz to permutacja całego alfabetu, co oznacza, że każda litera ma przypisanego dokładnie jednego odpowiednika. Na przykład, litera „A” może być zamieniona na „K”, „B” na „Z” i tak dalej. Szyfr ten jest łatwy do zrozumienia, ale nie zapewnia dużego bezpieczeństwa, ponieważ częstotliwość występowania liter w języku naturalnym może pomóc w jego złamaniu."},
    {"name": "Szyfr Transpozycyjny", "path": os.path.join("Transpozycyjny", "gui.py"), "description": "Szyfr transpozycyjny to metoda szyfrowania, w której litery tekstu są przestawiane według określonego wzoru, zamiast zastępowania ich innymi znakami. Oznacza to, że zawartość wiadomości pozostaje ta sama, ale zmienia się kolejność liter. Na przykład w szyfrze kolumnowym tekst jest zapisywany w siatce wierszy i odczytywany kolumnami zgodnie z ustalonym kluczem."},
    {"name": "Hamak", "path": os.path.join("Hamak", "gui.py"), "description": "Hamak ziała na zasadzie przesunięcia wartości bajtów w danych i jest wzorowany na podstawowych operacjach używanych w szyfrowaniu, takich jak suma modulo. Każdy bajt danych (np. znak tekstu lub część pliku) jest modyfikowany poprzez dodanie wartości klucza (+ klucz) i obliczenie wyniku modulo 256. Dzięki temu wynik zawsze mieści się w zakresie wartości bajtu (0-255)."},
     {"name": "Diffie-Hellman - symulacja", "path": os.path.join("Diffie_Hellman", "simulation.py"), "description": "Protokół Diffie-Hellmana to metoda pozwalająca dwóm stronom na uzgodnienie wspólnego klucza kryptograficznego, nawet jeśli komunikują się przez niezabezpieczony kanał. W procesie tym każda ze stron generuje klucz prywatny oraz publiczny, a następnie wymienia się kluczami publicznymi. Dzięki matematycznym właściwościom liczb pierwszych i potęgowania modulo obie strony mogą obliczyć identyczny wspólny klucz, którego nie można łatwo odgadnąć, obserwując tylko wymienione informacje."},
    {"name": "Podpisy cyfrowe - czytnik", "path": os.path.join("Podpisy", "certificates.py"), "description": "Program do analizy podpisów cyfrowych umożliwia odczyt i weryfikację podpisów w plikach PDF. Pozwala zidentyfikować podpisującego, powód podpisu, datę jego złożenia oraz lokalizację. Dodatkowo analizuje certyfikaty związane z podpisem, prezentując informacje o wystawcy, podmiocie, okresie ważności i zastosowanym algorytmie."},
]

# Główne okno aplikacji
app = tk.Tk()
app.title("Cetera Bartłomiej 31230")
app.geometry("450x975")

# Nagłówek
tk.Label(app, text="Launcher - Kryptografia", font=("Arial", 14)).pack(pady=5)

# Tworzenie kontenerów dla każdego programu
for program in programs:
    frame = tk.LabelFrame(app, text=program["name"], padx=10, pady=10)
    frame.pack(fill="x", pady=10, padx=10)

    program_button = tk.Button(frame, text="Program", command=lambda p=program: open_program(p["path"]))
    program_button.pack(side="left", expand=True, fill="both", padx=5)

    description_button = tk.Button(frame, text="Opis", command=lambda p=program: open_description(p["name"], p["description"]))
    description_button.pack(side="left", expand=True, fill="both", padx=5)

# Uruchomienie pętli głównej
app.mainloop()
