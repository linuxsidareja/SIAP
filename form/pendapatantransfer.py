#Boa:Frame:masterdata
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
    return masterdata(parent)

[wxID_MASTERDATA, wxID_MASTERDATABUTTON1, wxID_MASTERDATACARINOREK, 
 wxID_MASTERDATAEDIT, wxID_MASTERDATAKEGIATAN, wxID_MASTERDATAMENU, 
 wxID_MASTERDATANOINDEX, wxID_MASTERDATANOREK, wxID_MASTERDATAPEMBANGUNANDESA, 
 wxID_MASTERDATAPENDAPATAN, wxID_MASTERDATAPENDAPATANTRANSFER, 
 wxID_MASTERDATAREKENING, wxID_MASTERDATASTATICBOX1, 
 wxID_MASTERDATASTATICTEXT2, wxID_MASTERDATASTATICTEXT3, 
 wxID_MASTERDATATAMBAH, 
] = [wx.NewId() for _init_ctrls in range(16)]

class masterdata(wx.Frame):
    def _init_coll_pembangunandesa_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT,
              heading='Nomor Rekening', width=120)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT, heading='Uraian',
              width=500)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_MASTERDATA, name=u'masterdata',
              parent=prnt, pos=wx.Point(561, 213), size=wx.Size(615, 437),
              style=wx.DEFAULT_FRAME_STYLE,
              title=u'Master Pendapatan Transfer')
        self.SetClientSize(wx.Size(607, 407))
        self.SetAutoLayout(False)
        self.Center(wx.BOTH)
        self.SetBackgroundColour(wx.Colour(192, 192, 192))

        self.pembangunandesa = wx.ListCtrl(id=wxID_MASTERDATAPEMBANGUNANDESA,
              name=u'pembangunandesa', parent=self, pos=wx.Point(8, 40),
              size=wx.Size(592, 280), style=wx.LC_REPORT)
        self._init_coll_pembangunandesa_Columns(self.pembangunandesa)
        self.pembangunandesa.Bind(wx.EVT_LIST_ITEM_SELECTED,
              self.OnPembangunandesaListItemSelected,
              id=wxID_MASTERDATAPEMBANGUNANDESA)

        self.pendapatan = wx.StaticText(id=wxID_MASTERDATAPENDAPATAN,
              label=u'1. PENDAPATAN', name=u'pendapatan', parent=self,
              pos=wx.Point(8, 8), size=wx.Size(86, 13), style=0)
        self.pendapatan.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Tahoma'))

        self.pendapatantransfer = wx.StaticText(id=wxID_MASTERDATAPENDAPATANTRANSFER,
              label=u'1.2. Pendapatan Transfer', name=u'pendapatantransfer',
              parent=self, pos=wx.Point(8, 24), size=wx.Size(142, 13), style=0)
        self.pendapatantransfer.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Tahoma'))

        self.staticText2 = wx.StaticText(id=wxID_MASTERDATASTATICTEXT2,
              label=u'Nomor Rekening', name='staticText2', parent=self,
              pos=wx.Point(8, 328), size=wx.Size(79, 13), style=0)

        self.norek = wx.TextCtrl(id=wxID_MASTERDATANOREK, name=u'norek',
              parent=self, pos=wx.Point(96, 328), size=wx.Size(48, 21), style=0,
              value=u'')

        self.staticText3 = wx.StaticText(id=wxID_MASTERDATASTATICTEXT3,
              label=u'Kegiatan', name='staticText3', parent=self,
              pos=wx.Point(152, 328), size=wx.Size(43, 13), style=0)

        self.kegiatan = wx.TextCtrl(id=wxID_MASTERDATAKEGIATAN,
              name=u'kegiatan', parent=self, pos=wx.Point(208, 328),
              size=wx.Size(392, 21), style=0, value=u'')

        self.tambah = wx.Button(id=wxID_MASTERDATATAMBAH, label=u'Tambah Data',
              name=u'tambah', parent=self, pos=wx.Point(210, 368),
              size=wx.Size(88, 23), style=0)
        self.tambah.Bind(wx.EVT_BUTTON, self.OnTambahButton,
              id=wxID_MASTERDATATAMBAH)

        self.edit = wx.Button(id=wxID_MASTERDATAEDIT, label=u'Edit Data',
              name=u'edit', parent=self, pos=wx.Point(307, 368),
              size=wx.Size(88, 23), style=0)
        self.edit.Bind(wx.EVT_BUTTON, self.OnEditButton, id=wxID_MASTERDATAEDIT)

        self.menu = wx.Button(id=wxID_MASTERDATAMENU, label=u'Kembali Ke Menu',
              name=u'menu', parent=self, pos=wx.Point(488, 368),
              size=wx.Size(112, 23), style=0)
        self.menu.Bind(wx.EVT_BUTTON, self.OnMenuButton, id=wxID_MASTERDATAMENU)

        self.staticBox1 = wx.StaticBox(id=wxID_MASTERDATASTATICBOX1,
              label=u'Cari Norek', name='staticBox1', parent=self,
              pos=wx.Point(8, 352), size=wx.Size(181, 48), style=0)

        self.rekening = wx.Button(id=wxID_MASTERDATAREKENING,
              label=u'Cari Norek', name=u'rekening', parent=self,
              pos=wx.Point(16, 368), size=wx.Size(75, 23), style=0)
        self.rekening.Bind(wx.EVT_BUTTON, self.OnRekeningButton,
              id=wxID_MASTERDATAREKENING)

        self.carinorek = wx.TextCtrl(id=wxID_MASTERDATACARINOREK,
              name=u'carinorek', parent=self, pos=wx.Point(96, 368),
              size=wx.Size(84, 21), style=0, value=u'')

        self.noindex = wx.TextCtrl(id=wxID_MASTERDATANOINDEX, name=u'noindex',
              parent=self, pos=wx.Point(-100, -100), size=wx.Size(100, 21),
              style=0, value=u'')

        self.button1 = wx.Button(id=wxID_MASTERDATABUTTON1, label=u'Hapus Data',
              name='button1', parent=self, pos=wx.Point(403, 368),
              size=wx.Size(75, 23), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_MASTERDATABUTTON1)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.awal()
    
    def awal(self):
        self.IsiList()
        self.carinorek.SetValue('')
        self.norek.SetValue('')
        self.kegiatan.SetValue('')
        self.noindex.SetValue('')
        
    def IsiList(self): 
        self.pembangunandesa.DeleteAllItems()    
        sql = "SELECT * FROM koderek WHERE kode='1.2'"
        cur.execute(sql) 
        hasil = cur.fetchall() 
        no_rek = self.pembangunandesa.GetItemCount() 
        for i in hasil : 
            self.pembangunandesa.InsertStringItem(no_rek, "%s"%i[2]) 
            self.pembangunandesa.SetStringItem(no_rek,1,"%s"%i[3]) 
            no_rek = no_rek + 1
    
    def Isi_Object(self) : 
        carinomor=str(self.carinorek.GetValue())
        sql="SELECT * FROM koderek WHERE norek='%s'"%(carinomor)
        cur.execute(sql)
        hasil = cur.fetchone()  
        if hasil :
            self.noindex.SetValue(str(hasil[0])) 
            self.norek.SetValue(str(hasil[2]))
            self.kegiatan.SetValue(str(hasil[3]))
        else : 
            self.pesan = wx.MessageDialog(self,"Data Tidak Ada","Konfirmasi",wx.OK) 
            self.pesan.ShowModal() 
            self.carinorek.Clear()
            self.carinorek.SetFocus()
            
    def OnPembangunandesaListItemSelected(self, event):
        self.currentItem = event.m_itemIndex 
        b=self.pembangunandesa.GetItem(self.currentItem).GetText() 
        self.carinorek.SetValue(b)
        self.Isi_Object()
        

    def OnTambahButton(self, event):
        nomorrekening = str(self.norek.GetValue())
        namakegiatan = str(self.kegiatan.GetValue())
        
        if nomorrekening == '':
            self.pesan = wx.MessageDialog(self,"Nomor Rekening Jangan Kosong","Peringatan",wx.OK) 
            self.pesan.ShowModal()
        else:
            sql="SELECT * FROM koderek WHERE norek='"+(nomorrekening)+"' "
            cur.execute(sql)
            hasil = cur.fetchone()  
            if hasil:
                self.pesan = wx.MessageDialog(self,"Nomor Rekening Sudah Ada","Konfirmasi",wx.OK) 
                self.pesan.ShowModal()
            else:
                add_rekening="INSERT INTO koderek (kode, norek ,kegiatan ) VALUES('1.2','"+(nomorrekening)+"', '"+(namakegiatan)+"')"        
                cur.execute(add_rekening)
                db.commit()
                self.pesan = wx.MessageDialog(self,"Data Sudah Tersimpan","Konfirmasi",wx.OK) 
                self.pesan.ShowModal()
                self.awal()
            
        

    def OnEditButton(self, event):
        nomorrekening = str(self.norek.GetValue())
        namakegiatan = str(self.kegiatan.GetValue())
        nomorindex = str(self.noindex.GetValue())
        sql = "UPDATE koderek SET norek = '"+nomorrekening+"', kegiatan = '"+namakegiatan+"'  WHERE no = '"+nomorindex+"'"
        cur.execute(sql)
        db.commit()
        self.pesan = wx.MessageDialog(self,"Data Telah Diupdate","Konfirmasi",wx.OK) 
        self.pesan.ShowModal()
        self.awal()
        
    def OnMenuButton(self, event):
        self.Close()
        self.Destroy()

    def OnRekeningButton(self, event):
        self.Isi_Object()

    def OnButton1Button(self, event):
        nomorindex = str(self.noindex.GetValue())
        hapus="DELETE FROM koderek WHERE no='"+nomorindex+"'"
        cur.execute(hapus)
        db.commit()
        self.pesan = wx.MessageDialog(self,"Data Sudah Dihapus","Konfirmasi",wx.OK) 
        self.pesan.ShowModal()
        self.awal()

    
    
