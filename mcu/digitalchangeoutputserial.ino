
int buttons[] = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, A0, A1, A2, A3, A4, A5};
int num_buttons = 18;

int buttonstates[18]; 

void setup() {
  Serial.begin(9600);
  for(int current = 0; current < num_buttons; current++) {
    pinMode(buttons[current], INPUT);
    digitalWrite(buttons[current], HIGH);
  }
  delay(2000);
  for(int current = 0; current < num_buttons; current++) {
    buttonstates[current] = digitalRead(buttons[current]);
  }
  delay(1000);
}

void loop() {
  for(int current = 0; current < num_buttons; current++) {
    int update = digitalRead(buttons[current]);
    if(update != buttonstates[current]) {
      Serial.print(current);
      Serial.print(":");
      Serial.println(update);
      buttonstates[current] = update;
    }
  }
  delay(1);
}



