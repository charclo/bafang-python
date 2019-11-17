#include "Arduino.h"
#include <LiquidCrystal_I2C.h>

// Set the LCD address to 0x27 for a 16 chars and 2 line display
LiquidCrystal_I2C lcd(0x20, 20, 4);

char sendArray[19] = {0x51, 0x10, 0x48, 0x5a, 0x58, 0x54, 0x53, 0x5a, 0x5a, 0x36, 0x32, 0x32, 0x32, 0x30, 0x31, 0x31, 0x01, 0x14, 0x1b};
int bytes_read;
byte test[80];

void setup() {
    Serial.begin(1200);
    lcd.begin();
	lcd.backlight();
}

void loop() {
    if(Serial.available() >= 5){
        bytes_read = Serial.readBytes(test, 5);
        Serial.write(sendArray, 19);
        
        lcd.clear();
        lcd.print(bytes_read);
        lcd.print(" bytes:");
        lcd.setCursor(0, 1);
        for (int i=0; i < bytes_read; i++){
          lcd.print(test[i], HEX);
          lcd.print(" ");
        }
        
        }
}
