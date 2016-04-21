#!/usr/bin/python

import java
import sys
import re
import jarray

from javax.swing import *
from java.awt import *
from java.lang import *

class PasswordDemo(java.lang.Runnable):
    def run(self):
        frame = JFrame(
        	'PasswordDemo', 
            size = (215, 120),
        	layout = FlowLayout(),
        	defaultCloseOperation = JFrame.DISPOSE_ON_CLOSE
        	)
        frame.add(JLabel("Password:"))
        self.pwd = frame.add(
            JPasswordField(
                10, 
                actionCommand = 'Submit',
                actionPerformed = self.enter
            )
        )
        frame.add(JButton('Show', actionPerformed = self.showHide))
        frame.add(JButton('Submit'))

        self.msg = frame.add(JLabel())
        self.echoChar = '*'
        frame.visible = 1

    def enter(self, event):
        print 'ActionCommand: "%s"' % event.getActionCommand()
        pwd = self.pwd.getPassword()
        if pwd == jarray.array('test', 'c'):
            result = 'correct'
        else:
            result = 'wrong!'
        self.msg.setText('Password is %s' % result)

    def showHide(self, event):
        button = event.getSource()
        if button.getText() == 'Show':
            self.pwd.setEchoChar(chr(0))
            button.setText('Hide')
        else:
            self.pwd.setEchoChar(self.echoChar)
            button.setText('Show')

if __name__ == '__main__':
    EventQueue.invokeLater(PasswordDemo())


    
    

