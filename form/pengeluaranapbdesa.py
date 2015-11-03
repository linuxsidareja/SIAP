#Boa:Dialog:apbdesa
#-------------------------------------------------------------------------------
#Sistem Informasi dan Administrasi Perdesaan
#pengembang johandri@ictwatch.id
#-------------------------------------------------------------------------------

import wx

def create(parent):
    return apbdesa(parent)

[wxID_APBDESA, wxID_APBDESABUTTON1, wxID_APBDESAEDIT, wxID_APBDESAHAPUS, 
 wxID_APBDESAKETERANGAN, wxID_APBDESALISTCTRL1, wxID_APBDESALISTCTRL2, 
 wxID_APBDESAMENU, wxID_APBDESANOMOR, wxID_APBDESANOREK, 
 wxID_APBDESASTATICTEXT1, wxID_APBDESASTATICTEXT2, wxID_APBDESASTATICTEXT3, 
 wxID_APBDESASTATICTEXT4, wxID_APBDESASTATICTEXT5, wxID_APBDESASTATICTEXT6, 
 wxID_APBDESASTATICTEXT7, wxID_APBDESATAHUN, wxID_APBDESATAMBAH, 
 wxID_APBDESATOTALANGGARAN, wxID_APBDESAURAIAN, 
] = [wx.NewId() for _init_ctrls in range(21)]

class apbdesa(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_APBDESA, name=u'apbdesa', parent=prnt,
              pos=wx.Point(528, 185), size=wx.Size(682, 494),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Penyusunan APB Desa')
        self.SetClientSize(wx.Size(674, 464))
        self.Center(wx.BOTH)
        self.SetBackgroundColour(wx.Colour(192, 192, 192))

        self.listCtrl1 = wx.ListCtrl(id=wxID_APBDESALISTCTRL1, name='listCtrl1',
              parent=self, pos=wx.Point(5, 6), size=wx.Size(287, 221),
              style=wx.LC_ICON)

        self.listCtrl2 = wx.ListCtrl(id=wxID_APBDESALISTCTRL2, name='listCtrl2',
              parent=self, pos=wx.Point(4, 234), size=wx.Size(666, 225),
              style=wx.LC_ICON)

        self.staticText1 = wx.StaticText(id=wxID_APBDESASTATICTEXT1,
              label=u'APB Desa Tahun :', name='staticText1', parent=self,
              pos=wx.Point(304, 16), size=wx.Size(87, 13), style=0)

        self.tahun = wx.TextCtrl(id=wxID_APBDESATAHUN, name=u'tahun',
              parent=self, pos=wx.Point(394, 16), size=wx.Size(58, 21), style=0,
              value=u'')

        self.button1 = wx.Button(id=wxID_APBDESABUTTON1, label='button1',
              name='button1', parent=self, pos=wx.Point(459, 15),
              size=wx.Size(99, 23), style=0)

        self.nomor = wx.TextCtrl(id=wxID_APBDESANOMOR, name=u'nomor',
              parent=self, pos=wx.Point(400, 48), size=wx.Size(39, 21), style=0,
              value=u'')

        self.staticText2 = wx.StaticText(id=wxID_APBDESASTATICTEXT2,
              label=u'Nomor Record', name='staticText2', parent=self,
              pos=wx.Point(304, 56), size=wx.Size(69, 13), style=0)

        self.staticText3 = wx.StaticText(id=wxID_APBDESASTATICTEXT3,
              label=u'Nomor Rekening', name='staticText3', parent=self,
              pos=wx.Point(304, 80), size=wx.Size(79, 13), style=0)

        self.staticText4 = wx.StaticText(id=wxID_APBDESASTATICTEXT4,
              label=u'Uraian', name='staticText4', parent=self,
              pos=wx.Point(304, 104), size=wx.Size(32, 13), style=0)

        self.staticText5 = wx.StaticText(id=wxID_APBDESASTATICTEXT5,
              label=u'Anggaran', name='staticText5', parent=self,
              pos=wx.Point(304, 128), size=wx.Size(48, 13), style=0)

        self.staticText6 = wx.StaticText(id=wxID_APBDESASTATICTEXT6,
              label=u'Keterangan', name='staticText6', parent=self,
              pos=wx.Point(304, 152), size=wx.Size(57, 13), style=0)

        self.norek = wx.TextCtrl(id=wxID_APBDESANOREK, name=u'norek',
              parent=self, pos=wx.Point(396, 80), size=wx.Size(49, 21), style=0,
              value=u'')

        self.uraian = wx.TextCtrl(id=wxID_APBDESAURAIAN, name=u'uraian',
              parent=self, pos=wx.Point(401, 112), size=wx.Size(188, 21),
              style=0, value=u'')

        self.keterangan = wx.TextCtrl(id=wxID_APBDESAKETERANGAN,
              name=u'keterangan', parent=self, pos=wx.Point(392, 144),
              size=wx.Size(100, 21), style=0, value=u'')

        self.tambah = wx.Button(id=wxID_APBDESATAMBAH, label=u'Tambah Data',
              name=u'tambah', parent=self, pos=wx.Point(301, 203),
              size=wx.Size(88, 23), style=0)

        self.edit = wx.Button(id=wxID_APBDESAEDIT, label=u'Edit Data',
              name=u'edit', parent=self, pos=wx.Point(395, 203),
              size=wx.Size(90, 23), style=0)

        self.hapus = wx.Button(id=wxID_APBDESAHAPUS, label=u'Hapus Data',
              name=u'hapus', parent=self, pos=wx.Point(490, 203),
              size=wx.Size(98, 23), style=0)

        self.menu = wx.Button(id=wxID_APBDESAMENU, label=u'Ke Menu',
              name=u'menu', parent=self, pos=wx.Point(592, 203),
              size=wx.Size(75, 23), style=0)

        self.totalanggaran = wx.TextCtrl(id=wxID_APBDESATOTALANGGARAN,
              name=u'totalanggaran', parent=self, pos=wx.Point(560, 168),
              size=wx.Size(100, 21), style=0, value=u'')

        self.staticText7 = wx.StaticText(id=wxID_APBDESASTATICTEXT7,
              label=u'Total Anggaran', name='staticText7', parent=self,
              pos=wx.Point(480, 176), size=wx.Size(75, 13), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)
