import re
import qrcode

data = "https://www.notion.so/97503c6705b948a3b8e9179f0f3c9ef5"

# Extract the domain after 'www.' or the main domain name
match = re.search(r"www\.([\w-]+)", data)
if match:
    site_name = match.group(1)
else:
    # Fallback: extract the main domain
    match2 = re.search(r"https?://([\w-]+)\.", data)
    site_name = match2.group(1) if match2 else "qr"

filename = f"{site_name}.png"

qr = qrcode.make(data)
qr.save(filename)
print(f"QR Code Has Been Generated and saved as {filename}")
