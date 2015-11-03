#Boa:Frame:lihatrkp
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
    return lihatrkp(parent)

[wxID_LIHATRKP, wxID_LIHATRKPEXCEL, wxID_LIHATRKPLAPORAN, wxID_LIHATRKPLIHAT, 
 wxID_LIHATRKPPERIODE, wxID_LIHATRKPSTATICTEXT1, wxID_LIHATRKPSTATICTEXT2, 
 wxID_LIHATRKPSTATICTEXT3, wxID_LIHATRKPTAHUN, 
] = [wx.NewId() for _init_ctrls in range(9)]

class lihatrkp(wx.Frame):
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
        parent.InsertColumn(col=4, format=wx.LIST_FORMAT_LEFT, heading='Satuan',
              width=100)
        parent.InsertColumn(col=5, format=wx.LIST_FORMAT_LEFT,
              heading='Sasaran', width=50)
        parent.InsertColumn(col=6, format=wx.LIST_FORMAT_LEFT, heading='B',
              width=50)
        parent.InsertColumn(col=7, format=wx.LIST_FORMAT_LEFT, heading='R',
              width=50)
        parent.InsertColumn(col=8, format=wx.LIST_FORMAT_LEFT, heading='L',
              width=50)
        parent.InsertColumn(col=9, format=wx.LIST_FORMAT_LEFT, heading='Sumber',
              width=50)
        parent.InsertColumn(col=10, format=wx.LIST_FORMAT_LEFT, heading='Biaya',
              width=50)
        parent.InsertColumn(col=11, format=wx.LIST_FORMAT_LEFT, heading='Pola',
              width=100)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_LIHATRKP, name=u'lihatrkp', parent=prnt,
              pos=wx.Point(403, 116), size=wx.Size(931, 652),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Lihat RKP Desa')
        self.SetClientSize(wx.Size(923, 622))
        self.Center(wx.BOTH)
        self.SetBackgroundColour(wx.Colour(192, 192, 192))

        self.laporan = wx.ListCtrl(id=wxID_LIHATRKPLAPORAN, name=u'laporan',
              parent=self, pos=wx.Point(0, 32), size=wx.Size(923, 584),
              style=wx.LC_REPORT)
        self._init_coll_laporan_Columns(self.laporan)

        self.staticText1 = wx.StaticText(id=wxID_LIHATRKPSTATICTEXT1,
              label=u'RKP Desa', name='staticText1', parent=self,
              pos=wx.Point(8, 8), size=wx.Size(91, 23), style=0)
        self.staticText1.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Tahoma'))

        self.staticText2 = wx.StaticText(id=wxID_LIHATRKPSTATICTEXT2,
              label=u'Periode RPJMDES :', name='staticText2', parent=self,
              pos=wx.Point(352, 8), size=wx.Size(92, 13), style=0)

        self.periode = wx.TextCtrl(id=wxID_LIHATRKPPERIODE, name=u'periode',
              parent=self, pos=wx.Point(448, 8), size=wx.Size(136, 21), style=0,
              value=u'')

        self.lihat = wx.Button(id=wxID_LIHATRKPLIHAT, label=u'Lihat',
              name=u'lihat', parent=self, pos=wx.Point(728, 8), size=wx.Size(75,
              23), style=0)
        self.lihat.Bind(wx.EVT_BUTTON, self.OnLihatButton,
              id=wxID_LIHATRKPLIHAT)

        self.excel = wx.Button(id=wxID_LIHATRKPEXCEL, label=u'Cetak Ke Excel',
              name=u'excel', parent=self, pos=wx.Point(816, 8), size=wx.Size(96,
              23), style=0)
        self.excel.Bind(wx.EVT_BUTTON, self.OnExcelButton,
              id=wxID_LIHATRKPEXCEL)

        self.staticText3 = wx.StaticText(id=wxID_LIHATRKPSTATICTEXT3,
              label=u'Tahun RKP', name='staticText3', parent=self,
              pos=wx.Point(592, 8), size=wx.Size(53, 13), style=0)

        self.tahun = wx.TextCtrl(id=wxID_LIHATRKPTAHUN, name=u'tahun',
              parent=self, pos=wx.Point(648, 8), size=wx.Size(72, 21), style=0,
              value=u'')

    def __init__(self, parent):
        self._init_ctrls(parent)

    def awal(self):
        self.IsiList()
       
        
        
    def IsiList(self):
        rperiode = str(self.periode.GetValue())
        rtahun = str(self.tahun.GetValue())
        self.laporan.DeleteAllItems()    
        sql1 = "SELECT * FROM rkpsid WHERE periode='"+(rperiode)+"' AND tahun='"+(rtahun)+"' ORDER BY REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(norek,'1', '0'),'2', '0'), '3', '0'), '4', '0'), '5', '0'), '6', '0'), '7', '0'), '8', '0'),  '9', '0') ASC "
        cur.execute(sql1) 
        hasil = cur.fetchall() 
        no_rek1 = self.laporan.GetItemCount() 
        for i in hasil : 
            self.laporan.InsertStringItem(no_rek1, "%s"%i[1])
            self.laporan.SetStringItem(no_rek1,1,"%s"%i[2])
            self.laporan.SetStringItem(no_rek1,2,"%s"%i[3])
            self.laporan.SetStringItem(no_rek1,3,"%s"%i[4])
            self.laporan.SetStringItem(no_rek1,4,"%s"%i[5])
            self.laporan.SetStringItem(no_rek1,5,"%s"%i[6])
            self.laporan.SetStringItem(no_rek1,6,"%s"%i[24])
            self.laporan.SetStringItem(no_rek1,7,"%s"%i[25])
            self.laporan.SetStringItem(no_rek1,8,"%s"%i[26])
            
                       
            no_rek1 = no_rek1 + 1 

    def OnLihatButton(self, event):
        self.awal()

    def OnExcelButton(self, event):
        

        rperiode = str(self.periode.GetValue())
        rtahun = str(self.tahun.GetValue())
        cursor = db.cursor()
        cursor.execute("SELECT no,norek,kegiatan,lokasi,volume,satuan,sasaran,baru,rehab,lama,sumber,biaya,pola FROM rkpsid WHERE periode='"+(rperiode)+"' AND tahun='"+(rtahun)+"' ORDER BY REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(norek,'1', '0'),'2', '0'), '3', '0'), '4', '0'), '5', '0'), '6', '0'), '7', '0'), '8', '0'),  '9', '0') ASC;" )
        with open("data/laporanrkp.csv", "wb") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["Nomor","Kode Rekening","Jenis Kegiatan","Lokasi RT/RW/DESA", "Volume","Satuan","Sasaran Manfaat","B","R","T","Sumber Biaya","Jumlah 000","Pola"]) # write headers
            csv_writer.writerows(cursor)
            db.commit()
            self.pesan = wx.MessageDialog(self,"Data Sudah Dicetak Dalam Bentuk Spreadsheet","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()     

