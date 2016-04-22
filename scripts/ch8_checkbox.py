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

class CheckBoxes(java.lang.Runnable):
    def addCB(self, pane, text):
        pane.add(
            JCheckBox(
                text, itemStateChanged = self.toggle)
            )

    def run(self):
        frame = JFrame(
            'Check Boxes',
            layout = FlowLayout(),
            size = (250, 100),
            defaultCloseOperation = JFrame.EXIT_ON_CLOSE
            )

        cp = frame.getContentPane()
        self.addCB(cp, 'Yes')
        self.addCB(cp, 'No')
        self.addCB(cp, 'Maybe')
        self.label = frame.add(JLabel('Nothing selected'))
        frame.visible = 1

    def toggle(self, event):
        cb = event.getItem()
        text = cb.getText()
        state = ['No', 'Yes'][cb.isSelected()]
        self.label.text = '%s selected? %s' % (text, state)


if __name__ == '__main__':
    EventQueue.invokeLater(CheckBoxes())


