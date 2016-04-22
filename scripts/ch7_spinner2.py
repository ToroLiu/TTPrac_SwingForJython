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

class Spinner2(java.lang.Runnable):
    def run(self):
        self.frame = frame = JFrame(
            'Spinner2',
            layout = FlowLayout(),
            defaultCloseOperation = JFrame.EXIT_ON_CLOSE,
            )

        #daysOfWeek = [ dow for dow in DFS().getWeekdays() if dow]
        #data = daysOfWeek

        frame.add(JSpinner())
        frame.pack()
        frame.visible = 1

if __name__ == '__main__':
    EventQueue.invokeLater(Spinner2())


    
    

