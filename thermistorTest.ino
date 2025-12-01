// the value of the 'other' resistor
#define SERIESRESISTOR 10000    
 
// What pin to connect the sensor to
#define THERMISTORPIN A0 
float tempRecip = 0;
float tempK = 0;
float tempC = 0;
#include <math.h>
 
void setup(void) {
  Serial.begin(9600);
}
 
void loop(void) {

  float reading;

  for(int i = 0; i < 5; i++){
    double power = pow(10,i);
    double log1 = log(power);
    Serial.print("THIS IS THE LOG:");
    Serial.println(log1);

  }
 
  reading = analogRead(THERMISTORPIN);
 
  Serial.print("Analog reading "); 
  Serial.println(reading);
 
  // convert the value to resistance
  reading = (1023 / reading)  - 1;     // (1023/ADC - 1) 
  reading = SERIESRESISTOR / reading;  // 10K / (1023/ADC - 1)
  Serial.print("Thermistor resistance "); 
  Serial.println(reading);
  
  //convert the resistance to temperature
  tempRecip = (1/298.15)+(1/3950)+log(reading/10000);
  tempK = 1/tempRecip;
  Serial.print("Temperature (K):");
  Serial.println(tempK);
  tempC = tempK - 273.15;
  Serial.print("Temperature (C):");
  Serial.println(tempC);
 
  delay(10000);
}

