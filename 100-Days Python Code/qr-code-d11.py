"""
upi_qr_generator.py
Simple UPI QR code generator for use in VS Code.
Dependencies: qrcode[pil], pillow
Install with: pip install qrcode[pil] pillow
"""

import qrcode
from PIL import Image
import urllib.parse
import sys

def build_upi_uri(vpa: str, name: str = "", amount: str = "", note: str = "") -> str:
    """
    Construct a UPI deep link / URI.
    Example output: upi://pay?pa=merchant@upi&pn=Merchant%20Name&am=10.00&tn=For%20order&cu=INR
    """
    params = {}
    # Mandatory parameter: pa (payee VPA)
    params["pa"] = vpa.strip()
    if name:
        params["pn"] = name.strip()
    if amount:
        # keep amount as string; validation minimal (you can add more)
        params["am"] = amount.strip()
    if note:
        params["tn"] = note.strip()

    params["cu"] = "INR"  # currency
    query = urllib.parse.urlencode(params, safe='')  # encode params safely
    uri = f"upi://pay?{query}"
    return uri

def generate_qr(data: str, filename: str = "upi_qr.png", box_size: int = 10, border: int = 4):
    """
    Generate and save QR code PNG.
    - data: text to encode (UPI URI)
    - filename: output file
    - box_size, border: visual tidy parameters
    """
    qr = qrcode.QRCode(
        version=None,  # automatic size
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    return filename, img

def main():
    print("UPI QR Code Generator — simple & safe")
    # Get user inputs
    vpa = input("Enter payee UPI ID (VPA) (e.g. example@upi): ").strip()
    if not vpa:
        print("Payee UPI ID is required. Exiting.")
        sys.exit(1)

    name = input("Enter payee name (optional): ").strip()
    amount = input("Enter amount (optional, e.g. 150.50) — leave blank for no amount: ").strip()
    note = input("Enter note / transaction reference (optional): ").strip()

    upi_uri = build_upi_uri(vpa=vpa, name=name, amount=amount, note=note)
    print("\nGenerated UPI URI:")
    print(upi_uri)

    filename = input("\nEnter output filename (press Enter for 'upi_qr.png'): ").strip() or "upi_qr.png"

    saved_file, img = generate_qr(upi_uri, filename=filename)
    print(f"\nQR saved to: {saved_file}")

    try:
        # Open image using default image viewer
        img.show()
        print("Opened the QR image in the default image viewer.")
    except Exception as e:
        print("Could not open image automatically. You can open the file manually.")
        print("Error:", e)

if __name__ == "__main__":
    main()
