/*UIInputSerializer

Reads input data from preset pins, assembles it into a message, and transmits it via serial line. 
*/

const int PIN_FREQ = 0;
const int PIN_MAXBRIGHT = 1;
const int PIN_SMOOTH = 2;
const int PIN_MODE0 = 4;
const int PIN_MODE1 = 5;
const int PIN_MODE2 = 6;
const int PIN_MODE3 = 7;
const int PIN_PLAY = 8;
const int PIN_RANDOM = 9;

int waitTime, freqVal, brightVal, smoothVal;
int freqVal;
int brightVal;
int smoothVal;
boolean modes[4];
boolean randomVal;
boolean playVal;

String freqStr, brightStr, smoothStr, modeStr, playStr, randomStr, message, separator;

long debounceDelay = 50;

void setup() {

  
}


void loop() {
  
 
}
