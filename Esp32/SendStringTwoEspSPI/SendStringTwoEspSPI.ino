#include <SPI.h>

#define SS_PIN 10 // Define o pino SS como 10
const char* data = {"Olá mundo"};

void setup() {
  Serial.begin(9600);
  pinMode(SS_PIN, OUTPUT);
  SPI.begin();
}

void loop() {
  if (SPI.transfer(data, 9)) { // Envie a string "Olá Mundo" com 9 caracteres
    Serial.println("String enviada com sucesso!");
  } else {
    Serial.println("Erro ao enviar a string.");
  }
  delay(1000);
}