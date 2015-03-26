#!/bin/env python3.4
# Lars Backer, Julius Sytstra, Guido Cnossen
# Gevorderd Programmeren

from PyQt4 import QtCore, QtGui

import sys

from random import random

from random import choice

class Cavern(QtGui.QWidget):
	
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self)
        self.setGeometry(1000, 1000, 1000, 1000)
        self.setWindowTitle('Hunt the Wumpus')
        
            
    def paintEvent(self, event): 
        
        self.paint = QtGui.QPainter()
        self.paint.begin(self)
        # black background
        self.paint.setBrush(QtCore.Qt.black)
        self.paint.drawRect(event.rect())
        
        # length and height of each room
        length = 250
        height = 160
        
        # 20 rooms that represent the cave
        room1 = self.paint.setPen(QtCore.Qt.white)
        room1 = self.paint.drawRect(1, 1, length, height)
        room1 = 1
        
        room2 = self.paint.setPen(QtCore.Qt.white)
        room2 = self.paint.drawRect(250, 1, length, height)
        room2 = 2
        
        room3 = self.paint.setPen(QtCore.Qt.white)
        room3 = self.paint.drawRect(500, 1, length, height)
        room3 = 3
        
        room4 = self.paint.setPen(QtCore.Qt.white)
        room4 = self.paint.drawRect(750, 1, length, height)
        room4 = 4 
        
        room5 = self.paint.setPen(QtCore.Qt.white)
        room5 = self.paint.drawRect(1, 160, length, height)
        room5 = 5 
        
        room6 = self.paint.setPen(QtCore.Qt.white)
        room6 = self.paint.drawRect(250, 160, length, height)
        room6 = 6
        
        room7 = self.paint.setPen(QtCore.Qt.white)
        room7 = self.paint.drawRect(500, 160, length, height)
        room7 = 7 
        
        room8 = self.paint.setPen(QtCore.Qt.white)
        room8 = self.paint.drawRect(750, 160, length, height)
        room8 = 8
        
        room9 = self.paint.setPen(QtCore.Qt.white)
        room9 = self.paint.drawRect(1, 320, length, height)
        room9 = 9
        
        room10 = self.paint.setPen(QtCore.Qt.white)
        room10 = self.paint.drawRect(250, 320, length, height)
        room10 = 10
        
        room11 = self.paint.setPen(QtCore.Qt.white)
        room11 = self.paint.drawRect(500, 320, length, height)
        room11 = 11
        
        room12 = self.paint.setPen(QtCore.Qt.white)
        room12 = self.paint.drawRect(750, 320, length, height)
        room12 = 12
        
        room13 = self.paint.setPen(QtCore.Qt.white)
        room13 = self.paint.drawRect(1, 480, length, height)
        room13 = 13
        
        room14 = self.paint.setPen(QtCore.Qt.white)
        room14 = self.paint.drawRect(250, 480, length, height)
        room14 = 14
        
        room15 = self.paint.setPen(QtCore.Qt.white)
        room15 = self.paint.drawRect(500, 480, length, height)
        room15 = 15
        
        room16 = self.paint.setPen(QtCore.Qt.white)
        room16 = self.paint.drawRect(750, 480, length, height)
        room16 = 16
        
        room17 = self.paint.setPen(QtCore.Qt.white)
        room17 = self.paint.drawRect(1, 640, length, height)
        room17 = 17
        
        room18 = self.paint.setPen(QtCore.Qt.white)
        room18 = self.paint.drawRect(250, 640, length, height)
        room18 = 18
        
        room19 = self.paint.setPen(QtCore.Qt.white)
        room19 = self.paint.drawRect(500, 640, length, height)
        room19 = 19
        
        room20 = self.paint.setPen(QtCore.Qt.white)
        room20 = self.paint.drawRect(750, 640, length, height)
        room20 = 20
        
        # in order to spawn the character randomly, choose a random number
        # that represents each room
        
        # determine each centerpoint of each room, which is the spawnpoint of 
        # the character
        
        room_numbers = range(1,21)
        spawn = choice(room_numbers)
        
        if spawn == 1:
            self.center_room = QtCore.QPoint((0.5 * length), (0.5 * height))
        if spawn == 2:
            self.center_room = QtCore.QPoint((1.5 * length), (0.5 * height))    
        if spawn == 3:
            self.center_room = QtCore.QPoint((2.5 * length), (0.5 * height))
        if spawn == 4:
            self.center_room = QtCore.QPoint((3.5 * length), (0.5 * height))
        if spawn == 5:
            self.center_room = QtCore.QPoint((0.5 * length), (1.5 * height))
        if spawn == 6:
            self.center_room = QtCore.QPoint((1.5 * length), (1.5 * height))    
        if spawn == 7:
            self.center_room = QtCore.QPoint((2.5 * length), (1.5 * height))
        if spawn == 8:
            self.center_room = QtCore.QPoint((3.5 * length), (1.5 * height))
        if spawn == 9:
            self.center_room = QtCore.QPoint((0.5 * length), (2.5 * height))
        if spawn == 10:
            self.center_room = QtCore.QPoint((1.5 * length), (2.5 * height))
        if spawn == 11:
            self.center_room = QtCore.QPoint((2.5 * length), (2.5 * height))
        if spawn == 12:
            self.center_room = QtCore.QPoint((3.5 * length), (2.5 * height))
        if spawn == 13:
            self.center_room = QtCore.QPoint((0.5 * length), (3.5 * height))
        if spawn == 14:
            self.center_room = QtCore.QPoint((1.5 * length), (3.5 * height))
        if spawn == 15:
            self.center_room = QtCore.QPoint((2.5 * length), (3.5 * height))
        if spawn == 16:
            self.center_room = QtCore.QPoint((3.5 * length), (3.5 * height))
        if spawn == 17:
            self.center_room = QtCore.QPoint((0.5 * length), (4.5 * height))
        if spawn == 18:
            self.center_room = QtCore.QPoint((1.5 * length), (4.5 * height))
        if spawn == 19:
            self.center_room = QtCore.QPoint((2.5 * length), (4.5 * height))
        if spawn == 20:
            self.center_room = QtCore.QPoint((3.5 * length), (4.5 * height))
        
        # create a character as a circle, which will be spawned randomly
        # in one of the rooms.
        self.radx = 25
        self.rady = 25    
        self.character = self.paint.setPen(QtCore.Qt.red)
        self.character = self.paint.drawEllipse(self.center_room, self.radx, self.rady)
        
        # create a screen under the room layout
        screen = self.paint.setPen(QtCore.Qt.green)
        screen = self.paint.drawRect(25, 825, 600, 150)
        
        # create 3 labels which will be used to show information during the game
        # it begins with a welcome message
        
        label1 = QtGui.QLabel("Welcome To Hunt The Wumpus", self)
        label1.move(50,840)
        label1.setStyleSheet('QLabel { font-size: 18pt; font-family: Calibri; color: white; }')
        label1.show()
        
        label2 = QtGui.QLabel("Enjoy Your Gametime", self)
        label2.move(50,890)
        label2.setStyleSheet('QLabel { font-size: 12pt; font-family: Calibri; color: white; }')
        label2.show()
        
        label3 = QtGui.QLabel("Made By Julius Sytstra, Guido Cnossen and Lars Backer", self)
        label3.move(50,940)
        label3.setStyleSheet('QLabel { font-size: 12pt; font-family: Calibri; color: white; }')
        label3.show()
        
        # create 4 buttons, which will be used to move the character 
        # trough different rooms
        button1 = QtGui.QPushButton("UP", self)
        button1.move(775, 850)
        button1.show()

        button2 = QtGui.QPushButton("DOWN", self)
        button2.move(775, 950)
        button2.show()
        
        button3 = QtGui.QPushButton("LEFT", self)
        button3.move(650, 900)
        button3.show()
        
        button4 = QtGui.QPushButton("RIGHT", self)
        button4.move(900, 900)
        button4.show()
                
        # connect the buttons to different functions
        button1.clicked.connect(self.buttonUpClicked)
        button2.clicked.connect(self.buttonDownClicked)
        button3.clicked.connect(self.buttonLeftClicked)
        button4.clicked.connect(self.buttonRightClicked)
        
        
    # create 4 function to determine what the different buttons do    
    def buttonUpClicked(self):
        # makes the player move a room upwards
        self.center_room = QtCore.QPoint((self.center_room.x()),(self.center_room.y() - 250))
        self.character = None
        self.character = self.paint.setPen(QtCore.Qt.red)
        self.character = self.paint.drawEllipse(self.center_room, self.radx, self.rady)
        
    def buttonDownClicked(self):
        # makes the player move a room downwards
        self.center_room = QtCore.QPoint((self.center_room.x()),(self.center_room.y() + 250))
        self.character = None
        self.character = self.paint.setPen(QtCore.Qt.red)
        self.character = self.paint.drawEllipse(self.center_room, self.radx, self.rady)
        
    def buttonLeftClicked(self):
        # makes the player move a room to the left
        self.center_room = QtCore.QPoint((self.center_room.x() - 160),(self.center_room.y()))
        self.character = None
        self.character = self.paint.setPen(QtCore.Qt.red)
        self.character = self.paint.drawEllipse(self.center_room, self.radx, self.rady)
        
    def buttonRightClicked(self):
        # makes the player move a room to the right
        self.center_room = QtCore.QPoint((self.center_room.x() + 160),(self.center_room.y()))
        self.character = None
        self.character = self.paint.setPen(QtCore.Qt.red)
        self.character = self.paint.drawEllipse(self.center_room, self.radx, self.rady)

        
if __name__=="__main__":
    
    app = QtGui.QApplication(sys.argv)
   
    ex = Cavern()
    ex.show()
    sys.exit(app.exec_())


