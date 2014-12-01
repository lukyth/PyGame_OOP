from practicum import McuBoard

RQ_GET_SWITCH_UP = 4
RQ_GET_SWITCH_DOWN = 1
RQ_GET_SWITCH_LEFT = 3
RQ_GET_SWITCH_RIGHT = 5
RQ_GET_SWITCH_BOMB = 0
RQ_GET_LIGHT  = 2

# from practicum import *
# from peri import PeriBoard
# devs = findDevices()
# b = PeriBoard(devs[0])

####################################
class PeriBoard(McuBoard):

    ################################
    def getSwitchUp(self):
        '''
        Return a boolean value indicating whether the switch on the peripheral
        board is currently pressed
        '''
        if (self.usbRead(request = RQ_GET_SWITCH_UP, length = 1)[0] == 1):
            return True
        return False

    ################################
    def getSwitchDown(self):
        '''
        Return a boolean value indicating whether the switch on the peripheral
        board is currently pressed
        '''
        if (self.usbRead(request = RQ_GET_SWITCH_DOWN, length = 1)[0] == 1):
            return True
        return False

    ################################
    def getSwitchLeft(self):
        '''
        Return a boolean value indicating whether the switch on the peripheral
        board is currently pressed
        '''
        if (self.usbRead(request = RQ_GET_SWITCH_LEFT, length = 1)[0] == 1):
            return True
        return False

    ################################
    def getSwitchRight(self):
        '''
        Return a boolean value indicating whether the switch on the peripheral
        board is currently pressed
        '''
        if (self.usbRead(request = RQ_GET_SWITCH_RIGHT, length = 1)[0] == 1):
            return True
        return False

    ################################
    def getSwitchBomb(self):
        '''
        Return a boolean value indicating whether the switch on the peripheral
        board is currently pressed
        '''
        if (self.usbRead(request = RQ_GET_SWITCH_BOMB, length = 1)[0] == 1):
            return True
        return False

    ################################
    def getLight(self):
        '''
        Return the current reading of light sensor on peripheral board
        '''
        return self.usbRead(request = RQ_GET_LIGHT, length = 2)[0] + (self.usbRead(request = RQ_GET_LIGHT, length = 2)[1] * 256)
