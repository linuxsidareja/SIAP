#Boa:Frame:edit_profil_desa
#-------------------------------------------------------------------------------
#Sistem Informasi dan Administrasi Perdesaan
#pengembang johandri@ictwatch.id
#-------------------------------------------------------------------------------

import wx
import sqlite3
import shutil
import os


db = sqlite3.connect('siap.db')
cur = db.cursor()


def create(parent):
    return edit_profil_desa(parent)

[wxID_EDIT_PROFIL_DESA, wxID_EDIT_PROFIL_DESAALAMAT, 
 wxID_EDIT_PROFIL_DESABUTTON1, wxID_EDIT_PROFIL_DESABUTTON2, 
 wxID_EDIT_PROFIL_DESABUTTON3, wxID_EDIT_PROFIL_DESABUTTON4, 
 wxID_EDIT_PROFIL_DESADESA, wxID_EDIT_PROFIL_DESAKABUPATEN, 
 wxID_EDIT_PROFIL_DESAKECAMATAN, wxID_EDIT_PROFIL_DESAKODE, 
 wxID_EDIT_PROFIL_DESALABEL_ALAMAT, wxID_EDIT_PROFIL_DESALABEL_KECAMATAN, 
 wxID_EDIT_PROFIL_DESALABEL_KODE_DESA, wxID_EDIT_PROFIL_DESALABEL_NAMA_DESA, 
 wxID_EDIT_PROFIL_DESALABEL_PROPINSI, wxID_EDIT_PROFIL_DESALABEL_WEB, 
 wxID_EDIT_PROFIL_DESALABLE_KABUPATEN, wxID_EDIT_PROFIL_DESALOGOPEMDA, 
 wxID_EDIT_PROFIL_DESANAMAEMAIL, wxID_EDIT_PROFIL_DESANOTELP, 
 wxID_EDIT_PROFIL_DESAPROPINSI, wxID_EDIT_PROFIL_DESASIMPANGAMBAR, 
 wxID_EDIT_PROFIL_DESASTATICTEXT2, wxID_EDIT_PROFIL_DESATELP, 
 wxID_EDIT_PROFIL_DESATOMBOL_KEMBALI, wxID_EDIT_PROFIL_DESATOMBOL_SIMPAN, 
 wxID_EDIT_PROFIL_DESAWEB, 
] = [wx.NewId() for _init_ctrls in range(27)]

class edit_profil_desa(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_EDIT_PROFIL_DESA,
              name=u'edit_profil_desa', parent=prnt, pos=wx.Point(601, 268),
              size=wx.Size(534, 328), style=wx.DEFAULT_FRAME_STYLE,
              title=u'Edit  Profil Desa')
        self.SetClientSize(wx.Size(526, 298))
        self.Center(wx.BOTH)
        self.SetBackgroundColour(wx.Colour(192, 192, 192))

        self.label_nama_desa = wx.StaticText(id=wxID_EDIT_PROFIL_DESALABEL_NAMA_DESA,
              label=u'Nama Desa', name=u'label_nama_desa', parent=self,
              pos=wx.Point(192, 16), size=wx.Size(77, 17), style=0)

        self.label_kecamatan = wx.StaticText(id=wxID_EDIT_PROFIL_DESALABEL_KECAMATAN,
              label=u'Kecamatan', name=u'label_kecamatan', parent=self,
              pos=wx.Point(192, 44), size=wx.Size(73, 16), style=0)

        self.lable_kabupaten = wx.StaticText(id=wxID_EDIT_PROFIL_DESALABLE_KABUPATEN,
              label=u'Kabupaten', name=u'lable_kabupaten', parent=self,
              pos=wx.Point(192, 65), size=wx.Size(70, 17), style=0)

        self.label_propinsi = wx.StaticText(id=wxID_EDIT_PROFIL_DESALABEL_PROPINSI,
              label=u'Propinsi', name=u'label_propinsi', parent=self,
              pos=wx.Point(193, 84), size=wx.Size(51, 17), style=0)

        self.desa = wx.TextCtrl(id=wxID_EDIT_PROFIL_DESADESA, name=u'desa',
              parent=self, pos=wx.Point(280, 16), size=wx.Size(240, 21),
              style=0, value='')

        self.kabupaten = wx.TextCtrl(id=wxID_EDIT_PROFIL_DESAKABUPATEN,
              name=u'kabupaten', parent=self, pos=wx.Point(280, 60),
              size=wx.Size(240, 21), style=0, value='')

        self.propinsi = wx.TextCtrl(id=wxID_EDIT_PROFIL_DESAPROPINSI,
              name=u'propinsi', parent=self, pos=wx.Point(280, 82),
              size=wx.Size(240, 21), style=0, value='')

        self.label_web = wx.StaticText(id=wxID_EDIT_PROFIL_DESALABEL_WEB,
              label=u'Alamat Web', name=u'label_web', parent=self,
              pos=wx.Point(192, 108), size=wx.Size(83, 17), style=0)

        self.label_kode_desa = wx.StaticText(id=wxID_EDIT_PROFIL_DESALABEL_KODE_DESA,
              label=u'No Kode Desa', name=u'label_kode_desa', parent=self,
              pos=wx.Point(192, 130), size=wx.Size(81, 17), style=0)

        self.label_alamat = wx.StaticText(id=wxID_EDIT_PROFIL_DESALABEL_ALAMAT,
              label=u'Alamat', name=u'label_alamat', parent=self,
              pos=wx.Point(192, 152), size=wx.Size(47, 17), style=0)

        self.alamat = wx.TextCtrl(id=wxID_EDIT_PROFIL_DESAALAMAT,
              name=u'alamat', parent=self, pos=wx.Point(280, 148),
              size=wx.Size(240, 20), style=0, value='')

        self.kecamatan = wx.TextCtrl(id=wxID_EDIT_PROFIL_DESAKECAMATAN,
              name=u'kecamatan', parent=self, pos=wx.Point(280, 38),
              size=wx.Size(240, 21), style=0, value='')

        self.tombol_simpan = wx.Button(id=wxID_EDIT_PROFIL_DESATOMBOL_SIMPAN,
              label=u'Simpan Data', name=u'tombol_simpan', parent=self,
              pos=wx.Point(8, 269), size=wx.Size(123, 23), style=0)
        self.tombol_simpan.Bind(wx.EVT_BUTTON, self.OnTombol_simpanButton,
              id=wxID_EDIT_PROFIL_DESATOMBOL_SIMPAN)

        self.tombol_kembali = wx.Button(id=wxID_EDIT_PROFIL_DESATOMBOL_KEMBALI,
              label=u'Kembali Ke Menu', name=u'tombol_kembali', parent=self,
              pos=wx.Point(136, 269), size=wx.Size(142, 23), style=0)
        self.tombol_kembali.Bind(wx.EVT_BUTTON, self.OnTombol_kembaliButton,
              id=wxID_EDIT_PROFIL_DESATOMBOL_KEMBALI)

        self.telp = wx.StaticText(id=wxID_EDIT_PROFIL_DESATELP, label=u'Telp',
              name=u'telp', parent=self, pos=wx.Point(192, 176),
              size=wx.Size(25, 15), style=0)

        self.notelp = wx.TextCtrl(id=wxID_EDIT_PROFIL_DESANOTELP,
              name=u'notelp', parent=self, pos=wx.Point(280, 169),
              size=wx.Size(105, 21), style=0, value='')

        self.staticText2 = wx.StaticText(id=wxID_EDIT_PROFIL_DESASTATICTEXT2,
              label=u'Email', name='staticText2', parent=self, pos=wx.Point(192,
              200), size=wx.Size(36, 15), style=0)

        self.namaemail = wx.TextCtrl(id=wxID_EDIT_PROFIL_DESANAMAEMAIL,
              name=u'namaemail', parent=self, pos=wx.Point(280, 191),
              size=wx.Size(104, 21), style=0, value='')

        self.web = wx.TextCtrl(id=wxID_EDIT_PROFIL_DESAWEB, name=u'web',
              parent=self, pos=wx.Point(280, 104), size=wx.Size(240, 21),
              style=0, value=u'')

        self.kode = wx.TextCtrl(id=wxID_EDIT_PROFIL_DESAKODE, name=u'kode',
              parent=self, pos=wx.Point(280, 126), size=wx.Size(240, 21),
              style=0, value=u'')

        self.logopemda = wx.TextCtrl(id=wxID_EDIT_PROFIL_DESALOGOPEMDA,
              name=u'logopemda', parent=self, pos=wx.Point(16, 208),
              size=wx.Size(168, 24), style=0, value=u'')

        self.simpangambar = wx.TextCtrl(id=wxID_EDIT_PROFIL_DESASIMPANGAMBAR,
              name=u'simpangambar', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(152, 24), style=0, value=u'png/')

        self.button1 = wx.Button(id=wxID_EDIT_PROFIL_DESABUTTON1,
              label=u'Upload Logo Pemda', name='button1', parent=self,
              pos=wx.Point(16, 234), size=wx.Size(168, 23), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_EDIT_PROFIL_DESABUTTON1)

        self.button2 = wx.Button(id=wxID_EDIT_PROFIL_DESABUTTON2,
              label=u'Input Perangkat Desa', name='button2', parent=self,
              pos=wx.Point(345, 215), size=wx.Size(176, 23), style=0)

        self.button3 = wx.Button(id=wxID_EDIT_PROFIL_DESABUTTON3,
              label=u'Input RT/RW/Dusun', name='button3', parent=self,
              pos=wx.Point(344, 242), size=wx.Size(178, 23), style=0)

        self.button4 = wx.Button(id=wxID_EDIT_PROFIL_DESABUTTON4,
              label=u'Input Pejabat Pemerintahan', name='button4', parent=self,
              pos=wx.Point(345, 269), size=wx.Size(176, 23), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.cekdata()
    
    def cekdata(self):
        sql="SELECT * FROM identitas WHERE no='1'"
        cur.execute(sql)
        hasil = cur.fetchone()  
        if hasil :
            
            self.desa.SetValue(str(hasil[15]))
            self.kecamatan.SetValue(str(hasil[16]))
            self.kabupaten.SetValue(str(hasil[17]))
            self.propinsi.SetValue(str(hasil[18]))
            self.alamat.SetValue(str(hasil[19]))
            self.web.SetValue(str(hasil[20]))
            self.kode.SetValue(str(hasil[25]))
            self.notelp.SetValue(str(hasil[22]))
            self.namaemail.SetValue(str(hasil[21]))
            self.logopemda.SetValue(str(hasil[1]))
            self.tombol_simpan.Disable()
            self.button1.Disable()
             
            self.PhotoMaxSize = 150
            img = wx.Image(self.logopemda.GetValue(), wx.BITMAP_TYPE_ANY)
            W = img.GetWidth()
            H = img.GetHeight()
            if W > H:
                NewW = self.PhotoMaxSize
                NewH = self.PhotoMaxSize * H / W
            else:
                NewH = self.PhotoMaxSize
                NewW = self.PhotoMaxSize * W / H
                img = img.Scale(NewW,NewH)
                self.imageCtrl = wx.StaticBitmap(self, wx.ID_ANY, wx.BitmapFromImage(img),wx.Point(16, 16))
            self.pesan = wx.MessageDialog(self,"Data Identitas Sudah Dimasukkan Anda Hanya Diperkenankan Untuk Mengedit Data Identitas Desa. Silahkan Buka Edit Profil Desa ","Peringatan",wx.OK) 
            self.pesan.ShowModal()    
        else : 
            self.loadgambar()
            self.tombol_simpan.Enable()
            self.button1.Enable()
      
            
    def loadgambar(self):
        self.PhotoMaxSize = 150
        img = wx.Image('png/pemda.jpg', wx.BITMAP_TYPE_ANY)
        W = img.GetWidth()
        H = img.GetHeight()
        if W > H:
            NewW = self.PhotoMaxSize
            NewH = self.PhotoMaxSize * H / W
        else:
            NewH = self.PhotoMaxSize
            NewW = self.PhotoMaxSize * W / H
            
        img = img.Scale(NewW,NewH)
        self.imageCtrl = wx.StaticBitmap(self, wx.ID_ANY, wx.BitmapFromImage(img),wx.Point(16, 16))
 
  
    def OnTombol_kembaliButton(self, event):
        
        
        self.Close()
        self.Destroy()
        

    def OnTombol_simpanButton(self, event):
        desa = str(self.desa.GetValue())
        kecamatan = str(self.kecamatan.GetValue())
        kabupaten = str(self.kabupaten.GetValue())
        propinsi = str(self.propinsi.GetValue())
        alamat = str(self.alamat.GetValue())
        web = str(self.web.GetValue())
        kode = str(self.kode.GetValue())
        notelp = str(self.notelp.GetValue())
        namaemail = str(self.namaemail.GetValue())
        gbr = str(self.simpangambar.GetValue())
        filepath = str(self.logopemda.GetValue())
        
        if desa == '':
            self.pesan = wx.MessageDialog(self,"Nama Desa Jangan Kosong","Peringatan",wx.OK) 
            self.pesan.ShowModal()
        elif kecamatan == '':
            self.pesan = wx.MessageDialog(self,"Nama Kecamatan Jangan Kosong","Peringatan",wx.OK) 
            self.pesan.ShowModal()
        elif kabupaten == '':
            self.pesan = wx.MessageDialog(self,"Nama Kabupaten Jangan Kosong","Peringatan",wx.OK) 
            self.pesan.ShowModal()        
        elif propinsi == '':
            self.pesan = wx.MessageDialog(self,"Nama Propinsi Jangan Kosong","Peringatan",wx.OK) 
            self.pesan.ShowModal()
        elif kode == '':
            self.pesan = wx.MessageDialog(self,"Kode Desa Jangan Kosong","Peringatan",wx.OK) 
            self.pesan.ShowModal()
        elif filepath == '':
            add_identitas="INSERT INTO identitas (logopemda,nama_kaur_kesra,nama_kaur_keuangan,nama_kaur_umum,nama_kaur_ekbang, nama_camat, nama_kaur_pemerintahan, nama_bupati,dusun6, dusun5, dusun4, dusun3, dusun2, dusun1, nama_desa, nama_kecamatan, nama_kabupaten, nama_propinsi, alamat_kantor, website, email, no_telp, nama_kades, nama_sekdes, nokode) VALUES('"+(gbr)+"pemda.jpg','"+(kesra)+"','"+(keuangan)+"','"+(umum)+"','"+(ekbang)+"','"+(camat)+"','"+(pemerintahan)+"','"+(bupati)+"','"+(dusun6)+"', '"+(dusun5)+"', '"+(dusun4)+"', '"+(dusun3)+"', '"+(dusun2)+"', '"+(dusun1)+"', '"+(desa)+"', '"+(kecamatan)+"', '"+(kabupaten)+"', '"+(propinsi)+"', '"+(alamat)+"', '"+(web)+"', '"+(namaemail)+"', '"+(notelp)+"', '"+(kades)+"', '"+(sekdes)+"', '"+(kode)+"')"
            cur.execute(add_identitas)
            db.commit()
        else :
            shutil.copy2(filepath, gbr+desa+'.jpg')       
            add_identitas="INSERT INTO identitas (logopemda,nama_kaur_kesra,nama_kaur_keuangan,nama_kaur_umum,nama_kaur_ekbang, nama_camat, nama_kaur_pemerintahan, nama_bupati,dusun6, dusun5, dusun4, dusun3, dusun2, dusun1, nama_desa, nama_kecamatan, nama_kabupaten, nama_propinsi, alamat_kantor, website, email, no_telp, nama_kades, nama_sekdes, nokode) VALUES('"+(gbr)+(desa)+".jpg','"+(kesra)+"','"+(keuangan)+"','"+(umum)+"','"+(ekbang)+"','"+(camat)+"','"+(pemerintahan)+"','"+(bupati)+"','"+(dusun6)+"', '"+(dusun5)+"', '"+(dusun4)+"', '"+(dusun3)+"', '"+(dusun2)+"', '"+(dusun1)+"', '"+(desa)+"', '"+(kecamatan)+"', '"+(kabupaten)+"', '"+(propinsi)+"', '"+(alamat)+"', '"+(web)+"', '"+(namaemail)+"', '"+(notelp)+"', '"+(kades)+"', '"+(sekdes)+"', '"+(kode)+"')"
            cur.execute(add_identitas)
            db.commit()
            self.pesan = wx.MessageDialog(self,"Data Identitas Desa Tersimpan ","Konfirmasi",wx.OK) 
            self.pesan.ShowModal() 
            self.Close()
            self.Destroy()
            

    def OnButton1Button(self, event):
        wildcard = "JPG PNG BMP File (*.jpg)|*.jpg"
        dialog = wx.FileDialog(None, "Ambil File",
                               wildcard=wildcard,
                               style=wx.OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            self.logopemda.SetValue(dialog.GetPath())
        dialog.Destroy()
        self.onView()
        
    def onView(self):
        filepath = self.logopemda.GetValue()
        img = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
        # scale the image, preserving the aspect ratio
        W = img.GetWidth()
        H = img.GetHeight()
        if W > H:
            NewW = self.PhotoMaxSize
            NewH = self.PhotoMaxSize * H / W
        else:
            NewH = self.PhotoMaxSize
            NewW = self.PhotoMaxSize * W / H
            
        img = img.Scale(NewW,NewH)
        self.imageCtrl.SetBitmap(wx.BitmapFromImage(img))
