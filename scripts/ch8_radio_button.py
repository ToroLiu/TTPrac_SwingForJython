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

class RadioButtonDemo(java.lang.Runnable):
    def addRB(self, pane, bg, text):
        bg.add(
            pane.add(
                JRadioButton(text, itemStateChanged = self.toggle)
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
        self.addRB(cp, bg, 'Yes')
        self.addRB(cp, bg, 'No')
        self.addRB(cp, bg, 'Maybe')
        self.label = frame.add(JLabel('Nothing selected'))
        frame.visible = 1

    def toggle(self, event):
        text = event.getItem().getText()
        self.label.text = 'Selection: %s' % text


if __name__ == '__main__':
    EventQueue.invokeLater(RadioButtonDemo())


