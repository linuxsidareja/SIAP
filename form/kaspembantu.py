#Boa:Frame:kaspembantu
#-------------------------------------------------------------------------------
#Sistem Informasi dan Administrasi Perdesaan
#pengembang johandri@ictwatch.id
#-------------------------------------------------------------------------------

import wx

def create(parent):
    return kaspembantu(parent)

[wxID_KASPEMBANTU, wxID_KASPEMBANTUBARANG, wxID_KASPEMBANTUBENDAHARA, 
 wxID_KASPEMBANTUBIDANG, wxID_KASPEMBANTUBUKTI, wxID_KASPEMBANTUBUTTON1, 
 wxID_KASPEMBANTUBUTTON2, wxID_KASPEMBANTUBUTTON3, wxID_KASPEMBANTUBUTTON4, 
 wxID_KASPEMBANTUBUTTON5, wxID_KASPEMBANTUJASA, wxID_KASPEMBANTULISTCTRL1, 
 wxID_KASPEMBANTULISTCTRL2, wxID_KASPEMBANTURECORD, wxID_KASPEMBANTUREKBIDANG, 
 wxID_KASPEMBANTUREKKEGIATAN, wxID_KASPEMBANTUSALDO, 
 wxID_KASPEMBANTUSTATICTEXT1, wxID_KASPEMBANTUSTATICTEXT10, 
 wxID_KASPEMBANTUSTATICTEXT11, wxID_KASPEMBANTUSTATICTEXT12, 
 wxID_KASPEMBANTUSTATICTEXT13, wxID_KASPEMBANTUSTATICTEXT14, 
 wxID_KASPEMBANTUSTATICTEXT2, wxID_KASPEMBANTUSTATICTEXT3, 
 wxID_KASPEMBANTUSTATICTEXT4, wxID_KASPEMBANTUSTATICTEXT5, 
 wxID_KASPEMBANTUSTATICTEXT6, wxID_KASPEMBANTUSTATICTEXT7, 
 wxID_KASPEMBANTUSTATICTEXT8, wxID_KASPEMBANTUSTATICTEXT9, 
 wxID_KASPEMBANTUSWADAYA, wxID_KASPEMBANTUTAHUN, wxID_KASPEMBANTUTANGGAL, 
 wxID_KASPEMBANTUURAIAN, 
] = [wx.NewId() for _init_ctrls in range(35)]

class kaspembantu(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_KASPEMBANTU, name=u'kaspembantu',
              parent=prnt, pos=wx.Point(409, 157), size=wx.Size(919, 550),
              style=wx.DEFAULT_FRAME_STYLE,
              title=u'Buku Kas Pembantu Kegiatan')
        self.SetClientSize(wx.Size(911, 520))
        self.Center(wx.BOTH)
        self.SetBackgroundColour(wx.Colour(192, 192, 192))

        self.tahun = wx.TextCtrl(id=wxID_KASPEMBANTUTAHUN, name=u'tahun',
              parent=self, pos=wx.Point(576, 9), size=wx.Size(100, 21), style=0,
              value=u'')

        self.button1 = wx.Button(id=wxID_KASPEMBANTUBUTTON1, label=u'Buat Kas',
              name='button1', parent=self, pos=wx.Point(827, 8),
              size=wx.Size(75, 23), style=0)

        self.staticText1 = wx.StaticText(id=wxID_KASPEMBANTUSTATICTEXT1,
              label=u'Bidang', name='staticText1', parent=self,
              pos=wx.Point(681, 11), size=wx.Size(33, 13), style=0)

        self.staticText2 = wx.StaticText(id=wxID_KASPEMBANTUSTATICTEXT2,
              label=u'Tahun', name='staticText2', parent=self, pos=wx.Point(542,
              14), size=wx.Size(31, 13), style=0)

        self.bidang = wx.ComboBox(choices=[], id=wxID_KASPEMBANTUBIDANG,
              name=u'bidang', parent=self, pos=wx.Point(719, 8),
              size=wx.Size(102, 21), style=0, value=u'')
        self.bidang.SetLabel(u'')

        self.listCtrl1 = wx.ListCtrl(id=wxID_KASPEMBANTULISTCTRL1,
              name='listCtrl1', parent=self, pos=wx.Point(8, 27),
              size=wx.Size(520, 285), style=wx.LC_ICON)

        self.listCtrl2 = wx.ListCtrl(id=wxID_KASPEMBANTULISTCTRL2,
              name='listCtrl2', parent=self, pos=wx.Point(8, 322),
              size=wx.Size(896, 248), style=wx.LC_ICON)

        self.button2 = wx.Button(id=wxID_KASPEMBANTUBUTTON2, label=u'Tambah',
              name='button2', parent=self, pos=wx.Point(589, 294),
              size=wx.Size(75, 23), style=0)

        self.button3 = wx.Button(id=wxID_KASPEMBANTUBUTTON3, label=u'Edit',
              name='button3', parent=self, pos=wx.Point(669, 294),
              size=wx.Size(75, 23), style=0)

        self.button4 = wx.Button(id=wxID_KASPEMBANTUBUTTON4, label=u'Hapus',
              name='button4', parent=self, pos=wx.Point(749, 294),
              size=wx.Size(75, 23), style=0)

        self.button5 = wx.Button(id=wxID_KASPEMBANTUBUTTON5, label=u'Ke Menu',
              name='button5', parent=self, pos=wx.Point(829, 294),
              size=wx.Size(75, 23), style=0)

        self.staticText3 = wx.StaticText(id=wxID_KASPEMBANTUSTATICTEXT3,
              label=u'Data Dari RAB', name='staticText3', parent=self,
              pos=wx.Point(16, 8), size=wx.Size(69, 13), style=0)

        self.record = wx.TextCtrl(id=wxID_KASPEMBANTURECORD, name=u'record',
              parent=self, pos=wx.Point(608, 33), size=wx.Size(100, 21),
              style=0, value=u'')

        self.tanggal = wx.DatePickerCtrl(id=wxID_KASPEMBANTUTANGGAL,
              name=u'tanggal', parent=self, pos=wx.Point(616, 105),
              size=wx.Size(90, 21), style=wx.DP_SHOWCENTURY)

        self.rekbidang = wx.TextCtrl(id=wxID_KASPEMBANTUREKBIDANG,
              name=u'rekbidang', parent=self, pos=wx.Point(608, 57),
              size=wx.Size(296, 21), style=0, value=u'')

        self.rekkegiatan = wx.TextCtrl(id=wxID_KASPEMBANTUREKKEGIATAN,
              name=u'rekkegiatan', parent=self, pos=wx.Point(608, 81),
              size=wx.Size(296, 21), style=0, value=u'')

        self.Uraian = wx.TextCtrl(id=wxID_KASPEMBANTUURAIAN, name=u'Uraian',
              parent=self, pos=wx.Point(608, 129), size=wx.Size(296, 21),
              style=0, value=u'')

        self.bendahara = wx.TextCtrl(id=wxID_KASPEMBANTUBENDAHARA,
              name=u'bendahara', parent=self, pos=wx.Point(712, 153),
              size=wx.Size(100, 21), style=0, value=u'')

        self.swadaya = wx.TextCtrl(id=wxID_KASPEMBANTUSWADAYA, name=u'swadaya',
              parent=self, pos=wx.Point(712, 177), size=wx.Size(100, 21),
              style=0, value=u'')

        self.bukti = wx.TextCtrl(id=wxID_KASPEMBANTUBUKTI, name=u'bukti',
              parent=self, pos=wx.Point(608, 198), size=wx.Size(120, 21),
              style=0, value=u'')

        self.barang = wx.TextCtrl(id=wxID_KASPEMBANTUBARANG, name=u'barang',
              parent=self, pos=wx.Point(712, 222), size=wx.Size(100, 21),
              style=0, value=u'')

        self.jasa = wx.TextCtrl(id=wxID_KASPEMBANTUJASA, name=u'jasa',
              parent=self, pos=wx.Point(712, 245), size=wx.Size(100, 21),
              style=0, value=u'')

        self.saldo = wx.TextCtrl(id=wxID_KASPEMBANTUSALDO, name=u'saldo',
              parent=self, pos=wx.Point(608, 269), size=wx.Size(100, 21),
              style=0, value=u'')

        self.staticText4 = wx.StaticText(id=wxID_KASPEMBANTUSTATICTEXT4,
              label=u'Record', name='staticText4', parent=self,
              pos=wx.Point(543, 40), size=wx.Size(35, 13), style=0)

        self.staticText5 = wx.StaticText(id=wxID_KASPEMBANTUSTATICTEXT5,
              label=u'Bidang', name='staticText5', parent=self,
              pos=wx.Point(543, 64), size=wx.Size(33, 13), style=0)

        self.staticText6 = wx.StaticText(id=wxID_KASPEMBANTUSTATICTEXT6,
              label=u'Kegiatan', name='staticText6', parent=self,
              pos=wx.Point(543, 88), size=wx.Size(43, 13), style=0)

        self.staticText7 = wx.StaticText(id=wxID_KASPEMBANTUSTATICTEXT7,
              label=u'Tanggal', name='staticText7', parent=self,
              pos=wx.Point(543, 112), size=wx.Size(39, 13), style=0)

        self.staticText8 = wx.StaticText(id=wxID_KASPEMBANTUSTATICTEXT8,
              label=u'Uraian', name='staticText8', parent=self,
              pos=wx.Point(543, 136), size=wx.Size(32, 13), style=0)

        self.staticText9 = wx.StaticText(id=wxID_KASPEMBANTUSTATICTEXT9,
              label=u'Dari Bendahara', name='staticText9', parent=self,
              pos=wx.Point(608, 161), size=wx.Size(75, 13), style=0)

        self.staticText10 = wx.StaticText(id=wxID_KASPEMBANTUSTATICTEXT10,
              label=u'Swadaya Masyarakat', name='staticText10', parent=self,
              pos=wx.Point(608, 177), size=wx.Size(104, 13), style=0)

        self.staticText11 = wx.StaticText(id=wxID_KASPEMBANTUSTATICTEXT11,
              label=u'Nomor Bukti', name='staticText11', parent=self,
              pos=wx.Point(543, 208), size=wx.Size(58, 13), style=0)

        self.staticText12 = wx.StaticText(id=wxID_KASPEMBANTUSTATICTEXT12,
              label=u'Belanja Barang/Jasa', name='staticText12', parent=self,
              pos=wx.Point(608, 225), size=wx.Size(99, 13), style=0)

        self.staticText13 = wx.StaticText(id=wxID_KASPEMBANTUSTATICTEXT13,
              label=u'Belanja Modal', name='staticText13', parent=self,
              pos=wx.Point(616, 249), size=wx.Size(67, 13), style=0)

        self.staticText14 = wx.StaticText(id=wxID_KASPEMBANTUSTATICTEXT14,
              label=u'Saldo', name='staticText14', parent=self,
              pos=wx.Point(535, 264), size=wx.Size(27, 13), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)
