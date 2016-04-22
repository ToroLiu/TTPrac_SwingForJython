#!/usr/bin/python

import java
import sys
import re
import jarray

from javax.swing import *
from java.awt import *
from java.lang import *
from java.awt.event import *
from java.text import *

class FormattedTextFieldDemo(java.lang.Runnable, ActionListener):
    def addFTF(self, name):
        pane = self.frame.getContentPane()
        pane.add(JLabel(name))
        pane.add(
            JFormattedTextField(
                eval('NumberFormat.' + name),
                value = 12345.67890,
                columns = 10
                )
            )

    def run(self):
        self.frame = frame = JFrame(
            'FormattedTextFieldDemo',
            layout = GridLayout(0, 2),
            defaultCloseOperation = JFrame.EXIT_ON_CLOSE
            )

        self.addFTF('getInstance()')
        self.addFTF('getCurrencyInstance()')
        self.addFTF('getIntegerInstance()')
        self.addFTF('getNumberInstance()')
        self.addFTF('getPercentInstance()')
        frame.pack()
        frame.visible = 1

if __name__ == '__main__':
    EventQueue.invokeLater(FormattedTextFieldDemo())


    
    

