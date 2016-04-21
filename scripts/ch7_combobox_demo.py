#!/usr/bin/python

import java
import sys
import re
import jarray

from javax.swing import *
from java.awt import *
from java.lang import *
from java.awt.event import *

class ComboBoxDemo(java.lang.Runnable, ActionListener):
    def run(self):
        frame = JFrame('ComboBoxDemo', size = (200, 100), layout = FlowLayout(), defaultCloseOperation = JFrame.EXIT_ON_CLOSE)

        frame.add(JLabel('Pick one:'))
        choices = 'The,quick,brown,fox,jumped'.split(',')
        choices.extend('over,the,lazy,spam'.split(','))

        cb = frame.add(JComboBox(choices))
        cb.addActionListener(self)
        self.msg = frame.add(JLabel())
        frame.visible = 1

    def actionPerformed(self, event):
        cb = event.getSource()
        msg = 'Selection: ' + cb.getSelectedItem()
        self.msg.text = msg

if __name__ == '__main__':
    EventQueue.invokeLater(ComboBoxDemo())


    
    

