/*UIInputSerializer

Reads input data from preset pins, assembles it into a message, and transmits it via serial line. 
*/
//Attributes

const int PIN_FREQ = 0;
const int PIN_MAXBRIGHT = 1;
const int PIN_SMOOTH = 2;
const int PIN_MODE0 = 4;
const int PIN_MODE1 = 5;
const int PIN_MODE2 = 6;
const int PIN_MODE3 = 7;
const int PIN_PLAY = 8;
const int PIN_RANDOM = 9;

int waitTime = 500;
int freqVal = 0.5;
int brightVal = 255;
int smoothVal = 16;

boolean modes[4];
boolean randomVal;
boolean playVal;
String freqStr, brightStr, smoothStr, modeStr, playStr, randomStr, message, separator, startterm, endterm;

long debounceDelay = 50;

void setup() {
  // put your setup code here, to run once:
  //open serial port
  Serial.begin(9600);
  
  pinMode(PIN_MODE0, INPUT);
  pinMode(PIN_MODE1, INPUT);
  pinMode(PIN_MODE2, INPUT);
  pinMode(PIN_MODE3, INPUT);
  pinMode(PIN_PLAY, INPUT);
  pinMode(PIN_RANDOM, INPUT);

  message = "";
  separator = ",";
  startterm = "{";
  endterm = "}";
  
  freqStr = "frequency:";
  brightStr = "brightness:";
  smoothStr = "smoothness:";
  modeStr = "mode:";
  playStr = "play:";
  randomStr = "random:";
}

void loop() {
  // put your main code here, to run repeatedly:
 //read active attributes, modes, and behaviors
  freqVal = analogRead(PIN_FREQ);
  brightVal = analogRead(PIN_MAXBRIGHT);
  smoothVal = analogRead(PIN_SMOOTH);
  
  modes[0] = (digitalRead(PIN_MODE0) == HIGH);
  modes[1] = (digitalRead(PIN_MODE1) == HIGH);
  modes[2] = (digitalRead(PIN_MODE2) == HIGH);
  modes[3] = (digitalRead(PIN_MODE3) == HIGH);

  playVal = (digitalRead(PIN_PLAY) == HIGH);
  randomVal = (digitalRead(PIN_RANDOM) == HIGH);
  
  //assemble message
  int modeVal = modes[3]*8+modes[2]*4+modes[1]*2+modes[0] ;
  
  message = startterm + freqStr + String(freqVal);
  message = message + separator + brightStr + String(brightVal);
  message = message + separator + smoothStr + String(smoothVal);
  message = message + separator + modeStr + String(modeVal);
  message = message + separator + playStr + String(playVal);
  message = message + separator + randomStr + String(randomVal) + endterm;
  
  //send message
  Serial.println(message);
  delay(waitTime);
}
