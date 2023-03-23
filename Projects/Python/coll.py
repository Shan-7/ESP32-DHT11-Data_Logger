import serial
import csv
import time
port = 'COM10'  # replace with your serial port
baud_rate = 115200  # replace with your ESP32 baud rate
ser = serial.Serial(port, baud_rate)
csvfile = open('data.csv', 'w', newline='')
csvwriter = csv.writer(csvfile)
csvwriter.writerow(['Temperature', 'Humidity', 'Timestamp'])
while True:
    line = ser.readline().decode('utf-8')
    if line.startswith('Temperature:'):
        temp = float(line.split()[1])
        hum = float(line.split()[4])
        timestamp = time.time()
        csvwriter.writerow([temp, hum, timestamp])
        csvfile.flush()
