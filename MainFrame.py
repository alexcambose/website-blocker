import platform, os, atexit, threading, wx, wx.xrc, sched, time, sys, About, Help
from datetime import datetime
from Hosts import Hosts

hostsFilepath = '/etc/hosts'
if platform.system() == 'Windows':
    hostsFilepath = 'C:\Windows\System32\Drivers\etc\hosts'

savedHosts = Hosts(os.path.join(os.getcwd(), 'data.txt'))
hosts = Hosts(hostsFilepath)

def onExit():
    dlg = wx.MessageDialog(None, 'Will stop blocking', 'Exiting')
    dlg.ShowModal()
    for host in hosts.getHosts():
        hosts.disableHost(host)
    hosts.write()
    dlg.Destroy()

atexit.register(onExit)

class MainFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Website blocker", pos=wx.DefaultPosition,
                          size=wx.Size(560, 350),
                          style=wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.Size(560, 350), wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(240, 240, 240))

        self.menubar = wx.MenuBar(0)
        self.file_menu = wx.Menu()
        self.exit_menuItem = wx.MenuItem(self.file_menu, wx.ID_EXIT, u"Exit", wx.EmptyString, wx.ITEM_NORMAL)
        self.file_menu.Append(self.exit_menuItem)

        self.menubar.Append(self.file_menu, u"&File")

        self.help_menu = wx.Menu()
        self.help_menu_item = wx.MenuItem(self.help_menu, wx.ID_HELP, u"Help", wx.EmptyString, wx.ITEM_NORMAL)
        self.help_menu.Append(self.help_menu_item)

        self.about_menu_item = wx.MenuItem(self.help_menu, wx.ID_ABOUT, u"About", wx.EmptyString, wx.ITEM_NORMAL)
        self.help_menu.Append(self.about_menu_item)

        self.menubar.Append(self.help_menu, u"Help")

        self.SetMenuBar(self.menubar)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        list_blocked_websitesChoices = []
        self.list_blocked_websites = wx.ListBox(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                list_blocked_websitesChoices, 0)
        bSizer1.Add(self.list_blocked_websites, 1, wx.ALL | wx.EXPAND, 5)

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        self.button_enable = wx.Button(self, wx.ID_ANY, u"Enable", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.button_enable, 1, wx.ALL, 5)

        self.button_disable = wx.Button(self, wx.ID_ANY, u"Disable", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.button_disable, 1, wx.ALL, 5)

        self.button_delete = wx.Button(self, wx.ID_DELETE, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.button_delete, 1, wx.ALL, 5)

        bSizer1.Add(bSizer2, 0, wx.EXPAND | wx.RIGHT | wx.LEFT, 5)

        sbSizer1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Add new website"), wx.HORIZONTAL)

        self.new_website_button = wx.Button(sbSizer1.GetStaticBox(), wx.ID_ANY, u"Add website", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        sbSizer1.Add(self.new_website_button, 1, wx.ALL, 5)

        self.website_textbox = wx.TextCtrl(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        sbSizer1.Add(self.website_textbox, 4, wx.ALL, 5)

        bSizer1.Add(sbSizer1, 0, wx.EXPAND | wx.ALL, 5)

        sbSizer2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Working hours"), wx.HORIZONTAL)

        self.m_staticText2 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Start:", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        sbSizer2.Add(self.m_staticText2, 0, wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.BOTTOM | wx.LEFT, 5)

        self.start_hour_spinner = wx.SpinCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                              wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 23, 10)
        sbSizer2.Add(self.start_hour_spinner, 1, wx.ALL | wx.EXPAND, 5)

        self.button_start_blocking = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Start", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        self.button_start_blocking.SetToolTip(u"Starts or stops the website blocking timer")
        self.button_start_blocking.SetMinSize(wx.Size(0, 0))

        sbSizer2.Add(self.button_start_blocking, 2, wx.ALL | wx.EXPAND, 5)

        self.button_stop_blocking = wx.Button(sbSizer2.GetStaticBox(), wx.ID_STOP, u"Stop", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.button_stop_blocking.SetMinSize(wx.Size(0, 0))

        sbSizer2.Add(self.button_stop_blocking, 2, wx.ALL | wx.EXPAND, 5)

        self.m_staticText4 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"End:", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        sbSizer2.Add(self.m_staticText4, 0, wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.BOTTOM | wx.LEFT, 5)

        self.end_hour_spiner = wx.SpinCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                           wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 23, 18)
        sbSizer2.Add(self.end_hour_spiner, 1, wx.ALL | wx.EXPAND, 5)

        bSizer1.Add(sbSizer2, 0, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()
        self.statusBar = self.CreateStatusBar(3, wx.STB_SIZEGRIP, wx.ID_ANY)

        self.Centre(wx.BOTH)

        self.Show()
        # Disabling
        self.new_website_button.Disable()
        self.button_enable.Disable()
        self.button_disable.Disable()
        self.button_delete.Disable()
        self.button_stop_blocking.Disable()
        # Connect Events
        self.Bind(wx.EVT_MENU, self.quit, id=self.exit_menuItem.GetId())
        self.Bind(wx.EVT_MENU, self.openHelp, id=self.help_menu_item.GetId())
        self.Bind(wx.EVT_MENU, self.openAbout, id=self.about_menu_item.GetId())
        self.new_website_button.Bind(wx.EVT_BUTTON, self.addWebsite)
        self.button_start_blocking.Bind(wx.EVT_BUTTON, self.startBlocking)
        self.button_stop_blocking.Bind(wx.EVT_BUTTON, self.stopBlocking)
        self.button_delete.Bind(wx.EVT_BUTTON, self.deleteWebsite)
        self.button_enable.Bind(wx.EVT_BUTTON, self.enableWebsite)
        self.button_disable.Bind(wx.EVT_BUTTON, self.disableWebsite)
        self.list_blocked_websites.Bind(wx.EVT_LISTBOX, self.listItemSelected)
        self.website_textbox.Bind(wx.EVT_TEXT, self.websiteTextboxChanged)
        # Insert hosts into listBox
        self.refreshHosts()
        self.isBlocking = False
        self.t = threading.Thread(target=self.check)
        self.t.daemon = True
        self.t.start()

        self.statusBar.SetStatusText('Stopped', 1)
    def __del__(self):
        self.isBlocking = False
        pass

    def check(self):
        while True:
            time.sleep(1)
            if self.isBlocking:
                hosts.hosts = savedHosts.hosts
                if 'lastCheck' not in locals():
                    lastCheck = -1
                startHour = self.start_hour_spinner.GetValue()
                endHour = self.end_hour_spiner.GetValue()
                currentCheck = startHour <= datetime.now().hour <= endHour
                if currentCheck != lastCheck:
                    if currentCheck:
                        for host in hosts.getHosts():
                            hosts.enableHost(host)
                    else:
                        for host in hosts.getHosts():
                            hosts.disableHost(host)
                    hosts.write()
                lastCheck = currentCheck

    # Virtual event handlers, overide them in your derived class
    def quit(self, event):
        self.Close()
        event.Skip()

    def refreshHosts(self):
        savedHosts.write()
        while self.list_blocked_websites.GetCount():
            self.list_blocked_websites.Delete(0)
        if savedHosts.getHosts():
            websites = []
            blockedWebsites = 0
            for host in savedHosts.getHosts():
                if savedHosts.isHostEnabled(host):
                    websites.append(host)
                    blockedWebsites = 1 + blockedWebsites
                else:
                    websites.append('(disabled) ' + host)
            self.statusBar.SetStatusText(str(blockedWebsites) + ' websites blocked', 0)
            # self.statusBar.SetStatusText('', 3)
            self.list_blocked_websites.InsertItems(websites, 0)
            self.button_start_blocking.Enable()
        else:
            self.button_start_blocking.Disable()
        self.button_enable.Disable()
        self.button_disable.Disable()
        self.button_delete.Disable()

    def listItemSelected(self, e):
        selectedHost = savedHosts.getHosts()[self.list_blocked_websites.GetSelection()]
        if savedHosts.isHostEnabled(selectedHost):
            self.button_enable.Disable()
            self.button_disable.Enable()
        else:
            self.button_enable.Enable()
            self.button_disable.Disable()
        self.button_delete.Enable()

    def addWebsite(self, event):
        website = self.website_textbox.GetValue()
        if not savedHosts.addHost(website):
            wx.MessageBox(message=website + " is not a valid website or it already exists!", caption='Error',
                          style=wx.ICON_ERROR)
            return False
        self.website_textbox.SetValue("")
        self.refreshHosts()
        event.Skip()

    def deleteWebsite(self, event):
        selectedHost = savedHosts.getHosts()[self.list_blocked_websites.GetSelection()]
        savedHosts.deleteHost(selectedHost)
        self.refreshHosts()
        event.Skip()

    def websiteTextboxChanged(self, event):
        if event.GetEventObject().GetValue().strip() != '':
            self.new_website_button.Enable()
        else:
            self.new_website_button.Disable()
        event.Skip()

    def startBlocking(self, event):
        self.isBlocking = True
        self.button_start_blocking.Disable()
        self.button_stop_blocking.Enable()
        self.statusBar.SetStatusText('Running...', 1)
        event.Skip()

    def stopBlocking(self, event):
        self.isBlocking = False
        self.button_start_blocking.Enable()
        self.button_stop_blocking.Disable()
        self.statusBar.SetStatusText('Stopped', 1)
        event.Skip()

    def enableWebsite(self, event):
        selectedHost = savedHosts.getHosts()[self.list_blocked_websites.GetSelection()]
        savedHosts.enableHost(selectedHost)
        self.refreshHosts()
        event.Skip()

    def disableWebsite(self, event):
        selectedHost = savedHosts.getHosts()[self.list_blocked_websites.GetSelection()]
        savedHosts.disableHost(selectedHost)
        self.refreshHosts()
        event.Skip()

    def openAbout(self, event):
        dlg = About.AboutDialog(self)
        dlg.ShowModal()
        event.Skip()

    def openHelp(self, event):
        dlg = Help.HelpDialog(self)
        dlg.ShowModal()
        event.Skip()
