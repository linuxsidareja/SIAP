#Boa:Dialog:jabatan

import wx

def create(parent):
    return jabatan(parent)

[wxID_JABATAN, wxID_JABATANJABATAN, wxID_JABATANLISTCTRL1, 
 wxID_JABATANSTATICTEXT1, 
] = [wx.NewId() for _init_ctrls in range(4)]

class jabatan(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_JABATAN, name=u'jabatan', parent=prnt,
              pos=wx.Point(542, 316), size=wx.Size(419, 286),
              style=wx.DEFAULT_DIALOG_STYLE,
              title=u'Input Jabatan Dan Pangkat')
        self.SetClientSize(wx.Size(411, 256))

        self.staticText1 = wx.StaticText(id=wxID_JABATANSTATICTEXT1,
              label=u'Jabatan', name='staticText1', parent=self,
              pos=wx.Point(10, 9), size=wx.Size(39, 13), style=0)

        self.jabatan = wx.TextCtrl(id=wxID_JABATANJABATAN, name=u'jabatan',
              parent=self, pos=wx.Point(64, 7), size=wx.Size(336, 21), style=0,
              value=u'')

        self.listCtrl1 = wx.ListCtrl(id=wxID_JABATANLISTCTRL1, name='listCtrl1',
              parent=self, pos=wx.Point(8, 32), size=wx.Size(392, 192),
              style=wx.LC_ICON)

    def __init__(self, parent):
        self._init_ctrls(parent)
