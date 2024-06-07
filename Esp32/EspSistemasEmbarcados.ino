#include <Wire.h>

#define meuEnd 0x09
#define pinoLed1 2

boolean estadoPino1 = LOW;
int dado_recebido = 0;

void setup() {
  // put your setup code here, to run once:
  Wire.begin(meuEnd);
  Serial.begin(9600);
  pinMode(pinoLed1, OUTPUT);
  Wire.onReceive(receiveEvent);
  Wire.onRequest(requestEvent);
}

void loop() {
  // put your main code here, to run repeatedly:

}

void requestEvent() {
  Wire.write("ESP 2");
}

void receiveEvent(int numBytes){
  if (numBytes == 1){
    dado_recebido = Wire.read();
    Serial.print(F("Dado recebido -> "));
    Serial.println(dado_recebido);
    digitalWrite(pinoLed1, estadoPino1);
  } else {
    Serial.print(F("Nenhum parametro recebido"));
  }
}