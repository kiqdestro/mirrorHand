#include <SoftwareSerial.h>

//const int txPin = 5;
//const int rxPin = 6;

//SoftwareSerial BTSerial(rxPin, txPin); // RX, TX

void setup() {
  Serial.begin(115200);
  Serial.println("Enter AT commands:");
  Serial1.begin(115200);
}

void loop() {
  if (Serial1.available())
  {
    Serial.write(Serial1.read());
  }
  if (Serial.available())
    Serial1.write(Serial.read());
}
