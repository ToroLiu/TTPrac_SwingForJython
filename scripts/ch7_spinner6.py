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

class Spinner3(java.lang.Runnable):
    def run(self):
        self.frame = frame = JFrame(
            'Spinner2',
            layout = FlowLayout(),
            defaultCloseOperation = JFrame.EXIT_ON_CLOSE,
            )

        model = SpinnerDateModel(
            Date(2000, 2, 1), # zero origin month
            None,   # minimum
            None,   # maximum
            Calendar.DAY_OF_MONTH   # Ignored by GUI
            )

        spinner = JSpinner(model)
        spinner.setEditor(
            JSpinner.DateEditor(
                spinner, 'dd MMM yy'
            )
        )
        frame.add(spinner)
        frame.pack()
        frame.visible = 1

if __name__ == '__main__':
    EventQueue.invokeLater(Spinner3())


    
    

