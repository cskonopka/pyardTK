void setup(){
  // Setup serial port 
  Serial.begin(9600);
}

void loop(){

  // Tap and receive a single stream from the serial port
  int8_t inner = Serial.parseInt();

  // Receive the data from the button press
  // The flush orientation is what enabled singular button presses to
  // work otherwise you need to double click and a value gets stuck
  // in the buffer. This has proven to be the most efficient setup for 
  // the current design parameters. The delays are needed to create 
  // enough space for data to travel and not clog the pipe. If you 
  // wanted a faster reaction time the delay messages is what you would 
  // play around with but beware, it can clog up fast.
  if (inner == 1){
    Serial.print('1',DEC);
    Serial.flush();
    delay(0.1);
    Serial.flush();    
  }
  if (inner == 2){
    Serial.print('2',DEC);
    Serial.flush();
    delay(0.1);
    Serial.flush();
  }
  Serial.flush();
  delay(1);
}
