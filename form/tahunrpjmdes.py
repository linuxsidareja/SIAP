#Boa:Frame:Frame1
#-------------------------------------------------------------------------------
#Sistem Informasi dan Administrasi Perdesaan
#pengembang johandri@ictwatch.id
#-------------------------------------------------------------------------------

import wx

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1BUTTON2, wxID_FRAME1LISTCTRL1, 
 wxID_FRAME1STATICLINE1, wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2, 
 wxID_FRAME1TEXTCTRL1, 
] = [wx.NewId() for _init_ctrls in range(8)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(326, 120), size=wx.Size(903, 477),
              style=wx.DEFAULT_FRAME_STYLE, title='Frame1')
        self.SetClientSize(wx.Size(895, 447))
        self.SetBackgroundColour(wx.Colour(192, 192, 192))

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'Tahun RPJM Desa', name='staticText1', parent=self,
              pos=wx.Point(8, 8), size=wx.Size(87, 13), style=0)

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self, pos=wx.Point(104, 8), size=wx.Size(184, 21), style=0,
              value=u'')

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1, label=u'Edit Data',
              name='button1', parent=self, pos=wx.Point(200, 40),
              size=wx.Size(88, 23), style=0)

        self.listCtrl1 = wx.ListCtrl(id=wxID_FRAME1LISTCTRL1, name='listCtrl1',
              parent=self, pos=wx.Point(296, 8), size=wx.Size(336, 56),
              style=wx.LC_ICON)

        self.button2 = wx.Button(id=wxID_FRAME1BUTTON2, label=u'Tambah Data',
              name='button2', parent=self, pos=wx.Point(104, 40),
              size=wx.Size(88, 23), style=0)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'Catatan:\nBuat Terlebih Dahulu Tahun RPJM Desa\nSecara Otomatis Program Akan Menyediakan\nPembuatan Data Untuk Tahun Tersebut',
              name='staticText2', parent=self, pos=wx.Point(640, 8),
              size=wx.Size(216, 52), style=0)

        self.staticLine1 = wx.StaticLine(id=wxID_FRAME1STATICLINE1,
              name='staticLine1', parent=self, pos=wx.Point(8, 74),
              size=wx.Size(880, 2), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)
