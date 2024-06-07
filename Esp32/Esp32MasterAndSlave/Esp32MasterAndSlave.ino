#include <Wire.h>
#include <Arduino.h>

#define meuEnd 0xb

const int pinoLed1 = 19;
boolean estadoPino1 = LOW;
int dado_recebido = 0;
bool pulsaLed = false;
const int touch = 4;
String tempoFuncionamento = "Tempo de funcionamento: ";
int dadoRecebido = 0;

void setup() {
  // put your setup code here, to run once:
  Wire.begin(meuEnd);
  Serial.begin(9600);
  pinMode(pinoLed1, OUTPUT);
  pinMode(touch, INPUT);
  Wire.onReceive(receiveEvent);
  Wire.onRequest(requestEvent);

}

void loop() {

  if (touchRead(touch) < 50)
  {
    Serial.println(showTime());
    pulsaLed = !pulsaLed;
    digitalWrite(pinoLed1, pulsaLed);
    delay(200);
  }

  if (dadoRecebido == 0)
  {
    if (touchRead(touch) < 50)
    {
      delay(100);
      pulsaLed = !pulsaLed;
      digitalWrite(pinoLed1, pulsaLed);
    }
  } else if (dadoRecebido == 1)
  {
    delay(100);
    pulsaLed = !pulsaLed;
    digitalWrite(pinoLed1, pulsaLed);
  } else if (dadoRecebido == 2)
  {
    delay(100);
    pulsaLed = !pulsaLed;
    digitalWrite(pinoLed1, pulsaLed);
  }
}

void receiveEvent(int numBytes){
  if (numBytes == 1)
  {
    dado_recebido = Wire.read();
    Serial.print(F("Dado recebido -> "));
    Serial.println(dado_recebido);
    pulsaLed = !pulsaLed;
    digitalWrite(pinoLed1, pulsaLed);
    switch(dadoRecebido){
      case 0:
        Wire.write("SAMUEL's ESP32");
        break;
      case 1:
        Wire.write("Pulsando a 5Hz");
        break;
      case 2:
        Wire.write(showTime().toInt());
        break;
      default:
        Serial.println("ERROR");
    }
  }
  else 
  {
    Serial.println("Me parece que algo deu errado :/");
  }
}

void requestEvent(){
  Serial.println(dadoRecebido);
  switch(dadoRecebido){
    case 0:
      Wire.write("SAMUEL's ESP32");
      break;
    case 1:
      Wire.write("Pulsando a 5Hz");
      break;
    case 2:
      Wire.write(showTime().toInt());
      break;
    default:
      Serial.println("ERROR");
  }
  
}

String showTime()
{
  unsigned long uptime = millis(); 
  unsigned long segundos = uptime / 1000;
  unsigned long minutos = segundos / 60;
  unsigned long horas = minutos / 60;
  tempoFuncionamento = "Tempo de funcionamento: ";
  tempoFuncionamento = tempoFuncionamento + horas + ":" + (minutos % 60) + ":" + (segundos % 60);
  return tempoFuncionamento;
}
