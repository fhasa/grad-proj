import time
import sys
import cv2
from pyzbar import pyzbar
import RPi.GPIO as GPIO
from hx711_lib import HX711

def read_barcodes(frame, val, barcode_info_lower):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y, w, h = barcode.rect
        barcode_info = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)

        barcode_info_lower = barcode_info.lower()
        if "city a" in barcode_info_lower:
            if val <= 300:
                print("City A Light")
            else:
                print("City A Heavy")
        elif "city b" in barcode_info_lower:
            if val <= 300:
                print("City B Light")
            else:
                print("City B Heavy")

        with open("barcode_result.txt", mode='w') as file:
            file.write("Recognized Barcode: " + barcode_info)

    return frame


def cleanAndExit():
    print("Cleaning...")
    if not EMULATE_HX711:
        GPIO.cleanup()
    print("Bye!")
    sys.exit()

referenceUnit = 113
hx = HX711(5, 6)
hx.set_reading_format("MSB", "MSB")
hx.set_reference_unit(referenceUnit)
hx.reset()
hx.tare()

print("Tare done! Add weight now...")
val=0
camera = cv2.VideoCapture(0)
ret, frame = camera.read()
while True:
    try:
        if abs(val-((abs(hx.get_weight(5))/2)*0.05+((abs(hx.get_weight(5))/2)))) > 5 :
            val = (abs(hx.get_weight(5))/2)*0.05+((abs(hx.get_weight(5))/2))
            print(val)
            frame = read_barcodes(frame, val, barcode_info_lower)
            cv2.imshow('Barcode/QR code reader', frame)
            if cv2.waitKey(1) & 0xFF == 27:
                break

            hx.power_down()
            hx.power_up()
            time.sleep(0.1)

        val = (abs(hx.get_weight(5))/2)*0.05+((abs(hx.get_weight(5))/2))

    except (KeyboardInterrupt, SystemExit):
        cleanAndExit()


camera.release()
cv2.destroyAllWindows()
