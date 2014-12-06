// Pin 13 has an LED connected on most Arduino boards.
// give it a name:
int led = 13;

int rr = 2;

// the setup routine runs once when you press reset:
void setup() {                
  // initialize the digital pin as an output.
  Serial.begin(9600);
  pinMode(led, OUTPUT);
  pinMode(rr, INPUT);
  
}

void tube_impulse(){               //procedure for capturing events from Geiger Kit

    digitalWrite(13, HIGH);
    Serial.println('0');
    digitalWrite(13, LOW);
 
}
// the loop routine runs over and over again forever:
void loop() {
  
  
  int buttonState = digitalRead(rr);
  if (buttonState==0) {
  // print out the state of the button:
    digitalWrite(13, HIGH);
    Serial.println('0');
    digitalWrite(13, LOW);
    buttonState=1;
    delay(10);
  }

}
