#Boa:Dialog:lihatrpjmdesa
#-------------------------------------------------------------------------------
#Sistem Informasi dan Administrasi Perdesaan
#pengembang johandri@ictwatch.id
#-------------------------------------------------------------------------------

import os
import wx
import sqlite3
import csv

db = sqlite3.connect('siap.db')
cur = db.cursor()


def create(parent):
    return lihatrpjmdesa(parent)

[wxID_LIHATRPJMDESA, wxID_LIHATRPJMDESAEXCEL, wxID_LIHATRPJMDESALAPORAN, 
 wxID_LIHATRPJMDESALIHAT, wxID_LIHATRPJMDESAPERIODE, 
 wxID_LIHATRPJMDESASTATICBOX1, wxID_LIHATRPJMDESASTATICTEXT1, 
 wxID_LIHATRPJMDESASTATICTEXT2, wxID_LIHATRPJMDESASTATICTEXT3, 
 wxID_LIHATRPJMDESATAHUN1, wxID_LIHATRPJMDESATAHUN2, wxID_LIHATRPJMDESATAHUN3, 
 wxID_LIHATRPJMDESATAHUN4, wxID_LIHATRPJMDESATAHUN5, wxID_LIHATRPJMDESATAHUN6, 
] = [wx.NewId() for _init_ctrls in range(15)]

class lihatrpjmdesa(wx.Dialog):
    def _init_coll_laporan_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT, heading='Norek',
              width=40)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT, heading='Uraian',
              width=100)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT, heading='Lokasi',
              width=100)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_LEFT, heading='Volume',
              width=100)
        parent.InsertColumn(col=4, format=wx.LIST_FORMAT_LEFT,
              heading='Sasaran', width=100)
        parent.InsertColumn(col=5, format=wx.LIST_FORMAT_LEFT, heading='satu',
              width=50)
        parent.InsertColumn(col=6, format=wx.LIST_FORMAT_LEFT, heading='',
              width=50)
        parent.InsertColumn(col=7, format=wx.LIST_FORMAT_LEFT, heading='',
              width=50)
        parent.InsertColumn(col=8, format=wx.LIST_FORMAT_LEFT, heading='',
              width=50)
        parent.InsertColumn(col=9, format=wx.LIST_FORMAT_LEFT, heading='',
              width=50)
        parent.InsertColumn(col=10, format=wx.LIST_FORMAT_LEFT, heading='',
              width=50)
        parent.InsertColumn(col=11, format=wx.LIST_FORMAT_LEFT,
              heading='APBN/APBD', width=100)
        parent.InsertColumn(col=12, format=wx.LIST_FORMAT_LEFT,
              heading='APBDesa', width=100)
        parent.InsertColumn(col=13, format=wx.LIST_FORMAT_LEFT,
              heading='Lain-Lain', width=100)
        parent.InsertColumn(col=14, format=wx.LIST_FORMAT_LEFT, heading='Biaya',
              width=100)
        parent.InsertColumn(col=15, format=wx.LIST_FORMAT_LEFT, heading='Pola',
              width=100)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_LIHATRPJMDESA, name=u'lihatrpjmdesa',
              parent=prnt, pos=wx.Point(394, 92), size=wx.Size(948, 652),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Lihat RPJM Desa')
        self.SetClientSize(wx.Size(940, 622))
        self.Center(wx.BOTH)
        self.SetBackgroundColour(wx.Colour(192, 192, 192))

        self.laporan = wx.ListCtrl(id=wxID_LIHATRPJMDESALAPORAN,
              name=u'laporan', parent=self, pos=wx.Point(8, 88),
              size=wx.Size(923, 528), style=wx.LC_REPORT)
        self._init_coll_laporan_Columns(self.laporan)

        self.staticText1 = wx.StaticText(id=wxID_LIHATRPJMDESASTATICTEXT1,
              label=u'RPJM Desa ', name='staticText1', parent=self,
              pos=wx.Point(8, 8), size=wx.Size(111, 23), style=0)
        self.staticText1.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Tahoma'))

        self.staticText2 = wx.StaticText(id=wxID_LIHATRPJMDESASTATICTEXT2,
              label=u'Tahun Awal Periode RPJMDES :', name='staticText2',
              parent=self, pos=wx.Point(595, 12), size=wx.Size(151, 13),
              style=0)

        self.periode = wx.TextCtrl(id=wxID_LIHATRPJMDESAPERIODE,
              name=u'periode', parent=self, pos=wx.Point(751, 8),
              size=wx.Size(68, 21), style=0, value=u'')

        self.lihat = wx.Button(id=wxID_LIHATRPJMDESALIHAT, label=u'Lihat',
              name=u'lihat', parent=self, pos=wx.Point(824, 8), size=wx.Size(75,
              23), style=0)
        self.lihat.Bind(wx.EVT_BUTTON, self.OnLihatButton,
              id=wxID_LIHATRPJMDESALIHAT)

        self.excel = wx.Button(id=wxID_LIHATRPJMDESAEXCEL, label=u'Cetak',
              name=u'excel', parent=self, pos=wx.Point(808, 48),
              size=wx.Size(96, 23), style=0)
        self.excel.Bind(wx.EVT_BUTTON, self.OnExcelButton,
              id=wxID_LIHATRPJMDESAEXCEL)

        self.staticBox1 = wx.StaticBox(id=wxID_LIHATRPJMDESASTATICBOX1,
              label=u'Form Khusus Untuk Pencetakan Ke Spreedsheat',
              name='staticBox1', parent=self, pos=wx.Point(184, 32),
              size=wx.Size(728, 48), style=0)

        self.staticText3 = wx.StaticText(id=wxID_LIHATRPJMDESASTATICTEXT3,
              label=u'Masukan Tahun RPJMDesa Secara Berurutan',
              name='staticText3', parent=self, pos=wx.Point(200, 53),
              size=wx.Size(216, 13), style=0)

        self.tahun1 = wx.TextCtrl(id=wxID_LIHATRPJMDESATAHUN1, name=u'tahun1',
              parent=self, pos=wx.Point(421, 52), size=wx.Size(56, 21), style=0,
              value=u'')

        self.tahun2 = wx.TextCtrl(id=wxID_LIHATRPJMDESATAHUN2, name=u'tahun2',
              parent=self, pos=wx.Point(485, 52), size=wx.Size(56, 20), style=0,
              value=u'')

        self.tahun3 = wx.TextCtrl(id=wxID_LIHATRPJMDESATAHUN3, name=u'tahun3',
              parent=self, pos=wx.Point(549, 51), size=wx.Size(56, 21), style=0,
              value=u'')

        self.tahun4 = wx.TextCtrl(id=wxID_LIHATRPJMDESATAHUN4, name=u'tahun4',
              parent=self, pos=wx.Point(613, 51), size=wx.Size(56, 21), style=0,
              value=u'')

        self.tahun5 = wx.TextCtrl(id=wxID_LIHATRPJMDESATAHUN5, name=u'tahun5',
              parent=self, pos=wx.Point(677, 50), size=wx.Size(56, 21), style=0,
              value=u'')

        self.tahun6 = wx.TextCtrl(id=wxID_LIHATRPJMDESATAHUN6, name=u'tahun6',
              parent=self, pos=wx.Point(744, 49), size=wx.Size(56, 21), style=0,
              value=u'')

    def __init__(self, parent):
        self._init_ctrls(parent)

    def awal(self):
        self.IsiList()
        
        
        
    def IsiList(self):
        rperiode = str(self.periode.GetValue()) 
        self.laporan.DeleteAllItems()    
        sql1 = "SELECT * FROM rpjmdesasid WHERE periode='"+(rperiode)+"' ORDER BY REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(norek,'1', '0'),'2', '0'), '3', '0'), '4', '0'), '5', '0'), '6', '0'), '7', '0'), '8', '0'),  '9', '0') ASC "
        cur.execute(sql1) 
        hasil = cur.fetchall() 
        no_rek1 = self.laporan.GetItemCount() 
        for i in hasil : 
            self.laporan.InsertStringItem(no_rek1, "%s"%i[1])
            self.laporan.SetStringItem(no_rek1,1,"%s"%i[2])
            self.laporan.SetStringItem(no_rek1,2,"%s"%i[3])
            self.laporan.SetStringItem(no_rek1,3,"%s"%i[4])
            self.laporan.SetStringItem(no_rek1,4,"%s"%i[119])
            self.laporan.SetStringItem(no_rek1,5,"%s"%i[7])
            self.laporan.SetStringItem(no_rek1,6,"%s"%i[8])
            self.laporan.SetStringItem(no_rek1,7,"%s"%i[9])
            self.laporan.SetStringItem(no_rek1,8,"%s"%i[10])
            self.laporan.SetStringItem(no_rek1,9,"%s"%i[11])
            self.laporan.SetStringItem(no_rek1,10,"%s"%i[12])
            self.laporan.SetStringItem(no_rek1,11,"%s"%i[145])
            self.laporan.SetStringItem(no_rek1,12,"%s"%i[146])
            self.laporan.SetStringItem(no_rek1,13,"%s"%i[147])
            self.laporan.SetStringItem(no_rek1,14,"%s"%i[19])
            self.laporan.SetStringItem(no_rek1,15,"%s"%i[118])
                       
            no_rek1 = no_rek1 + 1 

    def OnLihatButton(self, event):
        self.awal()

    def OnExcelButton(self, event):
        rtahun1 = str(self.tahun1.GetValue())
        rtahun2 = str(self.tahun2.GetValue())
        rtahun3 = str(self.tahun3.GetValue())
        rtahun4 = str(self.tahun4.GetValue())
        rtahun5 = str(self.tahun5.GetValue())
        rtahun6 = str(self.tahun6.GetValue())
        rperiode = str(self.periode.GetValue()) 
        cursor = db.cursor()
        cursor.execute("SELECT no,norek,kegiatan,lokasi1,volume1,sasaran,waktu1,waktu2,waktu3,waktu4,waktu5,waktu6,apbnd,apbdes,lain,biaya1,pola FROM rpjmdesasid WHERE periode='"+(rperiode)+"' ORDER BY REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(norek,'1', '0'),'2', '0'), '3', '0'), '4', '0'), '5', '0'), '6', '0'), '7', '0'), '8', '0'),  '9', '0') ASC;" )
        with open("data/laporanrpjmdes.csv", "wb") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["Nomor","Kode Rekening","Jenis Kegiatan","Lokasi RT/RW/DESA", "Volume","Sasaran Manfaat",rtahun1,rtahun2,rtahun3,rtahun4,rtahun5,rtahun6,"APBN/APBD","APBDesa","Lain-lain","Jumlah 000","Pola"]) # write headers
            csv_writer.writerows(cursor)
        db.commit()
        self.pesan = wx.MessageDialog(self,"Data Sudah Dicetak Dalam Bentuk Spreadsheet","Konfirmasi",wx.OK) 
        self.pesan.ShowModal()     
