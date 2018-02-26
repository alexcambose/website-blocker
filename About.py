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
## Class AboutDialog
###########################################################################

class AboutDialog(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                           size=wx.Size(334, 194), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"Website blocker", wx.DefaultPosition, wx.DefaultSize,
                                           wx.ALIGN_CENTRE)
        self.m_staticText3.Wrap(-1)
        self.m_staticText3.SetFont(
            wx.Font(20, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Sans"))

        bSizer3.Add(self.m_staticText3, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.m_staticText4 = wx.StaticText(self, wx.ID_ANY, u"v 1.0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        bSizer3.Add(self.m_staticText4, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText6 = wx.StaticText(self, wx.ID_ANY, u"Copyright ©", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)
        bSizer4.Add(self.m_staticText6, 0, wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.BOTTOM | wx.LEFT, 5)

        self.m_staticText8 = wx.StaticText(self, wx.ID_ANY, u"Alexandru Cambose", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText8.Wrap(-1)
        bSizer4.Add(self.m_staticText8, 0, wx.ALL, 5)

        bSizer3.Add(bSizer4, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.m_staticline2 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer3.Add(self.m_staticline2, 0, wx.EXPAND | wx.ALL, 5)

        bSizer5 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button7 = wx.Button(self, wx.ID_ANY, u"License", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.m_button7, 0, wx.ALL, 5)

        self.m_button8 = wx.Button(self, wx.ID_ANY, u"Repository", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.m_button8, 0, wx.ALL, 5)

        bSizer5.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_button9 = wx.Button(self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.m_button9, 0, wx.ALL, 5)

        bSizer3.Add(bSizer5, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer3)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button7.Bind(wx.EVT_BUTTON, self.openLicense)
        self.m_button8.Bind(wx.EVT_BUTTON, self.openRepository)
        self.m_button9.Bind(wx.EVT_BUTTON, self.close)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def openLicense(self, event):
        webbrowser.open('http://github.com/website-blocker/LICENSE')
        event.Skip()

    def openRepository(self, event):
        webbrowser.open('https://github.com/alexcambose/website-blocker')
        event.Skip()

    def close(self, event):
        self.Close();
        event.Skip()
