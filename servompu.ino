#include <MPU6050.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>
#include <Servo.h>

Servo servo;
Adafruit_MPU6050 srituhobby;

void setup(void) {
  Serial.begin(115200);
  servo.attach(11);
  Wire.begin();
  srituhobby.begin();
  servo.write(0);

  srituhobby.setAccelerometerRange(MPU6050_RANGE_8_G);
  srituhobby.setGyroRange(MPU6050_RANGE_500_DEG);
  srituhobby.setFilterBandwidth(MPU6050_BAND_21_HZ);

  delay(100);
}

void loop() {

 
  sensors_event_t a, g, temp;
  srituhobby.getEvent(&a, &g, &temp);

  int value = a.acceleration.y;

  value = map(value, -10, 10, 180,0);
  servo.write(value);  
  Serial.println(value);
  

}