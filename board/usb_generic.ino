#include <Practicum.h>

extern "C" {
#include "usbdrv.h"
}

#define RQ_GET_SWITCH_UP 4
#define RQ_GET_SWITCH_DOWN 1
#define RQ_GET_SWITCH_LEFT 3
#define RQ_GET_SWITCH_RIGHT 5
#define RQ_GET_SWITCH_BOMB 0
#define RQ_GET_LIGHT  2

//////////////////////////////////////////////////////////////////////
usbMsgLen_t usbFunctionSetup(uint8_t data[8])
{
  usbRequest_t *rq = (usbRequest_t*)data;
  static uint8_t switch_up_state;  /* must stay when usbFunctionSetup returns */
  static uint8_t switch_down_state;  /* must stay when usbFunctionSetup returns */
  static uint8_t switch_left_state;  /* must stay when usbFunctionSetup returns */
  static uint8_t switch_right_state;  /* must stay when usbFunctionSetup returns */
  static uint8_t switch_bomb_state;  /* must stay when usbFunctionSetup returns */
  static uint16_t light_state;  /* must stay when usbFunctionSetup returns */

  if (rq->bRequest == RQ_GET_SWITCH_UP)
  {
    if (digitalRead(PIN_PC4) == LOW) /* switch is pressed */
      switch_up_state = 1;
    else
      switch_up_state = 0;

    /* point usbMsgPtr to the data to be returned to host */
    usbMsgPtr = (uint8_t*) &switch_up_state;

    /* return the number of bytes of data to be returned to host */
    return sizeof(switch_up_state);
  }

  else if (rq->bRequest == RQ_GET_SWITCH_DOWN)
  {
    if (digitalRead(PIN_PC1) == LOW) /* switch is pressed */
      switch_down_state = 1;
    else
      switch_down_state = 0;

    /* point usbMsgPtr to the data to be returned to host */
    usbMsgPtr = (uint8_t*) &switch_down_state;

    /* return the number of bytes of data to be returned to host */
    return sizeof(switch_down_state);
  }

  else if (rq->bRequest == RQ_GET_SWITCH_LEFT)
  {
    if (digitalRead(PIN_PC3) == LOW) /* switch is pressed */
      switch_left_state = 1;
    else
      switch_left_state = 0;

    /* point usbMsgPtr to the data to be returned to host */
    usbMsgPtr = (uint8_t*) &switch_left_state;

    /* return the number of bytes of data to be returned to host */
    return sizeof(switch_left_state);
  }

  else if (rq->bRequest == RQ_GET_SWITCH_RIGHT)
  {
    if (digitalRead(PIN_PC5) == LOW) /* switch is pressed */
      switch_right_state = 1;
   else
      switch_right_state= 0;

    /* point usbMsgPtr to the data to be returned to host */
    usbMsgPtr = (uint8_t*) &switch_right_state;

    /* return the number of bytes of data to be returned to host */
    return sizeof(switch_right_state);
  }

  else if (rq->bRequest == RQ_GET_SWITCH_BOMB)
  {
    if (digitalRead(PIN_PC0) == LOW) /* switch is pressed */
      switch_bomb_state = 1;
    else
      switch_bomb_state = 0;

    /* point usbMsgPtr to the data to be returned to host */
    usbMsgPtr = (uint8_t*) &switch_bomb_state;

    /* return the number of bytes of data to be returned to host */
    return sizeof(switch_bomb_state);
  }

  else if (rq->bRequest == RQ_GET_LIGHT)
  {
    light_state = analogRead(PIN_PC2);

    /* point usbMsgPtr to the data to be returned to host */
    usbMsgPtr = (uint8_t*) &light_state;

    /* return the number of bytes of data to be returned to host */
    return sizeof(light_state);
  }

  return 0;   /* nothing to do; return no data back to host */
}

//////////////////////////////////////////////////////////////////////
void setup()
{
    pinMode(PIN_PC4, INPUT_PULLUP); // Up
    pinMode(PIN_PC1, INPUT_PULLUP); // Down
    pinMode(PIN_PC3, INPUT_PULLUP); // Left
    pinMode(PIN_PC5, INPUT_PULLUP); // Right
    pinMode(PIN_PC0, INPUT_PULLUP); // Bomb
    pinMode(PIN_PC2, INPUT); // Light
    pinMode(PIN_PD3, OUTPUT);

    usbInit();

    /* enforce re-enumeration of USB devices */
    usbDeviceDisconnect();
    delay(300);
    usbDeviceConnect();
}

//////////////////////////////////////////////////////////////////////
void loop()
{
  usbPoll();
}
