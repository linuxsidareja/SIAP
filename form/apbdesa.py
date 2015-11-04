#Boa:Dialog:apbdesa
#-------------------------------------------------------------------------------
#Sistem Informasi dan Administrasi Perdesaan
#pengembang johandri@ictwatch.id
#-------------------------------------------------------------------------------

import wx
import sqlite3

db = sqlite3.connect('siap.db')
cur = db.cursor()


def create(parent):
    return apbdesa(parent)

[wxID_APBDESA, wxID_APBDESAANGGARAN, wxID_APBDESABUTTON1, wxID_APBDESAEDIT, 
 wxID_APBDESAHAPUS, wxID_APBDESAKETERANGAN, wxID_APBDESALISTAPBDES, 
 wxID_APBDESALISTRKP, wxID_APBDESAMENU, wxID_APBDESANOMOR, 
 wxID_APBDESANOMORRKP, wxID_APBDESANOREK, wxID_APBDESAPERIODE, 
 wxID_APBDESARESET, wxID_APBDESARKP, wxID_APBDESASTATICTEXT1, 
 wxID_APBDESASTATICTEXT10, wxID_APBDESASTATICTEXT11, wxID_APBDESASTATICTEXT12, 
 wxID_APBDESASTATICTEXT2, wxID_APBDESASTATICTEXT3, wxID_APBDESASTATICTEXT4, 
 wxID_APBDESASTATICTEXT5, wxID_APBDESASTATICTEXT6, wxID_APBDESASTATICTEXT7, 
 wxID_APBDESASTATICTEXT8, wxID_APBDESASTATICTEXT9, wxID_APBDESATAHUN, 
 wxID_APBDESATAMBAH, wxID_APBDESATOTALANGGARAN, wxID_APBDESAURAIAN, 
] = [wx.NewId() for _init_ctrls in range(31)]

class apbdesa(wx.Dialog):
    def _init_coll_listapbdes_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT,
              heading=u'Record', width=60)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT, heading=u'Norek',
              width=60)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT,
              heading=u'Uraian', width=400)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_LEFT,
              heading=u'Anggaran (Rp)', width=100)
        parent.InsertColumn(col=4, format=wx.LIST_FORMAT_LEFT,
              heading=u'Keterangan', width=150)

    def _init_coll_listrkp_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT,
              heading=u'Record', width=60)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT, heading=u'Norek',
              width=50)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT,
              heading=u'Uraian', width=400)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_APBDESA, name=u'apbdesa', parent=prnt,
              pos=wx.Point(485, 172), size=wx.Size(767, 520),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Penyusunan APB Desa')
        self.SetClientSize(wx.Size(759, 490))
        self.Center(wx.BOTH)
        self.SetBackgroundColour(wx.Colour(192, 192, 192))
        self.SetHelpText(u'')

        self.listrkp = wx.ListCtrl(id=wxID_APBDESALISTRKP, name=u'listrkp',
              parent=self, pos=wx.Point(5, 23), size=wx.Size(287, 228),
              style=wx.LC_REPORT)
        self._init_coll_listrkp_Columns(self.listrkp)
        self.listrkp.Bind(wx.EVT_LIST_ITEM_SELECTED,
              self.OnListrkpListItemSelected, id=wxID_APBDESALISTRKP)

        self.listapbdes = wx.ListCtrl(id=wxID_APBDESALISTAPBDES,
              name=u'listapbdes', parent=self, pos=wx.Point(4, 257),
              size=wx.Size(748, 227), style=wx.LC_REPORT)
        self._init_coll_listapbdes_Columns(self.listapbdes)
        self.listapbdes.Bind(wx.EVT_LIST_ITEM_SELECTED,
              self.OnListapbdesListItemSelected, id=wxID_APBDESALISTAPBDES)

        self.staticText1 = wx.StaticText(id=wxID_APBDESASTATICTEXT1,
              label=u'APB Desa Tahun :', name='staticText1', parent=self,
              pos=wx.Point(304, 37), size=wx.Size(87, 13), style=0)

        self.tahun = wx.TextCtrl(id=wxID_APBDESATAHUN, name=u'tahun',
              parent=self, pos=wx.Point(395, 35), size=wx.Size(60, 21), style=0,
              value=u'')

        self.button1 = wx.Button(id=wxID_APBDESABUTTON1, label=u'Buat APBDesa',
              name='button1', parent=self, pos=wx.Point(652, 4),
              size=wx.Size(99, 23), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_APBDESABUTTON1)

        self.nomor = wx.TextCtrl(id=wxID_APBDESANOMOR, name=u'nomor',
              parent=self, pos=wx.Point(395, 58), size=wx.Size(60, 21), style=0,
              value=u'')

        self.staticText2 = wx.StaticText(id=wxID_APBDESASTATICTEXT2,
              label=u'Nomor Record', name='staticText2', parent=self,
              pos=wx.Point(304, 61), size=wx.Size(69, 13), style=0)

        self.staticText3 = wx.StaticText(id=wxID_APBDESASTATICTEXT3,
              label=u'Nomor Rekening', name='staticText3', parent=self,
              pos=wx.Point(304, 83), size=wx.Size(79, 13), style=0)

        self.staticText4 = wx.StaticText(id=wxID_APBDESASTATICTEXT4,
              label=u'Uraian', name='staticText4', parent=self,
              pos=wx.Point(304, 105), size=wx.Size(32, 13), style=0)

        self.staticText5 = wx.StaticText(id=wxID_APBDESASTATICTEXT5,
              label=u'Anggaran', name='staticText5', parent=self,
              pos=wx.Point(304, 156), size=wx.Size(48, 13), style=0)

        self.staticText6 = wx.StaticText(id=wxID_APBDESASTATICTEXT6,
              label=u'Keterangan', name='staticText6', parent=self,
              pos=wx.Point(304, 182), size=wx.Size(57, 13), style=0)

        self.norek = wx.TextCtrl(id=wxID_APBDESANOREK, name=u'norek',
              parent=self, pos=wx.Point(395, 81), size=wx.Size(60, 21), style=0,
              value=u'')

        self.keterangan = wx.TextCtrl(id=wxID_APBDESAKETERANGAN,
              name=u'keterangan', parent=self, pos=wx.Point(396, 177),
              size=wx.Size(356, 21), style=0, value=u'')

        self.tambah = wx.Button(id=wxID_APBDESATAMBAH, label=u'Tambah Data',
              name=u'tambah', parent=self, pos=wx.Point(386, 230),
              size=wx.Size(88, 23), style=0)
        self.tambah.Bind(wx.EVT_BUTTON, self.OnTambahButton,
              id=wxID_APBDESATAMBAH)

        self.edit = wx.Button(id=wxID_APBDESAEDIT, label=u'Edit Data',
              name=u'edit', parent=self, pos=wx.Point(480, 230),
              size=wx.Size(90, 23), style=0)
        self.edit.Bind(wx.EVT_BUTTON, self.OnEditButton, id=wxID_APBDESAEDIT)

        self.hapus = wx.Button(id=wxID_APBDESAHAPUS, label=u'Hapus Data',
              name=u'hapus', parent=self, pos=wx.Point(575, 230),
              size=wx.Size(98, 23), style=0)
        self.hapus.Bind(wx.EVT_BUTTON, self.OnHapusButton, id=wxID_APBDESAHAPUS)

        self.menu = wx.Button(id=wxID_APBDESAMENU, label=u'Ke Menu',
              name=u'menu', parent=self, pos=wx.Point(677, 230),
              size=wx.Size(75, 23), style=0)
        self.menu.Bind(wx.EVT_BUTTON, self.OnMenuButton, id=wxID_APBDESAMENU)

        self.totalanggaran = wx.TextCtrl(id=wxID_APBDESATOTALANGGARAN,
              name=u'totalanggaran', parent=self, pos=wx.Point(563, 200),
              size=wx.Size(189, 21), style=0, value=u'')

        self.staticText7 = wx.StaticText(id=wxID_APBDESASTATICTEXT7,
              label=u'Total Anggaran', name='staticText7', parent=self,
              pos=wx.Point(465, 204), size=wx.Size(75, 13), style=0)

        self.periode = wx.TextCtrl(id=wxID_APBDESAPERIODE, name=u'periode',
              parent=self, pos=wx.Point(481, 4), size=wx.Size(72, 21), style=0,
              value=u'')

        self.rkp = wx.ComboBox(choices=['1', '2', '3', '4', '5', '6'],
              id=wxID_APBDESARKP, name=u'rkp', parent=self, pos=wx.Point(605,
              4), size=wx.Size(43, 21), style=0, value=u'')
        self.rkp.SetLabel(u'')
        self.rkp.Bind(wx.EVT_COMBOBOX, self.OnRkpCombobox, id=wxID_APBDESARKP)

        self.staticText8 = wx.StaticText(id=wxID_APBDESASTATICTEXT8,
              label=u'Dari RKP', name='staticText8', parent=self,
              pos=wx.Point(561, 8), size=wx.Size(42, 13), style=0)

        self.staticText9 = wx.StaticText(id=wxID_APBDESASTATICTEXT9,
              label=u'Periode Anggaran', name='staticText9', parent=self,
              pos=wx.Point(388, 7), size=wx.Size(89, 16), style=0)

        self.staticText10 = wx.StaticText(id=wxID_APBDESASTATICTEXT10,
              label=u'Daftar RKP Bidang Belanja', name='staticText10',
              parent=self, pos=wx.Point(8, 6), size=wx.Size(147, 13), style=0)
        self.staticText10.SetForegroundColour(wx.Colour(0, 0, 0))
        self.staticText10.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Tahoma'))

        self.anggaran = wx.TextCtrl(id=wxID_APBDESAANGGARAN, name=u'anggaran',
              parent=self, pos=wx.Point(416, 154), size=wx.Size(100, 21),
              style=0, value=u'')

        self.staticText11 = wx.StaticText(id=wxID_APBDESASTATICTEXT11,
              label=u'Rp', name='staticText11', parent=self, pos=wx.Point(400,
              155), size=wx.Size(14, 13), style=0)

        self.staticText12 = wx.StaticText(id=wxID_APBDESASTATICTEXT12,
              label=u'Rp', name='staticText12', parent=self, pos=wx.Point(544,
              204), size=wx.Size(14, 13), style=0)

        self.uraian = wx.TextCtrl(id=wxID_APBDESAURAIAN, name=u'uraian',
              parent=self, pos=wx.Point(395, 104), size=wx.Size(357, 48),
              style=wx.TE_MULTILINE, value=u'')

        self.nomorrkp = wx.TextCtrl(id=wxID_APBDESANOMORRKP, name=u'nomorrkp',
              parent=self, pos=wx.Point(-464, -56), size=wx.Size(100, 21),
              style=0, value=u'')

        self.reset = wx.Button(id=wxID_APBDESARESET, label=u'Reset',
              name=u'reset', parent=self, pos=wx.Point(296, 230),
              size=wx.Size(75, 23), style=0)
        self.reset.Bind(wx.EVT_BUTTON, self.OnResetButton, id=wxID_APBDESARESET)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.pertama()
        rrkp=str(self.rkp.GetValue())
        perio=str(self.periode.GetValue())
        sql1="SELECT sum(anggaran) FROM apbdes WHERE norek LIKE '2.%' AND id_rkp='"+rrkp+"' AND periode='"+perio+"'"
        cur.execute(sql1)
        hasil1=cur.fetchone()
        self.totalanggaran.SetValue(str(hasil1[0]))
        self.totalanggaran.Disable()
    
    def pertama(self):
        
        self.periode.SetValue('0')
        self.rkp.SetValue('')
        self.tahun.SetValue('')
        self.nomor.SetValue('')
        self.norek.SetValue('')
        self.uraian.SetValue('')
        self.anggaran.SetValue('0')
        self.keterangan.SetValue('')
        self.totalanggaran.SetValue('0')
        
        self.tahun.Disable()
        self.nomor.Disable()
        self.norek.Disable()
        self.uraian.Disable()
        self.anggaran.Disable()
        self.totalanggaran.Disable()
        
        
    
    def kedua(self):
        self.pertama()
        self.isirkp()
        self.isiapbdes()
        
    def isirkp(self): 
        rperiode=str(self.periode.GetValue())
        rrkp=str(self.rkp.GetValue())
        self.listrkp.DeleteAllItems()    
        sql = "SELECT * FROM rkpsid WHERE norek LIKE '2.%' AND periode='"+rperiode+"' AND id_rkp='"+rrkp+"' AND cekapbdes='0'"
        cur.execute(sql)
        db.commit()
        hasil = cur.fetchall() 
        no_rek = self.listrkp.GetItemCount() 
        for i in hasil : 
            self.listrkp.InsertStringItem(no_rek, "%s"%i[0]) 
            self.listrkp.SetStringItem(no_rek,1,"%s"%i[1])
            self.listrkp.SetStringItem(no_rek,2,"%s"%i[2]) 
            no_rek = no_rek + 1
            
            
    def isiapbdes(self):
        rperiode=str(self.periode.GetValue())
        rrkp=str(self.rkp.GetValue())
        self.listapbdes.DeleteAllItems()    
        sql2 = "SELECT * FROM apbdes WHERE norek LIKE '2.%' AND periode='"+rperiode+"' AND id_rkp='"+rrkp+"'"
        cur.execute(sql2) 
        hasil = cur.fetchall() 
        no_rek = self.listapbdes.GetItemCount() 
        for i in hasil : 
            self.listapbdes.InsertStringItem(no_rek, "%s"%i[0]) 
            self.listapbdes.SetStringItem(no_rek,1,"%s"%i[1])
            self.listapbdes.SetStringItem(no_rek,2,"%s"%i[2])
            self.listapbdes.SetStringItem(no_rek,3,"%s"%i[3])
            self.listapbdes.SetStringItem(no_rek,4,"%s"%i[4]) 
            no_rek = no_rek + 1
        

    def OnEditButton(self, event):
        rnomorrkp = str(self.nomor.GetValue())
        rketerangan = str(self.keterangan.GetValue())
        sql2 = "UPDATE apbdes SET keterangan='"+rketerangan+"' WHERE no='"+rnomorrkp+"'"
        cur.execute(sql2) 
        db.commit()
        self.pesan = wx.MessageDialog(self,"Data Sudah Di Update","Konfirmasi",wx.OK) 
        self.pesan.ShowModal()
        self.nomor.Clear()
        self.norek.Clear()
        self.uraian.Clear()
        self.anggaran.Clear()
        self.keterangan.Clear()
        self.tambah.Disable()
        self.hapus.Disable()
        self.edit.Disable()
        self.isirkp()
        self.isiapbdes()

    def OnTambahButton(self, event):
        rperiode=str(self.periode.GetValue())
        rrkp=str(self.rkp.GetValue())
        rtahun=str(self.tahun.GetValue())
        rnomor=str(self.nomor.GetValue())
        rnorek=str(self.norek.GetValue())
        ruraian=str(self.uraian.GetValue())
        ranggaran=str(self.anggaran.GetValue())
        rketerangan=str(self.keterangan.GetValue())
        rtotalanggaran=str(self.totalanggaran.GetValue())
        sql1 = "INSERT INTO apbdes (norek,uraian,anggaran,keterangan,id_rkp,rkp,periode,tahun) VALUES ('"+(rnorek)+"','"+(ruraian)+"','"+(ranggaran)+"','"+(rketerangan)+"','"+(rrkp)+"','"+(rnomor)+"','"+(rperiode)+"','"+(rtahun)+"')"
        cur.execute(sql1) 
        sql2 = "UPDATE rkpsid SET cekapbdes='1' WHERE no='"+rnomor+"'"
        cur.execute(sql2)
        db.commit()
        self.pesan = wx.MessageDialog(self,"Data  Sudah Tersimpan","Konfirmasi",wx.OK) 
        self.pesan.ShowModal()
        self.nomor.Clear()
        self.norek.Clear()
        self.uraian.Clear()
        self.anggaran.Clear()
        self.keterangan.Clear()
        self.tambah.Disable()
        self.hapus.Disable()
        self.edit.Disable()
        self.isirkp()
        self.isiapbdes()
        
    def OnHapusButton(self, event):
        rnomorrkp = str(self.nomorrkp.GetValue())
        nomorindex = str(self.nomor.GetValue())
        sql2 = "UPDATE rkpsid SET cekapbdes='0' WHERE no='"+rnomorrkp+"'"
        cur.execute(sql2) 
        hapus="DELETE FROM apbdes WHERE no='"+nomorindex+"'"
        cur.execute(hapus)
        db.commit()
        self.pesan = wx.MessageDialog(self,"Data Sudah Dihapus","Konfirmasi",wx.OK) 
        self.pesan.ShowModal()
        self.nomor.Clear()
        self.norek.Clear()
        self.uraian.Clear()
        self.anggaran.Clear()
        self.keterangan.Clear()
        self.tambah.Disable()
        self.hapus.Disable()
        self.edit.Disable()
        self.isirkp()
        self.isiapbdes()
        

    def OnMenuButton(self, event):
        self.Close()
        self.Destroy()
        db.commit()

    def OnButton1Button(self, event):
        self.tambah.Disable()
        self.hapus.Disable()
        self.edit.Disable()
        self.isirkp()
        self.isiapbdes()
        
    def OnListrkpListItemSelected(self, event):
        self.currentItem = event.m_itemIndex 
        b=self.listrkp.GetItem(self.currentItem).GetText() 
        self.nomor.SetValue(b)
        self.kiri()
        self.hapus.Disable()
        self.edit.Disable()
        self.tambah.Enable()

    def OnListapbdesListItemSelected(self, event):
        self.currentItem = event.m_itemIndex 
        b=self.listapbdes.GetItem(self.currentItem).GetText() 
        self.nomor.SetValue(b)
        self.bawah()
        self.tambah.Disable()
        self.hapus.Enable()
        self.edit.Enable()
    
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

    def OnRkpCombobox(self, event):
        cek=int(self.periode.GetValue())
        cek2=str(self.rkp.GetValue())
        if cek2=='1':
            intcek2=int(cek2)
            cekdulu=cek+0
            self.tahun.SetValue(str(cekdulu))
        if cek2=='2':
            intcek2=int(cek2)
            cekdulu=cek+1
            self.tahun.SetValue(str(cekdulu))
        if cek2=='3':
            intcek2=int(cek2)
            cekdulu=cek+2
            self.tahun.SetValue(str(cekdulu))
        if cek2=='4':
            intcek2=int(cek2)
            cekdulu=cek+3
            self.tahun.SetValue(str(cekdulu))
        if cek2=='5':
            intcek2=int(cek2)
            cekdulu=cek+4
            self.tahun.SetValue(str(cekdulu))
        if cek2=='6':
            intcek2=int(cek2)
            cekdulu=cek+5
            self.tahun.SetValue(str(cekdulu)) 
    
    def bawah(self):
        rperiode=str(self.periode.GetValue())
        rrkp=str(self.rkp.GetValue())
        carinomor=str(self.nomor.GetValue())
        sql="SELECT * FROM apbdes WHERE periode='"+rperiode+"' AND id_rkp='"+rrkp+"'"
        cur.execute(sql)
        hasil = cur.fetchone()
        if hasil :
            self.nomor.SetValue(str(hasil[0]))
            self.norek.SetValue(str(hasil[1]))
            self.uraian.SetValue(str(hasil[2]))
            self.anggaran.SetValue(str(hasil[3]))
            self.keterangan.SetValue(str(hasil[4]))
            self.nomorrkp.SetValue(str(hasil[7]))
            
        else : 
            self.pesan = wx.MessageDialog(self,"Data Tidak Ada","Konfirmasi",wx.OK) 
            self.pesan.ShowModal() 
            self.keterangan.Clear()
            self.keterangan.SetFocus()

    def OnResetButton(self, event):
        self.nomor.SetValue('')
        self.norek.SetValue('')
        self.uraian.SetValue('')
        self.anggaran.SetValue('0')
        self.keterangan.SetValue('')
        self.tambah.Disable()
        self.hapus.Disable()
        self.edit.Disable()
        self.isirkp()
        self.isiapbdes()
