#!/usr/bin/python

import java
import sys
import re

from javax.swing import *
from java.awt import *
from java.lang import *

class AvailableFonts(java.lang.Runnable):
    def run(self):
        frame = JFrame('Available Fonts', defaultCloseOperation = JFrame.DISPOSE_ON_CLOSE)

        lge = GraphicsEnvironment.getLocalGraphicsEnvironment()
        fontNames = lge.getAvailableFontFamilyNames()
        frame.add(
            JScrollPane(
                JTextArea(
                    '\n'.join(fontNames),
                    editable = 0,
                    rows = 8,
                    columns = 32
                )
            )
        )
        frame.pack()
        frame.visible = 1

if __name__ == '__main__':
    EventQueue.invokeLater(AvailableFonts())


    
    

