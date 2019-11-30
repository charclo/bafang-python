#include "Arduino.h"
#include <LiquidCrystal_I2C.h>

#define READ 0x11
#define WRITE 0x16
#define CONNECT 0x51
#define BASIC 0x52
#define PEDAL 0x53
#define THROTTLE 0x54

#define COMMANDLENGTH 2
#define INFOLENGTH 3

typedef enum app_states
{
    READINGCOMMAND,
    GETTINGDATA,
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
int i = 0;
unsigned char received_char;
bool getting_commands;

/////////// FUNCTIONS ////////////////
void get_data(){
    if (commandbuffer[0] == READ){
        switch (commandbuffer[1])
        {   
        case CONNECT:
            read_bytes(INFOLENGTH);
            printreceivedchar(databuffer);
            Serial.write(infoMessage, 19);
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
        state = READINGCOMMAND;
    }
}

void read_command(){
    if (Serial.available() > 1){
        Serial.readBytes(commandbuffer, COMMANDLENGTH);
        printreceivedchar(commandbuffer);
        state = GETTINGDATA;
    }
}

void printreceivedchar(unsigned char * buffer){
    int bytes_written = lcd.write(*buffer);
    lcd.print(" bytes written: ");
    lcd.print(bytes_written);

    // if (received_char<0x10)
    // {
    //     lcd.print("0");
    // }
    // lcd.print(received_char, HEX);
    // lcd.print(" ");
}

void setup() {
    Serial.begin(1200);
    lcd.begin();
    lcd.backlight();

    state = READINGCOMMAND;
}

void loop() {
    switch (state)
    {
    case READINGCOMMAND:
        read_command();
        break;
    case GETTINGDATA:
        get_data();
        break;
    default:
        break;
    }

    // switch (received_char)
    // {
    //     case READ:
    //     case WRITE:
    //         buffer[i] = received_char;
    //         i++;
    //         break;
    //     case CONNECT:
    //         if (i>0)
    //         {
    //             if (buffer[i-1] == READ)
    //             {
    //                 Serial.write(infoMessage, 19);
    //                 i = 0;
    //                 // lcd.clear();
    //             }
    //         }
    //         break;
    //     case BASIC:
    //         if (i>0)
    //         {
    //             if (buffer[i-1] == WRITE)
    //             {
    //                 // send back succes
    //                 i = 0;
    //             }
    //             else if (buffer[i-1] == READ)
    //             {
    //                 Serial.write(basicMessage, 27);
    //                 i = 0;
    //                 getting_commands = false;
    //                 // lcd.clear();
    //             }
    //         }
    //         break;
    //     case PEDAL:
    //         if (i>0)
    //         {
    //             if (buffer[i-1] == WRITE)
    //             {
    //                 // send back succes
    //                 i = 0;
    //             }
    //             else if (buffer[i-1] == READ)
    //             {
    //                 Serial.write(pedalMessage, 14);
    //                 i = 0;
    //             }
    //         }
    //         break;
    //     default:
    //         break;
   // }
}