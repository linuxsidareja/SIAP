#Boa:Dialog:Dialog1

import wx

def create(parent):
    return Dialog1(parent)

[wxID_DIALOG1, wxID_DIALOG1STATICTEXT1, wxID_DIALOG1STATICTEXT2, 
 wxID_DIALOG1TUTUP, 
] = [wx.NewId() for _init_ctrls in range(4)]

class Dialog1(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt,
              pos=wx.Point(750, 332), size=wx.Size(237, 200),
              style=wx.DEFAULT_DIALOG_STYLE, title=u'Tentang SIAP')
        self.SetClientSize(wx.Size(229, 170))
        self.Center(wx.BOTH)

        self.staticText1 = wx.StaticText(id=wxID_DIALOG1STATICTEXT1,
              label=u'Versi : 1.0 ( Beta )\nPengembang : Andri Johandri\nemail : johandri@ictwatch.id\nLicense : GPL V3',
              name='staticText1', parent=self, pos=wx.Point(30, 16),
              size=wx.Size(169, 64), style=0)
        self.staticText1.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))

        self.tutup = wx.Button(id=wxID_DIALOG1TUTUP, label=u'Tutup',
              name=u'tutup', parent=self, pos=wx.Point(81, 133),
              size=wx.Size(75, 23), style=0)
        self.tutup.Bind(wx.EVT_BUTTON, self.OnTutupButton, id=wxID_DIALOG1TUTUP)

        self.staticText2 = wx.StaticText(id=wxID_DIALOG1STATICTEXT2,
              label=u'Bantuan Penggunaan Aplikasi SIAP kunjungi\nhttp://sisteminformasidesa.web.id',
              name='staticText2', parent=self, pos=wx.Point(8, 91),
              size=wx.Size(211, 24), style=0)
        self.staticText2.SetForegroundColour(wx.Colour(0, 0, 128))

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnTutupButton(self, event):
        self.Close()
        self.Destroy()
