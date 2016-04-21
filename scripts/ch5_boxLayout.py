#!/usr/bin/python

import java
import sys

from javax.swing import *
from java.awt import *
from java.lang import *

class BoxLayoutDemo(java.lang.Runnable):
    def run(self):
        frame = JFrame(
            'BoxLayoutDemo',
            defaultCloseOperation = JFrame.EXIT_ON_CLOSE
        )
        
        self.addTabs(frame.getContentPane())
        frame.size = (300, 175)
        frame.visible = 1

    def addTabs(self, container):
        align = [
            ['Left', Component.LEFT_ALIGNMENT ],
            ['Center', Component.CENTER_ALIGNMENT ],
            ['Right', Component.RIGHT_ALIGNMENT ],
        ]

        names = '1,2,3 being the third number'.split(',')
        tabs = JTabbedPane()
        for aName, aConst in align:
            tab = JPanel()
            tab.setLayout(BoxLayout(tab, BoxLayout.Y_AXIS))
            for name in names:
                tab.add( JButton(name, alignmentX = aConst))

            tabs.addTab(aName, tab)

        container.add(tabs)

if __name__ == '__main__':
    EventQueue.invokeLater(BoxLayoutDemo())


    
    

