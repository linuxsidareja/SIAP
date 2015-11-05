#Boa:Frame:rab
#-------------------------------------------------------------------------------
#Sistem Informasi dan Administrasi Perdesaan
#pengembang johandri@ictwatch.id
#-------------------------------------------------------------------------------

import wx
import sqlite3

db = sqlite3.connect('siap.db')
cur = db.cursor()


def create(parent):
    return rab(parent)

[wxID_RAB, wxID_RABAPBDES, wxID_RABBIDANG, wxID_RABEDIT, wxID_RABHAPUS, 
 wxID_RABHARGA, wxID_RABJUMLAH, wxID_RABKEGIATAN, wxID_RABMENU, wxID_RABNOMOR, 
 wxID_RABNOMORREK, wxID_RABRAB, wxID_RABRESET, wxID_RABSATUAN, 
 wxID_RABSTATICTEXT1, wxID_RABSTATICTEXT10, wxID_RABSTATICTEXT11, 
 wxID_RABSTATICTEXT12, wxID_RABSTATICTEXT2, wxID_RABSTATICTEXT3, 
 wxID_RABSTATICTEXT4, wxID_RABSTATICTEXT5, wxID_RABSTATICTEXT6, 
 wxID_RABSTATICTEXT7, wxID_RABSTATICTEXT8, wxID_RABSTATICTEXT9, wxID_RABTAHUN, 
 wxID_RABTAMBAH, wxID_RABURAIAN, wxID_RABURAIANRAB, wxID_RABVOLUME, 
 wxID_RABWAKTU, 
] = [wx.NewId() for _init_ctrls in range(32)]

class rab(wx.Frame):
    def _init_coll_apbdes_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT,
              heading=u'Record', width=-1)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT, heading=u'Norek',
              width=-1)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT,
              heading=u'Kegiatan', width=-1)

    def _init_coll_rab_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT,
              heading=u'Record', width=-1)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT,
              heading=u'Bidang', width=-1)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT, heading=u'Norek',
              width=-1)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_LEFT,
              heading=u'Uraian', width=-1)
        parent.InsertColumn(col=4, format=wx.LIST_FORMAT_LEFT, heading=u'Waktu',
              width=-1)
        parent.InsertColumn(col=5, format=wx.LIST_FORMAT_LEFT,
              heading=u'Volume', width=-1)
        parent.InsertColumn(col=6, format=wx.LIST_FORMAT_LEFT,
              heading=u'Satuan', width=-1)
        parent.InsertColumn(col=7, format=wx.LIST_FORMAT_LEFT,
              heading=u'Harga Satuan', width=-1)
        parent.InsertColumn(col=8, format=wx.LIST_FORMAT_LEFT,
              heading=u'Jumlah', width=-1)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_RAB, name=u'rab', parent=prnt,
              pos=wx.Point(424, 194), size=wx.Size(889, 475),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Rencana Anggaran Biaya')
        self.SetClientSize(wx.Size(881, 445))
        self.Center(wx.BOTH)
        self.SetBackgroundColour(wx.Colour(192, 192, 192))

        self.apbdes = wx.ListCtrl(id=wxID_RABAPBDES, name=u'apbdes',
              parent=self, pos=wx.Point(6, 10), size=wx.Size(340, 221),
              style=wx.LC_REPORT)
        self._init_coll_apbdes_Columns(self.apbdes)
        self.apbdes.Bind(wx.EVT_LIST_ITEM_SELECTED,
              self.OnApbdesListItemSelected, id=wxID_RABAPBDES)

        self.rab = wx.ListCtrl(id=wxID_RABRAB, name=u'rab', parent=self,
              pos=wx.Point(8, 238), size=wx.Size(865, 202), style=wx.LC_REPORT)
        self._init_coll_rab_Columns(self.rab)
        self.rab.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnRabListItemActivated,
              id=wxID_RABRAB)

        self.staticText1 = wx.StaticText(id=wxID_RABSTATICTEXT1,
              label=u'APB Desa Tahun', name='staticText1', parent=self,
              pos=wx.Point(352, 16), size=wx.Size(80, 13), style=0)

        self.tahun = wx.TextCtrl(id=wxID_RABTAHUN, name=u'tahun', parent=self,
              pos=wx.Point(449, 16), size=wx.Size(58, 21), style=0, value=u'0')

        self.bidang = wx.ComboBox(choices=['2.1. Bidang Penyelenggaraan Pemerintahan Desa',
              '2.2. Bidang Pembangunan Desa',
              '2.3. Bidang Pembinaan Kemasyarakatan',
              '2.4. Bidang Pemberdayaan Masyarakat',
              '2.5. Bidang Tidak Terduga'], id=wxID_RABBIDANG, name=u'bidang',
              parent=self, pos=wx.Point(551, 16), size=wx.Size(318, 21),
              style=0, value=u'')
        self.bidang.SetLabel(u'')
        self.bidang.Bind(wx.EVT_COMBOBOX, self.OnBidangCombobox,
              id=wxID_RABBIDANG)

        self.staticText2 = wx.StaticText(id=wxID_RABSTATICTEXT2,
              label=u'Bidang', name='staticText2', parent=self,
              pos=wx.Point(512, 17), size=wx.Size(33, 13), style=0)

        self.staticText3 = wx.StaticText(id=wxID_RABSTATICTEXT3, label=u'Nomor',
              name='staticText3', parent=self, pos=wx.Point(352, 69),
              size=wx.Size(32, 13), style=0)

        self.staticText4 = wx.StaticText(id=wxID_RABSTATICTEXT4,
              label=u'Nomor Rekening', name='staticText4', parent=self,
              pos=wx.Point(527, 67), size=wx.Size(79, 13), style=0)

        self.uraian = wx.StaticText(id=wxID_RABURAIAN, label=u'Kegiatan',
              name=u'uraian', parent=self, pos=wx.Point(352, 96),
              size=wx.Size(43, 13), style=0)

        self.staticText5 = wx.StaticText(id=wxID_RABSTATICTEXT5,
              label=u'Volume', name='staticText5', parent=self,
              pos=wx.Point(352, 165), size=wx.Size(35, 13), style=0)

        self.staticText6 = wx.StaticText(id=wxID_RABSTATICTEXT6,
              label=u'satuan', name='staticText6', parent=self,
              pos=wx.Point(529, 164), size=wx.Size(34, 13), style=0)

        self.staticText7 = wx.StaticText(id=wxID_RABSTATICTEXT7,
              label=u'Harga Satuan', name='staticText7', parent=self,
              pos=wx.Point(353, 187), size=wx.Size(67, 13), style=0)

        self.staticText8 = wx.StaticText(id=wxID_RABSTATICTEXT8,
              label=u'Jumlah', name='staticText8', parent=self,
              pos=wx.Point(527, 187), size=wx.Size(33, 13), style=0)

        self.nomorrek = wx.TextCtrl(id=wxID_RABNOMORREK, name=u'nomorrek',
              parent=self, pos=wx.Point(608, 64), size=wx.Size(70, 21), style=0,
              value=u'')

        self.uraianrab = wx.TextCtrl(id=wxID_RABURAIANRAB, name=u'uraianrab',
              parent=self, pos=wx.Point(448, 124), size=wx.Size(421, 35),
              style=wx.TE_MULTILINE, value=u'')

        self.volume = wx.TextCtrl(id=wxID_RABVOLUME, name=u'volume',
              parent=self, pos=wx.Point(447, 160), size=wx.Size(70, 21),
              style=0, value=u'')

        self.satuan = wx.TextCtrl(id=wxID_RABSATUAN, name=u'satuan',
              parent=self, pos=wx.Point(589, 161), size=wx.Size(70, 21),
              style=0, value=u'')

        self.harga = wx.TextCtrl(id=wxID_RABHARGA, name=u'harga', parent=self,
              pos=wx.Point(447, 182), size=wx.Size(70, 21), style=0, value=u'')

        self.jumlah = wx.TextCtrl(id=wxID_RABJUMLAH, name=u'jumlah',
              parent=self, pos=wx.Point(589, 183), size=wx.Size(70, 21),
              style=0, value=u'')

        self.nomor = wx.TextCtrl(id=wxID_RABNOMOR, name=u'nomor', parent=self,
              pos=wx.Point(448, 66), size=wx.Size(70, 21), style=0, value=u'')

        self.tambah = wx.Button(id=wxID_RABTAMBAH, label=u'Tambah Data',
              name=u'tambah', parent=self, pos=wx.Point(459, 210),
              size=wx.Size(99, 23), style=0)
        self.tambah.Bind(wx.EVT_BUTTON, self.OnTambahButton, id=wxID_RABTAMBAH)

        self.edit = wx.Button(id=wxID_RABEDIT, label=u'Edit Data', name=u'edit',
              parent=self, pos=wx.Point(564, 210), size=wx.Size(99, 23),
              style=0)
        self.edit.Bind(wx.EVT_BUTTON, self.OnEditButton, id=wxID_RABEDIT)

        self.hapus = wx.Button(id=wxID_RABHAPUS, label=u'Hapus Data',
              name=u'hapus', parent=self, pos=wx.Point(670, 210),
              size=wx.Size(99, 23), style=0)
        self.hapus.Bind(wx.EVT_BUTTON, self.OnHapusButton, id=wxID_RABHAPUS)

        self.menu = wx.Button(id=wxID_RABMENU, label=u'Ke Menu', name=u'menu',
              parent=self, pos=wx.Point(772, 210), size=wx.Size(99, 23),
              style=0)
        self.menu.Bind(wx.EVT_BUTTON, self.OnMenuButton, id=wxID_RABMENU)

        self.staticText9 = wx.StaticText(id=wxID_RABSTATICTEXT9,
              label=u'Waktu Pelaksanaan', name='staticText9', parent=self,
              pos=wx.Point(352, 46), size=wx.Size(95, 13), style=0)

        self.staticText10 = wx.StaticText(id=wxID_RABSTATICTEXT10, label=u'Rp',
              name='staticText10', parent=self, pos=wx.Point(429, 186),
              size=wx.Size(14, 13), style=0)

        self.staticText11 = wx.StaticText(id=wxID_RABSTATICTEXT11, label=u'Rp',
              name='staticText11', parent=self, pos=wx.Point(572, 186),
              size=wx.Size(14, 13), style=0)

        self.staticText12 = wx.StaticText(id=wxID_RABSTATICTEXT12,
              label=u'Uraian', name='staticText12', parent=self,
              pos=wx.Point(352, 128), size=wx.Size(32, 13), style=0)

        self.kegiatan = wx.TextCtrl(id=wxID_RABKEGIATAN, name=u'kegiatan',
              parent=self, pos=wx.Point(448, 88), size=wx.Size(420, 35),
              style=wx.TE_MULTILINE, value=u'')

        self.waktu = wx.TextCtrl(id=wxID_RABWAKTU, name=u'waktu', parent=self,
              pos=wx.Point(449, 44), size=wx.Size(100, 21), style=0, value=u'')

        self.reset = wx.Button(id=wxID_RABRESET, label=u'Reset', name=u'reset',
              parent=self, pos=wx.Point(352, 210), size=wx.Size(75, 23),
              style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)
    
    def mulai(self):
        self.waktu.SetValue('')
        self.nomor.SetValue('')
        self.nomorrek.SetValue('')
        self.kegiatan.SetValue('')
        self.uraianrab.SetValue('')
        self.volume.SetValue('')
        self.satuan.SetValue('')
        self.harga.SetValue('')
        self.jumlah.SetValue('')
        
        self.nomor.Disable()
        self.nomorrek.Disable()
        self.kegiatan.Disable()
        
        self.tambah.Disable()
        self.edit.Disable()
        self.hapus.Disable()

    def OnBidangCombobox(self, event):
        rtahun=str(self.tahun.GetValue())
        rbidang=str(self.bidang.GetValue())
        
        if rbidang == '2.1. Bidang Penyelenggaraan Pemerintahan Desa':
            self.apbdes.DeleteAllItems()
            sql = "SELECT * FROM apbdes WHERE tahun='"+rtahun+"' AND norek LIKE '2.1%'"
            cur.execute(sql)
            db.commit()
            hasil = cur.fetchall() 
            no_rek = self.apbdes.GetItemCount() 
            for i in hasil : 
                self.apbdes.InsertStringItem(no_rek, "%s"%i[0]) 
                self.apbdes.SetStringItem(no_rek,1,"%s"%i[1])
                self.apbdes.SetStringItem(no_rek,2,"%s"%i[2]) 
                no_rek = no_rek + 1
        
        if rbidang == '2.2. Bidang Pembangunan Desa':
            self.apbdes.DeleteAllItems()
            sql = "SELECT * FROM apbdes WHERE tahun='"+rtahun+"' AND norek LIKE '2.2%'"
            cur.execute(sql)
            db.commit()
            hasil = cur.fetchall() 
            no_rek = self.apbdes.GetItemCount() 
            for i in hasil : 
                self.apbdes.InsertStringItem(no_rek, "%s"%i[0]) 
                self.apbdes.SetStringItem(no_rek,1,"%s"%i[1])
                self.apbdes.SetStringItem(no_rek,2,"%s"%i[2]) 
                no_rek = no_rek + 1
                
        if rbidang == '2.3. Bidang Pembinaan Kemasyarakatan':
            self.apbdes.DeleteAllItems()
            sql = "SELECT * FROM apbdes WHERE tahun='"+rtahun+"' AND norek LIKE '2.3%'"
            cur.execute(sql)
            db.commit()
            hasil = cur.fetchall() 
            no_rek = self.apbdes.GetItemCount() 
            for i in hasil : 
                self.apbdes.InsertStringItem(no_rek, "%s"%i[0]) 
                self.apbdes.SetStringItem(no_rek,1,"%s"%i[1])
                self.apbdes.SetStringItem(no_rek,2,"%s"%i[2]) 
                no_rek = no_rek + 1
        
        if rbidang == '2.4. Bidang Pemberdayaan Masyarakat':
            self.apbdes.DeleteAllItems()
            sql = "SELECT * FROM apbdes WHERE tahun='"+rtahun+"' AND norek LIKE '2.4%'"
            cur.execute(sql)
            db.commit()
            hasil = cur.fetchall() 
            no_rek = self.apbdes.GetItemCount() 
            for i in hasil : 
                self.apbdes.InsertStringItem(no_rek, "%s"%i[0]) 
                self.apbdes.SetStringItem(no_rek,1,"%s"%i[1])
                self.apbdes.SetStringItem(no_rek,2,"%s"%i[2]) 
                no_rek = no_rek + 1
        
        if rbidang == '2.5. Bidang Tidak Terduga':
            self.apbdes.DeleteAllItems()
            sql = "SELECT * FROM apbdes WHERE tahun='"+rtahun+"' AND norek LIKE '2.5%'"
            cur.execute(sql)
            db.commit()
            hasil = cur.fetchall() 
            no_rek = self.apbdes.GetItemCount() 
            for i in hasil : 
                self.apbdes.InsertStringItem(no_rek, "%s"%i[0]) 
                self.apbdes.SetStringItem(no_rek,1,"%s"%i[1])
                self.apbdes.SetStringItem(no_rek,2,"%s"%i[2]) 
                no_rek = no_rek + 1
            
            
    def OnTambahButton(self, event):
        event.Skip()

    def OnEditButton(self, event):
        event.Skip()

    def OnHapusButton(self, event):
        event.Skip()

    def OnMenuButton(self, event):
        event.Skip()

    def OnApbdesListItemSelected(self, event):
        self.currentItem = event.m_itemIndex 
        b=self.apbdes.GetItem(self.currentItem).GetText() 
        self.nomor.SetValue(b)
        self.kiri()
        self.hapus.Disable()
        self.edit.Disable()
        self.tambah.Enable()
    def OnRabListItemActivated(self, event):
        event.Skip()
        
    def kiri(self):
        rperiode=str(self.periode.GetValue())
        rrkp=str(self.rkp.GetValue())
        carinomor=str(self.nomor.GetValue())
        sql="SELECT * FROM rkpsid WHERE no='%s'"%(carinomor)
        cur.execute(sql)
        hasil = cur.fetchone()  
        if hasil :
            self.nomor.SetValue(str(hasil[0]))
            self.norek.SetValue(str(hasil[1]))
            self.uraian.SetValue(str(hasil[2]))
            self.anggaran.SetValue(str(hasil[38]))
            self.keterangan.SetFocus()
            
        else : 
            self.pesan = wx.MessageDialog(self,"Data Tidak Ada","Konfirmasi",wx.OK) 
            self.pesan.ShowModal() 
            self.keterangan.Clear()
            self.keterangan.SetFocus()
