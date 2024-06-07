/* Escravo Slave2 (SPI): recebe comando do Master
para comandar o Led na porta 32
e retonar solicitacao do master, como a seguir:
dado recebido acao
 0 inverte estado do led1
 1 retorna código asso. ao id do ESP
 2 a definir
*/
#include <ESP32SPISlave.h>

#define pinoLed1 32 // numero do pino onde o LED1 esta conectado
#define pinoLed2 33 // numero do pino onde o LED2 esta conectado

// Definindo variáveis e objetos
ESP32SPISlave slave;
static constexpr uint32_t BUFFER_SIZE {32};
uint8_t spi_slave_tx_buf[BUFFER_SIZE];
uint8_t spi_slave_rx_buf[BUFFER_SIZE];
boolean estadoPino1 = LOW;
boolean estadoPino2 = LOW;
int dado_recebido;
const int tempo_piscar = 300; //(ms)
char opcao_pisca = 0;
uint64_t ultimo_instante = 0;
enum codigo { INV_LED, ID_ESP, OUTRO };
String tempoFuncionamento;

void trata_dados(){
  switch(dado_recebido) {
    case INV_LED:
      estadoPino1 = !estadoPino1;
      digitalWrite(pinoLed1, estadoPino1);
      memset(spi_slave_tx_buf, 20, BUFFER_SIZE);
      break;
    case ID_ESP:
      memset(spi_slave_tx_buf, 21, BUFFER_SIZE);
      break;
    case 2:
      tempoFuncionamento = showTime();
      Serial.println(tempoFuncionamento);
      memset(&tempoFuncionamento, 22, BUFFER_SIZE);
      digitalWrite(pinoLed1, HIGH);
      delay(1000);
      digitalWrite(pinoLed1, LOW);
      break;
    default:
      break;
  }
}

void setup() {
 Serial.begin(115200);
 //delay(2000);
 pinMode(pinoLed1, OUTPUT);
 pinMode(pinoLed2, OUTPUT);
 slave.setDataMode(SPI_MODE0);
 slave.begin(VSPI);
 // clear buffers
 memset(spi_slave_tx_buf, 0, BUFFER_SIZE);
 memset(spi_slave_rx_buf, 0, BUFFER_SIZE);
 //print default SPI pins
}

void loop() {
  // block until the transaction comes from master
  slave.wait(spi_slave_rx_buf, spi_slave_tx_buf, BUFFER_SIZE);
  // slave.wait(100);
  // if transaction has completed from master,
  // available() returns size of results of transaction,
  // and buffer is automatically updated

  while (slave.available()) {
    // show received data
    Serial.print("Command Received: ");
    Serial.println(spi_slave_rx_buf[0]);
    dado_recebido = spi_slave_rx_buf[0];
    slave.pop();
  }
  trata_dados();
}

String showTime()
{
  unsigned long uptime = millis(); 
  unsigned long segundos = uptime / 1000;
  unsigned long minutos = segundos / 60;
  unsigned long horas = minutos / 60;
  //tempoFuncionamento = "Tempo de funcionamento: ";
  tempoFuncionamento = tempoFuncionamento + horas + ":" + (minutos % 60) + ":" + (segundos % 60);
  return tempoFuncionamento;
}