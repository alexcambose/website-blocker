# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Feb 18 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import webbrowser

###########################################################################
## Class HelpDialog
###########################################################################

class HelpDialog(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                           size=wx.Size(490, 252), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText7 = wx.StaticText(self, wx.ID_ANY, u"Help", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)
        self.m_staticText7.SetFont(
            wx.Font(17, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans"))

        bSizer8.Add(self.m_staticText7, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText8 = wx.StaticText(self, wx.ID_ANY,
                                           u"How to use:\n1. Add the websites that you want to block\n2. Set the start and the end workign hour when you want the websites to be blocked\n3. Press start to enable website blockign and disable to disable it\n\n",
                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText8.Wrap(-1)
        bSizer8.Add(self.m_staticText8, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer6.Add(bSizer8, 0, wx.EXPAND | wx.ALL, 5)

        self.m_staticline1 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer6.Add(self.m_staticline1, 0, wx.EXPAND | wx.ALL, 5)

        bSizer7 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button10 = wx.Button(self, wx.ID_ANY, u"Repository", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7.Add(self.m_button10, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer7.Add((0, 0), 1, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_button11 = wx.Button(self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7.Add(self.m_button11, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer6.Add(bSizer7, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer6)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button10.Bind(wx.EVT_BUTTON, self.repository)
        self.m_button11.Bind(wx.EVT_BUTTON, self.close)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def repository(self, event):
        webbrowser.open('https://github.com/alexcambose/website-blocker')
        event.Skip()

    def close(self, event):
        self.Close();
        event.Skip()
