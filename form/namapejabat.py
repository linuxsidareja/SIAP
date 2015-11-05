#Boa:Dialog:pejabatdesa

import wx
import sqlite3

db = sqlite3.connect('siap.db')
cur = db.cursor()

sql = "SELECT * FROM jabatan"
cur.execute(sql) 
pilihan = [item[1] for item in cur.fetchall()] 

def create(parent):
    return pejabatdesa(parent)

[wxID_PEJABATDESA, wxID_PEJABATDESAALAMAT, wxID_PEJABATDESAEDIT, 
 wxID_PEJABATDESAHAPUS, wxID_PEJABATDESAJABATAN, wxID_PEJABATDESAMENU, 
 wxID_PEJABATDESANAMA, wxID_PEJABATDESANOMOR, wxID_PEJABATDESAPEJABAT, 
 wxID_PEJABATDESARESET, wxID_PEJABATDESASTATICTEXT1, 
 wxID_PEJABATDESASTATICTEXT2, wxID_PEJABATDESASTATICTEXT3, 
 wxID_PEJABATDESASTATICTEXT4, wxID_PEJABATDESATAMBAH, 
] = [wx.NewId() for _init_ctrls in range(15)]

class pejabatdesa(wx.Dialog):
    def _init_coll_pejabat_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT, heading=u'No',
              width=30)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT,
              heading=u'Nama Pejabat', width=200)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT,
              heading=u'Jabatan', width=300)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_LEFT,
              heading=u'Alamat', width=400)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_PEJABATDESA, name=u'pejabatdesa',
              parent=prnt, pos=wx.Point(644, 254), size=wx.Size(448, 356),
              style=wx.DEFAULT_DIALOG_STYLE,
              title=u'Input Pejabat Desa dan Pemda')
        self.SetClientSize(wx.Size(440, 326))
        self.Center(wx.BOTH)

        self.staticText1 = wx.StaticText(id=wxID_PEJABATDESASTATICTEXT1,
              label=u'Nomor', name='staticText1', parent=self, pos=wx.Point(16,
              16), size=wx.Size(32, 13), style=0)

        self.nomor = wx.TextCtrl(id=wxID_PEJABATDESANOMOR, name=u'nomor',
              parent=self, pos=wx.Point(72, 8), size=wx.Size(100, 21), style=0,
              value=u'')

        self.nama = wx.TextCtrl(id=wxID_PEJABATDESANAMA, name=u'nama',
              parent=self, pos=wx.Point(72, 32), size=wx.Size(360, 21), style=0,
              value=u'')

        self.alamat = wx.TextCtrl(id=wxID_PEJABATDESAALAMAT, name=u'alamat',
              parent=self, pos=wx.Point(72, 80), size=wx.Size(360, 48),
              style=wx.TE_MULTILINE, value=u'')

        self.jabatan = wx.ComboBox(choices=pilihan, id=wxID_PEJABATDESAJABATAN,
              name=u'jabatan', parent=self, pos=wx.Point(72, 56),
              size=wx.Size(360, 21), style=0, value=u'')
        self.jabatan.SetLabel(u'')

        self.staticText2 = wx.StaticText(id=wxID_PEJABATDESASTATICTEXT2,
              label=u'Nama', name='staticText2', parent=self, pos=wx.Point(16,
              40), size=wx.Size(28, 13), style=0)

        self.staticText3 = wx.StaticText(id=wxID_PEJABATDESASTATICTEXT3,
              label=u'Jabatan', name='staticText3', parent=self,
              pos=wx.Point(16, 64), size=wx.Size(39, 13), style=0)

        self.staticText4 = wx.StaticText(id=wxID_PEJABATDESASTATICTEXT4,
              label=u'Alamat', name='staticText4', parent=self, pos=wx.Point(16,
              88), size=wx.Size(34, 13), style=0)

        self.pejabat = wx.ListCtrl(id=wxID_PEJABATDESAPEJABAT, name=u'pejabat',
              parent=self, pos=wx.Point(8, 136), size=wx.Size(424, 160),
              style=wx.LC_REPORT)
        self._init_coll_pejabat_Columns(self.pejabat)
        self.pejabat.Bind(wx.EVT_LIST_ITEM_ACTIVATED,
              self.OnPejabatListItemActivated, id=wxID_PEJABATDESAPEJABAT)

        self.tambah = wx.Button(id=wxID_PEJABATDESATAMBAH, label=u'Tambah',
              name=u'tambah', parent=self, pos=wx.Point(113, 299),
              size=wx.Size(75, 23), style=0)
        self.tambah.Bind(wx.EVT_BUTTON, self.OnTambahButton,
              id=wxID_PEJABATDESATAMBAH)

        self.edit = wx.Button(id=wxID_PEJABATDESAEDIT, label=u'Edit',
              name=u'edit', parent=self, pos=wx.Point(194, 299),
              size=wx.Size(75, 23), style=0)
        self.edit.Bind(wx.EVT_BUTTON, self.OnEditButton,
              id=wxID_PEJABATDESAEDIT)

        self.hapus = wx.Button(id=wxID_PEJABATDESAHAPUS, label=u'Hapus',
              name=u'hapus', parent=self, pos=wx.Point(276, 299),
              size=wx.Size(75, 23), style=0)
        self.hapus.Bind(wx.EVT_BUTTON, self.OnHapusButton,
              id=wxID_PEJABATDESAHAPUS)

        self.menu = wx.Button(id=wxID_PEJABATDESAMENU, label=u'Ke Menu',
              name=u'menu', parent=self, pos=wx.Point(356, 299),
              size=wx.Size(75, 23), style=0)
        self.menu.Bind(wx.EVT_BUTTON, self.OnMenuButton,
              id=wxID_PEJABATDESAMENU)

        self.reset = wx.Button(id=wxID_PEJABATDESARESET, label=u'Reset',
              name=u'reset', parent=self, pos=wx.Point(8, 299), size=wx.Size(75,
              23), style=0)
        self.reset.Bind(wx.EVT_BUTTON, self.OnResetButton,
              id=wxID_PEJABATDESARESET)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.mulai()
        self.isipejabat()
        
    def mulai(self):
        self.nomor.SetValue('')
        self.nama.SetValue('')
        self.jabatan.SetValue('')
        self.alamat.SetValue('')
        self.nomor.Disable()
        self.tambah.Enable()
        self.edit.Disable()
        self.hapus.Disable()
    
    def isipejabat(self):
        self.pejabat.DeleteAllItems()      
        sql = "SELECT * FROM pejabat"
        cur.execute(sql) 
        hasil = cur.fetchall() 
        nokk = self.pejabat.GetItemCount() 
        for i in hasil : 
            self.pejabat.InsertStringItem(nokk, "%s"%i[0]) 
            self.pejabat.SetStringItem(nokk,1,"%s"%i[1])
            self.pejabat.SetStringItem(nokk,2,"%s"%i[2])
            self.pejabat.SetStringItem(nokk,3,"%s"%i[3]) 
            nokk = nokk + 1         

    def OnTambahButton(self, event):
        rnama=str(self.nama.GetValue())
        rjabatan=str(self.jabatan.GetValue())
        ralamat=str(self.alamat.GetValue())
       
        add_identitas="INSERT INTO pejabat (nama,jabatan,alamat) VALUES('"+(rnama)+"','"+(rjabatan)+"','"+(ralamat)+"')"
        cur.execute(add_identitas)
        db.commit()
        self.pesan = wx.MessageDialog(self,"Data Sudah Dimasukkan","Peringatan",wx.OK) 
        self.pesan.ShowModal()
        self.nomor.Clear()
        self.nama.Clear()
        self.jabatan.SetValue('')
        self.alamat.Clear()
        self.isipejabat()

    def OnEditButton(self, event):
        rnomor=str(self.nomor.GetValue())
        rnama=str(self.nama.GetValue())
        rjabatan=str(self.jabatan.GetValue())
        ralamat=str(self.alamat.GetValue())
       
        add_identitas="UPDATE pejabat SET nama='"+rnama+"',jabatan='"+rjabatan+"',alamat='"+ralamat+"' WHERE no='"+rnomor+"'"
        cur.execute(add_identitas)
        db.commit()
        self.pesan = wx.MessageDialog(self,"Data Sudah Di Update","Peringatan",wx.OK) 
        self.pesan.ShowModal()
        self.nomor.Clear()
        self.nama.Clear()
        self.jabatan.SetValue('')
        self.alamat.Clear()
        self.isipejabat()

    def OnHapusButton(self, event):
        rnomor=str(self.nomor.GetValue())
        add_identitas="DELETE FROM pejabat WHERE no='"+rnomor+"'"
        cur.execute(add_identitas)
        db.commit()
        self.pesan = wx.MessageDialog(self,"Data Sudah DI Hapus","Peringatan",wx.OK) 
        self.pesan.ShowModal()
        self.nomor.Clear()
        self.nama.Clear()
        self.jabatan.SetValue('')
        self.alamat.Clear()
        self.isipejabat()

    def OnMenuButton(self, event):
        self.Close()
        self.Destroy()

    def OnResetButton(self, event):
        self.mulai()
        self.isipejabat()

    def OnPejabatListItemActivated(self, event):
        self.currentItem = event.m_itemIndex 
        b=self.pejabat.GetItem(self.currentItem).GetText() 
        self.nomor.SetValue(b)
        self.isilist()
    
    def isilist(self):
        carinomor=str(self.nomor.GetValue())
        sql="SELECT * FROM pejabat WHERE no='%s'"%(carinomor)
        cur.execute(sql)
        hasil = cur.fetchone()  
        if hasil :
            self.nomor.SetValue(str(hasil[0]))
            self.nama.SetValue(str(hasil[1]))
            self.jabatan.SetValue(str(hasil[2]))
            self.alamat.SetValue(str(hasil[3]))
            self.nomor.Disable()
            self.tambah.Disable()
            self.edit.Enable()
            self.hapus.Enable()
            
        else : 
            self.pesan = wx.MessageDialog(self,"Data Tidak Ada","Konfirmasi",wx.OK) 
            self.pesan.ShowModal() 
            self.nomor.Clear()
            self.jabatan.Clear()
            self.jabatan.SetFocus()
