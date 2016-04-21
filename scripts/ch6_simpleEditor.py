#!/usr/bin/python

import java
import sys
import re

from javax.swing import *
from java.awt import *
from java.lang import *

class SimpleEditor(java.lang.Runnable):
    def run(self):
        frame = JFrame(
        	'Simple Editor', 
        	layout = BorderLayout(),
        	defaultCloseOperation = JFrame.DISPOSE_ON_CLOSE
        	)

        self.area = JTextArea(
        	rows = 8,
        	columns = 32,
        	caretUpdate = self.caretUpdate
        )
        frame.add(JScrollPane(self.area), BorderLayout.CENTER)
        self.words = JLabel('# words: 0 # lines: 0')
        frame.add(self.words, BorderLayout.SOUTH)

        frame.pack()
        frame.visible = 1

    def caretUpdate(self, event, regexp = None):
    	if not regexp:
    		regexp = re.compile('\W+', re.MULTILINE)
    	pos = event.getDot()
    	text = self.area.getText()

    	if text.strip() == '':
    		words = lines = 0
    	else:
    		words = len(re.split(regexp, text))
    		lines = len(text.splitlines())

    	msg = '# words:%d # lines: %d' % (words, lines)
    	self.words.setText(msg)

if __name__ == '__main__':
    EventQueue.invokeLater(SimpleEditor())


    
    

