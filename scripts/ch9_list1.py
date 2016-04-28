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

class List1(java.lang.Runnable):
    def run(self):
        frame = JFrame(
            'List1',
            size = (250, 200),
            defaultCloseOperation = JFrame.EXIT_ON_CLOSE
            )

        data = 'Now is the time for all good spam'.split(' ')
        frame.add(JList(data))
        frame.visible = 1

if __name__ == '__main__':
    EventQueue.invokeLater(List1())


