// Master

#include <HardwareSerial.h>

HardwareSerial SerialPort(2); // Usando UART2
String liga = "LIGA\n";
String desliga = "DESLIGA\n";
//const int numOfElements = (liga.length());  
//char charbuffer[numOfElements];
//shape_sequence.toCharArray(charbuffer, numOfElements);

void setup() {
  SerialPort.begin(115200, SERIAL_8N1, 16, 17);
}

void loop() {
  SerialPort.print(liga); //Write the serial data
  delay(2000);
  SerialPort.print(desliga); //Write the serial data
  delay(2000);
}

