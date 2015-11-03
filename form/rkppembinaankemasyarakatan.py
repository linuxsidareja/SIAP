#Boa:Dialog:rkppembinaan
#-------------------------------------------------------------------------------
#Sistem Informasi dan Administrasi Perdesaan
#pengembang johandri@ictwatch.id
#-------------------------------------------------------------------------------

import wx
import os

import sqlite3

db = sqlite3.connect('siap.db')
cur = db.cursor()

def create(parent):
    return rkppembinaan(parent)

[wxID_RKPPEMBINAAN, wxID_RKPPEMBINAANAKHIR, wxID_RKPPEMBINAANAMBILAPBDES, 
 wxID_RKPPEMBINAANAMBILAPBN, wxID_RKPPEMBINAANAMBILLAIN, 
 wxID_RKPPEMBINAANAPBDES, wxID_RKPPEMBINAANAPBN, wxID_RKPPEMBINAANASLIDESA, 
 wxID_RKPPEMBINAANBARU, wxID_RKPPEMBINAANBUTTON2, wxID_RKPPEMBINAANCARINOREK, 
 wxID_RKPPEMBINAANDIAMBIL1, wxID_RKPPEMBINAANDIAMBIL2, 
 wxID_RKPPEMBINAANDIAMBIL3, wxID_RKPPEMBINAANDIAMBIL4, 
 wxID_RKPPEMBINAANDIAMBIL5, wxID_RKPPEMBINAANDIAMBIL6, wxID_RKPPEMBINAANEDIT, 
 wxID_RKPPEMBINAANHAPUS, wxID_RKPPEMBINAANIDJOIN, wxID_RKPPEMBINAANJUMLAH, 
 wxID_RKPPEMBINAANJUMLAHDIAMBIL, wxID_RKPPEMBINAANJUMLAHSISA, 
 wxID_RKPPEMBINAANJUMLAHSISA1, wxID_RKPPEMBINAANJUMLAHSISA2, 
 wxID_RKPPEMBINAANJUMLAHSUMBER, wxID_RKPPEMBINAANKEGIATAN, 
 wxID_RKPPEMBINAANLAIN, wxID_RKPPEMBINAANLAMA, wxID_RKPPEMBINAANLOKASI, 
 wxID_RKPPEMBINAANMENU, wxID_RKPPEMBINAANNOMOR, wxID_RKPPEMBINAANNOREK, 
 wxID_RKPPEMBINAANPEMBANGUNANDESA, wxID_RKPPEMBINAANPENDAPATAN, 
 wxID_RKPPEMBINAANPERIODE, wxID_RKPPEMBINAANPOLA, wxID_RKPPEMBINAANREHAB, 
 wxID_RKPPEMBINAANRESET, wxID_RKPPEMBINAANRKP, 
 wxID_RKPPEMBINAANRPJMPEMBANGUNANDESA, wxID_RKPPEMBINAANSASARAN, 
 wxID_RKPPEMBINAANSATUAN, wxID_RKPPEMBINAANSISA1, wxID_RKPPEMBINAANSISA2, 
 wxID_RKPPEMBINAANSISA3, wxID_RKPPEMBINAANSISA4, wxID_RKPPEMBINAANSISA5, 
 wxID_RKPPEMBINAANSISA6, wxID_RKPPEMBINAANSISAAPBDES, 
 wxID_RKPPEMBINAANSISAAPBN, wxID_RKPPEMBINAANSISALAIN, 
 wxID_RKPPEMBINAANSTATICBOX1, wxID_RKPPEMBINAANSTATICTEXT1, 
 wxID_RKPPEMBINAANSTATICTEXT10, wxID_RKPPEMBINAANSTATICTEXT11, 
 wxID_RKPPEMBINAANSTATICTEXT12, wxID_RKPPEMBINAANSTATICTEXT13, 
 wxID_RKPPEMBINAANSTATICTEXT14, wxID_RKPPEMBINAANSTATICTEXT15, 
 wxID_RKPPEMBINAANSTATICTEXT16, wxID_RKPPEMBINAANSTATICTEXT17, 
 wxID_RKPPEMBINAANSTATICTEXT18, wxID_RKPPEMBINAANSTATICTEXT19, 
 wxID_RKPPEMBINAANSTATICTEXT2, wxID_RKPPEMBINAANSTATICTEXT20, 
 wxID_RKPPEMBINAANSTATICTEXT21, wxID_RKPPEMBINAANSTATICTEXT22, 
 wxID_RKPPEMBINAANSTATICTEXT23, wxID_RKPPEMBINAANSTATICTEXT24, 
 wxID_RKPPEMBINAANSTATICTEXT25, wxID_RKPPEMBINAANSTATICTEXT26, 
 wxID_RKPPEMBINAANSTATICTEXT27, wxID_RKPPEMBINAANSTATICTEXT28, 
 wxID_RKPPEMBINAANSTATICTEXT29, wxID_RKPPEMBINAANSTATICTEXT3, 
 wxID_RKPPEMBINAANSTATICTEXT30, wxID_RKPPEMBINAANSTATICTEXT31, 
 wxID_RKPPEMBINAANSTATICTEXT32, wxID_RKPPEMBINAANSTATICTEXT33, 
 wxID_RKPPEMBINAANSTATICTEXT34, wxID_RKPPEMBINAANSTATICTEXT35, 
 wxID_RKPPEMBINAANSTATICTEXT36, wxID_RKPPEMBINAANSTATICTEXT37, 
 wxID_RKPPEMBINAANSTATICTEXT38, wxID_RKPPEMBINAANSTATICTEXT39, 
 wxID_RKPPEMBINAANSTATICTEXT4, wxID_RKPPEMBINAANSTATICTEXT40, 
 wxID_RKPPEMBINAANSTATICTEXT41, wxID_RKPPEMBINAANSTATICTEXT5, 
 wxID_RKPPEMBINAANSTATICTEXT6, wxID_RKPPEMBINAANSTATICTEXT7, 
 wxID_RKPPEMBINAANSTATICTEXT8, wxID_RKPPEMBINAANSTATICTEXT9, 
 wxID_RKPPEMBINAANTAHUNINI1, wxID_RKPPEMBINAANTAHUNINI2, 
 wxID_RKPPEMBINAANTAHUNINI3, wxID_RKPPEMBINAANTAHUNINI4, 
 wxID_RKPPEMBINAANTAHUNINI5, wxID_RKPPEMBINAANTAHUNINI6, 
 wxID_RKPPEMBINAANTAHUNRKP, wxID_RKPPEMBINAANTAMBAH, wxID_RKPPEMBINAANWAKTU1, 
 wxID_RKPPEMBINAANWAKTU2, wxID_RKPPEMBINAANWAKTU3, wxID_RKPPEMBINAANWAKTU4, 
 wxID_RKPPEMBINAANWAKTU5, wxID_RKPPEMBINAANWAKTU6, 
] = [wx.NewId() for _init_ctrls in range(108)]

class rkppembinaan(wx.Dialog):
    def _init_coll_pembangunandesa_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT, heading='Record',
              width=40)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT,
              heading='Rekening', width=60)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT, heading='Uraian',
              width=400)

    def _init_coll_rpjmpembangunandesa_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT, heading='Norek',
              width=40)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT, heading='Uraian',
              width=300)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT, heading='Lokasi',
              width=100)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_LEFT, heading='Volume',
              width=100)
        parent.InsertColumn(col=4, format=wx.LIST_FORMAT_LEFT, heading='Satuan',
              width=100)
        parent.InsertColumn(col=5, format=wx.LIST_FORMAT_LEFT,
              heading='Sasaran', width=400)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_RKPPEMBINAAN, name=u'rkppembinaan',
              parent=prnt, pos=wx.Point(406, 47), size=wx.Size(916, 648),
              style=wx.DEFAULT_FRAME_STYLE,
              title=u'RKP Desa  Belanja Bidang Pembinaan Kemasyarakatan')
        self.SetClientSize(wx.Size(908, 618))
        self.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.SetBackgroundColour(wx.Colour(192, 192, 192))
        self.Center(wx.BOTH)

        self.pendapatan = wx.StaticText(id=wxID_RKPPEMBINAANPENDAPATAN,
              label=u'2. BELANJA', name=u'pendapatan', parent=self,
              pos=wx.Point(8, 8), size=wx.Size(62, 13), style=0)
        self.pendapatan.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Tahoma'))

        self.aslidesa = wx.StaticText(id=wxID_RKPPEMBINAANASLIDESA,
              label=u'2.3. Bidang Pembinaan Kemasyarakatan', name=u'aslidesa',
              parent=self, pos=wx.Point(8, 24), size=wx.Size(227, 13), style=0)
        self.aslidesa.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Tahoma'))

        self.pembangunandesa = wx.ListCtrl(id=wxID_RKPPEMBINAANPEMBANGUNANDESA,
              name=u'pembangunandesa', parent=self, pos=wx.Point(8, 40),
              size=wx.Size(368, 368), style=wx.LC_REPORT)
        self._init_coll_pembangunandesa_Columns(self.pembangunandesa)
        self.pembangunandesa.Bind(wx.EVT_LIST_ITEM_SELECTED,
              self.OnPembangunandesaListItemSelected,
              id=wxID_RKPPEMBINAANPEMBANGUNANDESA)

        self.staticText2 = wx.StaticText(id=wxID_RKPPEMBINAANSTATICTEXT2,
              label=u'Nomor Rekening', name='staticText2', parent=self,
              pos=wx.Point(384, 75), size=wx.Size(79, 13), style=0)

        self.norek = wx.TextCtrl(id=wxID_RKPPEMBINAANNOREK, name=u'norek',
              parent=self, pos=wx.Point(512, 73), size=wx.Size(96, 21), style=0,
              value=u'')

        self.staticText3 = wx.StaticText(id=wxID_RKPPEMBINAANSTATICTEXT3,
              label=u'Jenis Kegiatan', name='staticText3', parent=self,
              pos=wx.Point(384, 99), size=wx.Size(69, 13), style=0)

        self.kegiatan = wx.TextCtrl(id=wxID_RKPPEMBINAANKEGIATAN,
              name=u'kegiatan', parent=self, pos=wx.Point(512, 95),
              size=wx.Size(387, 21), style=0, value=u'')

        self.tambah = wx.Button(id=wxID_RKPPEMBINAANTAMBAH,
              label=u'Tambah Data', name=u'tambah', parent=self,
              pos=wx.Point(511, 389), size=wx.Size(88, 23), style=0)
        self.tambah.Bind(wx.EVT_BUTTON, self.OnTambahButton,
              id=wxID_RKPPEMBINAANTAMBAH)

        self.edit = wx.Button(id=wxID_RKPPEMBINAANEDIT, label=u'Edit Data',
              name=u'edit', parent=self, pos=wx.Point(684, 389),
              size=wx.Size(96, 23), style=0)
        self.edit.Bind(wx.EVT_BUTTON, self.OnEditButton,
              id=wxID_RKPPEMBINAANEDIT)

        self.menu = wx.Button(id=wxID_RKPPEMBINAANMENU,
              label=u'Kembali Ke Menu', name=u'menu', parent=self,
              pos=wx.Point(785, 389), size=wx.Size(112, 23), style=0)
        self.menu.Bind(wx.EVT_BUTTON, self.OnMenuButton,
              id=wxID_RKPPEMBINAANMENU)

        self.staticText1 = wx.StaticText(id=wxID_RKPPEMBINAANSTATICTEXT1,
              label=u'Lokasi (RT/RW/DESA)', name='staticText1', parent=self,
              pos=wx.Point(384, 122), size=wx.Size(105, 13), style=0)

        self.staticText4 = wx.StaticText(id=wxID_RKPPEMBINAANSTATICTEXT4,
              label=u'Volume', name='staticText4', parent=self,
              pos=wx.Point(385, 143), size=wx.Size(35, 13), style=0)

        self.staticText5 = wx.StaticText(id=wxID_RKPPEMBINAANSTATICTEXT5,
              label=u'Sasaran/Manfaat', name='staticText5', parent=self,
              pos=wx.Point(384, 261), size=wx.Size(84, 13), style=0)

        self.sasaran = wx.TextCtrl(id=wxID_RKPPEMBINAANSASARAN, name=u'sasaran',
              parent=self, pos=wx.Point(512, 251), size=wx.Size(387, 22),
              style=0, value=u'')

        self.staticText7 = wx.StaticText(id=wxID_RKPPEMBINAANSTATICTEXT7,
              label=u'Sumber Dana', name='staticText7', parent=self,
              pos=wx.Point(384, 283), size=wx.Size(65, 13), style=0)

        self.staticText9 = wx.StaticText(id=wxID_RKPPEMBINAANSTATICTEXT9,
              label=u'Prakiraan Pola Pelaksaan', name='staticText9',
              parent=self, pos=wx.Point(384, 369), size=wx.Size(120, 13),
              style=0)

        self.carinorek = wx.TextCtrl(id=wxID_RKPPEMBINAANCARINOREK,
              name=u'carinorek', parent=self, pos=wx.Point(512, 51),
              size=wx.Size(96, 21), style=0, value=u'')

        self.staticText10 = wx.StaticText(id=wxID_RKPPEMBINAANSTATICTEXT10,
              label=u'Nomor Record', name='staticText10', parent=self,
              pos=wx.Point(384, 51), size=wx.Size(69, 13), style=0)

        self.rpjmpembangunandesa = wx.ListCtrl(id=wxID_RKPPEMBINAANRPJMPEMBANGUNANDESA,
              name=u'rpjmpembangunandesa', parent=self, pos=wx.Point(7, 416),
              size=wx.Size(893, 197), style=wx.LC_REPORT)
        self._init_coll_rpjmpembangunandesa_Columns(self.rpjmpembangunandesa)
        self.rpjmpembangunandesa.Bind(wx.EVT_LIST_ITEM_SELECTED,
              self.OnRpjmpembangunandesaListItemSelected,
              id=wxID_RKPPEMBINAANRPJMPEMBANGUNANDESA)

        self.pola = wx.ComboBox(choices=['Swakelola', 'Kerjasama Antar Desa',
              'Kerjasama Pihak Ketiga'], id=wxID_RKPPEMBINAANPOLA, name=u'pola',
              parent=self, pos=wx.Point(512, 364), size=wx.Size(385, 21),
              style=0, value=u'')
        self.pola.SetLabel(u'')

        self.staticText13 = wx.StaticText(id=wxID_RKPPEMBINAANSTATICTEXT13,
              label=u'TAHUN RPJMDES', name='staticText13', parent=self,
              pos=wx.Point(398, 20), size=wx.Size(83, 13), style=0)

        self.periode = wx.TextCtrl(id=wxID_RKPPEMBINAANPERIODE, name=u'periode',
              parent=self, pos=wx.Point(486, 16), size=wx.Size(93, 21), style=0,
              value=u'')

        self.button2 = wx.Button(id=wxID_RKPPEMBINAANBUTTON2,
              label=u'Buat RKP Desa', name='button2', parent=self,
              pos=wx.Point(784, 15), size=wx.Size(104, 23), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_RKPPEMBINAANBUTTON2)

        self.staticBox1 = wx.StaticBox(id=wxID_RKPPEMBINAANSTATICBOX1,
              label=u'Pertama Yang Di Isi', name='staticBox1', parent=self,
              pos=wx.Point(392, 2), size=wx.Size(505, 46), style=0)
        self.staticBox1.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Tahoma'))
        self.staticBox1.SetForegroundColour(wx.Colour(255, 0, 0))

        self.staticText14 = wx.StaticText(id=wxID_RKPPEMBINAANSTATICTEXT14,
              label=u'TAHUN KE', name='staticText14', parent=self,
              pos=wx.Point(584, 22), size=wx.Size(50, 13), style=0)

        self.tahunrkp = wx.TextCtrl(id=wxID_RKPPEMBINAANTAHUNRKP,
              name=u'tahunrkp', parent=self, pos=wx.Point(703, 17),
              size=wx.Size(68, 21), style=0, value=u'')

        self.rkp = wx.ComboBox(choices=['1', '2', '3', '4', '5', '6'],
              id=wxID_RKPPEMBINAANRKP, name=u'rkp', parent=self,
              pos=wx.Point(637, 16), size=wx.Size(39, 21), style=0, value=u'')
        self.rkp.SetLabel(u'')
        self.rkp.Bind(wx.EVT_COMBOBOX, self.OnRkpCombobox,
              id=wxID_RKPPEMBINAANRKP)

        self.ambilapbn = wx.TextCtrl(id=wxID_RKPPEMBINAANAMBILAPBN,
              name=u'ambilapbn', parent=self, pos=wx.Point(734, 276),
              size=wx.Size(60, 21), style=0, value=u'')
        self.ambilapbn.Bind(wx.EVT_TEXT, self.OnAmbilapbnText,
              id=wxID_RKPPEMBINAANAMBILAPBN)

        self.apbn = wx.TextCtrl(id=wxID_RKPPEMBINAANAPBN, name=u'apbn',
              parent=self, pos=wx.Point(608, 276), size=wx.Size(64, 21),
              style=wx.TE_READONLY, value=u'')

        self.lokasi = wx.TextCtrl(id=wxID_RKPPEMBINAANLOKASI, name=u'lokasi',
              parent=self, pos=wx.Point(512, 117), size=wx.Size(72, 21),
              style=0, value=u'')

        self.satuan = wx.TextCtrl(id=wxID_RKPPEMBINAANSATUAN, name=u'satuan',
              parent=self, pos=wx.Point(801, 229), size=wx.Size(96, 21),
              style=0, value=u'')

        self.staticText18 = wx.StaticText(id=wxID_RKPPEMBINAANSTATICTEXT18,
              label=u'Tahun ini  :', name='staticText18', parent=self,
              pos=wx.Point(675, 280), size=wx.Size(54, 13), style=0)

        self.hapus = wx.Button(id=wxID_RKPPEMBINAANHAPUS, label=u'Hapus Data',
              name=u'hapus', parent=self, pos=wx.Point(604, 389),
              size=wx.Size(75, 23), style=0)
        self.hapus.Bind(wx.EVT_BUTTON, self.OnButton3Button,
              id=wxID_RKPPEMBINAANHAPUS)

        self.staticText22 = wx.StaticText(id=wxID_RKPPEMBINAANSTATICTEXT22,
              label=u'Tahun RKP Ini', name='staticText22', parent=self,
              pos=wx.Point(431, 189), size=wx.Size(68, 13), style=0)

        self.staticText23 = wx.StaticText(id=wxID_RKPPEMBINAANSTATICTEXT23,
              label=u'Volume Tersedia', name='staticText23', parent=self,
              pos=wx.Point(431, 166), size=wx.Size(79, 13), style=0)

        self.staticText15 = wx.StaticText(id=wxID_RKPPEMBINAANSTATICTEXT15,
              label=u'3.', name='staticText15', parent=self, pos=wx.Point(640,
              139), size=wx.Size(10, 13), style=0)

        self.waktu1 = wx.TextCtrl(id=wxID_RKPPEMBINAANWAKTU1, name=u'waktu1',
              parent=self, pos=wx.Point(524, 139), size=wx.Size(49, 21),
              style=0, value=u'')

        self.waktu2 = wx.TextCtrl(id=wxID_RKPPEMBINAANWAKTU2, name=u'waktu2',
              parent=self, pos=wx.Point(590, 139), size=wx.Size(48, 21),
              style=0, value=u'')

        self.waktu3 = wx.TextCtrl(id=wxID_RKPPEMBINAANWAKTU3, name=u'waktu3',
              parent=self, pos=wx.Point(655, 139), size=wx.Size(48, 21),
              style=0, value=u'')

        self.waktu4 = wx.TextCtrl(id=wxID_RKPPEMBINAANWAKTU4, name=u'waktu4',
              parent=self, pos=wx.Point(720, 139), size=wx.Size(48, 21),
              style=0, value=u'')

        self.waktu5 = wx.TextCtrl(id=wxID_RKPPEMBINAANWAKTU5, name=u'waktu5',
              parent=self, pos=wx.Point(786, 139), size=wx.Size(48, 21),
              style=0, value=u'')

        self.waktu6 = wx.TextCtrl(id=wxID_RKPPEMBINAANWAKTU6, name=u'waktu6',
              parent=self, pos=wx.Point(851, 139), size=wx.Size(48, 21),
              style=0, value=u'')

        self.tahunini1 = wx.TextCtrl(id=wxID_RKPPEMBINAANTAHUNINI1,
              name=u'tahunini1', parent=self, pos=wx.Point(512, 162),
              size=wx.Size(62, 21), style=0, value=u'')

        self.tahunini2 = wx.TextCtrl(id=wxID_RKPPEMBINAANTAHUNINI2,
              name=u'tahunini2', parent=self, pos=wx.Point(577, 161),
              size=wx.Size(62, 21), style=0, value=u'')

        self.tahunini3 = wx.TextCtrl(id=wxID_RKPPEMBINAANTAHUNINI3,
              name=u'tahunini3', parent=self, pos=wx.Point(642, 161),
              size=wx.Size(62, 21), style=0, value=u'')

        self.tahunini4 = wx.TextCtrl(id=wxID_RKPPEMBINAANTAHUNINI4,
              name=u'tahunini4', parent=self, pos=wx.Point(707, 161),
              size=wx.Size(62, 21), style=0, value=u'')

        self.tahunini5 = wx.TextCtrl(id=wxID_RKPPEMBINAANTAHUNINI5,
              name=u'tahunini5', parent=self, pos=wx.Point(772, 161),
              size=wx.Size(62, 21), style=0, value=u'')

        self.tahunini6 = wx.TextCtrl(id=wxID_RKPPEMBINAANTAHUNINI6,
              name=u'tahunini6', parent=self, pos=wx.Point(837, 161),
              size=wx.Size(62, 21), style=0, value=u'')

        self.staticText19 = wx.StaticText(id=wxID_RKPPEMBINAANSTATICTEXT19,
              label=u'2.', name='staticText19', parent=self, pos=wx.Point(576,
              139), size=wx.Size(10, 13), style=0)

        self.staticText16 = wx.StaticText(id=wxID_RKPPEMBINAANSTATICTEXT16,
              label=u'4.', name='staticText16', parent=self, pos=wx.Point(707,
              139), size=wx.Size(10, 13), style=0)

        self.staticText17 = wx.StaticText(id=wxID_RKPPEMBINAANSTATICTEXT17,
              label=u'5.', name='staticText17', parent=self, pos=wx.Point(773,
              139), size=wx.Size(10, 13), style=0)

        self.staticText20 = wx.StaticText(id=wxID_RKPPEMBINAANSTATICTEXT20,
              label=u'6.', name='staticText20', parent=self, pos=wx.Point(838,
              139), size=wx.Size(10, 13), style=0)

        self.nomor = wx.TextCtrl(id=wxID_RKPPEMBINAANNOMOR, name=u'nomor',
              parent=self, pos=wx.Point(-100, -100), size=wx.Size(100, 21),
              style=0, value=u'')

        self.staticText21 = wx.StaticText(id=wxID_RKPPEMBINAANSTATICTEXT21,
              label=u'1.', name='staticText21', parent=self, pos=wx.Point(512,
              139), size=wx.Size(10, 13), style=0)

        self.staticText24 = wx.StaticText(id=wxID_RKPPEMBINAANSTATICTEXT24,
              label=u'Sifat  :', name='staticText24', parent=self,
              pos=wx.Point(607, 121), size=wx.Size(33, 13), style=0)

        self.staticText26 = wx.StaticText(id=wxID_RKPPEMBINAANSTATICTEXT26,
              label=u'Baru', name='staticText26', parent=self, pos=wx.Point(647,
              119), size=wx.Size(23, 13), style=0)

        self.baru = wx.ComboBox(choices=['Ya', 'Tidak'],
              id=wxID_RKPPEMBINAANBARU, name=u'baru', parent=self,
              pos=wx.Point(669, 117), size=wx.Size(56, 21), style=0, value=u'')
        self.baru.SetLabel(u'')

        self.staticText27 = wx.StaticText(id=wxID_RKPPEMBINAANSTATICTEXT27,
              label=u'Rehab', name='staticText27', parent=self,
              pos=wx.Point(728, 121), size=wx.Size(32, 13), style=0)

        self.rehab = wx.ComboBox(choices=['Ya', 'Tidak'],
              id=wxID_RKPPEMBINAANREHAB, name=u'rehab', parent=self,
              pos=wx.Point(761, 117), size=wx.Size(53, 21), style=0, value=u'')
        self.rehab.SetLabel(u'')

        self.staticText28 = wx.StaticText(id=wxID_RKPPEMBINAANSTATICTEXT28,
              label=u'Lama', name='staticText28', parent=self, pos=wx.Point(817,
              120), size=wx.Size(26, 13), style=0)

        self.lama = wx.ComboBox(choices=['Ya', 'Tidak'],
              id=wxID_RKPPEMBINAANLAMA, name=u'lama', parent=self,
              pos=wx.Point(843, 117), size=wx.Size(55, 21), style=0, value=u'')
        self.lama.SetLabel(u'')

        self.staticText29 = wx.StaticText(id=wxID_RKPPEMBINAANSTATICTEXT29,
              label=u'RKP', name='staticText29', parent=self, pos=wx.Point(680,
              20), size=wx.Size(24, 13), style=0)

        self.diambil1 = wx.TextCtrl(id=wxID_RKPPEMBINAANDIAMBIL1,
              name=u'diambil1', parent=self, pos=wx.Point(512, 184),
              size=wx.Size(62, 21), style=0, value=u'')
        self.diambil1.Bind(wx.EVT_TEXT, self.OnDiambil1Text,
              id=wxID_RKPPEMBINAANDIAMBIL1)

        self.diambil2 = wx.TextCtrl(id=wxID_RKPPEMBINAANDIAMBIL2,
              name=u'diambil2', parent=self, pos=wx.Point(577, 183),
              size=wx.Size(62, 21), style=0, value=u'')
        self.diambil2.Bind(wx.EVT_TEXT, self.OnDiambil2Text,
              id=wxID_RKPPEMBINAANDIAMBIL2)

        self.diambil3 = wx.TextCtrl(id=wxID_RKPPEMBINAANDIAMBIL3,
              name=u'diambil3', parent=self, pos=wx.Point(642, 183),
              size=wx.Size(62, 21), style=0, value=u'')
        self.diambil3.Bind(wx.EVT_TEXT, self.OnDiambil3Text,
              id=wxID_RKPPEMBINAANDIAMBIL3)

        self.diambil4 = wx.TextCtrl(id=wxID_RKPPEMBINAANDIAMBIL4,
              name=u'diambil4', parent=self, pos=wx.Point(707, 183),
              size=wx.Size(62, 21), style=0, value=u'')
        self.diambil4.Bind(wx.EVT_TEXT, self.OnDiambil4Text,
              id=wxID_RKPPEMBINAANDIAMBIL4)

        self.diambil5 = wx.TextCtrl(id=wxID_RKPPEMBINAANDIAMBIL5,
              name=u'diambil5', parent=self, pos=wx.Point(772, 183),
              size=wx.Size(62, 21), style=0, value=u'')
        self.diambil5.Bind(wx.EVT_TEXT, self.OnDiambil5Text,
              id=wxID_RKPPEMBINAANDIAMBIL5)

        self.diambil6 = wx.TextCtrl(id=wxID_RKPPEMBINAANDIAMBIL6,
              name=u'diambil6', parent=self, pos=wx.Point(837, 183),
              size=wx.Size(62, 21), style=0, value=u'')
        self.diambil6.Bind(wx.EVT_TEXT, self.OnDiambil6Text,
              id=wxID_RKPPEMBINAANDIAMBIL6)

        self.staticText6 = wx.StaticText(id=wxID_RKPPEMBINAANSTATICTEXT6,
              label=u'1. RAPBN / RAPBD', name='staticText6', parent=self,
              pos=wx.Point(512, 280), size=wx.Size(89, 14), style=0)

        self.staticText8 = wx.StaticText(id=wxID_RKPPEMBINAANSTATICTEXT8,
              label=u'2. RAPBDES', name='staticText8', parent=self,
              pos=wx.Point(513, 303), size=wx.Size(58, 13), style=0)

        self.staticText11 = wx.StaticText(id=wxID_RKPPEMBINAANSTATICTEXT11,
              label=u'3. Lain-lain', name='staticText11', parent=self,
              pos=wx.Point(513, 324), size=wx.Size(52, 13), style=0)

        self.apbdes = wx.TextCtrl(id=wxID_RKPPEMBINAANAPBDES, name=u'apbdes',
              parent=self, pos=wx.Point(608, 298), size=wx.Size(64, 21),
              style=wx.TE_READONLY, value=u'')

        self.lain = wx.TextCtrl(id=wxID_RKPPEMBINAANLAIN, name=u'lain',
              parent=self, pos=wx.Point(608, 320), size=wx.Size(64, 21),
              style=wx.TE_READONLY, value=u'')

        self.staticText12 = wx.StaticText(id=wxID_RKPPEMBINAANSTATICTEXT12,
              label=u'Sisa    :', name='staticText12', parent=self,
              pos=wx.Point(801, 278), size=wx.Size(36, 13), style=0)

        self.sisaapbn = wx.TextCtrl(id=wxID_RKPPEMBINAANSISAAPBN,
              name=u'sisaapbn', parent=self, pos=wx.Point(838, 276),
              size=wx.Size(60, 21), style=0, value=u'')

        self.staticText25 = wx.StaticText(id=wxID_RKPPEMBINAANSTATICTEXT25,
              label=u'Tahun ini  :', name='staticText25', parent=self,
              pos=wx.Point(675, 303), size=wx.Size(54, 13), style=0)

        self.ambilapbdes = wx.TextCtrl(id=wxID_RKPPEMBINAANAMBILAPBDES,
              name=u'ambilapbdes', parent=self, pos=wx.Point(734, 298),
              size=wx.Size(60, 21), style=0, value=u'')
        self.ambilapbdes.Bind(wx.EVT_TEXT, self.OnAmbilapbdesText,
              id=wxID_RKPPEMBINAANAMBILAPBDES)

        self.staticText30 = wx.StaticText(id=wxID_RKPPEMBINAANSTATICTEXT30,
              label=u'Sisa    :', name='staticText30', parent=self,
              pos=wx.Point(801, 301), size=wx.Size(36, 13), style=0)

        self.sisaapbdes = wx.TextCtrl(id=wxID_RKPPEMBINAANSISAAPBDES,
              name=u'sisaapbdes', parent=self, pos=wx.Point(838, 298),
              size=wx.Size(60, 21), style=0, value=u'')

        self.staticText31 = wx.StaticText(id=wxID_RKPPEMBINAANSTATICTEXT31,
              label=u'Tahun ini  :', name='staticText31', parent=self,
              pos=wx.Point(675, 325), size=wx.Size(54, 13), style=0)

        self.ambillain = wx.TextCtrl(id=wxID_RKPPEMBINAANAMBILLAIN,
              name=u'ambillain', parent=self, pos=wx.Point(734, 320),
              size=wx.Size(60, 21), style=0, value=u'')
        self.ambillain.Bind(wx.EVT_TEXT, self.OnAmbillainText,
              id=wxID_RKPPEMBINAANAMBILLAIN)

        self.staticText32 = wx.StaticText(id=wxID_RKPPEMBINAANSTATICTEXT32,
              label=u'Sisa    :', name='staticText32', parent=self,
              pos=wx.Point(801, 323), size=wx.Size(36, 13), style=0)

        self.sisalain = wx.TextCtrl(id=wxID_RKPPEMBINAANSISALAIN,
              name=u'sisalain', parent=self, pos=wx.Point(838, 320),
              size=wx.Size(60, 21), style=0, value=u'')

        self.jumlahsumber = wx.TextCtrl(id=wxID_RKPPEMBINAANJUMLAHSUMBER,
              name=u'jumlahsumber', parent=self, pos=wx.Point(608, 342),
              size=wx.Size(64, 20), style=wx.TE_READONLY, value=u'')

        self.jumlahdiambil = wx.TextCtrl(id=wxID_RKPPEMBINAANJUMLAHDIAMBIL,
              name=u'jumlahdiambil', parent=self, pos=wx.Point(734, 342),
              size=wx.Size(60, 21), style=0, value=u'')

        self.akhir = wx.TextCtrl(id=wxID_RKPPEMBINAANAKHIR, name=u'akhir',
              parent=self, pos=wx.Point(838, 342), size=wx.Size(60, 21),
              style=0, value=u'')

        self.staticText33 = wx.StaticText(id=wxID_RKPPEMBINAANSTATICTEXT33,
              label=u'JUMLAH', name='staticText33', parent=self,
              pos=wx.Point(527, 344), size=wx.Size(39, 13), style=0)

        self.sisa1 = wx.TextCtrl(id=wxID_RKPPEMBINAANSISA1, name=u'sisa1',
              parent=self, pos=wx.Point(512, 207), size=wx.Size(62, 21),
              style=wx.TE_READONLY, value=u'')

        self.sisa2 = wx.TextCtrl(id=wxID_RKPPEMBINAANSISA2, name=u'sisa2',
              parent=self, pos=wx.Point(577, 206), size=wx.Size(62, 21),
              style=wx.TE_READONLY, value=u'')

        self.sisa3 = wx.TextCtrl(id=wxID_RKPPEMBINAANSISA3, name=u'sisa3',
              parent=self, pos=wx.Point(642, 206), size=wx.Size(62, 21),
              style=wx.TE_READONLY, value=u'')

        self.sisa4 = wx.TextCtrl(id=wxID_RKPPEMBINAANSISA4, name=u'sisa4',
              parent=self, pos=wx.Point(707, 206), size=wx.Size(62, 21),
              style=wx.TE_READONLY, value=u'')

        self.sisa5 = wx.TextCtrl(id=wxID_RKPPEMBINAANSISA5, name=u'sisa5',
              parent=self, pos=wx.Point(772, 206), size=wx.Size(62, 21),
              style=wx.TE_READONLY, value=u'')

        self.jumlahsisa = wx.TextCtrl(id=wxID_RKPPEMBINAANJUMLAHSISA,
              name=u'jumlahsisa', parent=self, pos=wx.Point(716, 229),
              size=wx.Size(40, 21), style=wx.TE_READONLY, value=u'')

        self.staticText34 = wx.StaticText(id=wxID_RKPPEMBINAANSTATICTEXT34,
              label=u'Sisa', name='staticText34', parent=self, pos=wx.Point(431,
              211), size=wx.Size(20, 13), style=0)

        self.staticText35 = wx.StaticText(id=wxID_RKPPEMBINAANSTATICTEXT35,
              label=u'Satuan', name='staticText35', parent=self,
              pos=wx.Point(762, 234), size=wx.Size(35, 13), style=0)

        self.sisa6 = wx.TextCtrl(id=wxID_RKPPEMBINAANSISA6, name=u'sisa6',
              parent=self, pos=wx.Point(837, 206), size=wx.Size(62, 21),
              style=wx.TE_READONLY, value=u'')

        self.staticText36 = wx.StaticText(id=wxID_RKPPEMBINAANSTATICTEXT36,
              label=u'Jumlah Volume', name='staticText36', parent=self,
              pos=wx.Point(432, 233), size=wx.Size(70, 13), style=0)

        self.staticText37 = wx.StaticText(id=wxID_RKPPEMBINAANSTATICTEXT37,
              label=u'Tahun', name='staticText37', parent=self,
              pos=wx.Point(433, 141), size=wx.Size(31, 14), style=0)

        self.jumlahsisa2 = wx.TextCtrl(id=wxID_RKPPEMBINAANJUMLAHSISA2,
              name=u'jumlahsisa2', parent=self, pos=wx.Point(559, 229),
              size=wx.Size(40, 21), style=wx.TE_READONLY, value=u'')

        self.jumlahsisa1 = wx.TextCtrl(id=wxID_RKPPEMBINAANJUMLAHSISA1,
              name=u'jumlahsisa1', parent=self, pos=wx.Point(646, 229),
              size=wx.Size(40, 21), style=wx.TE_READONLY, value=u'')

        self.staticText38 = wx.StaticText(id=wxID_RKPPEMBINAANSTATICTEXT38,
              label=u'Sisa', name='staticText38', parent=self, pos=wx.Point(692,
              232), size=wx.Size(20, 13), style=0)

        self.staticText39 = wx.StaticText(id=wxID_RKPPEMBINAANSTATICTEXT39,
              label=u'Tersedia', name='staticText39', parent=self,
              pos=wx.Point(514, 232), size=wx.Size(42, 13), style=0)

        self.staticText40 = wx.StaticText(id=wxID_RKPPEMBINAANSTATICTEXT40,
              label=u'Diambil', name='staticText40', parent=self,
              pos=wx.Point(603, 232), size=wx.Size(34, 13), style=0)

        self.reset = wx.Button(id=wxID_RKPPEMBINAANRESET, label=u'Reset Data',
              name=u'reset', parent=self, pos=wx.Point(383, 389),
              size=wx.Size(75, 23), style=0)
        self.reset.Bind(wx.EVT_BUTTON, self.OnResetButton,
              id=wxID_RKPPEMBINAANRESET)

        self.idjoin = wx.TextCtrl(id=wxID_RKPPEMBINAANIDJOIN, name=u'idjoin',
              parent=self, pos=wx.Point(-392, -328), size=wx.Size(100, 21),
              style=0, value=u'')

        self.jumlah = wx.TextCtrl(id=wxID_RKPPEMBINAANJUMLAH, name=u'jumlah',
              parent=self, pos=wx.Point(797, 53), size=wx.Size(100, 21),
              style=0, value=u'')

        self.staticText41 = wx.StaticText(id=wxID_RKPPEMBINAANSTATICTEXT41,
              label=u'Jumlah Biaya : Rp.', name='staticText41', parent=self,
              pos=wx.Point(706, 56), size=wx.Size(89, 13), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.tahunrkp.Disable()
        self.tambah.Disable()
        self.hapus.Disable()
        self.edit.Disable()
        self.reset.Disable()
        
    def awal(self):
        self.isilist0()
        self.isilist1()
        self.setisi()
        rrkp=str(self.rkp.GetValue())
        perio=str(self.periode.GetValue())
        sql1="SELECT sum(totalbiaya) FROM rpjmdesasid WHERE norek LIKE '2.3%' AND id_rkp='"+rrkp+"' AND periode='"+perio+"'"
        cur.execute(sql1)
        hasil1=cur.fetchone()
        self.jumlah.SetValue(str(hasil1[0]))
        self.jumlah.Disable()
        
    def setisi(self):    
       
        self.norek.SetValue('')
        self.kegiatan.SetValue('')
        self.lokasi.SetValue('')
        self.waktu1.SetValue('')
        self.waktu2.SetValue('')
        self.waktu3.SetValue('')
        self.waktu4.SetValue('')
        self.waktu5.SetValue('')
        self.waktu6.SetValue('')
        self.tahunini1.SetValue('0')
        self.tahunini2.SetValue('0')
        self.tahunini3.SetValue('0')
        self.tahunini4.SetValue('0')
        self.tahunini5.SetValue('0')
        self.tahunini6.SetValue('0')
        self.diambil1.SetValue('0')
        self.diambil2.SetValue('0')
        self.diambil3.SetValue('0')
        self.diambil4.SetValue('0')
        self.diambil5.SetValue('0')
        self.diambil6.SetValue('0')
        self.sisa1.SetValue('')
        self.sisa2.SetValue('')
        self.sisa3.SetValue('')
        self.sisa4.SetValue('')
        self.sisa5.SetValue('')
        self.sisa6.SetValue('')
        self.jumlahsisa.SetValue('')
        self.satuan.SetValue('')
        self.sasaran.SetValue('')
        self.apbn.SetValue('0')
        self.apbdes.SetValue('0')
        self.lain.SetValue('0')
        self.jumlahsumber.SetValue('')
        self.ambilapbn.SetValue('0')
        self.ambilapbdes.SetValue('0')
        self.ambillain.SetValue('0')
        self.jumlahdiambil.SetValue('')
        self.sisaapbn.SetValue('')
        self.sisaapbdes.SetValue('')
        self.sisalain.SetValue('')
        self.akhir.SetValue('')
        self.pola.SetValue('')
        self.nomor.SetValue('')
        self.baru.SetValue('Tidak')
        self.rehab.SetValue('Tidak')
        self.lama.SetValue('Tidak')
        
        self.carinorek.Disable()
        self.norek.Disable()
        self.kegiatan.Disable()
        self.lokasi.Disable()
        self.waktu1.Disable()
        self.waktu2.Disable()
        self.waktu3.Disable()
        self.waktu4.Disable()
        self.waktu5.Disable()
        self.waktu6.Disable()
        self.tahunini1.Disable()
        self.tahunini2.Disable()
        self.tahunini3.Disable()
        self.tahunini4.Disable()
        self.tahunini5.Disable()
        self.tahunini6.Disable()
        
        self.sisa1.Disable()
        self.sisa2.Disable()
        self.sisa3.Disable()
        self.sisa4.Disable()
        self.sisa5.Disable()
        self.sisa6.Disable()
        self.jumlahsisa.Disable()
        self.jumlahsisa1.Disable()
        self.jumlahsisa2.Disable()
        self.satuan.Disable()
        self.sasaran.Disable()
        self.apbn.Disable()
        self.apbdes.Disable()
        self.lain.Disable()
        self.jumlahsumber.Disable()
        self.ambilapbn.Enable()
        self.ambilapbdes.Enable()
        self.ambillain.Enable()
        self.jumlahdiambil.Disable()
        self.sisaapbn.Disable()
        self.sisaapbdes.Disable()
        self.sisalain.Disable()
        self.akhir.Disable()
        self.pola.Disable()
        self.nomor.Disable()
        self.baru.Enable()
        self.rehab.Enable()
        self.lama.Enable()
        
        
        self.diambil1.Enable()
        self.diambil2.Enable()
        self.diambil3.Enable()
        self.diambil4.Enable()
        self.diambil5.Enable()
        self.diambil6.Enable()
        
        self.reset.Enable()
        
        self.idjoin.SetValue('')
    
#-------------------------------------------------------------------------------
#isilist kiri
#-------------------------------------------------------------------------------

    def isilist0(self):
        rperiode = str(self.periode.GetValue())
        rrkp = str(self.rkp.GetValue())
        intrkp=int(rrkp)
        cekrkp=intrkp-1
        strrkp=str(cekrkp) 
        self.pembangunandesa.DeleteAllItems()    
        sql = "SELECT * FROM rpjmdesasid WHERE periode='"+rperiode+"' AND norek LIKE '2.3%' AND id_rkp='"+strrkp+"' ORDER BY REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(norek,'1', '0'),'2', '0'), '3', '0'), '4', '0'), '5', '0'), '6', '0'), '7', '0'), '8', '0'),  '9', '0') ASC"
        cur.execute(sql) 
        hasil = cur.fetchall() 
        no_rek = self.pembangunandesa.GetItemCount() 
        for i in hasil : 
            self.pembangunandesa.InsertStringItem(no_rek, "%s"%i[0]) 
            self.pembangunandesa.SetStringItem(no_rek,1,"%s"%i[1])
            self.pembangunandesa.SetStringItem(no_rek,2,"%s"%i[2])
            no_rek = no_rek + 1
            db.commit()
#-------------------------------------------------------------------------------
#Isi List Bawah
#-------------------------------------------------------------------------------
    
    def isilist1(self):
        rrkp = str(self.rkp.GetValue())
        rperiode = str(self.periode.GetValue()) 
        self.rpjmpembangunandesa.DeleteAllItems()    
        sql1 = "SELECT * FROM rkpsid WHERE norek LIKE '2.3%' AND id_rkp='"+(rrkp)+"' AND periode='"+(rperiode)+"'"
        cur.execute(sql1) 
        hasil = cur.fetchall() 
        no_rek1 = self.rpjmpembangunandesa.GetItemCount() 
        for i in hasil : 
            self.rpjmpembangunandesa.InsertStringItem(no_rek1, "%s"%i[0]) 
            self.rpjmpembangunandesa.SetStringItem(no_rek1,1,"%s"%i[1])
            self.rpjmpembangunandesa.SetStringItem(no_rek1,2,"%s"%i[2]) 
            self.rpjmpembangunandesa.SetStringItem(no_rek1,3,"%s"%i[3])
            self.rpjmpembangunandesa.SetStringItem(no_rek1,4,"%s"%i[4])
            self.rpjmpembangunandesa.SetStringItem(no_rek1,5,"%s"%i[5])
            no_rek1 = no_rek1 + 1
            db.commit()
         
#-------------------------------------------------------------------------------
# Isi yang Kiri
#-------------------------------------------------------------------------------
    
    def isi0(self) :
        self.setisi()
        rkode = str(self.rkp.GetValue())
        carinomor=str(self.carinorek.GetValue())
        sql="SELECT * FROM rpjmdesasid WHERE norek LIKE '2.3%' AND no='"+carinomor+"' AND jumlahsisa1='0' "
        cur.execute(sql)
        hasil = cur.fetchone()  
        if hasil:
            self.carinorek.SetValue(str(hasil[0]))
            self.norek.SetValue(str(hasil[1]))
            self.kegiatan.SetValue(str(hasil[2]))
            self.lokasi.SetValue(str(hasil[3]))
            self.tahunini1.SetValue(str(hasil[4]))
            self.tahunini2.SetValue(str(hasil[5]))
            self.tahunini3.SetValue(str(hasil[6]))
            self.tahunini4.SetValue(str(hasil[7]))
            self.tahunini5.SetValue(str(hasil[8]))
            self.tahunini6.SetValue(str(hasil[9]))
            self.satuan.SetValue(str(hasil[11]))
            self.waktu1.SetValue(str(hasil[12]))
            self.waktu2.SetValue(str(hasil[13]))
            self.waktu3.SetValue(str(hasil[14]))
            self.waktu4.SetValue(str(hasil[15]))
            self.waktu5.SetValue(str(hasil[16]))
            self.waktu6.SetValue(str(hasil[17]))
            self.sasaran.SetValue(str(hasil[18]))
            self.diambil1.SetValue(str(hasil[31]))
            self.diambil2.SetValue(str(hasil[32]))
            self.diambil3.SetValue(str(hasil[33]))
            self.diambil4.SetValue(str(hasil[34]))
            self.diambil5.SetValue(str(hasil[35]))
            self.diambil6.SetValue(str(hasil[36]))
            self.apbn.SetValue(str(hasil[22]))
            self.apbdes.SetValue(str(hasil[23]))
            self.lain.SetValue(str(hasil[24]))
            self.jumlahsumber.SetValue(str(hasil[25]))
            self.ambilapbn.SetValue('0')
            self.ambilapbdes.SetValue('0')
            self.ambillain.SetValue('0')
            self.pola.SetValue(str(hasil[26]))
            self.baru.SetValue('Tidak')
            self.rehab.SetValue('Tidak')
            self.lama.SetValue('Tidak')
            self.nomor.SetValue(str(hasil[0]))
            if self.tahunini1.GetValue()=='0':
                self.diambil1.Disable()
            if self.tahunini2.GetValue()=='0':
                self.diambil2.Disable()
            if self.tahunini3.GetValue()=='0':
                self.diambil3.Disable()
            if self.tahunini4.GetValue()=='0':
                self.diambil4.Disable()
            if self.tahunini5.GetValue()=='0':
                self.diambil5.Disable()
            if self.tahunini6.GetValue()=='0':
                self.diambil6.Disable()
            if self.apbn.GetValue()=='0':
                self.ambilapbn.Disable()   
            if self.apbdes.GetValue()=='0':
                self.ambilapbdes.Disable() 
            if self.lain.GetValue()=='0':
                self.ambillain.Disable()
            self.tambah.Enable()
            self.edit.Disable()
            self.hapus.Disable()
            
            
            db.commit()
            
        else : 
            self.pesan = wx.MessageDialog(self,"Rekening Sudah digunakan RKP Cek RKP","Konfirmasi",wx.OK) 
            self.pesan.ShowModal() 
            self.carinorek.Clear()
            self.carinorek.SetFocus()
#-------------------------------------------------------------------------------
#Isi Bawah
#-------------------------------------------------------------------------------
    
    def isi1(self) : 
        self.setisi()
        rkode = str(self.rkp.GetValue())
        rperiode = str(self.periode.GetValue())
        carinomor=str(self.carinorek.GetValue())
        sql1="SELECT * FROM rkpsid WHERE norek LIKE '2.3%' AND no='"+carinomor+"' and id_rkp='"+rkode+"' AND periode='"+rperiode+"'  "
        cur.execute(sql1)
        hasil = cur.fetchone()  
        if hasil :
            self.carinorek.SetValue(str(hasil[0]))
            self.norek.SetValue(str(hasil[1]))
            self.kegiatan.SetValue(str(hasil[2]))
            self.lokasi.SetValue(str(hasil[3]))
            self.tahunini1.SetValue(str(hasil[4]))
            self.tahunini2.SetValue(str(hasil[5]))
            self.tahunini3.SetValue(str(hasil[6]))
            self.tahunini4.SetValue(str(hasil[7]))
            self.tahunini5.SetValue(str(hasil[8]))
            self.tahunini6.SetValue(str(hasil[9]))
            self.satuan.SetValue(str(hasil[11]))
            self.waktu1.SetValue(str(hasil[12]))
            self.waktu2.SetValue(str(hasil[13]))
            self.waktu3.SetValue(str(hasil[14]))
            self.waktu4.SetValue(str(hasil[15]))
            self.waktu5.SetValue(str(hasil[16]))
            self.waktu6.SetValue(str(hasil[17]))
            self.sasaran.SetValue(str(hasil[18]))
            self.diambil1.SetValue(str(hasil[28]))
            self.diambil2.SetValue(str(hasil[29]))
            self.diambil3.SetValue(str(hasil[30]))
            self.diambil4.SetValue(str(hasil[31]))
            self.diambil5.SetValue(str(hasil[32]))
            self.diambil6.SetValue(str(hasil[33]))
            self.apbn.SetValue(str(hasil[19]))
            self.apbdes.SetValue(str(hasil[20]))
            self.lain.SetValue(str(hasil[21]))
            self.jumlahsumber.SetValue(str(hasil[22]))
            self.ambilapbn.SetValue(str(hasil[35]))
            self.ambilapbdes.SetValue(str(hasil[36]))
            self.ambillain.SetValue(str(hasil[37]))
            self.pola.SetValue(str(hasil[23]))
            self.baru.SetValue(str(hasil[39]))
            self.rehab.SetValue(str(hasil[40]))
            self.lama.SetValue(str(hasil[41]))
            self.nomor.SetValue(str(hasil[0]))
            self.idjoin.SetValue(str(hasil[26]))
            
            if self.tahunini1.GetValue()=='0':
                self.diambil1.Disable()
            if self.tahunini2.GetValue()=='0':
                self.diambil2.Disable()
            if self.tahunini3.GetValue()=='0':
                self.diambil3.Disable()
            if self.tahunini4.GetValue()=='0':
                self.diambil4.Disable()
            if self.tahunini5.GetValue()=='0':
                self.diambil5.Disable()
            if self.tahunini6.GetValue()=='0':
                self.diambil6.Disable()
            if self.apbn.GetValue()=='0':
                self.ambilapbn.Disable()   
            if self.apbdes.GetValue()=='0':
                self.ambilapbdes.Disable() 
            if self.lain.GetValue()=='0':
                self.ambillain.Disable()
            
            self.tambah.Disable()
            self.edit.Enable()
            self.hapus.Enable()
            db.commit()
           
        else : 
            self.pesan = wx.MessageDialog(self,"Rekening Tidak Ada","Konfirmasi",wx.OK) 
            self.pesan.ShowModal() 
            self.carinorek.Clear()
            self.carinorek.SetFocus()

#-------------------------------------------------------------------------------
                
    def OnPembangunandesaListItemSelected(self, event):
        self.currentItem = event.m_itemIndex 
        b1=self.pembangunandesa.GetItem(self.currentItem).GetText() 
        self.carinorek.SetValue(b1)
        self.isi0()
    
    def OnRpjmpembangunandesaListItemSelected(self, event):
        self.currentItem = event.m_itemIndex 
        b=self.rpjmpembangunandesa.GetItem(self.currentItem).GetText() 
        self.carinorek.SetValue(b)
        self.isi1()   
#-------------------------------------------------------------------------------

    def OnMenuButton(self, event):
        self.Close()
        self.Destroy()
        db.commit()
#-------------------------------------------------------------------------------
#Tambah Data
#-------------------------------------------------------------------------------

    def OnTambahButton(self, event):
        rnorek=str(self.norek.GetValue())
        rkegiatan=str(self.kegiatan.GetValue())
        rlokasi=str(self.lokasi.GetValue())
        rwaktu1=str(self.waktu1.GetValue())
        rwaktu2=str(self.waktu2.GetValue())
        rwaktu3=str(self.waktu3.GetValue())
        rwaktu4=str(self.waktu4.GetValue())
        rwaktu5=str(self.waktu5.GetValue())
        rwaktu6=str(self.waktu6.GetValue())
        rtahunini1=str(self.tahunini1.GetValue())
        rtahunini2=str(self.tahunini2.GetValue())
        rtahunini3=str(self.tahunini3.GetValue())
        rtahunini4=str(self.tahunini4.GetValue())
        rtahunini5=str(self.tahunini5.GetValue())
        rtahunini6=str(self.tahunini6.GetValue())
        rdiambil1=str(self.diambil1.GetValue())
        rdiambil2=str(self.diambil2.GetValue())
        rdiambil3=str(self.diambil3.GetValue())
        rdiambil4=str(self.diambil4.GetValue())
        rdiambil5=str(self.diambil5.GetValue())
        rdiambil6=str(self.diambil6.GetValue())
        rsisa1=str(self.sisa1.GetValue())
        rsisa2=str(self.sisa2.GetValue())
        rsisa3=str(self.sisa3.GetValue())
        rsisa4=str(self.sisa4.GetValue())
        rsisa5=str(self.sisa5.GetValue())
        rsisa6=str(self.sisa6.GetValue())
        rjumlahsisa=str(self.jumlahsisa.GetValue())
        rjumlahsisa1=str(self.jumlahsisa1.GetValue())
        rjumlahsisa2=str(self.jumlahsisa2.GetValue())
        rsatuan=str(self.satuan.GetValue())
        rsasaran=str(self.sasaran.GetValue())
        rapbn=str(self.apbn.GetValue())
        rapbdes=str(self.apbdes.GetValue())
        rlain=str(self.lain.GetValue())
        rjumlahsumber=str(self.jumlahsumber.GetValue())
        rambilapbn=str(self.ambilapbn.GetValue())
        rambilapbdes=str(self.ambilapbdes.GetValue())
        rambillain=str(self.ambillain.GetValue())
        rjumlahdiambil=str(self.jumlahdiambil.GetValue())
        rsisaapbn=str(self.sisaapbn.GetValue())
        rsisaapbdes=str(self.sisaapbdes.GetValue())
        rsisalain=str(self.sisalain.GetValue())
        rakhir=str(self.akhir.GetValue())
        rpola=str(self.pola.GetValue())
        rnomor=str(self.nomor.GetValue())
        rbaru=str(self.baru.GetValue())
        rrehab=str(self.rehab.GetValue())
        rlama=str(self.lama.GetValue())
        rrkp=str(self.rkp.GetValue())
        rperiode=str(self.periode.GetValue())
        rjoin=str(self.idjoin.GetValue())
        
        if rjumlahsisa1 == '0':
            self.pesan = wx.MessageDialog(self,"Volume Pekerjan Tahun ini Belum Diisi","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
        else:    
            add_kejadian="INSERT INTO rkpsid (norek,kegiatan,lokasi,volume0,volume1,volume2,volume3,volume4,volume5,jumlahvolume,satuan,waktu1,waktu2,waktu3,waktu4,waktu5,waktu6,sasaran,apbn,apbdes,lain,totalbiaya,pola,id_rkp,id_join,periode,diambil1,diambil2,diambil3,diambil4,diambil5,diambil6,jumlahsisa1,ambilapbn,ambilapbdes,ambillain,jumlahdiambil,baru,rehab,lama,cekapbdes)  VALUES ('"+(rnorek)+"','"+(rkegiatan)+"','"+(rlokasi)+"','"+(rtahunini1)+"','"+(rtahunini2)+"','"+(rtahunini3)+"','"+(rtahunini4)+"','"+(rtahunini5)+"','"+(rtahunini6)+"','"+(rjumlahsisa2)+"','"+(rsatuan)+"','"+(rwaktu1)+"','"+(rwaktu2)+"','"+(rwaktu3)+"','"+(rwaktu4)+"','"+(rwaktu5)+"','"+(rwaktu6)+"','"+(rsasaran)+"','"+(rapbn)+"','"+(rapbdes)+"','"+(rlain)+"','"+(rjumlahsumber)+"','"+(rpola)+"','"+(rrkp)+"','"+(rnomor)+"','"+(rperiode)+"','"+(rdiambil1)+"','"+(rdiambil2)+"','"+(rdiambil3)+"','"+(rdiambil4)+"','"+(rdiambil5)+"','"+(rdiambil6)+"','"+(rjumlahsisa1)+"','"+(rambilapbn)+"','"+(rambilapbdes)+"','"+(rambillain)+"','"+(rjumlahdiambil)+"','"+(rbaru)+"','"+(rrehab)+"','"+(rlama)+"','0')"
            cur.execute(add_kejadian)
            update_rpjmdes="UPDATE rpjmdesasid SET diambil1='"+rdiambil1+"',diambil2='"+rdiambil2+"',diambil3='"+rdiambil3+"',diambil4='"+rdiambil4+"',diambil5='"+rdiambil5+"',diambil6='"+rdiambil6+"',jumlahsisa1='"+rjumlahsisa1+"',ambilapbn='"+rambilapbn+"',ambilapbdes='"+rambilapbdes+"',ambillain='"+rambillain+"',jumlahdiambil='"+rjumlahdiambil+"'  WHERE no='"+rnomor+"'"
            cur.execute(update_rpjmdes)
            add_baru="INSERT INTO rpjmdesasid (norek,kegiatan,lokasi,volume0,volume1,volume2,volume3,volume4,volume5,jumlahvolume,satuan,waktu1,waktu2,waktu3,waktu4,waktu5,waktu6,sasaran,biaya0,biaya1,biaya2,totalbiaya,pola,id_rkp,periode,diambil1,diambil2,diambil3,diambil4,diambil5,diambil6,jumlahsisa1,ambilapbn,ambilapbdes,ambillain,jumlahdiambil,id_join,keterangan) VALUES ('"+(rnorek)+"','"+(rkegiatan)+"','"+(rlokasi)+"','"+(rsisa1)+"','"+(rsisa2)+"','"+(rsisa3)+"','"+(rsisa4)+"','"+(rsisa5)+"','"+(rsisa6)+"','"+(rjumlahsisa)+"','"+(rsatuan)+"','"+(rwaktu1)+"','"+(rwaktu2)+"','"+(rwaktu3)+"','"+(rwaktu4)+"','"+(rwaktu5)+"','"+(rwaktu6)+"','"+(rsasaran)+"','"+(rsisaapbn)+"','"+(rsisaapbdes)+"','"+(rsisalain)+"','"+(rakhir)+"','"+(rpola)+"','"+(rrkp)+"','"+(rperiode)+"','0','0','0','0','0','0','0','0','0','0','0','"+(rnomor)+"','0')"
            cur.execute(add_baru)
            db.commit()
                
            self.pesan = wx.MessageDialog(self,"RKP Sudah Disimpan","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.awal()
#-------------------------------------------------------------------------------

    def OnEditButton(self, event):
        rnorek=str(self.norek.GetValue())
        rkegiatan=str(self.kegiatan.GetValue())
        rlokasi=str(self.lokasi.GetValue())
        rwaktu1=str(self.waktu1.GetValue())
        rwaktu2=str(self.waktu2.GetValue())
        rwaktu3=str(self.waktu3.GetValue())
        rwaktu4=str(self.waktu4.GetValue())
        rwaktu5=str(self.waktu5.GetValue())
        rwaktu6=str(self.waktu6.GetValue())
        rtahunini1=str(self.tahunini1.GetValue())
        rtahunini2=str(self.tahunini2.GetValue())
        rtahunini3=str(self.tahunini3.GetValue())
        rtahunini4=str(self.tahunini4.GetValue())
        rtahunini5=str(self.tahunini5.GetValue())
        rtahunini6=str(self.tahunini6.GetValue())
        rdiambil1=str(self.diambil1.GetValue())
        rdiambil2=str(self.diambil2.GetValue())
        rdiambil3=str(self.diambil3.GetValue())
        rdiambil4=str(self.diambil4.GetValue())
        rdiambil5=str(self.diambil5.GetValue())
        rdiambil6=str(self.diambil6.GetValue())
        rsisa1=str(self.sisa1.GetValue())
        rsisa2=str(self.sisa2.GetValue())
        rsisa3=str(self.sisa3.GetValue())
        rsisa4=str(self.sisa4.GetValue())
        rsisa5=str(self.sisa5.GetValue())
        rsisa6=str(self.sisa6.GetValue())
        rjumlahsisa=str(self.jumlahsisa.GetValue())
        rjumlahsisa1=str(self.jumlahsisa1.GetValue())
        rjumlahsisa2=str(self.jumlahsisa2.GetValue())
        rsatuan=str(self.satuan.GetValue())
        rsasaran=str(self.sasaran.GetValue())
        rapbn=str(self.apbn.GetValue())
        rapbdes=str(self.apbdes.GetValue())
        rlain=str(self.lain.GetValue())
        rjumlahsumber=str(self.jumlahsumber.GetValue())
        rambilapbn=str(self.ambilapbn.GetValue())
        rambilapbdes=str(self.ambilapbdes.GetValue())
        rambillain=str(self.ambillain.GetValue())
        rjumlahdiambil=str(self.jumlahdiambil.GetValue())
        rsisaapbn=str(self.sisaapbn.GetValue())
        rsisaapbdes=str(self.sisaapbdes.GetValue())
        rsisalain=str(self.sisalain.GetValue())
        rakhir=str(self.akhir.GetValue())
        rpola=str(self.pola.GetValue())
        rnomor=str(self.nomor.GetValue())
        rbaru=str(self.baru.GetValue())
        rrehab=str(self.rehab.GetValue())
        rlama=str(self.lama.GetValue())
        rrkp=str(self.rkp.GetValue())
        rperiode=str(self.periode.GetValue())
        rjoin=str(self.idjoin.GetValue())
        
        settahun=int(self.tahunrkp.GetValue())
        rkptahun=settahun+1
        srkptahun=str(rkptahun)
        
        cekrkp=int(rrkp)+1
        srkp=str(cekrkp)
        sql="SELECT * FROM rkpsid WHERE norek LIKE '2.3%' AND norek='"+rnorek+"' AND lokasi='"+rlokasi+"' AND id_rkp='"+srkp+"'"
        cur.execute(sql)
        hasil = cur.fetchone() 
        if hasil:
            self.pesan = wx.MessageDialog(self,"Anda Tidak Bisa Mengedit\n Karena Terdapat RKP Tahun ke:"+srkp+" \n Hapus Terlebih dahulu RKP Ke:"+srkp+" Tahun: "+srkptahun+" !!! ","Peringatan !!!",wx.OK) 
            self.pesan.ShowModal()
        else:    
            add_kejadian5="UPDATE rkpsid SET diambil1='"+rdiambil1+"',diambil2='"+rdiambil2+"',diambil3='"+rdiambil3+"',diambil4='"+rdiambil4+"',diambil5='"+rdiambil5+"',diambil6='"+rdiambil6+"',jumlahsisa1='"+rjumlahsisa1+"',ambilapbn='"+rambilapbn+"',ambilapbdes='"+rambilapbdes+"',ambillain='"+rambillain+"',jumlahdiambil='"+rjumlahdiambil+"',baru='"+rbaru+"',rehab='"+rrehab+"',lama='"+rlama+"'  WHERE no='"+rnomor+"'"
            cur.execute(add_kejadian5)
            update_rpjmdesa="UPDATE rpjmdesasid SET diambil1='"+rdiambil1+"',diambil2='"+rdiambil2+"',diambil3='"+rdiambil3+"',diambil4='"+rdiambil4+"',diambil5='"+rdiambil5+"',diambil6='"+rdiambil6+"',jumlahsisa1='"+rjumlahsisa1+"',ambilapbn='"+rambilapbn+"',ambilapbdes='"+rambilapbdes+"',ambillain='"+rambillain+"',jumlahdiambil='"+rjumlahdiambil+"'  WHERE no='"+rjoin+"'"
            cur.execute(update_rpjmdesa)
            update_rpjmdesa1="UPDATE rpjmdesasid SET volume0='"+rsisa1+"',volume1='"+rsisa2+"',volume2='"+rsisa3+"',volume3='"+rsisa4+"',volume4='"+rsisa5+"',volume5='"+rsisa6+"',jumlahvolume='"+rjumlahsisa2+"',biaya0='"+rsisaapbn+"',biaya1='"+rsisaapbdes+"',biaya2='"+rsisalain+"',totalbiaya='"+rakhir+"'  WHERE id_join='"+rjoin+"'"
            cur.execute(update_rpjmdesa1)
            self.pesan = wx.MessageDialog(self,"Data RKP Sudah Di Update","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.awal()
#-------------------------------------------------------------------------------

    def OnButton2Button(self, event):
        self.carinorek.SetValue('')
        self.awal()
#-------------------------------------------------------------------------------

    def OnButton3Button(self, event):
        rnorek=str(self.norek.GetValue())
        rlokasi=str(self.lokasi.GetValue())
        rrkp=str(self.rkp.GetValue())
       
        rjoin=str(self.idjoin.GetValue())
        rnomoran1 = str(self.nomor.GetValue())
        if rrkp=='1':   
            update_rpjmdesa="UPDATE rpjmdesasid SET diambil1='0',diambil2='0',diambil3='0',diambil4='0',diambil5='0',diambil6='0',jumlahsisa1='0',ambilapbn='0',ambilapbdes='0',ambillain='0',jumlahdiambil='0'  WHERE no='"+rjoin+"'"
            cur.execute(update_rpjmdesa)
            dihapus1="DELETE FROM rpjmdesasid WHERE norek='"+rnorek+"' AND lokasi='"+rlokasi+"' AND id_rkp='1'"
            cur.execute(dihapus1)
            dihapus2="DELETE FROM rpjmdesasid WHERE norek='"+rnorek+"' AND lokasi='"+rlokasi+"' AND id_rkp='2'"
            cur.execute(dihapus2)
            dihapus3="DELETE FROM rpjmdesasid WHERE norek='"+rnorek+"' AND lokasi='"+rlokasi+"' AND id_rkp='3'"
            cur.execute(dihapus3)
            dihapus4="DELETE FROM rpjmdesasid WHERE norek='"+rnorek+"' AND lokasi='"+rlokasi+"' AND id_rkp='4'"
            cur.execute(dihapus4)
            dihapus5="DELETE FROM rpjmdesasid WHERE norek='"+rnorek+"' AND lokasi='"+rlokasi+"' AND id_rkp='5'"
            cur.execute(dihapus5)
            dihapus6="DELETE FROM rpjmdesasid WHERE norek='"+rnorek+"' AND lokasi='"+rlokasi+"' AND id_rkp='6'"
            cur.execute(dihapus6)
            dihapus7="DELETE FROM rkpsid WHERE norek='"+rnorek+"' AND lokasi='"+rlokasi+"' AND id_rkp='2'"
            cur.execute(dihapus7)
            dihapus8="DELETE FROM rkpsid WHERE norek='"+rnorek+"' AND lokasi='"+rlokasi+"' AND id_rkp='3'"
            cur.execute(dihapus8)
            dihapus9="DELETE FROM rkpsid WHERE norek='"+rnorek+"' AND lokasi='"+rlokasi+"' AND id_rkp='4'"
            cur.execute(dihapus9)
            dihapus10="DELETE FROM rkpsid WHERE norek='"+rnorek+"' AND lokasi='"+rlokasi+"' AND id_rkp='5'"
            cur.execute(dihapus10)
            dihapus11="DELETE FROM rkpsid WHERE norek='"+rnorek+"' AND lokasi='"+rlokasi+"' AND id_rkp='6'"
            cur.execute(dihapus11)
            dihapus12="DELETE FROM rkpsid WHERE no='"+rnomoran1+"'"
            cur.execute(dihapus12)
            db.commit()
            self.pesan = wx.MessageDialog(self,"Data Sudah Dihapus","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.awal()
            
        if rrkp=='2':   
            update_rpjmdesa="UPDATE rpjmdesasid SET diambil1='0',diambil2='0',diambil3='0',diambil4='0',diambil5='0',diambil6='0',jumlahsisa1='0',ambilapbn='0',ambilapbdes='0',ambillain='0',jumlahdiambil='0'  WHERE no='"+rjoin+"'"
            cur.execute(update_rpjmdesa)
            dihapus2="DELETE FROM rpjmdesasid WHERE norek='"+rnorek+"' AND lokasi='"+rlokasi+"' AND id_rkp='2'"
            cur.execute(dihapus2)
            dihapus3="DELETE FROM rpjmdesasid WHERE norek='"+rnorek+"' AND lokasi='"+rlokasi+"' AND id_rkp='3'"
            cur.execute(dihapus3)
            dihapus4="DELETE FROM rpjmdesasid WHERE norek='"+rnorek+"' AND lokasi='"+rlokasi+"' AND id_rkp='4'"
            cur.execute(dihapus4)
            dihapus5="DELETE FROM rpjmdesasid WHERE norek='"+rnorek+"' AND lokasi='"+rlokasi+"' AND id_rkp='5'"
            cur.execute(dihapus5)
            dihapus6="DELETE FROM rpjmdesasid WHERE norek='"+rnorek+"' AND lokasi='"+rlokasi+"' AND id_rkp='6'"
            cur.execute(dihapus6)
            dihapus8="DELETE FROM rkpsid WHERE norek='"+rnorek+"' AND lokasi='"+rlokasi+"' AND id_rkp='3'"
            cur.execute(dihapus8)
            dihapus9="DELETE FROM rkpsid WHERE norek='"+rnorek+"' AND lokasi='"+rlokasi+"' AND id_rkp='4'"
            cur.execute(dihapus9)
            dihapus10="DELETE FROM rkpsid WHERE norek='"+rnorek+"' AND lokasi='"+rlokasi+"' AND id_rkp='5'"
            cur.execute(dihapus10)
            dihapus11="DELETE FROM rkpsid WHERE norek='"+rnorek+"' AND lokasi='"+rlokasi+"' AND id_rkp='6'"
            cur.execute(dihapus11)
            dihapus12="DELETE FROM rkpsid WHERE no='"+rnomoran1+"'"
            cur.execute(dihapus12)
            db.commit()
            self.pesan = wx.MessageDialog(self,"Data Sudah Dihapus","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.awal()
        
        if rrkp=='3':   
            update_rpjmdesa="UPDATE rpjmdesasid SET diambil1='0',diambil2='0',diambil3='0',diambil4='0',diambil5='0',diambil6='0',jumlahsisa1='0',ambilapbn='0',ambilapbdes='0',ambillain='0',jumlahdiambil='0'  WHERE no='"+rjoin+"'"
            cur.execute(update_rpjmdesa)
            dihapus3="DELETE FROM rpjmdesasid WHERE norek='"+rnorek+"' AND lokasi='"+rlokasi+"' AND id_rkp='3'"
            cur.execute(dihapus3)
            dihapus4="DELETE FROM rpjmdesasid WHERE norek='"+rnorek+"' AND lokasi='"+rlokasi+"' AND id_rkp='4'"
            cur.execute(dihapus4)
            dihapus5="DELETE FROM rpjmdesasid WHERE norek='"+rnorek+"' AND lokasi='"+rlokasi+"' AND id_rkp='5'"
            cur.execute(dihapus5)
            dihapus6="DELETE FROM rpjmdesasid WHERE norek='"+rnorek+"' AND lokasi='"+rlokasi+"' AND id_rkp='6'"
            cur.execute(dihapus6)
            dihapus9="DELETE FROM rkpsid WHERE norek='"+rnorek+"' AND lokasi='"+rlokasi+"' AND id_rkp='4'"
            cur.execute(dihapus9)
            dihapus10="DELETE FROM rkpsid WHERE norek='"+rnorek+"' AND lokasi='"+rlokasi+"' AND id_rkp='5'"
            cur.execute(dihapus10)
            dihapus11="DELETE FROM rkpsid WHERE norek='"+rnorek+"' AND lokasi='"+rlokasi+"' AND id_rkp='6'"
            cur.execute(dihapus11)
            dihapus12="DELETE FROM rkpsid WHERE no='"+rnomoran1+"'"
            cur.execute(dihapus12)
            db.commit()
            self.pesan = wx.MessageDialog(self,"Data Sudah Dihapus","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.awal()
        if rrkp=='4':   
            update_rpjmdesa="UPDATE rpjmdesasid SET diambil1='0',diambil2='0',diambil3='0',diambil4='0',diambil5='0',diambil6='0',jumlahsisa1='0',ambilapbn='0',ambilapbdes='0',ambillain='0',jumlahdiambil='0'  WHERE no='"+rjoin+"'"
            cur.execute(update_rpjmdesa)
            dihapus4="DELETE FROM rpjmdesasid WHERE norek='"+rnorek+"' AND lokasi='"+rlokasi+"' AND id_rkp='4'"
            cur.execute(dihapus4)
            dihapus5="DELETE FROM rpjmdesasid WHERE norek='"+rnorek+"' AND lokasi='"+rlokasi+"' AND id_rkp='5'"
            cur.execute(dihapus5)
            dihapus6="DELETE FROM rpjmdesasid WHERE norek='"+rnorek+"' AND lokasi='"+rlokasi+"' AND id_rkp='6'"
            cur.execute(dihapus6)
            dihapus10="DELETE FROM rkpsid WHERE norek='"+rnorek+"' AND lokasi='"+rlokasi+"' AND id_rkp='5'"
            cur.execute(dihapus10)
            dihapus11="DELETE FROM rkpsid WHERE norek='"+rnorek+"' AND lokasi='"+rlokasi+"' AND id_rkp='6'"
            cur.execute(dihapus11)
            dihapus12="DELETE FROM rkpsid WHERE no='"+rnomoran1+"'"
            cur.execute(dihapus12)
            db.commit()
            self.pesan = wx.MessageDialog(self,"Data Sudah Dihapus","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.awal()
        
        if rrkp=='5':   
            update_rpjmdesa="UPDATE rpjmdesasid SET diambil1='0',diambil2='0',diambil3='0',diambil4='0',diambil5='0',diambil6='0',jumlahsisa1='0',ambilapbn='0',ambilapbdes='0',ambillain='0',jumlahdiambil='0'  WHERE no='"+rjoin+"'"
            cur.execute(update_rpjmdesa)
            dihapus5="DELETE FROM rpjmdesasid WHERE norek='"+rnorek+"' AND lokasi='"+rlokasi+"' AND id_rkp='5'"
            cur.execute(dihapus5)
            dihapus6="DELETE FROM rpjmdesasid WHERE norek='"+rnorek+"' AND lokasi='"+rlokasi+"' AND id_rkp='6'"
            cur.execute(dihapus6)
            dihapus11="DELETE FROM rkpsid WHERE norek='"+rnorek+"' AND lokasi='"+rlokasi+"' AND id_rkp='6'"
            cur.execute(dihapus11)
            dihapus12="DELETE FROM rkpsid WHERE no='"+rnomoran1+"'"
            cur.execute(dihapus12)
            db.commit()
            self.pesan = wx.MessageDialog(self,"Data Sudah Dihapus","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.awal()
            
        if rrkp=='6':   
            update_rpjmdesa="UPDATE rpjmdesasid SET diambil1='0',diambil2='0',diambil3='0',diambil4='0',diambil5='0',diambil6='0',jumlahsisa1='0',ambilapbn='0',ambilapbdes='0',ambillain='0',jumlahdiambil='0'  WHERE no='"+rjoin+"'"
            cur.execute(update_rpjmdesa)
            dihapus6="DELETE FROM rpjmdesasid WHERE norek='"+rnorek+"' AND lokasi='"+rlokasi+"' AND id_rkp='6'"
            cur.execute(dihapus6)
            dihapus12="DELETE FROM rkpsid WHERE no='"+rnomoran1+"'"
            cur.execute(dihapus12)
            db.commit()
            self.pesan = wx.MessageDialog(self,"Data Sudah Dihapus","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.awal()
#-------------------------------------------------------------------------------

    def OnDiambil1Text(self, event):
        rdiambil1=str(self.diambil1.GetValue())
        if rdiambil1.isdigit():
            self.diambil2.SetValue('0')
            self.diambil3.SetValue('0')
            self.diambil4.SetValue('0')
            self.diambil5.SetValue('0')
            self.diambil6.SetValue('0')
            rdiambil2=str(self.diambil2.GetValue())
            rdiambil3=str(self.diambil3.GetValue())
            rdiambil4=str(self.diambil4.GetValue())
            rdiambil5=str(self.diambil5.GetValue())
            rdiambil6=str(self.diambil6.GetValue())
            intdiambil1=int(rdiambil1)
            intdiambil2=int(rdiambil2)
            intdiambil3=int(rdiambil3)
            intdiambil4=int(rdiambil4)
            intdiambil5=int(rdiambil5)
            intdiambil6=int(rdiambil6)
            rambil1=int(self.tahunini1.GetValue())
            rambil2=int(self.tahunini2.GetValue())
            rambil3=int(self.tahunini3.GetValue())
            rambil4=int(self.tahunini4.GetValue())
            rambil5=int(self.tahunini5.GetValue())
            rambil6=int(self.tahunini6.GetValue())
            rambiltotal=rambil1+rambil2+rambil3+rambil4+rambil5+rambil6
            rtotal=rambil1-intdiambil1
            rhabis=intdiambil1+intdiambil2+intdiambil3+intdiambil4+intdiambil5+intdiambil6
            rsisa=rambiltotal-intdiambil1
            self.sisa1.SetValue(str(rtotal))
            self.jumlahsisa2.SetValue(str(rambiltotal))
            self.jumlahsisa1.SetValue(str(rhabis))
            self.jumlahsisa.SetValue(str(rsisa))
            
        elif rdiambil1 =='':
            self.pesan = wx.MessageDialog(self,"hanya angka","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.diambil1.SetValue('0')
        else:
            self.pesan = wx.MessageDialog(self,"hanya angka","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.diambil1.SetValue('0')

    def OnDiambil2Text(self, event):
        rdiambil2=str(self.diambil2.GetValue())
        if rdiambil2.isdigit():
            self.diambil3.SetValue('0')
            self.diambil4.SetValue('0')
            self.diambil5.SetValue('0')
            self.diambil6.SetValue('0')
            rdiambil1=str(self.diambil1.GetValue())
            rdiambil3=str(self.diambil3.GetValue())
            rdiambil4=str(self.diambil4.GetValue())
            rdiambil5=str(self.diambil5.GetValue())
            rdiambil6=str(self.diambil6.GetValue())
            intdiambil1=int(rdiambil1)
            intdiambil2=int(rdiambil2)
            intdiambil3=int(rdiambil3)
            intdiambil4=int(rdiambil4)
            intdiambil5=int(rdiambil5)
            intdiambil6=int(rdiambil6)
            rambil1=int(self.tahunini1.GetValue())
            rambil2=int(self.tahunini2.GetValue())
            rambil3=int(self.tahunini3.GetValue())
            rambil4=int(self.tahunini4.GetValue())
            rambil5=int(self.tahunini5.GetValue())
            rambil6=int(self.tahunini6.GetValue())
            rambiltotal=rambil1+rambil2+rambil3+rambil4+rambil5+rambil6
            rtotal=rambil2-intdiambil2
            rhabis=intdiambil2+intdiambil1+intdiambil3+intdiambil4+intdiambil5+intdiambil6
            rsisa=rambiltotal-rhabis
            self.sisa2.SetValue(str(rtotal))
            self.jumlahsisa2.SetValue(str(rambiltotal))
            self.jumlahsisa1.SetValue(str(rhabis))
            self.jumlahsisa.SetValue(str(rsisa))
        
        elif rdiambil2 =='':
            self.pesan = wx.MessageDialog(self,"hanya angka","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.diambil2.SetValue('0')
        else:
            self.pesan = wx.MessageDialog(self,"hanya angka","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.diambil2.SetValue('0')

    def OnDiambil3Text(self, event):
        rdiambil3=str(self.diambil3.GetValue())
        if rdiambil3.isdigit():
            self.diambil4.SetValue('0')
            self.diambil5.SetValue('0')
            self.diambil6.SetValue('0')
            rdiambil1=str(self.diambil1.GetValue())
            rdiambil2=str(self.diambil2.GetValue())
            rdiambil4=str(self.diambil4.GetValue())
            rdiambil5=str(self.diambil5.GetValue())
            rdiambil6=str(self.diambil6.GetValue())
            intdiambil1=int(rdiambil1)
            intdiambil2=int(rdiambil2)
            intdiambil3=int(rdiambil3)
            intdiambil4=int(rdiambil4)
            intdiambil5=int(rdiambil5)
            intdiambil6=int(rdiambil6)
            rambil1=int(self.tahunini1.GetValue())
            rambil2=int(self.tahunini2.GetValue())
            rambil3=int(self.tahunini3.GetValue())
            rambil4=int(self.tahunini4.GetValue())
            rambil5=int(self.tahunini5.GetValue())
            rambil6=int(self.tahunini6.GetValue())
            rambiltotal=rambil1+rambil2+rambil3+rambil4+rambil5+rambil6
            rtotal=rambil3-intdiambil3
            rhabis=intdiambil2+intdiambil1+intdiambil3+intdiambil4+intdiambil5+intdiambil6
            rsisa=rambiltotal-rhabis
            self.sisa3.SetValue(str(rtotal))
            self.jumlahsisa2.SetValue(str(rambiltotal))
            self.jumlahsisa1.SetValue(str(rhabis))
            self.jumlahsisa.SetValue(str(rsisa))
            
        elif rdiambil3 =='':
            self.pesan = wx.MessageDialog(self,"hanya angka","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.diambil3.SetValue('0')
        else:
            self.pesan = wx.MessageDialog(self,"hanya angka","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.diambil3.SetValue('0')

    def OnDiambil4Text(self, event):
        rdiambil4=str(self.diambil4.GetValue())
        if rdiambil4.isdigit():
            self.diambil5.SetValue('0')
            self.diambil6.SetValue('0')
            rdiambil1=str(self.diambil1.GetValue())
            rdiambil2=str(self.diambil2.GetValue())
            rdiambil3=str(self.diambil3.GetValue())
            rdiambil5=str(self.diambil5.GetValue())
            rdiambil6=str(self.diambil6.GetValue())
            intdiambil1=int(rdiambil1)
            intdiambil2=int(rdiambil2)
            intdiambil3=int(rdiambil3)
            intdiambil4=int(rdiambil4)
            intdiambil5=int(rdiambil5)
            intdiambil6=int(rdiambil6)
            rambil1=int(self.tahunini1.GetValue())
            rambil2=int(self.tahunini2.GetValue())
            rambil3=int(self.tahunini3.GetValue())
            rambil4=int(self.tahunini4.GetValue())
            rambil5=int(self.tahunini5.GetValue())
            rambil6=int(self.tahunini6.GetValue())
            rambiltotal=rambil1+rambil2+rambil3+rambil4+rambil5+rambil6
            rtotal=rambil4-intdiambil4
            rhabis=intdiambil2+intdiambil1+intdiambil3+intdiambil4+intdiambil5+intdiambil6
            rsisa=rambiltotal-rhabis
            self.sisa4.SetValue(str(rtotal))
            self.jumlahsisa2.SetValue(str(rambiltotal))
            self.jumlahsisa1.SetValue(str(rhabis))
            self.jumlahsisa.SetValue(str(rsisa))
            
        elif rdiambil4 =='':
            self.pesan = wx.MessageDialog(self,"hanya angka","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.diambil4.SetValue('0')
        else:
            self.pesan = wx.MessageDialog(self,"hanya angka","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.diambil4.SetValue('0')
    def OnDiambil5Text(self, event):
        rdiambil5=str(self.diambil5.GetValue())
        if rdiambil5.isdigit():
            self.diambil6.SetValue('0')
            rdiambil1=str(self.diambil1.GetValue())
            rdiambil2=str(self.diambil2.GetValue())
            rdiambil3=str(self.diambil3.GetValue())
            rdiambil4=str(self.diambil4.GetValue())
            rdiambil6=str(self.diambil6.GetValue())
            intdiambil1=int(rdiambil1)
            intdiambil2=int(rdiambil2)
            intdiambil3=int(rdiambil3)
            intdiambil4=int(rdiambil4)
            intdiambil5=int(rdiambil5)
            intdiambil6=int(rdiambil6)
            rambil1=int(self.tahunini1.GetValue())
            rambil2=int(self.tahunini2.GetValue())
            rambil3=int(self.tahunini3.GetValue())
            rambil4=int(self.tahunini4.GetValue())
            rambil5=int(self.tahunini5.GetValue())
            rambil6=int(self.tahunini6.GetValue())
            rambiltotal=rambil1+rambil2+rambil3+rambil4+rambil5+rambil6
            
            rtotal=rambil5-intdiambil5
            rhabis=intdiambil2+intdiambil1+intdiambil3+intdiambil4+intdiambil5+intdiambil6
            rsisa=rambiltotal-rhabis
            
            self.sisa5.SetValue(str(rtotal))
            self.jumlahsisa2.SetValue(str(rambiltotal))
            self.jumlahsisa1.SetValue(str(rhabis))
            self.jumlahsisa.SetValue(str(rsisa))
            
        elif rdiambil5 =='':
            self.pesan = wx.MessageDialog(self,"Tidak Boleh Kosong Hanya Angka","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.diambil5.SetValue('0')
        else:
            self.pesan = wx.MessageDialog(self,"hanya angka","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.diambil5.SetValue('0')

    def OnDiambil6Text(self, event):
        rdiambil6=str(self.diambil6.GetValue())
        if rdiambil6.isdigit():
            rdiambil1=str(self.diambil1.GetValue())
            rdiambil2=str(self.diambil2.GetValue())
            rdiambil3=str(self.diambil3.GetValue())
            rdiambil4=str(self.diambil4.GetValue())
            rdiambil5=str(self.diambil5.GetValue())
            intdiambil1=int(rdiambil1)
            intdiambil2=int(rdiambil2)
            intdiambil3=int(rdiambil3)
            intdiambil4=int(rdiambil4)
            intdiambil5=int(rdiambil5)
            intdiambil6=int(rdiambil6)
            rambil1=int(self.tahunini1.GetValue())
            rambil2=int(self.tahunini2.GetValue())
            rambil3=int(self.tahunini3.GetValue())
            rambil4=int(self.tahunini4.GetValue())
            rambil5=int(self.tahunini5.GetValue())
            rambil6=int(self.tahunini6.GetValue())
            rambiltotal=rambil1+rambil2+rambil3+rambil4+rambil5+rambil6
            rtotal=rambil6-intdiambil6
            rhabis=intdiambil2+intdiambil1+intdiambil3+intdiambil4+intdiambil5+intdiambil6
            rsisa=rambiltotal-rhabis
            self.sisa6.SetValue(str(rtotal))
            self.jumlahsisa2.SetValue(str(rambiltotal))
            self.jumlahsisa1.SetValue(str(rhabis))
            self.jumlahsisa.SetValue(str(rsisa))
        elif rdiambil6 =='':
            self.pesan = wx.MessageDialog(self,"hanya angka","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.diambil6.SetValue('0')
        else:
            self.pesan = wx.MessageDialog(self,"hanya angka","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.diambil6.SetValue('0')
#-------------------------------------------------------------------------------
#Pemilihan Tahun RKP
#-------------------------------------------------------------------------------

    def OnRkpCombobox(self, event):
        cek=int(self.periode.GetValue())
        cek2=str(self.rkp.GetValue())
        if cek2=='1':
            intcek2=int(cek2)
            cekdulu=cek+0
            self.tahunrkp.SetValue(str(cekdulu))
        if cek2=='2':
            intcek2=int(cek2)
            cekdulu=cek+1
            self.tahunrkp.SetValue(str(cekdulu))
        if cek2=='3':
            intcek2=int(cek2)
            cekdulu=cek+2
            self.tahunrkp.SetValue(str(cekdulu))
        if cek2=='4':
            intcek2=int(cek2)
            cekdulu=cek+3
            self.tahunrkp.SetValue(str(cekdulu))
        if cek2=='5':
            intcek2=int(cek2)
            cekdulu=cek+4
            self.tahunrkp.SetValue(str(cekdulu))
        if cek2=='6':
            intcek2=int(cek2)
            cekdulu=cek+5
            self.tahunrkp.SetValue(str(cekdulu))    

    def OnResetButton(self, event):
        self.carinorek.SetValue('')
        self.tambah.Disable()
        self.awal()

    def OnAmbilapbnText(self, event):
        #self.ambilapbdes.SetValue('0')
        #self.ambillain.SetValue('0')
        
        rambilapbn=str(self.ambilapbn.GetValue())
        if rambilapbn.isdigit():
            self.ambilapbdes.SetValue('0')
            self.ambillain.SetValue('0')
        
            rambilapbn=str(self.ambilapbn.GetValue())
            rambilapbdes=str(self.ambilapbdes.GetValue())
            rambillain=str(self.ambillain.GetValue())
                
            intrambilapbn=int(rambilapbn)
            intrambilapbdes=int(rambilapbdes)
            intrambillain=int(rambillain)
            
            irambilapbn=int(self.apbn.GetValue())
            irambilapbdes=int(self.apbdes.GetValue())
            irambillain=int(self.lain.GetValue())
            
            rambiltotalsumber=irambilapbn+irambilapbdes+irambillain
            
            rtotalapbn=irambilapbn-intrambilapbn
            rhabisapbn=intrambilapbn+intrambilapbdes+intrambillain
            rsisaapbn=rambiltotalsumber-rhabisapbn
            
            self.sisaapbn.SetValue(str(rtotalapbn))
            self.jumlahdiambil.SetValue(str(rhabisapbn))
            self.akhir.SetValue(str(rsisaapbn))
            
        elif rambilapbn =='':
            self.pesan = wx.MessageDialog(self,"hanya angka","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.ambilapbn.SetValue('0')
        
        else:
            self.pesan = wx.MessageDialog(self,"hanya angka","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.ambilapbn.SetValue('0')
        
    def OnAmbilapbdesText(self, event):
        rambilapbdes=str(self.ambilapbdes.GetValue())
        if rambilapbdes.isdigit():
            self.ambillain.SetValue('0')
            rambilapbn=str(self.ambilapbn.GetValue())
            rambillain=str(self.ambillain.GetValue())
            intrambilapbn=int(rambilapbn)
            intrambilapbdes=int(rambilapbdes)
            intrambillain=int(rambillain)
            irambilapbn=int(self.apbn.GetValue())
            irambilapbdes=int(self.apbdes.GetValue())
            irambillain=int(self.lain.GetValue())
            rambiltotalsumber=irambilapbn+irambilapbdes+irambillain
            rtotalapbdes=irambilapbdes-intrambilapbdes
            rhabisapbdes=intrambilapbn+intrambilapbdes+intrambillain
            rsisaapbdes=rambiltotalsumber-rhabisapbdes
            self.sisaapbdes.SetValue(str(rtotalapbdes))
            self.jumlahdiambil.SetValue(str(rhabisapbdes))
            self.akhir.SetValue(str(rsisaapbdes))
        elif rambilapbdes =='':
            self.pesan = wx.MessageDialog(self,"hanya angka","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.ambilapbdes.SetValue('0')
        else:
            self.pesan = wx.MessageDialog(self,"hanya angka","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.ambilapbdes.SetValue('0')

    def OnAmbillainText(self, event):
        rambillain=str(self.ambillain.GetValue())
        if rambillain.isdigit():
            rambilapbn=str(self.ambilapbn.GetValue())
            rambilapbdes=str(self.ambilapbdes.GetValue())
            
                
            intrambilapbn=int(rambilapbn)
            intrambilapbdes=int(rambilapbdes)
            intrambillain=int(rambillain)
            
            irambilapbn=int(self.apbn.GetValue())
            irambilapbdes=int(self.apbdes.GetValue())
            irambillain=int(self.lain.GetValue())
            
            rambiltotalsumber=irambilapbn+irambilapbdes+irambillain
            
            rtotallain=irambillain-intrambillain
            rhabislain=intrambilapbn+intrambilapbdes+intrambillain
            rsisalain=rambiltotalsumber-rhabislain
            
            self.sisalain.SetValue(str(rtotallain))
            self.jumlahdiambil.SetValue(str(rhabislain))
            self.akhir.SetValue(str(rsisalain))
            
        elif rambillain =='':
            self.pesan = wx.MessageDialog(self,"hanya angka","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.ambillain.SetValue('0')
        else:
            self.pesan = wx.MessageDialog(self,"hanya angka","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.ambillain.SetValue('0')

   
