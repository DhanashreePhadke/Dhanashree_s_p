// Pins for the first leftt ultrasonic sensor
const int trigPin1 = 22;
const int echoPin1 = 23;
int l1 = 40; // blue led left
int l2 = 41; // red led left


// Pins for the second front ultrasonic sensor
const int trigPin2 = 24;
const int echoPin2 = 25;
int l3 = 42; // blue led left
int l4 = 43; // red led left

// Pins for the third right ultrasonic sensor
const int trigPin3 = 26;
const int echoPin3 = 27; 
int l5 = 44; // blue led left


int l6 = 45 ; // red led left

// Pins for the 4th Back ultrasonic sensor
const int trigPin4 = 28;
const int echoPin4 = 29; 
int l7 = 46; // blue led left
int l8 = 47 ; // red led left

//buzzer pin
const int buzzerPin = 2;

void setup() {
  Serial.begin(9600);
  
  // Initialize trigger pins as OUTPUT
  pinMode(trigPin1, OUTPUT);
  pinMode(trigPin2, OUTPUT);
  pinMode(trigPin3, OUTPUT);
  pinMode(trigPin4, OUTPUT);

  // Initialize echo pins as INPUT
  pinMode(echoPin1, INPUT);
  pinMode(echoPin2, INPUT);
  pinMode(echoPin3, INPUT);
  pinMode(echoPin4, INPUT);

  //initialize led pins
  pinMode(l1, OUTPUT);
  pinMode(l2, OUTPUT);
  pinMode(l3, OUTPUT);
  pinMode(l4, OUTPUT);
  pinMode(l5, OUTPUT);
  pinMode(l6, OUTPUT);
  pinMode(l7, OUTPUT);
  pinMode(l8, OUTPUT);

//initialize buzzer
  pinMode(buzzerPin, OUTPUT);
}

void loop() {
  // Measure distance using the first ultrasonic sensor
  long duration1, distance1;
  digitalWrite(trigPin1, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin1, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin1, LOW);
  duration1 = pulseIn(echoPin1, HIGH);
  distance1 = duration1 * 0.034 / 2;

  // Measure distance using the second ultrasonic sensor
  long duration2, distance2;
  digitalWrite(trigPin2, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin2, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin2, LOW);
  duration2 = pulseIn(echoPin2, HIGH);
  distance2 = duration2 * 0.034 / 2;

  // Measure distance using the third ultrasonic sensor
  long duration3, distance3;
  digitalWrite(trigPin3, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin3, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin3, LOW);
  duration3 = pulseIn(echoPin3, HIGH);
  distance3 = duration3 * 0.034 / 2;

  // Measure distance using the fourth ultrasonic sensor
  long duration4, distance4;
  digitalWrite(trigPin4, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin4, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin4, LOW);
  duration4 = pulseIn(echoPin4, HIGH);
  distance4 = duration4 * 0.034 / 2;



  // Print the distances to the Serial Monitor
  Serial.print("Distance 1: ");
  Serial.print(distance1);
  Serial.print(" cm\t");
  Serial.print("Distance 2: ");
  Serial.print(distance2);
  Serial.print(" cm\t");
  Serial.print("Distance 3: ");
  Serial.print(distance3);
  Serial.println(" cm");
  Serial.print("distance 4 : ");
  Serial.print(distance4);
  Serial.println(" cm");

  if (distance1 < 300 && distance1 >50 )
  {
  digitalWrite(l1, HIGH);
  digitalWrite(l2, LOW);
  digitalWrite(l3, LOW);
  digitalWrite(l4, LOW);
  digitalWrite(l5, LOW);
  digitalWrite(l6, LOW);
  digitalWrite(l6, LOW);
  digitalWrite(l7, LOW);
  digitalWrite(buzzerPin, LOW);
  delay(100);
  }
   else
 {
  digitalWrite(l1, LOW);
  digitalWrite(l2, LOW);
  digitalWrite(l3, LOW);
  digitalWrite(l4, LOW);
  digitalWrite(l5, LOW);
  digitalWrite(l6, LOW);
  digitalWrite(l7, LOW);
  digitalWrite(l8, LOW);
  digitalWrite(buzzerPin, LOW);
  delay(100);
 }
 
  if (distance2 < 300 && distance2 >50 )
  {
  digitalWrite(l1, LOW);
  digitalWrite(l2, LOW);
  digitalWrite(l3, HIGH);
  digitalWrite(l4, LOW);
  digitalWrite(l5, LOW);
  digitalWrite(l6, LOW);
  digitalWrite(l7, LOW);
  digitalWrite(l8, LOW);
  digitalWrite(buzzerPin, LOW);
  delay(100);
  }
  else
 {
  digitalWrite(l1, LOW);
  digitalWrite(l2, LOW);
  digitalWrite(l3, LOW);
  digitalWrite(l4, LOW);
  digitalWrite(l5, LOW);
  digitalWrite(l6, LOW);
  digitalWrite(l7, LOW);
  digitalWrite(l8, LOW);
  digitalWrite(buzzerPin, LOW);
  delay(100);
 }
   if (distance3 < 300 && distance3 >50 )
  {
  digitalWrite(l1, LOW);
  digitalWrite(l2, LOW);
  digitalWrite(l3, LOW);
  digitalWrite(l4, LOW);
  digitalWrite(l5, HIGH);
  digitalWrite(l6, LOW);
  digitalWrite(l7, LOW);
  digitalWrite(l8, LOW);
  digitalWrite(buzzerPin, LOW);
  delay(100);
  }
  else
 {
  digitalWrite(l1, LOW);
  digitalWrite(l2, LOW);
  digitalWrite(l3, LOW);
  digitalWrite(l4, LOW);
  digitalWrite(l5, LOW);
  digitalWrite(l6, LOW);
  digitalWrite(l7, LOW);
  digitalWrite(l8, LOW);
  digitalWrite(buzzerPin, LOW);
  delay(100);
 } 

  if (distance4 < 300 && distance4 >50 )
  {
  digitalWrite(l1, LOW);
  digitalWrite(l2, LOW);
  digitalWrite(l3, LOW);
  digitalWrite(l4, LOW);
  digitalWrite(l5, LOW);
  digitalWrite(l6, LOW);
  digitalWrite(l7, HIGH);
  digitalWrite(l8, LOW);
  digitalWrite(buzzerPin, LOW);
  delay(100);
  }
  else
 {
  digitalWrite(l1, LOW);
  digitalWrite(l2, LOW);
  digitalWrite(l3, LOW);
  digitalWrite(l4, LOW);
  digitalWrite(l5, LOW);
  digitalWrite(l6, LOW);
  digitalWrite(l7, LOW);
  digitalWrite(l8, LOW);
  digitalWrite(buzzerPin, LOW);
  delay(100);
 } 


  if (distance1 < 100 )
  {
  digitalWrite(l1, LOW);
  digitalWrite(l2, HIGH);
  digitalWrite(l3, LOW);
  digitalWrite(l4, LOW);
  digitalWrite(l5, LOW);
  digitalWrite(l6, LOW);
  digitalWrite(l7, LOW);
  digitalWrite(l8, LOW);
  digitalWrite(buzzerPin, HIGH);
  delay(100);
  }
 else
 {
  digitalWrite(l1, LOW);
  digitalWrite(l2, LOW);
  digitalWrite(l3, LOW);
  digitalWrite(l4, LOW);
  digitalWrite(l5, LOW);
  digitalWrite(l6, LOW);
  digitalWrite(l7, LOW);
  digitalWrite(l8, LOW);
  digitalWrite(buzzerPin, LOW);
  delay(100);
 }
}
