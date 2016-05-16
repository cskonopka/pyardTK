//
//String inputString = "";         // a string to hold incoming data
//boolean stringComplete = false; 
//
//void setup() 
//{ 
//  //  Create/open serial port
//    Serial.begin(9600);   
//      inputString.reserve(200);
//}
//
//void loop() 
//{
//int j =1;
// while (j==1){
//  Serial.write(12);
// }
////   while (Serial.available()) {
////    // get the new byte:
////    char inChar = (char)Serial.read(); 
////    // add it to the inputString:
////    inputString += inChar;
////    Serial.println(inChar);
////    Serial.println(inputString);
////    // if the incoming character is a newline, set a flag
////    // so the main loop can do something about it:
////    if (inChar == '\n') {
////      stringComplete = true;
////    } 
////          Serial.println(10);
////  }
////    if (stringComplete) {
////    Serial.println(inputString); 
//////    Serial.write('hello');
////    // clear the string:
////    inputString = "";
////    stringComplete = false;
//////          Serial.println(10);
////  }
////        Serial.write(10);
//}

  int cupcake = 1;
void setup(){
  Serial.begin(9600);

}

void loop(){

//while (cupcake == 1){
  int8_t inner = Serial.parseInt();


  if (inner == 1){
    Serial.print('1',DEC);
    Serial.flush();
//    Serial.println(' ');
    delay(0.1);
    Serial.flush();    

  }
  if (inner == 2){
    Serial.print('2',DEC);
    Serial.flush();
//    Serial.println(' ');
    delay(0.1);
    Serial.flush();

  }
  Serial.flush();
  delay(1);

  
//}
  
}
