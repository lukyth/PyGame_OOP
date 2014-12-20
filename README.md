Bomber Board
==========
A 2D game similar to Bomberman with background color changable, obstacle movable and MCU controller.

This is a project in "Practicum for Computer Engineering" (01204223), Department of Computer Engineering, Faculty of Engineering, Kasetsart University, First Semister 2014


Files Description
------
|   Files/Folders       |          Description                   |
| --------------------- | -------------------------------------- |
| main.py               | main scene class                       |
| element.py            | game object class (Player, Bomb, Wall) |
| gamelib.py            | game class                             |
| img/                  | images used in game                    |
| sound/                | sounds used in game                    |
| board/usb_generic.ino | MCU Board controller script            |
| board/practicum.py    | MCU Board basic function               |
| board/peri.py         | MCU Board function to get input        |
| board/test-usb.py     | board tester script                    |


Require
------
* [Arduino Makefile](https://github.com/sudar/Arduino-Makefile)
* [V-USB](http://www.obdev.at/products/vusb/)
* [libusb](http://www.libusb.org/)
* [PyUSB](http://walac.github.io/pyusb/)
* [Pygame](http://www.pygame.org/)
* [MCU Board](http://theory.cpe.ku.ac.th/wiki/images/Mcu-schematic.jpg)


Contributors
------
* Kanitkorn Sujautra 5610500311
* Worathon Wuttisakulchai 5610503957
