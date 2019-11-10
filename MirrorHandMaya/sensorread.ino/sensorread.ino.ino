/*
  ReadAnalogVoltage

  Reads an analog input on pin 0, converts it to voltage, and prints the result to the Serial Monitor.
  Graphical representation is available using Serial Plotter (Tools > Serial Plotter menu).
  Attach the center pin of a potentiometer to pin A0, and the outside pins to +5V and ground.

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/ReadAnalogVoltage
*/

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(115200);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pins 0 to 10:
  int sensor[10];
  sensor[0] = analogRead(A0);
  sensor[1] = analogRead(A1);
  sensor[2] = analogRead(A2);
  sensor[3] = analogRead(A3);
  sensor[4] = analogRead(A4);
  //sensor[5] = analogRead(A5);
  //sensor[6] = analogRead(A6);
  //sensor[7] = analogRead(A7);
  //sensor[8] = analogRead(A8);
  //sensor[9] = analogRead(A9);

  //Print the values to serial
  for(int i = 0; i < 10; i++)
  {
    Serial.print(">s="); Serial.print(i); Serial.print("\t");Serial.print(sensor[i]); Serial.print("\t");
    Serial.println("");
   delayMicroseconds(86);
  }
}
