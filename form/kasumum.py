#Boa:Frame:kasumum
#-------------------------------------------------------------------------------
#Sistem Informasi dan Administrasi Perdesaan
#pengembang johandri@ictwatch.id
#-------------------------------------------------------------------------------

import wx

def create(parent):
    return kasumum(parent)

[wxID_KASUMUM, wxID_KASUMUMBUAT, wxID_KASUMUMCETAK, wxID_KASUMUMLISTCTRL1, 
 wxID_KASUMUMMENU, wxID_KASUMUMPERIODE, wxID_KASUMUMSTATICTEXT1, 
 wxID_KASUMUMSTATICTEXT2, wxID_KASUMUMSTATICTEXT3, wxID_KASUMUMSTATICTEXT4, 
 wxID_KASUMUMTAHUN, wxID_KASUMUMTAHUNRKP, 
] = [wx.NewId() for _init_ctrls in range(12)]

class kasumum(wx.Frame):
    def _init_coll_listCtrl1_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT, heading=u'No',
              width=-1)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT,
              heading=u'Tanggal', width=-1)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT,
              heading=u'Nomor Rekening', width=-1)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_LEFT,
              heading=u'Uraian', width=-1)
        parent.InsertColumn(col=4, format=wx.LIST_FORMAT_LEFT,
              heading=u'Penerimaan (Rp)', width=-1)
        parent.InsertColumn(col=5, format=wx.LIST_FORMAT_LEFT,
              heading=u'Pengeluaran (Rp)', width=-1)
        parent.InsertColumn(col=6, format=wx.LIST_FORMAT_LEFT,
              heading=u'No Bukti', width=-1)
        parent.InsertColumn(col=7, format=wx.LIST_FORMAT_LEFT,
              heading=u'Jumlah Pengeluaran Komulatif', width=-1)
        parent.InsertColumn(col=8, format=wx.LIST_FORMAT_LEFT, heading=u'Saldo',
              width=-1)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_KASUMUM, name=u'kasumum', parent=prnt,
              pos=wx.Point(409, 194), size=wx.Size(919, 475),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Buku Kas Umum')
        self.SetClientSize(wx.Size(911, 445))
        self.Center(wx.BOTH)
        self.SetBackgroundColour(wx.Colour(192, 192, 192))

        self.listCtrl1 = wx.ListCtrl(id=wxID_KASUMUMLISTCTRL1, name='listCtrl1',
              parent=self, pos=wx.Point(5, 35), size=wx.Size(902, 380),
              style=wx.LC_REPORT)
        self._init_coll_listCtrl1_Columns(self.listCtrl1)

        self.staticText1 = wx.StaticText(id=wxID_KASUMUMSTATICTEXT1,
              label=u'BUKU KAS UMUM', name='staticText1', parent=self,
              pos=wx.Point(8, 15), size=wx.Size(94, 13), style=0)
        self.staticText1.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Tahoma'))

        self.cetak = wx.Button(id=wxID_KASUMUMCETAK, label=u'Cetak Buku Kas',
              name=u'cetak', parent=self, pos=wx.Point(663, 420),
              size=wx.Size(117, 23), style=0)

        self.menu = wx.Button(id=wxID_KASUMUMMENU, label=u'Kembali Ke Menu',
              name=u'menu', parent=self, pos=wx.Point(784, 419),
              size=wx.Size(118, 23), style=0)

        self.periode = wx.TextCtrl(id=wxID_KASUMUMPERIODE, name=u'periode',
              parent=self, pos=wx.Point(479, 8), size=wx.Size(100, 21), style=0,
              value=u'')

        self.tahunrkp = wx.ComboBox(choices=[], id=wxID_KASUMUMTAHUNRKP,
              name=u'tahunrkp', parent=self, pos=wx.Point(604, 8),
              size=wx.Size(39, 21), style=0, value=u'')
        self.tahunrkp.SetLabel(u'')

        self.tahun = wx.TextCtrl(id=wxID_KASUMUMTAHUN, name=u'tahun',
              parent=self, pos=wx.Point(687, 8), size=wx.Size(100, 21), style=0,
              value=u'')

        self.buat = wx.Button(id=wxID_KASUMUMBUAT, label=u'Buat Kas Umum',
              name=u'buat', parent=self, pos=wx.Point(792, 8), size=wx.Size(112,
              23), style=0)

        self.staticText2 = wx.StaticText(id=wxID_KASUMUMSTATICTEXT2,
              label=u'Tahun', name='staticText2', parent=self, pos=wx.Point(647,
              11), size=wx.Size(31, 13), style=0)

        self.staticText3 = wx.StaticText(id=wxID_KASUMUMSTATICTEXT3,
              label=u'RKP', name='staticText3', parent=self, pos=wx.Point(582,
              13), size=wx.Size(20, 13), style=0)

        self.staticText4 = wx.StaticText(id=wxID_KASUMUMSTATICTEXT4,
              label=u'Periode', name='staticText4', parent=self,
              pos=wx.Point(439, 11), size=wx.Size(37, 13), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)
