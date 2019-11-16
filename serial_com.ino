import "Arduino.h"

byte buf[80];
char sendArray[19] = {0x02, 0x10, 0x48, 0x5a, 0x58, 0x54, 0x53, 0x5a, 0x5a, 0x36, 0x32, 0x32, 0x32, 0x30, 0x31, 0x31, 0x01, 0x14, 0x1b};
int bytes_read;

void setup() {
    Serial.begin(1200);
}

void loop() {
    if(Serial.available() >= 5){
        bytes_read = Serial.readBytes(buf, 5);
        Serial.write(sendArray, 19);
        }
        delay(100);
}