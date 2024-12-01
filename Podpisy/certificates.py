import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader
from cryptography import x509
from cryptography.hazmat.primitives.serialization.pkcs7 import load_der_pkcs7_certificates
from cryptography.hazmat.backends import default_backend
from datetime import datetime
import base64


def format_pdf_date(pdf_date):
    """
    Konwertuje datę PDF z formatu D:YYYYMMDDHHmmSS±HH'mm' na czytelny format.
    """
    if pdf_date.startswith("D:"):
        pdf_date = pdf_date[2:]  # Usuń "D:"
    try:
        date = datetime.strptime(pdf_date[:14], "%Y%m%d%H%M%S")
        return date.strftime("%Y-%m-%d %H:%M:%S")
    except ValueError:
        return pdf_date  # Jeśli format nie jest standardowy, zwróć oryginalny


def parse_pkcs7_certificates(contents):
    """
    Parsuje certyfikaty z danych PKCS#7.
    """
    try:
        certs = load_der_pkcs7_certificates(contents)
        if not certs:
            return "Brak certyfikatów w danych PKCS#7."
        cert_details = []
        for cert in certs:
            cert_details.append({
                "Wystawca (Issuer)": cert.issuer.rfc4514_string(),
                "Podmiot (Subject)": cert.subject.rfc4514_string(),
                "Algorytm Podpisu": cert.signature_algorithm_oid._name,
                "Data Ważności Od": cert.not_valid_before.strftime("%Y-%m-%d"),
                "Data Ważności Do": cert.not_valid_after.strftime("%Y-%m-%d"),
            })
        return cert_details
    except Exception as e:
        return {"Błąd podczas parsowania PKCS#7": str(e)}


def debug_signature(sig):
    """
    Wyświetla pełną strukturę podpisu cyfrowego dla diagnostyki.
    """
    print("\n--- Debugowanie podpisu ---")
    for key, value in sig.items():
        try:
            if isinstance(value, bytes):
                print(f"{key}: {value[:100]}... (truncated)")
            else:
                print(f"{key}: {value}")
        except Exception as e:
            print(f"{key}: Błąd podczas odczytu: {e}")
    print("--- Koniec debugowania podpisu ---\n")


def extract_signature_details(file_path):
    """
    Wyciąga szczegóły podpisów z pliku PDF i próbuje znaleźć dane certyfikatu.
    """
    try:
        reader = PdfReader(file_path)
        root = reader.trailer['/Root'].get_object()
        acroform = root.get('/AcroForm')
        if acroform:
            acroform_obj = acroform.get_object()
            if '/SigFlags' in acroform_obj:
                signatures = []
                fields = acroform_obj.get('/Fields', [])
                for field in fields:
                    field_obj = field.get_object()
                    if '/V' in field_obj:
                        sig = field_obj['/V'].get_object()
                        debug_signature(sig)  # Debugowanie podpisu
                        signature_info = {
                            "Podpisujący": sig.get('/Name', 'Brak danych'),
                            "Powód": sig.get('/Reason', 'Brak danych'),
                            "Data": format_pdf_date(sig.get('/M', 'Brak danych')),
                            "Lokalizacja": sig.get('/Location', 'Brak danych'),
                        }
                        # Próbujemy odczytać dane z /Contents jako PKCS#7
                        if '/Contents' in sig:
                            contents = sig['/Contents']
                            try:
                                cert_details = parse_pkcs7_certificates(contents)
                                signature_info["Certyfikat"] = cert_details
                            except Exception as e:
                                signature_info["Certyfikat"] = {"Błąd": str(e)}
                        else:
                            signature_info["Certyfikat"] = "Dane podpisu nie zawierają certyfikatu."
                        signatures.append(signature_info)
                return signatures if signatures else None
        return None
    except Exception as e:
        raise e


def display_signature_details(signatures):
    """
    Wyświetla podpisy w czytelnej formie w polu tekstowym.
    """
    details_text.delete("1.0", tk.END)
    if signatures:
        for i, signature in enumerate(signatures, 1):
            details_text.insert(tk.END, f"Podpis {i}:\n")
            details_text.insert(tk.END, f"  Podpisujący: {signature.get('Podpisujący', 'Brak danych')}\n")
            details_text.insert(tk.END, f"  Powód: {signature.get('Powód', 'Brak danych')}\n")
            details_text.insert(tk.END, f"  Data: {signature.get('Data', 'Brak danych')}\n")
            details_text.insert(tk.END, f"  Lokalizacja: {signature.get('Lokalizacja', 'Brak danych')}\n")
            cert = signature.get("Certyfikat", {})
            if isinstance(cert, list):
                details_text.insert(tk.END, f"  Certyfikat:\n")
                for cert_detail in cert:
                    for key, value in cert_detail.items():
                        details_text.insert(tk.END, f"    {key}: {value}\n")
            elif isinstance(cert, dict):
                details_text.insert(tk.END, f"  Certyfikat:\n")
                for key, value in cert.items():
                    details_text.insert(tk.END, f"    {key}: {value}\n")
            else:
                details_text.insert(tk.END, f"  Certyfikat: {cert}\n")
            details_text.insert(tk.END, "\n")
    else:
        details_text.insert(tk.END, "Nie znaleziono podpisów cyfrowych.\n")


def select_pdf():
    """
    Otwiera okno wyboru pliku PDF i wyświetla szczegóły podpisu.
    """
    file_path = filedialog.askopenfilename(
        filetypes=[("PDF files", "*.pdf")],
        title="Wybierz plik PDF"
    )
    if file_path:
        try:
            signature_details = extract_signature_details(file_path)
            if signature_details:
                result_text.set("Podpis cyfrowy znaleziony. Szczegóły wyświetlono poniżej.")
                display_signature_details(signature_details)
            else:
                result_text.set("Nie znaleziono podpisu cyfrowego w pliku PDF.")
                details_text.delete("1.0", tk.END)
        except Exception as e:
            messagebox.showerror("Błąd", f"Nie można odczytać pliku PDF:\n{e}")


# Tworzenie GUI
app = tk.Tk()
app.title("Odczyt podpisów cyfrowych z PDF")
app.geometry("750x470")

tk.Label(app, text="Wybierz plik PDF, aby odczytać podpis cyfrowy:").pack(pady=10)
tk.Button(app, text="Wybierz PDF", command=select_pdf).pack(pady=10)

result_text = tk.StringVar()
result_label = tk.Label(app, textvariable=result_text, wraplength=750, justify="center")
result_label.pack(pady=10)

details_text = tk.Text(app, wrap=tk.WORD, height=20, width=90)
details_text.pack(pady=10)

# Uruchomienie aplikacji
app.mainloop()
