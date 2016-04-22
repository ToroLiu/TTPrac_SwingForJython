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
from java.text import DateFormatSymbols as DFS
from java.util import *

class ToggleButton(java.lang.Runnable):
    def run(self):
        self.frame = frame = JFrame(
            'Toggle Button',
            layout = FlowLayout(),
            size = (275, 85),
            defaultCloseOperation = JFrame.EXIT_ON_CLOSE,
            )

        button = JToggleButton(
            'Off',                         # Initial button text
            itemStateChanged = self.toggle # Event handler
            )
        frame.add(button)
        frame.visible = 1

    def toggle(self, event):
        button = event.getItem()
        button.text = ['Off', 'On'][button.isSelected()]

if __name__ == '__main__':
    EventQueue.invokeLater(ToggleButton())


    
    

