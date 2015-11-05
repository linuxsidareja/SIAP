#Boa:Dialog:jabatan

import wx
import sqlite3

db = sqlite3.connect('siap.db')
cur = db.cursor()

def create(parent):
    return jabatan(parent)

[wxID_JABATAN, wxID_JABATANEDIT, wxID_JABATANHAPUS, wxID_JABATANJABATAN, 
 wxID_JABATANLJABATAN, wxID_JABATANMENU, wxID_JABATANNOMOR, wxID_JABATANRESET, 
 wxID_JABATANSTATICTEXT1, wxID_JABATANSTATICTEXT2, wxID_JABATANTAMBAH, 
] = [wx.NewId() for _init_ctrls in range(11)]

class jabatan(wx.Dialog):
    def _init_coll_ljabatan_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT,
              heading=u'Record', width=-1)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT,
              heading=u'Nama Jabatan', width=200)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_JABATAN, name=u'jabatan', parent=prnt,
              pos=wx.Point(660, 289), size=wx.Size(417, 286),
              style=wx.DEFAULT_DIALOG_STYLE,
              title=u'Input Jabatan Dan Pangkat')
        self.SetClientSize(wx.Size(409, 256))
        self.Center(wx.BOTH)

        self.staticText1 = wx.StaticText(id=wxID_JABATANSTATICTEXT1,
              label=u'Jabatan', name='staticText1', parent=self, pos=wx.Point(9,
              35), size=wx.Size(39, 13), style=0)

        self.jabatan = wx.TextCtrl(id=wxID_JABATANJABATAN, name=u'jabatan',
              parent=self, pos=wx.Point(63, 33), size=wx.Size(336, 21), style=0,
              value=u'')

        self.ljabatan = wx.ListCtrl(id=wxID_JABATANLJABATAN, name=u'ljabatan',
              parent=self, pos=wx.Point(8, 60), size=wx.Size(392, 166),
              style=wx.LC_REPORT)
        self._init_coll_ljabatan_Columns(self.ljabatan)
        self.ljabatan.Bind(wx.EVT_LIST_ITEM_ACTIVATED,
              self.OnLjabatanListItemActivated, id=wxID_JABATANLJABATAN)

        self.tambah = wx.Button(id=wxID_JABATANTAMBAH, label=u'Tambah',
              name=u'tambah', parent=self, pos=wx.Point(83, 229),
              size=wx.Size(75, 23), style=0)
        self.tambah.Bind(wx.EVT_BUTTON, self.OnTambahButton,
              id=wxID_JABATANTAMBAH)

        self.edit = wx.Button(id=wxID_JABATANEDIT, label=u'Edit', name=u'edit',
              parent=self, pos=wx.Point(163, 228), size=wx.Size(75, 23),
              style=0)
        self.edit.Bind(wx.EVT_BUTTON, self.OnEditButton, id=wxID_JABATANEDIT)

        self.hapus = wx.Button(id=wxID_JABATANHAPUS, label=u'Hapus',
              name=u'hapus', parent=self, pos=wx.Point(243, 228),
              size=wx.Size(75, 24), style=0)
        self.hapus.Bind(wx.EVT_BUTTON, self.OnHapusButton, id=wxID_JABATANHAPUS)

        self.Menu = wx.Button(id=wxID_JABATANMENU, label=u'Ke Menu',
              name=u'Menu', parent=self, pos=wx.Point(324, 228),
              size=wx.Size(75, 23), style=0)
        self.Menu.Bind(wx.EVT_BUTTON, self.OnMenuButton, id=wxID_JABATANMENU)

        self.staticText2 = wx.StaticText(id=wxID_JABATANSTATICTEXT2,
              label=u'Nomor', name='staticText2', parent=self, pos=wx.Point(8,
              8), size=wx.Size(32, 13), style=0)

        self.nomor = wx.TextCtrl(id=wxID_JABATANNOMOR, name=u'nomor',
              parent=self, pos=wx.Point(64, 8), size=wx.Size(56, 21), style=0,
              value=u'')

        self.reset = wx.Button(id=wxID_JABATANRESET, label=u'Reset',
              name=u'reset', parent=self, pos=wx.Point(5, 229), size=wx.Size(75,
              23), style=0)
        self.reset.Bind(wx.EVT_BUTTON, self.OnResetButton, id=wxID_JABATANRESET)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.mulai()
    
    def mulai(self):
        
        self.jabatan.SetValue('')
        
        self.nomor.Disable()
        self.tambah.Enable()
        self.edit.Disable()
        self.hapus.Disable()
        
        self.isijabatan()
    
    def isijabatan(self):
        self.ljabatan.DeleteAllItems()      
        sql = "SELECT * FROM jabatan"
        cur.execute(sql) 
        hasil = cur.fetchall() 
        nokk = self.ljabatan.GetItemCount() 
        for i in hasil : 
            self.ljabatan.InsertStringItem(nokk, "%s"%i[0]) 
            self.ljabatan.SetStringItem(nokk,1,"%s"%i[1]) 
            nokk = nokk + 1     
        

    def OnTambahButton(self, event):
        rjabatan=str(self.jabatan.GetValue())
        add_identitas="INSERT INTO jabatan (jabatan) VALUES('"+(rjabatan)+"')"
        cur.execute(add_identitas)
        db.commit()
        self.pesan = wx.MessageDialog(self,"Jabatan Sudah Dimasukkan","Peringatan",wx.OK) 
        self.pesan.ShowModal()
        self.nomor.Clear()
        self.jabatan.Clear()
        self.jabatan.SetFocus()
        self.mulai()  

    def OnEditButton(self, event):
        rnomor=str(self.nomor.GetValue())
        rjabatan=str(self.jabatan.GetValue())
        add_identitas="UPDATE jabatan SET jabatan='"+rjabatan+"' WHERE no='"+rnomor+"'"
        cur.execute(add_identitas)
        db.commit()
        self.pesan = wx.MessageDialog(self,"Jabatan Sudah DiUpdate","Peringatan",wx.OK) 
        self.pesan.ShowModal()
        self.nomor.Clear()
        self.jabatan.Clear()
        self.jabatan.SetFocus()
        self.mulai()  

    def OnHapusButton(self, event):
        rnomor=str(self.nomor.GetValue())
        add_identitas="DELETE FROM jabatan WHERE no='"+rnomor+"'"
        cur.execute(add_identitas)
        db.commit()
        self.pesan = wx.MessageDialog(self,"Jabatan Sudah DI Hapus","Peringatan",wx.OK) 
        self.pesan.ShowModal()
        self.nomor.Clear()
        self.jabatan.Clear()
        self.jabatan.SetFocus()
        self.mulai()  

    def OnMenuButton(self, event):
        event.Skip()

    def OnLjabatanListItemActivated(self, event):
        self.currentItem = event.m_itemIndex 
        b=self.ljabatan.GetItem(self.currentItem).GetText() 
        self.nomor.SetValue(b)
        self.isilist()
    
    def isilist(self):
        carinomor=str(self.nomor.GetValue())
        sql="SELECT * FROM jabatan WHERE no='%s'"%(carinomor)
        cur.execute(sql)
        hasil = cur.fetchone()  
        if hasil :
            self.nomor.SetValue(str(hasil[0]))
            self.jabatan.SetValue(str(hasil[1]))
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

    def OnResetButton(self, event):
        self.nomor.Clear()
        self.mulai()
