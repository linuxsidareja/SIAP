#Boa:Frame:importdata
#-------------------------------------------------------------------------------
#Sistem Informasi dan Administrasi Perdesaan
#pengembang johandri@ictwatch.id
#-------------------------------------------------------------------------------

import wx
import os
import csv
import sys
import optparse
import sqlite3

db = sqlite3.connect('siap.db')
cur = db.cursor()

def create(parent):
    return importdata(parent)

[wxID_IMPORTDATA, wxID_IMPORTDATABUTTON1, wxID_IMPORTDATABUTTON2, 
 wxID_IMPORTDATABUTTON3, wxID_IMPORTDATAKABUPATEN, wxID_IMPORTDATAPROPINSI, 
 wxID_IMPORTDATASATU, wxID_IMPORTDATASTATICBOX1, wxID_IMPORTDATASTATICTEXT1, 
] = [wx.NewId() for _init_ctrls in range(9)]

class importdata(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_IMPORTDATA, name=u'importdata',
              parent=prnt, pos=wx.Point(713, 353), size=wx.Size(310, 182),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Import Database')
        self.SetClientSize(wx.Size(302, 152))
        self.Center(wx.BOTH)
        self.SetBackgroundColour(wx.Colour(192, 192, 192))

        self.satu = wx.TextCtrl(id=wxID_IMPORTDATASATU, name=u'satu',
              parent=self, pos=wx.Point(24, 48), size=wx.Size(256, 21), style=0,
              value=u'')

        self.button1 = wx.Button(id=wxID_IMPORTDATABUTTON1, label=u'Ambil File',
              name='button1', parent=self, pos=wx.Point(24, 80),
              size=wx.Size(128, 24), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_IMPORTDATABUTTON1)

        self.staticBox1 = wx.StaticBox(id=wxID_IMPORTDATASTATICBOX1,
              label=u'Ambil File Yang Di Import', name='staticBox1',
              parent=self, pos=wx.Point(16, 0), size=wx.Size(272, 112),
              style=0)

        self.button2 = wx.Button(id=wxID_IMPORTDATABUTTON2,
              label=u'Kembali Ke Menu Utama', name='button2', parent=self,
              pos=wx.Point(64, 120), size=wx.Size(176, 24), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_IMPORTDATABUTTON2)

        self.button3 = wx.Button(id=wxID_IMPORTDATABUTTON3, label=u'Import',
              name='button3', parent=self, pos=wx.Point(160, 80),
              size=wx.Size(120, 24), style=0)
        self.button3.Bind(wx.EVT_BUTTON, self.OnButton3Button,
              id=wxID_IMPORTDATABUTTON3)

        self.propinsi = wx.TextCtrl(id=wxID_IMPORTDATAPROPINSI,
              name=u'propinsi', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(152, 24), style=0, value=u'')

        self.kabupaten = wx.TextCtrl(id=wxID_IMPORTDATAKABUPATEN,
              name=u'kabupaten', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(152, 24), style=0, value=u'')

        self.staticText1 = wx.StaticText(id=wxID_IMPORTDATASTATICTEXT1,
              label=u'Sumber Data', name='staticText1', parent=self,
              pos=wx.Point(32, 24), size=wx.Size(79, 17), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.dataprofil()

    def OnButton1Button(self, event):
        wildcard = "CSV File (*.csv)|*.csv"
        dialog = wx.FileDialog(None, "Ambil File",
                               wildcard=wildcard,
                               style=wx.OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            self.satu.SetValue(dialog.GetPath())
        dialog.Destroy()

    def OnButton2Button(self, event):
        self.Close()
        self.Destroy()
    
    def dataprofil(self) : 
        sql="SELECT * FROM identitas WHERE no=1"
        cur.execute(sql)
        hasil = cur.fetchone()  
        if hasil : 
            self.propinsi.SetValue(str(hasil[18]))
            self.kabupaten.SetValue(str(hasil[17])) 
            
        else : 
            self.pesan = wx.MessageDialog(self,"Cek Data Profil","Konfirmasi",wx.OK) 
            self.pesan.ShowModal() 

    def OnButton3Button(self, event):
        filenya = str(self.satu.GetValue())
        
       
        if filenya == '':
            self.pesan = wx.MessageDialog(self,"Tidak Ada File","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
    
        else :
            csvfile = open(filenya, 'rb')
            creader = csv.reader(csvfile, delimiter=';')
            for item in creader:
                cur.execute("INSERT INTO penduduk (nik , nama , jk, tmpt_lahir, tgl_lahir, umur, gdr, agama, status, shdk, shdrt, pddk_akhir, pekerjaan, nama_ibu, nama_ayah, no_kk, nama_kep_kel, petugas, pekerjaan_lain, nama_petugas, alamat, nama_prop, nama_kab, nama_kec, nama_kel, rt, rw, warganegara, nama_dusun,  kemiskinan, pddk_saat_ini, status_pddk, status_tgl, difabelitas, kontrasepsi, resiko, kelahiran, kematian, kejadianlain, pindah, dok1, dok2, dok3, dok4, dok5, dok6, dok7, dok8, promis1, promis2,promis3, promis4, promis5, promis6, promis7, promis8, photo, keterangan) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,'','','Tidak Miskin','','','','','','','','Tidak','','','','','','','','','','','','','','','','','','','/opt/sidesa/penduduk/blank.jpg','')", item,)
                db.commit()
                
