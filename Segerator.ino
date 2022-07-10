#include <cvzone.h>
#include <AFMotor.h>

AF_DCMotor motor1(2);
SerialData serialData(1,1);
int valsRec[2];

void setup() {
  // put your setup code here, to run once:
  serialData.begin();
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  serialData.Get(valsRec);
  if(valsRec[0]){
     motor1.setSpeed(50);
     motor1.run(FORWARD);
     Serial.write('hi');
     delay(3000);
     motor1.setSpeed(50);
     motor1.run(BACKWARD);
  };
}
