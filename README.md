INSTALLATION REQUIREMENTS


make sure to do pip install -r requirements.txt 
because you dont do pip install escpos.printer

REQUIREMENTS TO RUN
and your all set! now you need to connect the Raspberry Pi with a USB cable to your Bixolon printer, 
or plug in your computer with a USB cable to the printer

Then, open a terminal
type lsusb ONLY, nothing else. this will list the USB  devices

Bus XXX Device XXX: ID [Vendor ID]:[Product ID] ...
so then you will copy the VENDOR ID and PRODUCT ID into the main.py

WARNING: IN ORDER TO GET LSUSB YOU MUST HAVE A LINUX MACHINE.