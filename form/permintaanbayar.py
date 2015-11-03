#Boa:Frame:permintaanbayar
#-------------------------------------------------------------------------------
#Sistem Informasi dan Administrasi Perdesaan
#pengembang johandri@ictwatch.id
#-------------------------------------------------------------------------------

import wx

def create(parent):
    return permintaanbayar(parent)

[wxID_PERMINTAANBAYAR, wxID_PERMINTAANBAYARBIDANG, wxID_PERMINTAANBAYARBUAT, 
 wxID_PERMINTAANBAYARBUTTON1, wxID_PERMINTAANBAYARBUTTON2, 
 wxID_PERMINTAANBAYARBUTTON3, wxID_PERMINTAANBAYARDATEPICKERCTRL1, 
 wxID_PERMINTAANBAYARJUMLAH, wxID_PERMINTAANBAYARKEGIATAN, 
 wxID_PERMINTAANBAYARLISTCTRL1, wxID_PERMINTAANBAYARLISTCTRL2, 
 wxID_PERMINTAANBAYARMENU, wxID_PERMINTAANBAYARNOREK, 
 wxID_PERMINTAANBAYARPAGU, wxID_PERMINTAANBAYARPENCAIRAN, 
 wxID_PERMINTAANBAYARPERIODE, wxID_PERMINTAANBAYARPERMINTAAN, 
 wxID_PERMINTAANBAYARRECORD, wxID_PERMINTAANBAYARRKP, 
 wxID_PERMINTAANBAYARSISA, wxID_PERMINTAANBAYARSTATICBOX1, 
 wxID_PERMINTAANBAYARSTATICTEXT1, wxID_PERMINTAANBAYARSTATICTEXT10, 
 wxID_PERMINTAANBAYARSTATICTEXT11, wxID_PERMINTAANBAYARSTATICTEXT12, 
 wxID_PERMINTAANBAYARSTATICTEXT13, wxID_PERMINTAANBAYARSTATICTEXT14, 
 wxID_PERMINTAANBAYARSTATICTEXT2, wxID_PERMINTAANBAYARSTATICTEXT3, 
 wxID_PERMINTAANBAYARSTATICTEXT4, wxID_PERMINTAANBAYARSTATICTEXT5, 
 wxID_PERMINTAANBAYARSTATICTEXT6, wxID_PERMINTAANBAYARSTATICTEXT7, 
 wxID_PERMINTAANBAYARSTATICTEXT8, wxID_PERMINTAANBAYARSTATICTEXT9, 
 wxID_PERMINTAANBAYARTAHUN, wxID_PERMINTAANBAYARURAIAN, 
] = [wx.NewId() for _init_ctrls in range(37)]

class permintaanbayar(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_PERMINTAANBAYAR,
              name=u'permintaanbayar', parent=prnt, pos=wx.Point(409, 194),
              size=wx.Size(919, 475), style=wx.DEFAULT_FRAME_STYLE,
              title=u'Surat Permintaan Pembayaran')
        self.SetClientSize(wx.Size(911, 445))
        self.Center(wx.BOTH)
        self.SetBackgroundColour(wx.Colour(192, 192, 192))

        self.staticBox1 = wx.StaticBox(id=wxID_PERMINTAANBAYARSTATICBOX1,
              label=u'', name='staticBox1', parent=self, pos=wx.Point(546, -3),
              size=wx.Size(360, 61), style=0)

        self.periode = wx.TextCtrl(id=wxID_PERMINTAANBAYARPERIODE,
              name=u'periode', parent=self, pos=wx.Point(669, 7),
              size=wx.Size(54, 21), style=0, value=u'')

        self.tahun = wx.TextCtrl(id=wxID_PERMINTAANBAYARTAHUN, name=u'tahun',
              parent=self, pos=wx.Point(834, 7), size=wx.Size(65, 21), style=0,
              value=u'')

        self.rkp = wx.ComboBox(choices=[], id=wxID_PERMINTAANBAYARRKP,
              name=u'rkp', parent=self, pos=wx.Point(753, 7), size=wx.Size(40,
              21), style=0, value=u'')
        self.rkp.SetLabel(u'')

        self.staticText1 = wx.StaticText(id=wxID_PERMINTAANBAYARSTATICTEXT1,
              label=u'Tahun', name='staticText1', parent=self, pos=wx.Point(797,
              12), size=wx.Size(31, 13), style=0)

        self.staticText2 = wx.StaticText(id=wxID_PERMINTAANBAYARSTATICTEXT2,
              label=u'RKP', name='staticText2', parent=self, pos=wx.Point(729,
              12), size=wx.Size(20, 13), style=0)

        self.staticText3 = wx.StaticText(id=wxID_PERMINTAANBAYARSTATICTEXT3,
              label=u'Periode', name='staticText3', parent=self,
              pos=wx.Point(628, 12), size=wx.Size(37, 13), style=0)

        self.buat = wx.Button(id=wxID_PERMINTAANBAYARBUAT,
              label=u'Buat Permintaan', name=u'buat', parent=self,
              pos=wx.Point(788, 31), size=wx.Size(112, 23), style=0)

        self.record = wx.TextCtrl(id=wxID_PERMINTAANBAYARRECORD, name=u'record',
              parent=self, pos=wx.Point(568, 69), size=wx.Size(66, 21), style=0,
              value=u'')

        self.staticText4 = wx.StaticText(id=wxID_PERMINTAANBAYARSTATICTEXT4,
              label=u'Record', name='staticText4', parent=self,
              pos=wx.Point(466, 71), size=wx.Size(35, 13), style=0)

        self.bidang = wx.ComboBox(choices=[], id=wxID_PERMINTAANBAYARBIDANG,
              name=u'bidang', parent=self, pos=wx.Point(605, 32),
              size=wx.Size(179, 21), style=0, value=u'')
        self.bidang.SetLabel(u'')

        self.norek = wx.TextCtrl(id=wxID_PERMINTAANBAYARNOREK, name=u'norek',
              parent=self, pos=wx.Point(722, 69), size=wx.Size(64, 21), style=0,
              value=u'')

        self.kegiatan = wx.TextCtrl(id=wxID_PERMINTAANBAYARKEGIATAN,
              name=u'kegiatan', parent=self, pos=wx.Point(568, 91),
              size=wx.Size(337, 22), style=0, value=u'')

        self.datePickerCtrl1 = wx.DatePickerCtrl(id=wxID_PERMINTAANBAYARDATEPICKERCTRL1,
              name='datePickerCtrl1', parent=self, pos=wx.Point(572, 113),
              size=wx.Size(90, 21), style=wx.DP_SHOWCENTURY)

        self.staticText5 = wx.StaticText(id=wxID_PERMINTAANBAYARSTATICTEXT5,
              label=u'Bidang', name='staticText5', parent=self,
              pos=wx.Point(564, 33), size=wx.Size(33, 13), style=0)

        self.pagu = wx.TextCtrl(id=wxID_PERMINTAANBAYARPAGU, name=u'pagu',
              parent=self, pos=wx.Point(568, 156), size=wx.Size(100, 21),
              style=0, value=u'')

        self.pencairan = wx.TextCtrl(id=wxID_PERMINTAANBAYARPENCAIRAN,
              name=u'pencairan', parent=self, pos=wx.Point(805, 156),
              size=wx.Size(100, 21), style=0, value=u'')

        self.permintaan = wx.TextCtrl(id=wxID_PERMINTAANBAYARPERMINTAAN,
              name=u'permintaan', parent=self, pos=wx.Point(568, 177),
              size=wx.Size(100, 21), style=0, value=u'')

        self.jumlah = wx.TextCtrl(id=wxID_PERMINTAANBAYARJUMLAH, name=u'jumlah',
              parent=self, pos=wx.Point(805, 177), size=wx.Size(100, 21),
              style=0, value=u'')

        self.sisa = wx.TextCtrl(id=wxID_PERMINTAANBAYARSISA, name=u'sisa',
              parent=self, pos=wx.Point(805, 198), size=wx.Size(100, 21),
              style=0, value=u'')

        self.staticText6 = wx.StaticText(id=wxID_PERMINTAANBAYARSTATICTEXT6,
              label=u'Nomor Rekening', name='staticText6', parent=self,
              pos=wx.Point(640, 71), size=wx.Size(79, 13), style=0)

        self.Uraian = wx.TextCtrl(id=wxID_PERMINTAANBAYARURAIAN, name=u'Uraian',
              parent=self, pos=wx.Point(568, 135), size=wx.Size(338, 21),
              style=0, value=u'')

        self.staticText7 = wx.StaticText(id=wxID_PERMINTAANBAYARSTATICTEXT7,
              label=u'Kegiatan', name='staticText7', parent=self,
              pos=wx.Point(465, 93), size=wx.Size(43, 13), style=0)

        self.staticText8 = wx.StaticText(id=wxID_PERMINTAANBAYARSTATICTEXT8,
              label=u'Waktu', name='staticText8', parent=self, pos=wx.Point(465,
              117), size=wx.Size(32, 13), style=0)

        self.staticText9 = wx.StaticText(id=wxID_PERMINTAANBAYARSTATICTEXT9,
              label=u'Uraian', name='staticText9', parent=self,
              pos=wx.Point(465, 139), size=wx.Size(32, 13), style=0)

        self.staticText10 = wx.StaticText(id=wxID_PERMINTAANBAYARSTATICTEXT10,
              label=u'Pagu Anggaran', name='staticText10', parent=self,
              pos=wx.Point(464, 159), size=wx.Size(75, 13), style=0)

        self.staticText11 = wx.StaticText(id=wxID_PERMINTAANBAYARSTATICTEXT11,
              label=u'Pencairan s.d. Yang Lalu', name='staticText11',
              parent=self, pos=wx.Point(676, 159), size=wx.Size(119, 13),
              style=0)

        self.staticText12 = wx.StaticText(id=wxID_PERMINTAANBAYARSTATICTEXT12,
              label=u'Permintaan Sekarang', name='staticText12', parent=self,
              pos=wx.Point(463, 181), size=wx.Size(103, 13), style=0)

        self.staticText13 = wx.StaticText(id=wxID_PERMINTAANBAYARSTATICTEXT13,
              label=u'Jumlah Sampai Saat Ini', name='staticText13', parent=self,
              pos=wx.Point(677, 183), size=wx.Size(110, 13), style=0)

        self.staticText14 = wx.StaticText(id=wxID_PERMINTAANBAYARSTATICTEXT14,
              label=u'Sisa Dana', name='staticText14', parent=self,
              pos=wx.Point(677, 207), size=wx.Size(48, 13), style=0)

        self.listCtrl1 = wx.ListCtrl(id=wxID_PERMINTAANBAYARLISTCTRL1,
              name='listCtrl1', parent=self, pos=wx.Point(8, 24),
              size=wx.Size(448, 222), style=wx.LC_ICON)

        self.listCtrl2 = wx.ListCtrl(id=wxID_PERMINTAANBAYARLISTCTRL2,
              name='listCtrl2', parent=self, pos=wx.Point(8, 252),
              size=wx.Size(896, 184), style=wx.LC_ICON)

        self.menu = wx.Button(id=wxID_PERMINTAANBAYARMENU, label=u'Ke Menu',
              name=u'menu', parent=self, pos=wx.Point(827, 223),
              size=wx.Size(75, 23), style=0)

        self.button1 = wx.Button(id=wxID_PERMINTAANBAYARBUTTON1, label=u'Hapus',
              name='button1', parent=self, pos=wx.Point(746, 223),
              size=wx.Size(75, 23), style=0)

        self.button2 = wx.Button(id=wxID_PERMINTAANBAYARBUTTON2, label=u'Edit',
              name='button2', parent=self, pos=wx.Point(664, 224),
              size=wx.Size(75, 23), style=0)

        self.button3 = wx.Button(id=wxID_PERMINTAANBAYARBUTTON3,
              label=u'Tambah', name='button3', parent=self, pos=wx.Point(582,
              224), size=wx.Size(75, 23), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)
