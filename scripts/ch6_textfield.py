#!/usr/bin/python

import java
import sys
import re

from javax.swing import *
from java.awt import *
from java.lang import *

timeout = "30"
def getTimeout():
    return timeout

def setTimeout(value):
    timeout = value
    return "Successfully modified."

class consoleTimeout1(Runnable):
    def run(self):
        frame = JFrame('Console timeout', defaultCloseOperation = JFrame.EXIT_ON_CLOSE)

        cp = frame.getContentPane()
        cp.setLayout(BoxLayout( cp, BoxLayout.Y_AXIS))

        input = JPanel(layout = FlowLayout())
        input.add(JLabel('Timeout:'))
        self.text = JTextField(3, actionPerformed = self.update )

        input.add(self.text)
        self.text.setText(getTimeout())

        input.add(JLabel('minutes'))
        cp.add(input)

        self.msg = cp.add(JLabel())

        frame.size = (290, 100)
        frame.visible = 1

    def update(self, event):
        value = self.text.getText().strip()
        if re.search('^\d+$', value):
            self.msg.setText(setTimeout(value))
        else:
            msg = 'Invalid value "%s" ignored.' % value
            self.msg.setText(msg)
            self.text.setText(getTimeout())

if __name__ == '__main__':
    EventQueue.invokeLater(consoleTimeout1())


    
    

