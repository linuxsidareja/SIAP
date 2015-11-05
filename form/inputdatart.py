#Boa:Dialog:iputrt

import wx

def create(parent):
    return iputrt(parent)

[wxID_IPUTRT, wxID_IPUTRTBUTTON1, wxID_IPUTRTBUTTON10, wxID_IPUTRTBUTTON2, 
 wxID_IPUTRTBUTTON3, wxID_IPUTRTBUTTON4, wxID_IPUTRTBUTTON5, 
 wxID_IPUTRTBUTTON6, wxID_IPUTRTBUTTON7, wxID_IPUTRTBUTTON8, 
 wxID_IPUTRTBUTTON9, wxID_IPUTRTLISTDUSUN, wxID_IPUTRTLISTRT, 
 wxID_IPUTRTLISTRW, wxID_IPUTRTSTATICBOX1, wxID_IPUTRTSTATICBOX2, 
 wxID_IPUTRTSTATICBOX3, wxID_IPUTRTSTATICTEXT1, wxID_IPUTRTSTATICTEXT2, 
 wxID_IPUTRTSTATICTEXT3, wxID_IPUTRTSTATICTEXT4, wxID_IPUTRTSTATICTEXT5, 
 wxID_IPUTRTSTATICTEXT6, wxID_IPUTRTSTATICTEXT7, wxID_IPUTRTSTATICTEXT8, 
 wxID_IPUTRTSTATICTEXT9, wxID_IPUTRTTEXTCTRL1, wxID_IPUTRTTEXTCTRL2, 
 wxID_IPUTRTTEXTCTRL3, wxID_IPUTRTTEXTCTRL4, wxID_IPUTRTTEXTCTRL5, 
 wxID_IPUTRTTEXTCTRL6, wxID_IPUTRTTEXTCTRL7, wxID_IPUTRTTEXTCTRL8, 
 wxID_IPUTRTTEXTCTRL9, 
] = [wx.NewId() for _init_ctrls in range(35)]

class iputrt(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_IPUTRT, name=u'iputrt', parent=prnt,
              pos=wx.Point(395, 173), size=wx.Size(719, 522),
              style=wx.DEFAULT_DIALOG_STYLE, title=u'Input Data RT, RW, Dusun')
        self.SetClientSize(wx.Size(711, 492))

        self.staticBox2 = wx.StaticBox(id=wxID_IPUTRTSTATICBOX2,
              label=u'Input Data RT', name='staticBox2', parent=self,
              pos=wx.Point(8, 8), size=wx.Size(696, 144), style=0)

        self.staticBox1 = wx.StaticBox(id=wxID_IPUTRTSTATICBOX1,
              label=u'Input Data RW', name='staticBox1', parent=self,
              pos=wx.Point(8, 160), size=wx.Size(696, 144), style=0)

        self.staticBox3 = wx.StaticBox(id=wxID_IPUTRTSTATICBOX3,
              label=u'Input Data Dusun', name='staticBox3', parent=self,
              pos=wx.Point(8, 312), size=wx.Size(696, 144), style=0)

        self.button1 = wx.Button(id=wxID_IPUTRTBUTTON1,
              label=u'Kembali Ke Menu', name='button1', parent=self,
              pos=wx.Point(575, 464), size=wx.Size(128, 23), style=0)

        self.staticText4 = wx.StaticText(id=wxID_IPUTRTSTATICTEXT4, label=u'RW',
              name='staticText4', parent=self, pos=wx.Point(309, 179),
              size=wx.Size(18, 13), style=0)

        self.textCtrl1 = wx.TextCtrl(id=wxID_IPUTRTTEXTCTRL1, name='textCtrl1',
              parent=self, pos=wx.Point(408, 174), size=wx.Size(56, 21),
              style=0, value=u'')

        self.staticText6 = wx.StaticText(id=wxID_IPUTRTSTATICTEXT6,
              label=u'Nama Ketua RW', name='staticText6', parent=self,
              pos=wx.Point(309, 206), size=wx.Size(79, 13), style=0)

        self.staticText5 = wx.StaticText(id=wxID_IPUTRTSTATICTEXT5,
              label=u'Alamat', name='staticText5', parent=self,
              pos=wx.Point(309, 230), size=wx.Size(34, 13), style=0)

        self.textCtrl2 = wx.TextCtrl(id=wxID_IPUTRTTEXTCTRL2, name='textCtrl2',
              parent=self, pos=wx.Point(408, 198), size=wx.Size(200, 21),
              style=0, value=u'')

        self.textCtrl3 = wx.TextCtrl(id=wxID_IPUTRTTEXTCTRL3, name='textCtrl3',
              parent=self, pos=wx.Point(408, 222), size=wx.Size(288, 45),
              style=wx.TE_MULTILINE, value=u'')

        self.button2 = wx.Button(id=wxID_IPUTRTBUTTON2, label=u'Tambah',
              name='button2', parent=self, pos=wx.Point(453, 274),
              size=wx.Size(75, 23), style=0)

        self.button3 = wx.Button(id=wxID_IPUTRTBUTTON3, label=u'Edit',
              name='button3', parent=self, pos=wx.Point(537, 274),
              size=wx.Size(75, 23), style=0)

        self.button4 = wx.Button(id=wxID_IPUTRTBUTTON4, label=u'Hapus',
              name='button4', parent=self, pos=wx.Point(621, 274),
              size=wx.Size(75, 23), style=0)

        self.listrw = wx.ListCtrl(id=wxID_IPUTRTLISTRW, name=u'listrw',
              parent=self, pos=wx.Point(16, 179), size=wx.Size(280, 117),
              style=wx.LC_ICON)

        self.listrt = wx.ListCtrl(id=wxID_IPUTRTLISTRT, name=u'listrt',
              parent=self, pos=wx.Point(16, 26), size=wx.Size(280, 117),
              style=wx.LC_ICON)

        self.listdusun = wx.ListCtrl(id=wxID_IPUTRTLISTDUSUN, name=u'listdusun',
              parent=self, pos=wx.Point(16, 329), size=wx.Size(280, 117),
              style=wx.LC_ICON)

        self.staticText2 = wx.StaticText(id=wxID_IPUTRTSTATICTEXT2, label=u'RT',
              name='staticText2', parent=self, pos=wx.Point(309, 28),
              size=wx.Size(14, 13), style=0)

        self.textCtrl6 = wx.TextCtrl(id=wxID_IPUTRTTEXTCTRL6, name='textCtrl6',
              parent=self, pos=wx.Point(408, 23), size=wx.Size(56, 21), style=0,
              value=u'')

        self.staticText1 = wx.StaticText(id=wxID_IPUTRTSTATICTEXT1,
              label=u'Nama Ketua RT', name='staticText1', parent=self,
              pos=wx.Point(309, 55), size=wx.Size(75, 13), style=0)

        self.textCtrl5 = wx.TextCtrl(id=wxID_IPUTRTTEXTCTRL5, name='textCtrl5',
              parent=self, pos=wx.Point(408, 47), size=wx.Size(200, 21),
              style=0, value=u'')

        self.staticText3 = wx.StaticText(id=wxID_IPUTRTSTATICTEXT3,
              label=u'Alamat', name='staticText3', parent=self,
              pos=wx.Point(309, 79), size=wx.Size(34, 13), style=0)

        self.textCtrl4 = wx.TextCtrl(id=wxID_IPUTRTTEXTCTRL4, name='textCtrl4',
              parent=self, pos=wx.Point(408, 71), size=wx.Size(288, 45),
              style=wx.TE_MULTILINE, value=u'')

        self.button6 = wx.Button(id=wxID_IPUTRTBUTTON6, label=u'Tambah',
              name='button6', parent=self, pos=wx.Point(453, 123),
              size=wx.Size(75, 23), style=0)

        self.button5 = wx.Button(id=wxID_IPUTRTBUTTON5, label=u'Edit',
              name='button5', parent=self, pos=wx.Point(537, 123),
              size=wx.Size(75, 23), style=0)

        self.button7 = wx.Button(id=wxID_IPUTRTBUTTON7, label=u'Hapus',
              name='button7', parent=self, pos=wx.Point(621, 123),
              size=wx.Size(75, 23), style=0)

        self.staticText8 = wx.StaticText(id=wxID_IPUTRTSTATICTEXT8,
              label=u'Dusun', name='staticText8', parent=self, pos=wx.Point(309,
              332), size=wx.Size(31, 13), style=0)

        self.textCtrl9 = wx.TextCtrl(id=wxID_IPUTRTTEXTCTRL9, name='textCtrl9',
              parent=self, pos=wx.Point(408, 327), size=wx.Size(56, 21),
              style=0, value=u'')

        self.staticText7 = wx.StaticText(id=wxID_IPUTRTSTATICTEXT7,
              label=u'Nama Ketua Dusun', name='staticText7', parent=self,
              pos=wx.Point(309, 359), size=wx.Size(92, 13), style=0)

        self.textCtrl8 = wx.TextCtrl(id=wxID_IPUTRTTEXTCTRL8, name='textCtrl8',
              parent=self, pos=wx.Point(408, 351), size=wx.Size(200, 21),
              style=0, value=u'')

        self.staticText9 = wx.StaticText(id=wxID_IPUTRTSTATICTEXT9,
              label=u'Alamat', name='staticText9', parent=self,
              pos=wx.Point(309, 383), size=wx.Size(34, 13), style=0)

        self.textCtrl7 = wx.TextCtrl(id=wxID_IPUTRTTEXTCTRL7, name='textCtrl7',
              parent=self, pos=wx.Point(408, 375), size=wx.Size(288, 45),
              style=wx.TE_MULTILINE, value=u'')

        self.button9 = wx.Button(id=wxID_IPUTRTBUTTON9, label=u'Tambah',
              name='button9', parent=self, pos=wx.Point(453, 427),
              size=wx.Size(75, 23), style=0)

        self.button8 = wx.Button(id=wxID_IPUTRTBUTTON8, label=u'Edit',
              name='button8', parent=self, pos=wx.Point(537, 427),
              size=wx.Size(75, 23), style=0)

        self.button10 = wx.Button(id=wxID_IPUTRTBUTTON10, label=u'Hapus',
              name='button10', parent=self, pos=wx.Point(621, 427),
              size=wx.Size(75, 23), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)
