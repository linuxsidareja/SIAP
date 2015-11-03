#Boa:Frame:lihatrekeningpendapatan
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
    return lihatrekeningpendapatan(parent)

[wxID_LIHATREKENINGPENDAPATAN, wxID_LIHATREKENINGPENDAPATANCARINOREK, 
 wxID_LIHATREKENINGPENDAPATANKEGIATAN, wxID_LIHATREKENINGPENDAPATANMENU, 
 wxID_LIHATREKENINGPENDAPATANNOINDEX, wxID_LIHATREKENINGPENDAPATANNOREK, 
 wxID_LIHATREKENINGPENDAPATANPEMBANGUNANDESA, 
 wxID_LIHATREKENINGPENDAPATANPENDAPATAN, wxID_LIHATREKENINGPENDAPATANREKENING, 
 wxID_LIHATREKENINGPENDAPATANSTATICBOX1, 
 wxID_LIHATREKENINGPENDAPATANSTATICTEXT2, 
 wxID_LIHATREKENINGPENDAPATANSTATICTEXT3, 
] = [wx.NewId() for _init_ctrls in range(12)]

class lihatrekeningpendapatan(wx.Frame):
    def _init_coll_pembangunandesa_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT,
              heading='Nomor Rekening', width=120)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT, heading='Uraian',
              width=500)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_LIHATREKENINGPENDAPATAN,
              name=u'lihatrekeningpendapatan', parent=prnt, pos=wx.Point(561,
              213), size=wx.Size(615, 437), style=wx.DEFAULT_FRAME_STYLE,
              title=u'Master Rekening Pendapatan')
        self.SetClientSize(wx.Size(607, 407))
        self.SetAutoLayout(False)
        self.Center(wx.BOTH)
        self.SetBackgroundColour(wx.Colour(192, 192, 192))

        self.pembangunandesa = wx.ListCtrl(id=wxID_LIHATREKENINGPENDAPATANPEMBANGUNANDESA,
              name=u'pembangunandesa', parent=self, pos=wx.Point(8, 24),
              size=wx.Size(592, 296), style=wx.LC_REPORT)
        self._init_coll_pembangunandesa_Columns(self.pembangunandesa)
        self.pembangunandesa.Bind(wx.EVT_LIST_ITEM_SELECTED,
              self.OnPembangunandesaListItemSelected,
              id=wxID_LIHATREKENINGPENDAPATANPEMBANGUNANDESA)

        self.pendapatan = wx.StaticText(id=wxID_LIHATREKENINGPENDAPATANPENDAPATAN,
              label=u'1. PENDAPATAN', name=u'pendapatan', parent=self,
              pos=wx.Point(8, 8), size=wx.Size(79, 13), style=0)

        self.staticText2 = wx.StaticText(id=wxID_LIHATREKENINGPENDAPATANSTATICTEXT2,
              label=u'Nomor Rekening', name='staticText2', parent=self,
              pos=wx.Point(8, 328), size=wx.Size(79, 13), style=0)

        self.norek = wx.TextCtrl(id=wxID_LIHATREKENINGPENDAPATANNOREK,
              name=u'norek', parent=self, pos=wx.Point(96, 328),
              size=wx.Size(48, 21), style=0, value=u'')

        self.staticText3 = wx.StaticText(id=wxID_LIHATREKENINGPENDAPATANSTATICTEXT3,
              label=u'Kegiatan', name='staticText3', parent=self,
              pos=wx.Point(152, 328), size=wx.Size(43, 13), style=0)

        self.kegiatan = wx.TextCtrl(id=wxID_LIHATREKENINGPENDAPATANKEGIATAN,
              name=u'kegiatan', parent=self, pos=wx.Point(208, 328),
              size=wx.Size(392, 21), style=0, value=u'')

        self.menu = wx.Button(id=wxID_LIHATREKENINGPENDAPATANMENU,
              label=u'Kembali Ke Menu', name=u'menu', parent=self,
              pos=wx.Point(488, 368), size=wx.Size(112, 23), style=0)
        self.menu.Bind(wx.EVT_BUTTON, self.OnMenuButton,
              id=wxID_LIHATREKENINGPENDAPATANMENU)

        self.staticBox1 = wx.StaticBox(id=wxID_LIHATREKENINGPENDAPATANSTATICBOX1,
              label=u'Cari Norek', name='staticBox1', parent=self,
              pos=wx.Point(8, 352), size=wx.Size(272, 48), style=0)

        self.rekening = wx.Button(id=wxID_LIHATREKENINGPENDAPATANREKENING,
              label=u'Cari Norek', name=u'rekening', parent=self,
              pos=wx.Point(16, 368), size=wx.Size(75, 23), style=0)
        self.rekening.Bind(wx.EVT_BUTTON, self.OnRekeningButton,
              id=wxID_LIHATREKENINGPENDAPATANREKENING)

        self.carinorek = wx.TextCtrl(id=wxID_LIHATREKENINGPENDAPATANCARINOREK,
              name=u'carinorek', parent=self, pos=wx.Point(96, 368),
              size=wx.Size(176, 21), style=0, value=u'')

        self.noindex = wx.TextCtrl(id=wxID_LIHATREKENINGPENDAPATANNOINDEX,
              name=u'noindex', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(100, 21), style=0, value=u'')

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
        sql = "SELECT * FROM koderek ORDER BY CAST(REPLACE(norek, '.', '') AS INT)"
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
        

    
        
    def OnMenuButton(self, event):
        self.Close()
        self.Destroy()

    def OnRekeningButton(self, event):
        self.Isi_Object()

    
    
