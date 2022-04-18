int x,y,z,roll;
int prev = 0;
const int relay_3v3_pin=3;
void setup() {
pinMode(relay_3v3_pin,OUTPUT);
Serial.begin(9600);
}

void loop() {
x = analogRead(A0);
y = analogRead(A1);
z = analogRead(A2);

roll = ( ( (atan2(y,z) * 180) / 3.14 ) + 180 );

if (roll==prev)
  { digitalWrite(relay_3v3_pin, LOW);
  Serial.print('0');
  delay(300);
} else {
  prev=roll;
  digitalWrite(relay_3v3_pin, HIGH);
  Serial.print('1');
  delay(10);
}
delay(200);
}
