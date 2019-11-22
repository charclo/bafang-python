#include "Arduino.h"
#include <LiquidCrystal_I2C.h>

// Set the LCD address to 0x27 for a 16 chars and 2 line display
LiquidCrystal_I2C lcd(0x20, 20, 4);

unsigned char infoMessage[19] = {0x51, 0x10, 0x48, 0x5a, 0x58, 0x54, 0x53, 0x5a, 0x5a, 0x36, 0x32, 0x32, 0x32, 0x30, 0x31, 0x31, 0x01, 0x14, 0x1b};
unsigned char basicMessage[27] = {0x52, 0x18, 0x1F, 0x0F, 0x00, 0x1C, 0x25, 0x2E, 0x37, 0x40, 0x49, 0x52, 0x5B, 0x64, 0x64, 0x64, 0x64, 0x64, 0x64, 0x64, 0x64, 0x64, 0x64, 0x64, 0x34, 0x01, 0xDF};
unsigned char pedalMessage[14] = {0x53, 0x0B, 0x03, 0xFF, 0xFF, 0x64, 0x06, 0x14, 0x0A, 0x19, 0x08, 0x14, 0x14, 0x27};
int bytes_read;
byte test[80];
bool info_received = false;
unsigned char received_char;
unsigned char last_char;

void setup() {
    Serial.begin(1200);
    lcd.begin();
    lcd.backlight();
}

void loop() {
    if (Serial.available() > 0){
        received_char = Serial.read();
        switch(received_char)
        {
        case 0x11:
            lcd.print(received_char, HEX);
            lcd.print(" ");
            break;
        case 0x51:
            lcd.print(received_char, HEX);
            lcd.print(" ");
            break;
        case 0x52:
            lcd.print(received_char, HEX);
            lcd.print(" ");
            if (last_char == 0x11)
            {
                Serial.write(basicMessage, 27);
            }
            break;
        case 0x53:
            lcd.print(received_char, HEX);
            lcd.print(" ");
            if (last_char == 0x11)
            {
                Serial.write(pedalMessage, 14);
            }
            // else
            // {
            //     /* code */
            // }
            break;
        case 0x04:
            lcd.print(received_char, HEX);
            lcd.print(" ");
            break;
        case 0xb0:
            lcd.print(received_char, HEX);
            lcd.print(" ");
            break;
        case 0x05:
            lcd.print(received_char, HEX);
            lcd.print(" ");
            if (last_char == 0xB0)
            {
                Serial.write(infoMessage, 19);
                lcd.clear();
            }
            break;
        default:
            lcd.print(received_char, HEX);
            lcd.print(" ");
            break;  
        }
        last_char = received_char;
    }
          

}