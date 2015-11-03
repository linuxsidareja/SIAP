#Boa:Frame:rpjmpembangunandesa
#-------------------------------------------------------------------------------
#Sistem Informasi dan Administrasi Perdesaan
#pengembang johandri@ictwatch.id
#-------------------------------------------------------------------------------

import wx
import os
import string

import sqlite3

db = sqlite3.connect('siap.db')
cur = db.cursor()


def create(parent):
    return rpjmpembangunandesa(parent)

[wxID_RPJMPEMBANGUNANDESA, wxID_RPJMPEMBANGUNANDESAAPBDES, 
 wxID_RPJMPEMBANGUNANDESAAPBN, wxID_RPJMPEMBANGUNANDESAASLIDESA, 
 wxID_RPJMPEMBANGUNANDESABERSIHKAN, wxID_RPJMPEMBANGUNANDESABIAYA0, 
 wxID_RPJMPEMBANGUNANDESABIAYA1, wxID_RPJMPEMBANGUNANDESABIAYA2, 
 wxID_RPJMPEMBANGUNANDESABIAYAAPBDES, wxID_RPJMPEMBANGUNANDESABIAYAAPBN, 
 wxID_RPJMPEMBANGUNANDESABIAYALAIN, wxID_RPJMPEMBANGUNANDESABUTTON2, 
 wxID_RPJMPEMBANGUNANDESACARINOREK, wxID_RPJMPEMBANGUNANDESAEDIT, 
 wxID_RPJMPEMBANGUNANDESAHAPUS, wxID_RPJMPEMBANGUNANDESAJUMLAH, 
 wxID_RPJMPEMBANGUNANDESAJUMLAHVOLUME, wxID_RPJMPEMBANGUNANDESAKEGIATAN, 
 wxID_RPJMPEMBANGUNANDESALAIN, wxID_RPJMPEMBANGUNANDESALOKASI, 
 wxID_RPJMPEMBANGUNANDESAMENU, wxID_RPJMPEMBANGUNANDESANOMOR, 
 wxID_RPJMPEMBANGUNANDESANOREK, wxID_RPJMPEMBANGUNANDESAPEMBANGUNANDESA, 
 wxID_RPJMPEMBANGUNANDESAPENDAPATAN, wxID_RPJMPEMBANGUNANDESAPERIODE0, 
 wxID_RPJMPEMBANGUNANDESAPOLA, wxID_RPJMPEMBANGUNANDESARPJMPEMBANGUNANDESA, 
 wxID_RPJMPEMBANGUNANDESASASARAN, wxID_RPJMPEMBANGUNANDESASATUAN, 
 wxID_RPJMPEMBANGUNANDESASTATICBOX1, wxID_RPJMPEMBANGUNANDESASTATICTEXT1, 
 wxID_RPJMPEMBANGUNANDESASTATICTEXT10, wxID_RPJMPEMBANGUNANDESASTATICTEXT11, 
 wxID_RPJMPEMBANGUNANDESASTATICTEXT12, wxID_RPJMPEMBANGUNANDESASTATICTEXT13, 
 wxID_RPJMPEMBANGUNANDESASTATICTEXT14, wxID_RPJMPEMBANGUNANDESASTATICTEXT15, 
 wxID_RPJMPEMBANGUNANDESASTATICTEXT16, wxID_RPJMPEMBANGUNANDESASTATICTEXT17, 
 wxID_RPJMPEMBANGUNANDESASTATICTEXT18, wxID_RPJMPEMBANGUNANDESASTATICTEXT19, 
 wxID_RPJMPEMBANGUNANDESASTATICTEXT2, wxID_RPJMPEMBANGUNANDESASTATICTEXT20, 
 wxID_RPJMPEMBANGUNANDESASTATICTEXT21, wxID_RPJMPEMBANGUNANDESASTATICTEXT22, 
 wxID_RPJMPEMBANGUNANDESASTATICTEXT23, wxID_RPJMPEMBANGUNANDESASTATICTEXT24, 
 wxID_RPJMPEMBANGUNANDESASTATICTEXT25, wxID_RPJMPEMBANGUNANDESASTATICTEXT26, 
 wxID_RPJMPEMBANGUNANDESASTATICTEXT27, wxID_RPJMPEMBANGUNANDESASTATICTEXT28, 
 wxID_RPJMPEMBANGUNANDESASTATICTEXT29, wxID_RPJMPEMBANGUNANDESASTATICTEXT3, 
 wxID_RPJMPEMBANGUNANDESASTATICTEXT30, wxID_RPJMPEMBANGUNANDESASTATICTEXT31, 
 wxID_RPJMPEMBANGUNANDESASTATICTEXT4, wxID_RPJMPEMBANGUNANDESASTATICTEXT5, 
 wxID_RPJMPEMBANGUNANDESASTATICTEXT6, wxID_RPJMPEMBANGUNANDESASTATICTEXT7, 
 wxID_RPJMPEMBANGUNANDESASTATICTEXT8, wxID_RPJMPEMBANGUNANDESASTATICTEXT9, 
 wxID_RPJMPEMBANGUNANDESATAMBAH, wxID_RPJMPEMBANGUNANDESATOTALBIAYA, 
 wxID_RPJMPEMBANGUNANDESAVOLUME0, wxID_RPJMPEMBANGUNANDESAVOLUME1, 
 wxID_RPJMPEMBANGUNANDESAVOLUME2, wxID_RPJMPEMBANGUNANDESAVOLUME3, 
 wxID_RPJMPEMBANGUNANDESAVOLUME4, wxID_RPJMPEMBANGUNANDESAVOLUME5, 
 wxID_RPJMPEMBANGUNANDESAWAKTU1, wxID_RPJMPEMBANGUNANDESAWAKTU2, 
 wxID_RPJMPEMBANGUNANDESAWAKTU3, wxID_RPJMPEMBANGUNANDESAWAKTU4, 
 wxID_RPJMPEMBANGUNANDESAWAKTU5, wxID_RPJMPEMBANGUNANDESAWAKTU6, 
] = [wx.NewId() for _init_ctrls in range(76)]

class rpjmpembangunandesa(wx.Frame):
    def _init_coll_pembangunandesa_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT, heading='Norek',
              width=80)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT, heading='Uraian',
              width=400)

    def _init_coll_rpjmpembangunandesa_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT, heading='No',
              width=40)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT,
              heading='No Rekening', width=50)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT, heading='Uraian',
              width=400)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_LEFT, heading='Lokasi',
              width=100)
        parent.InsertColumn(col=4, format=wx.LIST_FORMAT_LEFT, heading='Volume',
              width=100)
        parent.InsertColumn(col=5, format=wx.LIST_FORMAT_LEFT, heading='Satuan',
              width=100)
        parent.InsertColumn(col=6, format=wx.LIST_FORMAT_LEFT,
              heading='Sasaran', width=100)
        parent.InsertColumn(col=7, format=wx.LIST_FORMAT_LEFT, heading='Biaya',
              width=100)
        parent.InsertColumn(col=8, format=wx.LIST_FORMAT_LEFT,
              heading='Pola Pelaksanaan', width=100)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_RPJMPEMBANGUNANDESA,
              name=u'rpjmpembangunandesa', parent=prnt, pos=wx.Point(388, 34),
              size=wx.Size(952, 675), style=wx.DEFAULT_FRAME_STYLE,
              title=u'RPJMDesa  Belanja Bidang Pelaksanaan Pembangunan Desa')
        self.SetClientSize(wx.Size(944, 645))
        self.SetBackgroundStyle(wx.BG_STYLE_SYSTEM)
        self.SetBackgroundColour(wx.Colour(192, 192, 192))
        self.Center(wx.BOTH)

        self.pendapatan = wx.StaticText(id=wxID_RPJMPEMBANGUNANDESAPENDAPATAN,
              label=u'2. BELANJA', name=u'pendapatan', parent=self,
              pos=wx.Point(8, 8), size=wx.Size(62, 13), style=0)
        self.pendapatan.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Tahoma'))
        self.pendapatan.SetForegroundColour(wx.Colour(0, 0, 0))

        self.aslidesa = wx.StaticText(id=wxID_RPJMPEMBANGUNANDESAASLIDESA,
              label=u'2.2. Bidang Pelaksanaan Pembangunan Desa',
              name=u'aslidesa', parent=self, pos=wx.Point(8, 24),
              size=wx.Size(251, 13), style=0)
        self.aslidesa.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Tahoma'))
        self.aslidesa.SetForegroundColour(wx.Colour(0, 0, 0))

        self.pembangunandesa = wx.ListCtrl(id=wxID_RPJMPEMBANGUNANDESAPEMBANGUNANDESA,
              name=u'pembangunandesa', parent=self, pos=wx.Point(8, 40),
              size=wx.Size(368, 320), style=wx.LC_REPORT)
        self._init_coll_pembangunandesa_Columns(self.pembangunandesa)
        self.pembangunandesa.Bind(wx.EVT_LIST_ITEM_SELECTED,
              self.OnPembangunandesaListItemSelected,
              id=wxID_RPJMPEMBANGUNANDESAPEMBANGUNANDESA)

        self.staticText2 = wx.StaticText(id=wxID_RPJMPEMBANGUNANDESASTATICTEXT2,
              label=u'Nomor Rekening', name='staticText2', parent=self,
              pos=wx.Point(384, 96), size=wx.Size(79, 13), style=0)

        self.norek = wx.TextCtrl(id=wxID_RPJMPEMBANGUNANDESANOREK,
              name=u'norek', parent=self, pos=wx.Point(512, 96),
              size=wx.Size(96, 21), style=0, value=u'')

        self.staticText3 = wx.StaticText(id=wxID_RPJMPEMBANGUNANDESASTATICTEXT3,
              label=u'Jenis Kegiatan', name='staticText3', parent=self,
              pos=wx.Point(384, 120), size=wx.Size(69, 13), style=0)

        self.kegiatan = wx.TextCtrl(id=wxID_RPJMPEMBANGUNANDESAKEGIATAN,
              name=u'kegiatan', parent=self, pos=wx.Point(513, 120),
              size=wx.Size(424, 21), style=0, value=u'')

        self.tambah = wx.Button(id=wxID_RPJMPEMBANGUNANDESATAMBAH,
              label=u'Tambah Data', name=u'tambah', parent=self,
              pos=wx.Point(551, 336), size=wx.Size(88, 23), style=0)
        self.tambah.SetForegroundColour(wx.Colour(0, 0, 0))
        self.tambah.Bind(wx.EVT_BUTTON, self.OnTambahButton,
              id=wxID_RPJMPEMBANGUNANDESATAMBAH)

        self.edit = wx.Button(id=wxID_RPJMPEMBANGUNANDESAEDIT,
              label=u'Edit Data', name=u'edit', parent=self, pos=wx.Point(647,
              336), size=wx.Size(88, 23), style=0)
        self.edit.Bind(wx.EVT_BUTTON, self.OnEditButton,
              id=wxID_RPJMPEMBANGUNANDESAEDIT)

        self.menu = wx.Button(id=wxID_RPJMPEMBANGUNANDESAMENU,
              label=u'Kembali Ke Menu', name=u'menu', parent=self,
              pos=wx.Point(824, 336), size=wx.Size(112, 23), style=0)
        self.menu.Bind(wx.EVT_BUTTON, self.OnMenuButton,
              id=wxID_RPJMPEMBANGUNANDESAMENU)

        self.staticText1 = wx.StaticText(id=wxID_RPJMPEMBANGUNANDESASTATICTEXT1,
              label=u'Lokasi (RT/RW/DESA)', name='staticText1', parent=self,
              pos=wx.Point(386, 148), size=wx.Size(105, 13), style=0)

        self.staticText4 = wx.StaticText(id=wxID_RPJMPEMBANGUNANDESASTATICTEXT4,
              label=u'Perkiraan Volume', name='staticText4', parent=self,
              pos=wx.Point(384, 168), size=wx.Size(83, 13), style=0)

        self.staticText5 = wx.StaticText(id=wxID_RPJMPEMBANGUNANDESASTATICTEXT5,
              label=u'Sasaran/Manfaat', name='staticText5', parent=self,
              pos=wx.Point(384, 218), size=wx.Size(84, 12), style=0)

        self.sasaran = wx.TextCtrl(id=wxID_RPJMPEMBANGUNANDESASASARAN,
              name=u'sasaran', parent=self, pos=wx.Point(512, 213),
              size=wx.Size(425, 21), style=0, value=u'')

        self.staticText7 = wx.StaticText(id=wxID_RPJMPEMBANGUNANDESASTATICTEXT7,
              label=u'Sumber Dana & Biaya', name='staticText7', parent=self,
              pos=wx.Point(384, 240), size=wx.Size(97, 13), style=0)

        self.staticText9 = wx.StaticText(id=wxID_RPJMPEMBANGUNANDESASTATICTEXT9,
              label=u'Prakiraan Pola Pelaksaan', name='staticText9',
              parent=self, pos=wx.Point(384, 311), size=wx.Size(120, 13),
              style=0)

        self.carinorek = wx.TextCtrl(id=wxID_RPJMPEMBANGUNANDESACARINOREK,
              name=u'carinorek', parent=self, pos=wx.Point(512, 72),
              size=wx.Size(96, 21), style=0, value=u'')

        self.staticText10 = wx.StaticText(id=wxID_RPJMPEMBANGUNANDESASTATICTEXT10,
              label=u'Nomor Record', name='staticText10', parent=self,
              pos=wx.Point(384, 72), size=wx.Size(69, 13), style=0)
        self.staticText10.SetForegroundColour(wx.Colour(0, 0, 0))

        self.rpjmpembangunandesa = wx.ListCtrl(id=wxID_RPJMPEMBANGUNANDESARPJMPEMBANGUNANDESA,
              name=u'rpjmpembangunandesa', parent=self, pos=wx.Point(8, 368),
              size=wx.Size(928, 272), style=wx.LC_REPORT)
        self._init_coll_rpjmpembangunandesa_Columns(self.rpjmpembangunandesa)
        self.rpjmpembangunandesa.Bind(wx.EVT_LIST_ITEM_SELECTED,
              self.OnRpjmpembangunandesaListItemSelected,
              id=wxID_RPJMPEMBANGUNANDESARPJMPEMBANGUNANDESA)

        self.pola = wx.ComboBox(choices=['Swakelola', 'Kerjasama Antar Desa',
              'Kerjasama Pihak Ketiga'], id=wxID_RPJMPEMBANGUNANDESAPOLA,
              name=u'pola', parent=self, pos=wx.Point(512, 309),
              size=wx.Size(424, 21), style=0, value=u'')
        self.pola.SetLabel(u'')

        self.staticText13 = wx.StaticText(id=wxID_RPJMPEMBANGUNANDESASTATICTEXT13,
              label=u'Tahun Awal RPJMDES', name='staticText13', parent=self,
              pos=wx.Point(622, 28), size=wx.Size(105, 13), style=0)
        self.staticText13.SetForegroundColour(wx.Colour(0, 0, 128))

        self.periode0 = wx.TextCtrl(id=wxID_RPJMPEMBANGUNANDESAPERIODE0,
              name=u'periode0', parent=self, pos=wx.Point(736, 24),
              size=wx.Size(64, 21), style=0, value=u'')

        self.button2 = wx.Button(id=wxID_RPJMPEMBANGUNANDESABUTTON2,
              label=u'Buat RPJMDesa', name='button2', parent=self,
              pos=wx.Point(816, 24), size=wx.Size(104, 23), style=0)
        self.button2.SetForegroundColour(wx.Colour(0, 0, 160))
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_RPJMPEMBANGUNANDESABUTTON2)

        self.staticBox1 = wx.StaticBox(id=wxID_RPJMPEMBANGUNANDESASTATICBOX1,
              label=u'Pertama Yang Di Isi', name='staticBox1', parent=self,
              pos=wx.Point(608, 0), size=wx.Size(328, 64), style=0)
        self.staticBox1.SetForegroundColour(wx.Colour(255, 0, 0))

        self.staticText11 = wx.StaticText(id=wxID_RPJMPEMBANGUNANDESASTATICTEXT11,
              label=u'1.', name='staticText11', parent=self, pos=wx.Point(500,
              168), size=wx.Size(10, 13), style=0)
        self.staticText11.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Tahoma'))

        self.waktu2 = wx.TextCtrl(id=wxID_RPJMPEMBANGUNANDESAWAKTU2,
              name=u'waktu2', parent=self, pos=wx.Point(562, 190),
              size=wx.Size(40, 21), style=0, value=u'')
        self.waktu2.Bind(wx.EVT_TEXT, self.OnWaktu2Text,
              id=wxID_RPJMPEMBANGUNANDESAWAKTU2)

        self.staticText14 = wx.StaticText(id=wxID_RPJMPEMBANGUNANDESASTATICTEXT14,
              label=u'2.', name='staticText14', parent=self, pos=wx.Point(499,
              192), size=wx.Size(10, 13), style=0)
        self.staticText14.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Tahoma'))

        self.waktu3 = wx.TextCtrl(id=wxID_RPJMPEMBANGUNANDESAWAKTU3,
              name=u'waktu3', parent=self, pos=wx.Point(673, 166),
              size=wx.Size(40, 21), style=0, value=u'')

        self.staticText15 = wx.StaticText(id=wxID_RPJMPEMBANGUNANDESASTATICTEXT15,
              label=u'3.', name='staticText15', parent=self, pos=wx.Point(613,
              168), size=wx.Size(10, 13), style=0)
        self.staticText15.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Tahoma'))

        self.waktu4 = wx.TextCtrl(id=wxID_RPJMPEMBANGUNANDESAWAKTU4,
              name=u'waktu4', parent=self, pos=wx.Point(673, 190),
              size=wx.Size(40, 21), style=0, value=u'')

        self.staticText16 = wx.StaticText(id=wxID_RPJMPEMBANGUNANDESASTATICTEXT16,
              label=u'4.', name='staticText16', parent=self, pos=wx.Point(614,
              192), size=wx.Size(10, 13), style=0)
        self.staticText16.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Tahoma'))

        self.waktu5 = wx.TextCtrl(id=wxID_RPJMPEMBANGUNANDESAWAKTU5,
              name=u'waktu5', parent=self, pos=wx.Point(782, 168),
              size=wx.Size(40, 21), style=0, value=u'')

        self.staticText17 = wx.StaticText(id=wxID_RPJMPEMBANGUNANDESASTATICTEXT17,
              label=u'5.', name='staticText17', parent=self, pos=wx.Point(723,
              168), size=wx.Size(10, 13), style=0)
        self.staticText17.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Tahoma'))

        self.waktu6 = wx.TextCtrl(id=wxID_RPJMPEMBANGUNANDESAWAKTU6,
              name=u'waktu6', parent=self, pos=wx.Point(782, 191),
              size=wx.Size(40, 21), style=0, value=u'')

        self.staticText18 = wx.StaticText(id=wxID_RPJMPEMBANGUNANDESASTATICTEXT18,
              label=u'6.', name='staticText18', parent=self, pos=wx.Point(724,
              192), size=wx.Size(10, 13), style=0)
        self.staticText18.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Tahoma'))

        self.waktu1 = wx.TextCtrl(id=wxID_RPJMPEMBANGUNANDESAWAKTU1,
              name=u'waktu1', parent=self, pos=wx.Point(562, 167),
              size=wx.Size(40, 21), style=0, value=u'')
        self.waktu1.Bind(wx.EVT_TEXT, self.OnWaktu1Text,
              id=wxID_RPJMPEMBANGUNANDESAWAKTU1)

        self.biaya1 = wx.TextCtrl(id=wxID_RPJMPEMBANGUNANDESABIAYA1,
              name=u'biaya1', parent=self, pos=wx.Point(638, 261),
              size=wx.Size(80, 21), style=0, value=u'')
        self.biaya1.Bind(wx.EVT_TEXT, self.OnBiaya1Text,
              id=wxID_RPJMPEMBANGUNANDESABIAYA1)

        self.volume1 = wx.TextCtrl(id=wxID_RPJMPEMBANGUNANDESAVOLUME1,
              name=u'volume1', parent=self, pos=wx.Point(512, 191),
              size=wx.Size(30, 21), style=0, value=u'')
        self.volume1.Bind(wx.EVT_TEXT, self.OnVolume1Text,
              id=wxID_RPJMPEMBANGUNANDESAVOLUME1)

        self.jumlahvolume = wx.TextCtrl(id=wxID_RPJMPEMBANGUNANDESAJUMLAHVOLUME,
              name=u'jumlahvolume', parent=self, pos=wx.Point(883, 191),
              size=wx.Size(56, 21), style=0, value=u'')

        self.nomor = wx.TextCtrl(id=wxID_RPJMPEMBANGUNANDESANOMOR,
              name=u'nomor', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(100, 21), style=0, value=u'')

        self.hapus = wx.Button(id=wxID_RPJMPEMBANGUNANDESAHAPUS,
              label=u'Hapus Data', name=u'hapus', parent=self, pos=wx.Point(744,
              336), size=wx.Size(75, 23), style=0)
        self.hapus.Bind(wx.EVT_BUTTON, self.OnHapusButton,
              id=wxID_RPJMPEMBANGUNANDESAHAPUS)

        self.staticText19 = wx.StaticText(id=wxID_RPJMPEMBANGUNANDESASTATICTEXT19,
              label=u'Th', name='staticText19', parent=self, pos=wx.Point(545,
              168), size=wx.Size(13, 13), style=0)

        self.volume2 = wx.TextCtrl(id=wxID_RPJMPEMBANGUNANDESAVOLUME2,
              name=u'volume2', parent=self, pos=wx.Point(625, 167),
              size=wx.Size(30, 21), style=0, value=u'')
        self.volume2.Bind(wx.EVT_TEXT, self.OnVolume2Text,
              id=wxID_RPJMPEMBANGUNANDESAVOLUME2)

        self.volume3 = wx.TextCtrl(id=wxID_RPJMPEMBANGUNANDESAVOLUME3,
              name=u'volume3', parent=self, pos=wx.Point(625, 190),
              size=wx.Size(30, 21), style=0, value=u'')
        self.volume3.Bind(wx.EVT_TEXT, self.OnVolume3Text,
              id=wxID_RPJMPEMBANGUNANDESAVOLUME3)

        self.volume4 = wx.TextCtrl(id=wxID_RPJMPEMBANGUNANDESAVOLUME4,
              name=u'volume4', parent=self, pos=wx.Point(733, 167),
              size=wx.Size(30, 21), style=0, value=u'')
        self.volume4.Bind(wx.EVT_TEXT, self.OnVolume4Text,
              id=wxID_RPJMPEMBANGUNANDESAVOLUME4)

        self.volume5 = wx.TextCtrl(id=wxID_RPJMPEMBANGUNANDESAVOLUME5,
              name=u'volume5', parent=self, pos=wx.Point(733, 191),
              size=wx.Size(30, 21), style=0, value=u'')
        self.volume5.Bind(wx.EVT_TEXT, self.OnVolume5Text,
              id=wxID_RPJMPEMBANGUNANDESAVOLUME5)

        self.volume0 = wx.TextCtrl(id=wxID_RPJMPEMBANGUNANDESAVOLUME0,
              name=u'volume0', parent=self, pos=wx.Point(512, 167),
              size=wx.Size(30, 21), style=0, value=u'')
        self.volume0.Bind(wx.EVT_TEXT, self.OnVolume0Text,
              id=wxID_RPJMPEMBANGUNANDESAVOLUME0)

        self.biaya2 = wx.TextCtrl(id=wxID_RPJMPEMBANGUNANDESABIAYA2,
              name=u'biaya2', parent=self, pos=wx.Point(638, 285),
              size=wx.Size(80, 21), style=0, value=u'')
        self.biaya2.Bind(wx.EVT_TEXT, self.OnBiaya2Text,
              id=wxID_RPJMPEMBANGUNANDESABIAYA2)

        self.biaya0 = wx.TextCtrl(id=wxID_RPJMPEMBANGUNANDESABIAYA0,
              name=u'biaya0', parent=self, pos=wx.Point(638, 237),
              size=wx.Size(80, 21), style=0, value=u'')
        self.biaya0.Bind(wx.EVT_TEXT, self.OnBiaya0Text,
              id=wxID_RPJMPEMBANGUNANDESABIAYA0)

        self.totalbiaya = wx.TextCtrl(id=wxID_RPJMPEMBANGUNANDESATOTALBIAYA,
              name=u'totalbiaya', parent=self, pos=wx.Point(793, 286),
              size=wx.Size(100, 20), style=0, value=u'')

        self.staticText6 = wx.StaticText(id=wxID_RPJMPEMBANGUNANDESASTATICTEXT6,
              label=u'Total Biaya', name='staticText6', parent=self,
              pos=wx.Point(729, 288), size=wx.Size(54, 13), style=0)

        self.staticText20 = wx.StaticText(id=wxID_RPJMPEMBANGUNANDESASTATICTEXT20,
              label=u'Th', name='staticText20', parent=self, pos=wx.Point(545,
              193), size=wx.Size(13, 13), style=0)

        self.staticText21 = wx.StaticText(id=wxID_RPJMPEMBANGUNANDESASTATICTEXT21,
              label=u'Th', name='staticText21', parent=self, pos=wx.Point(655,
              171), size=wx.Size(13, 13), style=0)

        self.staticText22 = wx.StaticText(id=wxID_RPJMPEMBANGUNANDESASTATICTEXT22,
              label=u'Th', name='staticText22', parent=self, pos=wx.Point(656,
              191), size=wx.Size(13, 13), style=0)

        self.staticText24 = wx.StaticText(id=wxID_RPJMPEMBANGUNANDESASTATICTEXT24,
              label=u'Satuan', name='staticText24', parent=self,
              pos=wx.Point(840, 168), size=wx.Size(35, 13), style=0)

        self.satuan = wx.TextCtrl(id=wxID_RPJMPEMBANGUNANDESASATUAN,
              name=u'satuan', parent=self, pos=wx.Point(883, 168),
              size=wx.Size(56, 21), style=0, value=u'')

        self.staticText25 = wx.StaticText(id=wxID_RPJMPEMBANGUNANDESASTATICTEXT25,
              label=u'Jumlah', name='staticText25', parent=self,
              pos=wx.Point(840, 192), size=wx.Size(33, 13), style=0)

        self.staticText8 = wx.StaticText(id=wxID_RPJMPEMBANGUNANDESASTATICTEXT8,
              label=u'Th', name='staticText8', parent=self, pos=wx.Point(766,
              171), size=wx.Size(13, 13), style=0)

        self.staticText26 = wx.StaticText(id=wxID_RPJMPEMBANGUNANDESASTATICTEXT26,
              label=u'Th', name='staticText26', parent=self, pos=wx.Point(767,
              194), size=wx.Size(13, 13), style=0)

        self.apbn = wx.ComboBox(choices=['Ya', 'Tidak'],
              id=wxID_RPJMPEMBANGUNANDESAAPBN, name=u'apbn', parent=self,
              pos=wx.Point(584, 238), size=wx.Size(51, 21), style=0, value=u'')
        self.apbn.SetLabel(u'')
        self.apbn.Bind(wx.EVT_COMBOBOX, self.OnApbnCombobox,
              id=wxID_RPJMPEMBANGUNANDESAAPBN)

        self.apbdes = wx.ComboBox(choices=['Ya', 'Tidak'],
              id=wxID_RPJMPEMBANGUNANDESAAPBDES, name=u'apbdes', parent=self,
              pos=wx.Point(584, 261), size=wx.Size(51, 21), style=0, value=u'')
        self.apbdes.SetLabel(u'')
        self.apbdes.Bind(wx.EVT_COMBOBOX, self.OnApbdesCombobox,
              id=wxID_RPJMPEMBANGUNANDESAAPBDES)

        self.lain = wx.ComboBox(choices=['Ya', 'Tidak'],
              id=wxID_RPJMPEMBANGUNANDESALAIN, name=u'lain', parent=self,
              pos=wx.Point(584, 285), size=wx.Size(51, 21), style=0, value=u'')
        self.lain.SetLabel(u'')
        self.lain.Bind(wx.EVT_COMBOBOX, self.OnLainCombobox,
              id=wxID_RPJMPEMBANGUNANDESALAIN)

        self.staticText12 = wx.StaticText(id=wxID_RPJMPEMBANGUNANDESASTATICTEXT12,
              label=u'1. APBN/ABPD', name='staticText12', parent=self,
              pos=wx.Point(500, 240), size=wx.Size(69, 13), style=0)

        self.staticText27 = wx.StaticText(id=wxID_RPJMPEMBANGUNANDESASTATICTEXT27,
              label=u'2. APBDesa', name='staticText27', parent=self,
              pos=wx.Point(501, 265), size=wx.Size(56, 13), style=0)

        self.staticText28 = wx.StaticText(id=wxID_RPJMPEMBANGUNANDESASTATICTEXT28,
              label=u'3. Lain-lain', name='staticText28', parent=self,
              pos=wx.Point(502, 289), size=wx.Size(52, 13), style=0)

        self.bersihkan = wx.Button(id=wxID_RPJMPEMBANGUNANDESABERSIHKAN,
              label=u'Bersihkan', name=u'bersihkan', parent=self,
              pos=wx.Point(384, 336), size=wx.Size(75, 23), style=0)
        self.bersihkan.Bind(wx.EVT_BUTTON, self.OnBersihkanButton,
              id=wxID_RPJMPEMBANGUNANDESABERSIHKAN)

        self.lokasi = wx.ComboBox(choices=['Desa', 'RT', 'RW', 'Dusun'],
              id=wxID_RPJMPEMBANGUNANDESALOKASI, name=u'lokasi', parent=self,
              pos=wx.Point(512, 144), size=wx.Size(103, 21), style=0,
              value=u'')
        self.lokasi.SetLabel(u'')

        self.jumlah = wx.TextCtrl(id=wxID_RPJMPEMBANGUNANDESAJUMLAH,
              name=u'jumlah', parent=self, pos=wx.Point(845, 70),
              size=wx.Size(88, 21), style=0, value=u'')

        self.staticText23 = wx.StaticText(id=wxID_RPJMPEMBANGUNANDESASTATICTEXT23,
              label=u'Total Biaya : Rp.', name='staticText23', parent=self,
              pos=wx.Point(751, 73), size=wx.Size(90, 13), style=0)
        self.staticText23.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Tahoma'))
        self.staticText23.SetForegroundColour(wx.Colour(0, 0, 0))

        self.biayaapbdes = wx.TextCtrl(id=wxID_RPJMPEMBANGUNANDESABIAYAAPBDES,
              name=u'biayaapbdes', parent=self, pos=wx.Point(798, 96),
              size=wx.Size(52, 21), style=0, value=u'')

        self.biayalain = wx.TextCtrl(id=wxID_RPJMPEMBANGUNANDESABIAYALAIN,
              name=u'biayalain', parent=self, pos=wx.Point(880, 96),
              size=wx.Size(52, 21), style=0, value=u'')

        self.biayaapbn = wx.TextCtrl(id=wxID_RPJMPEMBANGUNANDESABIAYAAPBN,
              name=u'biayaapbn', parent=self, pos=wx.Point(699, 96),
              size=wx.Size(52, 21), style=0, value=u'')

        self.staticText29 = wx.StaticText(id=wxID_RPJMPEMBANGUNANDESASTATICTEXT29,
              label=u'APBN/D', name='staticText29', parent=self,
              pos=wx.Point(651, 100), size=wx.Size(43, 13), style=0)
        self.staticText29.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Tahoma'))
        self.staticText29.SetForegroundColour(wx.Colour(0, 0, 0))

        self.staticText30 = wx.StaticText(id=wxID_RPJMPEMBANGUNANDESASTATICTEXT30,
              label=u'APBDES', name='staticText30', parent=self,
              pos=wx.Point(754, 100), size=wx.Size(43, 13), style=0)
        self.staticText30.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Tahoma'))
        self.staticText30.SetForegroundColour(wx.Colour(0, 0, 0))

        self.staticText31 = wx.StaticText(id=wxID_RPJMPEMBANGUNANDESASTATICTEXT31,
              label=u'LAIN', name='staticText31', parent=self, pos=wx.Point(852,
              100), size=wx.Size(26, 13), style=0)
        self.staticText31.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Tahoma'))
        self.staticText31.SetForegroundColour(wx.Colour(0, 0, 0))

    def __init__(self, parent):
        
        self._init_ctrls(parent)
        self.carinorek.SetValue('')
        self.norek.SetValue('')
        self.kegiatan.SetValue('')
        self.lokasi.SetValue('')
        self.waktu1.SetValue('')
        self.waktu2.SetValue('')
        self.waktu3.SetValue('')
        self.waktu4.SetValue('')
        self.waktu5.SetValue('')
        self.waktu6.SetValue('')
        self.satuan.SetValue('')
        self.sasaran.SetValue('')
        self.pola.SetValue('')
        self.periode0.SetValue('0')
        
        self.volume0.SetValue('0')
        self.volume1.SetValue('0')
        self.volume2.SetValue('0')
        self.volume3.SetValue('0')
        self.volume4.SetValue('0')
        self.volume5.SetValue('0')

        self.biaya0.SetValue('0')
        self.biaya1.SetValue('0')
        self.biaya2.SetValue('0')
        
        rvolume0=int(self.volume0.GetValue())
        rvolume1=int(self.volume1.GetValue())
        rvolume2=int(self.volume2.GetValue())
        rvolume3=int(self.volume3.GetValue())
        rvolume4=int(self.volume4.GetValue())
        rvolume5=int(self.volume5.GetValue())
        
        self.biaya0.Disable()
        self.biaya1.Disable()
        self.biaya2.Disable()
        
        self.carinorek.Disable()
        self.norek.Disable()
        self.kegiatan.Disable()
        self.lokasi.Disable()
        self.jumlah.Disable()
        self.biayaapbn.Disable()
        self.biayaapbdes.Disable()
        self.biayalain.Disable()
        
    def awal(self):
        self.IsiList()
        self.IsiList1()
        ambilper=str(self.periode0.GetValue())
        sql1="SELECT sum(totalbiaya) FROM rpjmdesasid WHERE norek LIKE '2.2%' AND periode='"+ambilper+"'"
        cur.execute(sql1)
        hasil1=cur.fetchone()
        self.jumlah.SetValue(str(hasil1[0]))
        
        sql2="SELECT sum(biaya0) FROM rpjmdesasid WHERE norek LIKE '2.2%' AND periode='"+ambilper+"'"
        cur.execute(sql2)
        hasil2=cur.fetchone()
        self.biayaapbn.SetValue(str(hasil2[0]))
        
        sql3="SELECT sum(biaya1) FROM rpjmdesasid WHERE norek LIKE '2.2%' AND periode='"+ambilper+"'"
        cur.execute(sql3)
        hasil3=cur.fetchone()
        self.biayaapbdes.SetValue(str(hasil3[0]))
        
        sql4="SELECT sum(biaya2) FROM rpjmdesasid WHERE norek LIKE '2.2%' AND periode='"+ambilper+"'"
        cur.execute(sql4)
        hasil4=cur.fetchone()
        self.biayalain.SetValue(str(hasil4[0]))
        
        
        
#-------------------------------------------------------------------------------
#Isi Daftar Kanan
#-------------------------------------------------------------------------------
        

    def IsiList(self): 
        self.pembangunandesa.DeleteAllItems()    
        sql = "SELECT * FROM koderek WHERE kode='2.2'"
        cur.execute(sql) 
        hasil = cur.fetchall() 
        no_rek = self.pembangunandesa.GetItemCount() 
        for i in hasil : 
            self.pembangunandesa.InsertStringItem(no_rek, "%s"%i[2]) 
            self.pembangunandesa.SetStringItem(no_rek,1,"%s"%i[3]) 
            no_rek = no_rek + 1
#-------------------------------------------------------------------------------
#Isi Daftar Bawah
#-------------------------------------------------------------------------------
    
    def IsiList1(self):
        rperiode = str(self.periode0.GetValue()) 
        self.rpjmpembangunandesa.DeleteAllItems()    
        sql1 = "SELECT * FROM rpjmdesasid WHERE norek LIKE '2.2%' AND periode='"+(rperiode)+"' AND id_rkp='0' ORDER BY REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(norek,'1', '0'),'2', '0'), '3', '0'), '4', '0'), '5', '0'), '6', '0'), '7', '0'), '8', '0'),  '9', '0') ASC "
        cur.execute(sql1) 
        hasil = cur.fetchall() 
        no_rek1 = self.rpjmpembangunandesa.GetItemCount() 
        for i in hasil : 
            self.rpjmpembangunandesa.InsertStringItem(no_rek1, "%s"%i[0])   #norek
            self.rpjmpembangunandesa.SetStringItem(no_rek1,1,"%s"%i[1])
            self.rpjmpembangunandesa.SetStringItem(no_rek1,2,"%s"%i[2])     #kegiatan   
            self.rpjmpembangunandesa.SetStringItem(no_rek1,3,"%s"%i[3])     #lokasi
            self.rpjmpembangunandesa.SetStringItem(no_rek1,4,"%s"%i[10])     #volume
            self.rpjmpembangunandesa.SetStringItem(no_rek1,5,"%s"%i[11])     #satuan
            self.rpjmpembangunandesa.SetStringItem(no_rek1,6,"%s"%i[18])   #sasaran
            self.rpjmpembangunandesa.SetStringItem(no_rek1,7,"%s"%i[25])    #biaya
            self.rpjmpembangunandesa.SetStringItem(no_rek1,8,"%s"%i[26])   #pola
            no_rek1 = no_rek1 + 1    
#-------------------------------------------------------------------------------
#Isi Form dari Kiri
#-------------------------------------------------------------------------------
    
    def kiri(self) : 
        self.norek.SetValue('')
        self.kegiatan.SetValue('')
        self.lokasi.SetValue('')
        self.satuan.SetValue('')
        self.sasaran.SetValue('')
        self.waktu1.SetValue('')
        self.waktu2.SetValue('')
        self.waktu3.SetValue('')
        self.waktu4.SetValue('')
        self.waktu5.SetValue('')
        self.waktu6.SetValue('')
        self.pola.SetValue('')
        self.volume0.SetValue('0')
        self.volume1.SetValue('0')
        self.volume2.SetValue('0')
        self.volume3.SetValue('0')
        self.volume4.SetValue('0')
        self.volume5.SetValue('0')
        self.biaya0.SetValue('0')
        self.biaya1.SetValue('0')
        self.biaya2.SetValue('0')
        self.jumlahvolume.SetValue('0')
        self.totalbiaya.SetValue('0')
        self.apbn.SetValue('Tidak')
        self.apbdes.SetValue('Tidak')
        self.lain.SetValue('Tidak')
        self.biaya0.Disable()
        self.biaya1.Disable()
        self.biaya2.Disable()
        
        rperiode0 = str(self.periode0.GetValue())
        rrange=int(rperiode0)
        self.waktu1.SetValue(str(rrange+0))
        self.waktu2.SetValue(str(rrange+1))
        self.waktu3.SetValue(str(rrange+2))
        self.waktu4.SetValue(str(rrange+3))
        self.waktu5.SetValue(str(rrange+4))
        self.waktu6.SetValue(str(rrange+5))
        
        self.tambah.Enable()
        self.edit.Disable()
        self.hapus.Disable()
        self.lokasi.Enable()
        
        carinomor=str(self.carinorek.GetValue())
        sql="SELECT * FROM koderek WHERE norek='%s'"%(carinomor)
        cur.execute(sql)
        hasil = cur.fetchone()  
        if hasil :
            self.carinorek.SetValue(str(hasil[0]))
            self.norek.SetValue(str(hasil[2]))
            self.kegiatan.SetValue(str(hasil[3]))
            
        else : 
            self.pesan = wx.MessageDialog(self,"Data Tidak Ada","Konfirmasi",wx.OK) 
            self.pesan.ShowModal() 
            self.carinorek.Clear()
            self.carinorek.SetFocus()
#-------------------------------------------------------------------------------
#Isi Form dari Bawah
#-------------------------------------------------------------------------------
    
    def bawah(self) : 
        self.norek.SetValue('')
        self.kegiatan.SetValue('')
        self.lokasi.SetValue('')
        self.satuan.SetValue('')
        self.sasaran.SetValue('')
        self.waktu1.SetValue('')
        self.waktu2.SetValue('')
        self.waktu3.SetValue('')
        self.waktu4.SetValue('')
        self.waktu5.SetValue('')
        self.waktu6.SetValue('')
        self.pola.SetValue('')
        self.volume0.SetValue('0')
        self.volume1.SetValue('0')
        self.volume2.SetValue('0')
        self.volume3.SetValue('0')
        self.volume4.SetValue('0')
        self.volume5.SetValue('0')
        self.biaya0.SetValue('0')
        self.biaya1.SetValue('0')
        self.biaya2.SetValue('0')
        self.jumlahvolume.SetValue('0')
        self.totalbiaya.SetValue('0')
        self.apbn.SetValue('Tidak')
        self.apbdes.SetValue('Tidak')
        self.lain.SetValue('Tidak')
        self.biaya0.Enable()
        self.biaya1.Enable()
        self.biaya2.Enable()
        
        rperiode0 = str(self.periode0.GetValue())
        rrange=int(rperiode0)
        self.waktu1.SetValue(str(rrange+0))
        self.waktu2.SetValue(str(rrange+1))
        self.waktu3.SetValue(str(rrange+2))
        self.waktu4.SetValue(str(rrange+3))
        self.waktu5.SetValue(str(rrange+4))
        self.waktu6.SetValue(str(rrange+5))
        
        self.tambah.Disable()
        self.edit.Enable()
        self.hapus.Enable()
        
        
        
        carinomor1=str(self.carinorek.GetValue())
        sql="SELECT * FROM rpjmdesasid WHERE no='%s'"%(carinomor1)
        cur.execute(sql)
        hasil = cur.fetchone()  
        if hasil :
            
            self.nomor.SetValue(str(hasil[0]))
            self.norek.SetValue(str(hasil[1]))
            self.kegiatan.SetValue(str(hasil[2]))
            self.lokasi.SetValue(str(hasil[3]))
            self.volume0.SetValue(str(hasil[4]))
            self.volume1.SetValue(str(hasil[5]))
            self.volume2.SetValue(str(hasil[6]))
            self.volume3.SetValue(str(hasil[7]))
            self.volume4.SetValue(str(hasil[8]))
            self.volume5.SetValue(str(hasil[9]))
            self.jumlahvolume.SetValue(str(hasil[10]))
            self.satuan.SetValue(str(hasil[11]))
            self.waktu1.SetValue(str(hasil[12]))
            self.waktu2.SetValue(str(hasil[13]))
            self.waktu3.SetValue(str(hasil[14]))
            self.waktu4.SetValue(str(hasil[15]))
            self.waktu5.SetValue(str(hasil[16]))
            self.waktu6.SetValue(str(hasil[17]))
            self.sasaran.SetValue(str(hasil[18]))
            self.apbn.SetValue(str(hasil[19]))
            self.apbdes.SetValue(str(hasil[20]))
            self.lain.SetValue(str(hasil[21]))
            self.biaya0.SetValue(str(hasil[22]))
            self.biaya1.SetValue(str(hasil[23]))
            self.biaya2.SetValue(str(hasil[24]))
            self.totalbiaya.SetValue(str(hasil[25]))
            self.pola.SetValue(str(hasil[26]))
            
            self.totalbiaya.Disable()
            self.jumlahvolume.Disable()
            self.lokasi.Disable()
            
        else : 
            self.pesan = wx.MessageDialog(self,"Data Tidak Ada","Konfirmasi",wx.OK) 
            self.pesan.ShowModal() 
            self.carinorek.Clear()
            self.carinorek.SetFocus()
#-------------------------------------------------------------------------------
#Daftar Kanan
#-------------------------------------------------------------------------------
    
    def OnPembangunandesaListItemSelected(self, event):
        self.currentItem = event.m_itemIndex 
        b=self.pembangunandesa.GetItem(self.currentItem).GetText() 
        self.carinorek.SetValue(b)
        self.kiri()
#-------------------------------------------------------------------------------
#Daftar Bawah
#-------------------------------------------------------------------------------
    
    def OnRpjmpembangunandesaListItemSelected(self, event):
        self.currentItem = event.m_itemIndex 
        b=self.rpjmpembangunandesa.GetItem(self.currentItem).GetText() 
        self.carinorek.SetValue(b)
        self.bawah()
#-------------------------------------------------------------------------------
#Kembali Kemenu
#-------------------------------------------------------------------------------
    def OnMenuButton(self, event):
        self.Close()
        self.Destroy()
        db.commit()
#-------------------------------------------------------------------------------
#Tamabah Data 
#-------------------------------------------------------------------------------

    def OnTambahButton(self, event):
        rnorek=str(self.norek.GetValue())
        rkegiatan=str(self.kegiatan.GetValue())
        rlokasi=str(self.lokasi.GetValue())
        rvolume0=str(self.volume0.GetValue())
        rvolume1=str(self.volume1.GetValue())
        rvolume2=str(self.volume2.GetValue())
        rvolume3=str(self.volume3.GetValue())
        rvolume4=str(self.volume4.GetValue())
        rvolume5=str(self.volume5.GetValue())
        rjumlahvolume=str(self.jumlahvolume.GetValue())
        rsatuan=str(self.satuan.GetValue())
        rwaktu1=str(self.waktu1.GetValue())
        rwaktu2=str(self.waktu2.GetValue())
        rwaktu3=str(self.waktu3.GetValue())
        rwaktu4=str(self.waktu4.GetValue())
        rwaktu5=str(self.waktu5.GetValue())
        rwaktu6=str(self.waktu6.GetValue())
        rsasaran=str(self.sasaran.GetValue())
        rapbn=str(self.apbn.GetValue())
        rapbdes=str(self.apbdes.GetValue())
        rlain=str(self.lain.GetValue())
        rbiaya0=str(self.biaya0.GetValue())
        rbiaya1=str(self.biaya1.GetValue())
        rbiaya2=str(self.biaya2.GetValue())
        rtotalbiaya=str(self.totalbiaya.GetValue())
        rpola=str(self.pola.GetValue())
        rperiode = str(self.periode0.GetValue())
        
        if rnorek == '':
            self.pesan = wx.MessageDialog(self,"Nomor Rekening Jangan Kosong","Peringatan",wx.OK) 
            self.pesan.ShowModal()
        elif rkegiatan == '':
            self.pesan = wx.MessageDialog(self,"Nama Kegiatan Jangan Kosong","Peringatan",wx.OK) 
            self.pesan.ShowModal()
        elif rlokasi == '':
            self.pesan = wx.MessageDialog(self,"Nama Lokasi Jangan Kosong","Peringatan",wx.OK) 
            self.pesan.ShowModal()
        else:
            sql="SELECT * FROM rpjmdesasid WHERE norek='"+rnorek+"' AND lokasi='"+rlokasi+"'" 
            cur.execute(sql)
            hasil = cur.fetchone()  
            if hasil :   
                self.pesan = wx.MessageDialog(self,"Nomor Rekening Dan Lokasi Yang Sama Sudah Ada di RPJMDES","Peringatan",wx.OK) 
                self.pesan.ShowModal()
                self.lokasi.SetFocus()
            else:     
                add_kejadian="INSERT INTO rpjmdesasid (norek,kegiatan,lokasi,volume0,volume1,volume2,volume3,volume4,volume5,jumlahvolume,satuan,waktu1,waktu2,waktu3,waktu4,waktu5,waktu6,sasaran,apbn,apbdes,lain,biaya0,biaya1,biaya2,totalbiaya,pola,id_rkp,periode,diambil1,diambil2,diambil3,diambil4,diambil5,diambil6,jumlahsisa1,ambilapbn,ambilapbdes,ambillain,jumlahdiambil)  VALUES ('"+(rnorek)+"','"+(rkegiatan)+"','"+(rlokasi)+"','"+(rvolume0)+"','"+(rvolume1)+"','"+(rvolume2)+"','"+(rvolume3)+"','"+(rvolume4)+"','"+(rvolume5)+"','"+(rjumlahvolume)+"','"+(rsatuan)+"','"+(rwaktu1)+"','"+(rwaktu2)+"','"+(rwaktu3)+"','"+(rwaktu4)+"','"+(rwaktu5)+"','"+(rwaktu6)+"','"+(rsasaran)+"','"+(rapbn)+"','"+(rapbdes)+"','"+(rlain)+"','"+(rbiaya0)+"','"+(rbiaya1)+"','"+(rbiaya2)+"','"+(rtotalbiaya)+"','"+(rpola)+"','0','"+(rperiode)+"','0','0','0','0','0','0','0','0','0','0','0')"
                cur.execute(add_kejadian)
                db.commit()
                self.pesan = wx.MessageDialog(self,"Data  Sudah Tersimpan","Konfirmasi",wx.OK) 
                self.pesan.ShowModal()
                self.carinorek.SetValue('')
                self.norek.SetValue('')
                self.kegiatan.SetValue('')
                self.lokasi.SetValue('')
                self.satuan.SetValue('')
                self.sasaran.SetValue('')
                self.waktu1.SetValue('')
                self.waktu2.SetValue('')
                self.waktu3.SetValue('')
                self.waktu4.SetValue('')
                self.waktu5.SetValue('')
                self.waktu6.SetValue('')
                self.pola.SetValue('')
                self.volume0.SetValue('0')
                self.volume1.SetValue('0')
                self.volume2.SetValue('0')
                self.volume3.SetValue('0')
                self.volume4.SetValue('0')
                self.volume5.SetValue('0')
                self.biaya0.SetValue('0')
                self.biaya1.SetValue('0')
                self.biaya2.SetValue('0')
                self.jumlahvolume.SetValue('0')
                self.totalbiaya.SetValue('0')
                self.apbn.SetValue('Tidak')
                self.apbdes.SetValue('Tidak')
                self.lain.SetValue('Tidak')
                self.awal()
#-------------------------------------------------------------------------------
#Edit
#-------------------------------------------------------------------------------
                        
    def OnEditButton(self, event):
        rnorek=str(self.norek.GetValue())
        rkegiatan=str(self.kegiatan.GetValue())
        rlokasi=str(self.lokasi.GetValue())
        rvolume0=str(self.volume0.GetValue())
        rvolume1=str(self.volume1.GetValue())
        rvolume2=str(self.volume2.GetValue())
        rvolume3=str(self.volume3.GetValue())
        rvolume4=str(self.volume4.GetValue())
        rvolume5=str(self.volume5.GetValue())
        rjumlahvolume=str(self.jumlahvolume.GetValue())
        rsatuan=str(self.satuan.GetValue())
        rwaktu1=str(self.waktu1.GetValue())
        rwaktu2=str(self.waktu2.GetValue())
        rwaktu3=str(self.waktu3.GetValue())
        rwaktu4=str(self.waktu4.GetValue())
        rwaktu5=str(self.waktu5.GetValue())
        rwaktu6=str(self.waktu6.GetValue())
        rsasaran=str(self.sasaran.GetValue())
        rapbn=str(self.apbn.GetValue())
        rapbdes=str(self.apbdes.GetValue())
        rlain=str(self.lain.GetValue())
        rbiaya0=str(self.biaya0.GetValue())
        rbiaya1=str(self.biaya1.GetValue())
        rbiaya2=str(self.biaya2.GetValue())
        rtotalbiaya=str(self.totalbiaya.GetValue())
        rpola=str(self.pola.GetValue())
        rperiode = str(self.periode0.GetValue())
        rnomoran=str(self.nomor.GetValue())
        
        sql="SELECT * FROM rkpsid WHERE norek='"+rnorek+"' AND lokasi='"+rlokasi+"' AND id_rkp='1'"
        cur.execute(sql)
        hasil = cur.fetchone()
        db.commit() 
        if hasil:
            self.pesan = wx.MessageDialog(self,"Anda Tidak Bisa Mengedit\n Karena Rekening Sudah Terdapat di RKP \n Hapus Terlebih dahulu RKP Rekening Ini","Peringatan !!!",wx.OK) 
            self.pesan.ShowModal()
        else:    
                rnomoran = str(self.nomor.GetValue())
                ngedit="UPDATE rpjmdesasid SET norek='"+rnorek+"',kegiatan='"+rkegiatan+"',lokasi='"+rlokasi+"',volume0='"+rvolume0+"',volume1='"+rvolume1+"',volume2='"+rvolume2+"',volume3='"+rvolume3+"',volume4='"+rvolume4+"',volume5='"+rvolume5+"',jumlahvolume='"+rjumlahvolume+"',satuan='"+rsatuan+"',waktu1='"+rwaktu1+"',waktu2='"+rwaktu2+"',waktu3='"+rwaktu3+"',waktu4='"+rwaktu4+"',waktu5='"+rwaktu5+"',waktu6='"+rwaktu6+"',sasaran='"+rsasaran+"',apbn='"+rapbn+"',apbdes='"+rapbdes+"',lain='"+rlain+"',biaya0='"+rbiaya0+"',biaya1='"+rbiaya1+"',biaya2='"+rbiaya2+"',totalbiaya='"+rtotalbiaya+"',pola='"+rpola+"',periode='"+rperiode+"' WHERE no='"+rnomoran+"'"
                cur.execute(ngedit)
                db.commit()
                self.pesan = wx.MessageDialog(self,"Data Sudah Terupdate","Konfirmasi",wx.OK) 
                self.pesan.ShowModal()
                self.carinorek.SetValue('')
                self.norek.SetValue('')
                self.kegiatan.SetValue('')
                self.lokasi.SetValue('')
                self.satuan.SetValue('')
                self.sasaran.SetValue('')
                self.waktu1.SetValue('')
                self.waktu2.SetValue('')
                self.waktu3.SetValue('')
                self.waktu4.SetValue('')
                self.waktu5.SetValue('')
                self.waktu6.SetValue('')
                self.pola.SetValue('')
                self.volume0.SetValue('0')
                self.volume1.SetValue('0')
                self.volume2.SetValue('0')
                self.volume3.SetValue('0')
                self.volume4.SetValue('0')
                self.volume5.SetValue('0')
                self.biaya0.SetValue('0')
                self.biaya1.SetValue('0')
                self.biaya2.SetValue('0')
                self.jumlahvolume.SetValue('0')
                self.totalbiaya.SetValue('0')
                self.apbn.SetValue('Tidak')
                self.apbdes.SetValue('Tidak')
                self.lain.SetValue('Tidak')
                self.awal()
#-------------------------------------------------------------------------------
#Eksekusi Periode
#-------------------------------------------------------------------------------
    
    def OnButton2Button(self, event):
        self.carinorek.SetValue('')
        self.norek.SetValue('')
        self.kegiatan.SetValue('')
        self.lokasi.SetValue('')
        self.satuan.SetValue('')
        self.sasaran.SetValue('')
        self.waktu1.SetValue('')
        self.waktu2.SetValue('')
        self.waktu3.SetValue('')
        self.waktu4.SetValue('')
        self.waktu5.SetValue('')
        self.waktu6.SetValue('')
        self.pola.SetValue('')
        self.volume0.SetValue('0')
        self.volume1.SetValue('0')
        self.volume2.SetValue('0')
        self.volume3.SetValue('0')
        self.volume4.SetValue('0')
        self.volume5.SetValue('0')
        self.biaya0.SetValue('0')
        self.biaya1.SetValue('0')
        self.biaya2.SetValue('0')
        self.jumlahvolume.SetValue('0')
        self.totalbiaya.SetValue('0')
        self.apbn.SetValue('Tidak')
        self.apbdes.SetValue('Tidak')
        self.lain.SetValue('Tidak')
        rperiode0 = str(self.periode0.GetValue())
        rrange=int(rperiode0)
        self.waktu1.SetValue(str(rrange+0))
        self.waktu2.SetValue(str(rrange+1))
        self.waktu3.SetValue(str(rrange+2))
        self.waktu4.SetValue(str(rrange+3))
        self.waktu5.SetValue(str(rrange+4))
        self.waktu6.SetValue(str(rrange+5))
        self.waktu1.Disable()
        self.waktu2.Disable()
        self.waktu3.Disable()
        self.waktu4.Disable()
        self.waktu5.Disable()
        self.waktu6.Disable()
        self.awal()
#-------------------------------------------------------------------------------
#Hapus
#-------------------------------------------------------------------------------
        
    def OnHapusButton(self, event):
        rnomoran1 = str(self.nomor.GetValue())
        hapus="DELETE FROM rpjmdesasid WHERE no='"+rnomoran1+"'"
        cur.execute(hapus)
        db.commit()
        self.pesan = wx.MessageDialog(self,"Data Sudah Dihapus","Konfirmasi",wx.OK) 
        self.pesan.ShowModal()
        self.carinorek.SetValue('')
        self.norek.SetValue('')
        self.kegiatan.SetValue('')
        self.lokasi.SetValue('')
        self.satuan.SetValue('')
        self.sasaran.SetValue('')
        self.waktu1.SetValue('')
        self.waktu2.SetValue('')
        self.waktu3.SetValue('')
        self.waktu4.SetValue('')
        self.waktu5.SetValue('')
        self.waktu6.SetValue('')
        self.pola.SetValue('')
        self.volume0.SetValue('0')
        self.volume1.SetValue('0')
        self.volume2.SetValue('0')
        self.volume3.SetValue('0')
        self.volume4.SetValue('0')
        self.volume5.SetValue('0')
        self.biaya0.SetValue('0')
        self.biaya1.SetValue('0')
        self.biaya2.SetValue('0')
        self.jumlahvolume.SetValue('0')
        self.totalbiaya.SetValue('0')
        self.apbn.SetValue('Tidak')
        self.apbdes.SetValue('Tidak')
        self.lain.SetValue('Tidak')
        self.awal()
#-------------------------------------------------------------------------------

    def OnWaktu2Text(self, event):
        event.Skip()
#-------------------------------------------------------------------------------

    def OnWaktu1Text(self, event):
        event.Skip()
#-------------------------------------------------------------------------------
   
    def OnVolume0Text(self, event):
        rvolume0=str(self.volume0.GetValue())
        if rvolume0.isdigit():
            self.volume1.SetValue('0')
            self.volume2.SetValue('0')
            self.volume3.SetValue('0')
            self.volume4.SetValue('0')
            self.volume5.SetValue('0')
            rvolume1=str(self.volume1.GetValue())
            rvolume2=str(self.volume2.GetValue())
            rvolume3=str(self.volume3.GetValue())
            rvolume4=str(self.volume4.GetValue())
            rvolume5=str(self.volume5.GetValue())
            intvolume0=int(rvolume0)
            intvolume1=int(rvolume1)
            intvolume2=int(rvolume2)
            intvolume3=int(rvolume3)
            intvolume4=int(rvolume4)
            intvolume5=int(rvolume5)
            rtotal=rvolume0+rvolume1+rvolume2+rvolume3+rvolume4+rvolume5
            rtotal1=intvolume0 + intvolume1 + intvolume2 + intvolume3 + intvolume4 + intvolume5
            strtotal=str(rtotal)
            self.jumlahvolume.SetValue(str(rtotal1))
        elif rvolume0 =='':
            self.pesan = wx.MessageDialog(self,"hanya angka","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.volume0.SetValue('0')
        else:
            self.pesan = wx.MessageDialog(self,"hanya angka","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.volume0.SetValue('0')
#-------------------------------------------------------------------------------

    def OnVolume1Text(self, event):
        rvolume1=str(self.volume1.GetValue())
        if rvolume1.isdigit():
            self.volume2.SetValue('0')
            self.volume3.SetValue('0')
            self.volume4.SetValue('0')
            self.volume5.SetValue('0')
            rvolume0=str(self.volume0.GetValue())
            rvolume1=str(self.volume1.GetValue())
            rvolume2=str(self.volume2.GetValue())
            rvolume3=str(self.volume3.GetValue())
            rvolume4=str(self.volume4.GetValue())
            rvolume5=str(self.volume5.GetValue())
            intvolume0=int(rvolume0)
            intvolume1=int(rvolume1)
            intvolume2=int(rvolume2)
            intvolume3=int(rvolume3)
            intvolume4=int(rvolume4)
            intvolume5=int(rvolume5)
            rtotal=rvolume0+rvolume1+rvolume2+rvolume3+rvolume4+rvolume5
            rtotal1=intvolume0 + intvolume1 + intvolume2 + intvolume3 + intvolume4 + intvolume5
            strtotal=str(rtotal)
            self.jumlahvolume.SetValue(str(rtotal1))
        elif rvolume1 =='':
            self.pesan = wx.MessageDialog(self,"hanya angka","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.volume1.SetValue('0')
        else:
            self.pesan = wx.MessageDialog(self,"hanya angka","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.volume1.SetValue('0')
#-------------------------------------------------------------------------------

    def OnVolume2Text(self, event):
        rvolume2=str(self.volume2.GetValue())
        if rvolume2.isdigit():
            self.volume3.SetValue('0')
            self.volume4.SetValue('0')
            self.volume5.SetValue('0')
            rvolume0=str(self.volume0.GetValue())
            rvolume1=str(self.volume1.GetValue())
            rvolume2=str(self.volume2.GetValue())
            rvolume3=str(self.volume3.GetValue())
            rvolume4=str(self.volume4.GetValue())
            rvolume5=str(self.volume5.GetValue())
            intvolume0=int(rvolume0)
            intvolume1=int(rvolume1)
            intvolume2=int(rvolume2)
            intvolume3=int(rvolume3)
            intvolume4=int(rvolume4)
            intvolume5=int(rvolume5)
            rtotal=rvolume0+rvolume1+rvolume2+rvolume3+rvolume4+rvolume5
            rtotal1=intvolume0 + intvolume1 + intvolume2 + intvolume3 + intvolume4 + intvolume5
            strtotal=str(rtotal)
            self.jumlahvolume.SetValue(str(rtotal1))
        elif rvolume2 =='':
            self.pesan = wx.MessageDialog(self,"hanya angka","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.volume2.SetValue('0')
        else:
            self.pesan = wx.MessageDialog(self,"hanya angka","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.volume2.SetValue('0')
#-------------------------------------------------------------------------------

    def OnVolume3Text(self, event):
        rvolume3=str(self.volume3.GetValue())
        if rvolume3.isdigit():
            self.volume4.SetValue('0')
            self.volume5.SetValue('0')
            rvolume0=str(self.volume0.GetValue())
            rvolume1=str(self.volume1.GetValue())
            rvolume2=str(self.volume2.GetValue())
            rvolume3=str(self.volume3.GetValue())
            rvolume4=str(self.volume4.GetValue())
            rvolume5=str(self.volume5.GetValue())
            intvolume0=int(rvolume0)
            intvolume1=int(rvolume1)
            intvolume2=int(rvolume2)
            intvolume3=int(rvolume3)
            intvolume4=int(rvolume4)
            intvolume5=int(rvolume5)
            rtotal=rvolume0+rvolume1+rvolume2+rvolume3+rvolume4+rvolume5
            rtotal1=intvolume0 + intvolume1 + intvolume2 + intvolume3 + intvolume4 + intvolume5
            strtotal=str(rtotal)
            self.jumlahvolume.SetValue(str(rtotal1))
        elif rvolume3 =='':
            self.pesan = wx.MessageDialog(self,"hanya angka","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.volume3.SetValue('0')
        else:
            self.pesan = wx.MessageDialog(self,"hanya angka","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.volume3.SetValue('0')
#-------------------------------------------------------------------------------

    def OnVolume4Text(self, event):
        rvolume4=str(self.volume4.GetValue())
        if rvolume4.isdigit():
            self.volume5.SetValue('0')
            rvolume0=str(self.volume0.GetValue())
            rvolume1=str(self.volume1.GetValue())
            rvolume2=str(self.volume2.GetValue())
            rvolume3=str(self.volume3.GetValue())
            rvolume4=str(self.volume4.GetValue())
            rvolume5=str(self.volume5.GetValue())
            intvolume0=int(rvolume0)
            intvolume1=int(rvolume1)
            intvolume2=int(rvolume2)
            intvolume3=int(rvolume3)
            intvolume4=int(rvolume4)
            intvolume5=int(rvolume5)
            rtotal=rvolume0+rvolume1+rvolume2+rvolume3+rvolume4+rvolume5
            rtotal1=intvolume0 + intvolume1 + intvolume2 + intvolume3 + intvolume4 + intvolume5
            strtotal=str(rtotal)
            self.jumlahvolume.SetValue(str(rtotal1))
        elif rvolume4 =='':
            self.pesan = wx.MessageDialog(self,"hanya angka","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.volume4.SetValue('0')
        else:
            self.pesan = wx.MessageDialog(self,"hanya angka","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.volume4.SetValue('0')
#-------------------------------------------------------------------------------

    def OnVolume5Text(self, event):
        rvolume5=str(self.volume5.GetValue())
        if rvolume5.isdigit():
            rvolume0=str(self.volume0.GetValue())
            rvolume1=str(self.volume1.GetValue())
            rvolume2=str(self.volume2.GetValue())
            rvolume3=str(self.volume3.GetValue())
            rvolume4=str(self.volume4.GetValue())
            rvolume5=str(self.volume5.GetValue())
            intvolume0=int(rvolume0)
            intvolume1=int(rvolume1)
            intvolume2=int(rvolume2)
            intvolume3=int(rvolume3)
            intvolume4=int(rvolume4)
            intvolume5=int(rvolume5)
            rtotal=rvolume0+rvolume1+rvolume2+rvolume3+rvolume4+rvolume5
            rtotal1=intvolume0 + intvolume1 + intvolume2 + intvolume3 + intvolume4 + intvolume5
            strtotal=str(rtotal)
            self.jumlahvolume.SetValue(str(rtotal1))
        elif rvolume5 =='':
            self.pesan = wx.MessageDialog(self,"hanya angka","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.volume5.SetValue('0')
        else:
            self.pesan = wx.MessageDialog(self,"hanya angka","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.volume5.SetValue('0')
#-------------------------------------------------------------------------------
            
    def OnBiaya0Text(self, event):
        rbiaya0=str(self.biaya0.GetValue())
        if rbiaya0.isdigit():
            self.biaya1.SetValue('0')
            self.biaya2.SetValue('0')
            
            rbiaya0=str(self.biaya0.GetValue())
            rbiaya1=str(self.biaya1.GetValue())
            rbiaya2=str(self.biaya2.GetValue())
            intbiaya0=int(rbiaya0)
            intbiaya1=int(rbiaya1)
            intbiaya2=int(rbiaya2)
            rtotal=intbiaya0 + intbiaya1 + intbiaya2 
            strtotal=str(rtotal)
            self.totalbiaya.SetValue(str(rtotal))
        elif rbiaya0 =='':
            self.pesan = wx.MessageDialog(self,"hanya angka","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.biaya0.SetValue('0')
        else:
            self.pesan = wx.MessageDialog(self,"hanya angka","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.biaya0.SetValue('0')
#-------------------------------------------------------------------------------

    def OnBiaya1Text(self, event):
        rbiaya1=str(self.biaya1.GetValue())
        if rbiaya1.isdigit():
            self.biaya2.SetValue('0')
            rbiaya0=str(self.biaya0.GetValue())
            rbiaya1=str(self.biaya1.GetValue())
            rbiaya2=str(self.biaya2.GetValue())
            intbiaya0=int(rbiaya0)
            intbiaya1=int(rbiaya1)
            intbiaya2=int(rbiaya2)
            rtotal=intbiaya0 + intbiaya1 + intbiaya2 
            strtotal=str(rtotal)
            self.totalbiaya.SetValue(str(rtotal))
        elif rbiaya1 =='':
            self.pesan = wx.MessageDialog(self,"hanya angka","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.biaya1.SetValue('0')
        else:
            self.pesan = wx.MessageDialog(self,"hanya angka","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.biaya1.SetValue('0')
#-------------------------------------------------------------------------------

    def OnBiaya2Text(self, event):
        rbiaya2=str(self.biaya2.GetValue())
        if rbiaya2.isdigit():
            rbiaya0=str(self.biaya0.GetValue())
            rbiaya1=str(self.biaya1.GetValue())
            rbiaya2=str(self.biaya2.GetValue())
            intbiaya0=int(rbiaya0)
            intbiaya1=int(rbiaya1)
            intbiaya2=int(rbiaya2)
            rtotal=intbiaya0 + intbiaya1 + intbiaya2 
            strtotal=str(rtotal)
            self.totalbiaya.SetValue(str(rtotal))
        elif rbiaya2 =='':
            self.pesan = wx.MessageDialog(self,"hanya angka","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.biaya2.SetValue('0')
        else:
            self.pesan = wx.MessageDialog(self,"hanya angka","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.biaya2.SetValue('0')

    def OnApbnCombobox(self, event):
        apbnya=self.apbn.GetValue()
        if apbnya=='Ya':
            self.biaya0.Enable()
        else:
            self.biaya0.SetValue('0')
            self.biaya0.Disable()    

    def OnApbdesCombobox(self, event):
        apbnya=self.apbdes.GetValue()
        if apbnya=='Ya':
            self.biaya1.Enable()
        else:
            self.biaya1.SetValue('0')
            self.biaya1.Disable()
             
    def OnLainCombobox(self, event):
        apbnya=self.lain.GetValue()
        if apbnya=='Ya':
            self.biaya2.Enable()
        else:
            self.biaya2.SetValue('0')
            self.biaya2.Disable()

    def OnBersihkanButton(self, event):
        self.carinorek.SetValue('')
        self.norek.SetValue('')
        self.kegiatan.SetValue('')
        self.lokasi.SetValue('')
        self.satuan.SetValue('')
        self.sasaran.SetValue('')
        self.waktu1.SetValue('')
        self.waktu2.SetValue('')
        self.waktu3.SetValue('')
        self.waktu4.SetValue('')
        self.waktu5.SetValue('')
        self.waktu6.SetValue('')
        self.pola.SetValue('')
        self.volume0.SetValue('0')
        self.volume1.SetValue('0')
        self.volume2.SetValue('0')
        self.volume3.SetValue('0')
        self.volume4.SetValue('0')
        self.volume5.SetValue('0')
        self.biaya0.SetValue('0')
        self.biaya1.SetValue('0')
        self.biaya2.SetValue('0')
        self.jumlahvolume.SetValue('0')
        self.totalbiaya.SetValue('0')
        self.apbn.SetValue('Tidak')
        self.apbdes.SetValue('Tidak')
        self.lain.SetValue('Tidak')

        self.awal()
    
    
