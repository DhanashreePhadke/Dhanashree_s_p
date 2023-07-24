const int trigPin = 4;
const int echoPin = 7;
const int buzzPin = 11;

long duration;
float distance;

void setup() 
{
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT); 
  pinMode(buzzPin, OUTPUT);
}

void loop() 
{
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);
  distance = 0.034*(duration/2);
  
 if (distance==100 && distance<66 )
 {
   tone(buzzPin, 2000, 50);
   delay (1000);
   Serial.println("object is at distance greater than 66 and distance is");
   Serial.println(distance);
  }
 if (distance < 66 && distance>33)
  {
   tone(buzzPin, 2000, 70);
   delay (100);
   Serial.println("object is at distance greater than 33 and distance is");
   Serial.println(distance); 
  }
 if (distance < 33 && distance>0)
  {
   tone(buzzPin, 2000, 500);
   delay (10);
   Serial.println("object is at distance lesser than 33 and distance is");
   Serial.println(distance);   
    }

}