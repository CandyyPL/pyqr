from pyzbar import pyzbar
from PIL import Image
import qrcode
import sys
import os

def help():
  print()
  print('\t-e\tmake QR code')
  print('\t-d\tread QR code')
  print('\t-f\tfile to read/make QR code from')
  print('\t-h\tdisplay this help menu')
  print()

def makeQR(file):
  qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=2,
  )

  filename = file
  file = open(file)

  data = file.read()

  qr.add_data(data)
  qr.make(fit=True)

  filename = 'qrcode.png'

  img = qr.make_image(fill_color="black", back_color="white")
  img.save(filename)

  print(f'Saved QR code to {filename}')
  print()
  exit()

def readQR(file):
  img = Image.open(file)

  data = pyzbar.decode(img)
  data = data[0][0].strip().decode()

  filename = 'qrdata.txt'

  with open(filename, 'w') as f:
    f.write(data)

  print(f'Data from QR code saved to {filename}')
  print()
  exit()

def main():
  print('PyQR by Candyy v1.0')

  if '-h' in sys.argv:
    help()
    return

  print('note: use -h option to display the help')
  print()

  if len(sys.argv) < 3:
    return

  file = None

  for x in sys.argv:
    nextArgIdx = sys.argv.index(x) + 1

    if x == '-f':
      file = sys.argv[nextArgIdx]

  if '-e' in sys.argv:
    makeQR(file)
  if '-d' in sys.argv:
    readQR(file)

if __name__ == '__main__': main()
