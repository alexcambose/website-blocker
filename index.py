import os, sys, wx, ctypes
from datetime import datetime
from MainFrame import MainFrame

try:
    is_admin = os.getuid() == 0
except AttributeError:
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

if not is_admin:
    sys.exit('You need sudo/administrator rights!')

App = wx.App()
window = MainFrame(None)
App.MainLoop()
