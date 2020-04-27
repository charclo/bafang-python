#include "Arduino.h"
#include <LiquidCrystal_I2C.h>

#define READ 0x11
#define WRITE 0x16
#define CONNECT 0x51
#define BASIC 0x52
#define PEDAL 0x53
#define THROTTLE 0x54

#define COMMAND_LENGTH 2
#define INFO_LENGTH 3

typedef enum app_states
{
    READ_COMMAND,
    READ_DATA,
    OTHER    
} State_t;

State_t state;



// Set the LCD address to 0x27 for a 16 chars and 2 line display
LiquidCrystal_I2C lcd(0x20, 20, 4);

unsigned char infoMessage[19] = {0x51, 0x10, 0x48, 0x5a, 0x58, 0x54, 0x53, 0x5a, 0x5a, 0x36, 0x32, 0x32, 0x32, 0x30, 0x31, 0x31, 0x01, 0x14, 0x1b};
unsigned char basicMessage[27] = {0x52, 0x18, 0x1F, 0x0F, 0x00, 0x1C, 0x25, 0x2E, 0x37, 0x40, 0x49, 0x52, 0x5B, 0x64, 0x64, 0x64, 0x64, 0x64, 0x64, 0x64, 0x64, 0x64, 0x64, 0x64, 0x34, 0x01, 0xDF};
unsigned char pedalMessage[14] = {0x53, 0x0B, 0x03, 0xFF, 0xFF, 0x64, 0x06, 0x14, 0x0A, 0x19, 0x08, 0x14, 0x14, 0x27};
unsigned char databuffer[40];
unsigned char commandbuffer[2];

/////////// FUNCTIONS ////////////////
void get_data(){
    if (commandbuffer[0] == READ){
        switch (commandbuffer[1])
        {   
        case CONNECT:
            read_bytes(INFO_LENGTH);
            printreceivedchar(databuffer, INFO_LENGTH);
            Serial.write(infoMessage, 19);
            break;
        case BASIC:
            Serial.write(basicMessage, 27);
            state = READ_COMMAND;
            break;
        case PEDAL:
            Serial.write(pedalMessage, 14);
            state = READ_COMMAND;
            break;
        default:
            break;
        }
    }
}

void read_bytes(int length){
    if (Serial.available() > length - 1)
    {
        Serial.readBytes(databuffer, length);
        state = READ_COMMAND;
    }
}

void read_command(){
    if (Serial.available() > 1){
        Serial.readBytes(commandbuffer, COMMAND_LENGTH);
        printreceivedchar(commandbuffer, COMMAND_LENGTH);
        state = READ_DATA;
    }
}

void printreceivedchar(unsigned char buffer[], int length){
    for(int i = 0; i<length; i++){
        if (buffer[i]<0x10)
            lcd.print("0");
        lcd.print(buffer[i], HEX);
        lcd.print(" ");
    }
}

void setup() {
    Serial.begin(1200);
    lcd.begin();
    lcd.backlight();

    state = READ_COMMAND;
}

void loop() {
    switch (state)
    {
    case READ_COMMAND:
        read_command();
        break;
    case READ_DATA:
        get_data();
        break;
    default:
        break;
    }
}