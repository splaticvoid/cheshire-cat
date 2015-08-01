/*UIInputSerializer

Reads input data from preset pins, assembles it into a message, and transmits it via serial line. 
*/

//Attributes
#define PIN_FREQ 0
#define PIN_MAXBRIGHT 1
#define PIN_SMOOTH 2


//Modes
#define PIN_MODE0 4
#define PIN_MODE1 5
#define PIN_MODE2 6
#define PIN_MODE3 7
#define PIN_PLAY 8
#define PIN_RANDOM 9

int waitTime 1000;
int freqVal = 0;
int brightVal = 0;
int smoothVal = 0;
bool[4] modes;
bool randomVal;
bool playVal;

String freqStr, brightStr, smoothStr, modeStr, playStr, randomStr, message, separator;

long debounceDelay = 50;

void setup() {
	//open serial port
	Serial.begin(115200);
	
	pinMode(PIN_MODE0, INPUT);
	pinMode(PIN_MODE1, INPUT);
	pinMode(PIN_MODE2, INPUT);
	pinMode(PIN_MODE3, INPUT);
	pinMode(PIN_PLAY, INPUT);
	pinMode(PIN_RANDOM, INPUT);
	
	message = "";
	separator = ",";
	
	freqStr = "frequency: ";
	brightStr = "brightness: ";
	smoothStr = "smoothness: ";
	modeStr = "mode: ";
	playStr = "play: ";
	randomStr = "random:  ";
	
}


void loop() {
	
	//read active attributes, modes, and behaviors
	int freqVal = analogRead(PIN_FREQ);
	int brightVal = analogRead(PIN_MAXBRIGHT);
	int smoothVal = analogRead(PIN_SMOOTH);
	
	modes[0] = (digitalRead(PIN_MODE0) == HIGH);
	modes[1] = (digitalRead(PIN_MODE1) == HIGH);
	modes[2] = (digitalRead(PIN_MODE2) == HIGH);
	modes[3] = (digitalRead(PIN_MODE3) == HIGH);

	play = (digitalRead(PIN_PLAY) == HIGH);
	random = (digitalRead(PIN_RANDOM) == HIGH);
	
	//assemble message
	int modeVal = modes[3]*8+modes[2]*4+modes[1]*2+modes[0]	;
	
	message = freqStr + freqVal;
	message = message + separator + brightStr + brightVal;
	message = message + separator + smoothStr + smoothVal;
	message = message + separator + modeStr + modeVal;
	message = message + separator + playStr + playVal;
	message = message + separator + randomStr + randomVal;
	
	//send message
	Serial.print(message);
	delay(waitTime);
}