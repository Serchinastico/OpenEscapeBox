#include <Keypad.h>

const byte numRows = 4; //number of rows on the keypad
const byte numCols = 4; //number of columns on the keypad

char keymap[numRows][numCols] =
    {
        {'1', '2', '3', 'A'},
        {'4', '5', '6', 'B'},
        {'7', '8', '9', 'C'},
        {'*', '0', '#', 'D'}};

byte colPins[numRows] = {6, 7, 8, 9}; //Rows 0 to 3
byte rowPins[numCols] = {5, 4, 3, 2}; //Columns 0 to 3

Keypad keypad = Keypad(makeKeymap(keymap), rowPins, colPins, numRows, numCols);

void setup()
{
    Serial.begin(9600);
}

void loop()
{
    char key = keypad.getKey();
    if (key != NO_KEY)
    {
        Serial.print(key);
    }
}
