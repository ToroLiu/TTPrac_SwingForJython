#!/usr/bin/python

import java
import sys
import re
import jarray

from javax.swing import *
from java.awt import *
from java.lang import *
from java.awt.event import *

class DynamicComboBox(java.lang.Runnable, ActionListener):
    def run(self):
        frame = JFrame(
            'DynamicComboBox', 
            size = (310, 137), 
            layout = BorderLayout(), 
            defaultCloseOperation = JFrame.EXIT_ON_CLOSE
            )

        # North Panel
        panel = JPanel()
        panel.add(JLabel('Pick one'))
        self.choices = 'The,quick,brown,fox,jumped'.split(',')
        self.choices.extend('over,the,lazy,spam'.split(','))
        self.ComboBox = ComboBox = JComboBox(self.choices, editable = 1)
        ComboBox.addActionListener(self)
        panel.add(ComboBox)
        frame.add(panel, BorderLayout.NORTH)

        # Center Panel
        panel = JPanel()
        self.RemoveButton = JButton(
            'Remove',
            actionPerformed = self.remove
            )
        panel.add(self.RemoveButton)
        frame.add(panel, BorderLayout.CENTER)

        panel = JPanel(alignmentX = Component.CENTER_ALIGNMENT )
        self.msg = panel.add( JLabel('Make a selection'))
        frame.add(panel, BorderLayout.SOUTH)
        
        frame.visible = 1

    def actionPerformed(self, event):
        cb = self.ComboBox
        item = cb.getSelectedItem().strip()
        items = [
            cb.getItemAt(i)
            for i in range(cb.getItemCount())
        ]
        if item:
            if item not in items:
                cb.addItem(item)
                self.RemoveButton.setEnabled(1)
            msg = 'Selection: "%s"' % item
            self.msg.text = msg
        else:
            cb.setSelectedIndex(0)

    def remove(self, event):
        cb = self.ComboBox
        index = cb.getSelectedIndex()
        item = cb.getSelectedItem()
        
        try:
            cb.removeItem(item)
            self.msg.text = 'Item removed: "%s"' % item
        except:
            self.msg.text = 'Remove request failed'
        self.RemoveButton.setEnabled(cb.getItemCount() > 1)


if __name__ == '__main__':
    EventQueue.invokeLater(DynamicComboBox())


    
    

