// the value of the 'other' resistor
#define SERIESRESISTOR 10000    

#include <Servo.h>

Servo myservo;  // create servo object to control a servo

int pos = 0;    // variable to store the servo position

const int buzzer = 10; //buzzer to arduino pin 10

 
// What pin to connect the sensor to
#define THERMISTORPIN A2 
float tempRecip = 0;
float tempK = 0;
float tempC = 0;
#include <math.h>
 
void setup(void) {
  Serial.begin(9600);
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
  pinMode(buzzer, OUTPUT); // Set buzzer - pin 9 as an output
}
 
void loop(void) {

  float reading;
  reading = analogRead(THERMISTORPIN);
 
  Serial.print("Analog reading "); 
  Serial.println(reading);
 
  // convert the value to resistance
  reading = (1023 / reading)  - 1;     // (1023/ADC - 1) 
  reading = SERIESRESISTOR / reading;  // 10K / (1023/ADC - 1)
  Serial.print("Thermistor resistance "); 
  Serial.println(reading);
  
  //convert the resistance to temperature
  float stepA = 0;
  //float stepB = 0;
  float stepC = 0;
  float stepBC = 0;
  stepA = (1/298.15);
  Serial.println("Step A: "+String(stepA,9));
  float stepB = (float)1/3950;
  //Serial.println("TEST: "+String(1/1000,16));
  //Serial.println("Step B: "+String(stepB,16));
  stepBC = reading/10000;
  //Serial.println("Step BC: "+String(stepBC,9));
  stepC = log(stepBC);
  //Serial.println("Step C: "+String(stepC,9));
  tempRecip = stepA+stepB*stepC;
  //Serial.print("1/Temperature:");
 // Serial.println(tempRecip);
  tempK = 1/tempRecip;
  Serial.print("Temperature (K):");
  Serial.println(tempK);
  tempC = tempK - 273.15;
  Serial.print("Temperature (C):");
  Serial.println(tempC);
 
if(tempC < 10 || tempC > 30){
  tone(buzzer, 1000); // Send 1KHz sound signal...
  delay(1000);         // ...for 1 sec
  noTone(buzzer);     // Stop sound...
  delay(1000);         // ...for 1sec
   Serial.println("Opening door");
  for (pos = 0; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(20);                       // waits 15ms for the servo to reach the position
  }
  delay(10000);
   Serial.println("Closing door");
  for (pos = 180; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(20);                       // waits 15ms for the servo to reach the position
  
  }

}

  delay(5000);
}

