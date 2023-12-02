from escpos.printer import Usb 




printer = Usb(idVendor=0x04b8, idProduct=0x0202)


printer.text("Hello, World!\n")


printer.text("----------------------------\n")


printer.set(align='center', text_type='B', width=2, height=2)
printer.text("BIG TEXT\n")


printer.set()


printer.barcode('123456789012', 'EAN13', 64, 2, '', '')


printer.qr("Your QR Code Data Here")


printer.cut()


printer.close()
