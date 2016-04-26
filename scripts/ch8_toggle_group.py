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

class ButtonGroupDemo(java.lang.Runnable):
    def addRB(self, pane, bg, text):
        bg.add(
            pane.add(
                JToggleButton(text, selected = (text == '1'), itemStateChanged = self.toggle)
                )
            )

    def run(self):
        frame = JFrame(
            'Radio Buttons',
            layout = FlowLayout(),
            size = (250, 100),
            defaultCloseOperation = JFrame.EXIT_ON_CLOSE
            )

        cp = frame.getContentPane()
        bg = ButtonGroup() # A Group for radio buttons

        for i in range(1, 6):
            self.addRB(cp, bg, `i`)
        
        self.label = frame.add(JLabel('Selection: 1'))
        frame.visible = 1

    def toggle(self, event):
        text = event.getItem().getText()
        self.label.text = 'Selection: %s' % text


if __name__ == '__main__':
    EventQueue.invokeLater(ButtonGroupDemo())


