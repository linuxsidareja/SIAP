#Boa:Frame:surat_masuk
#-------------------------------------------------------------------------------
#Sistem Informasi dan Administrasi Perdesaan
#pengembang johandri@ictwatch.id
#-------------------------------------------------------------------------------

import wx
import wx.richtext
import wx.lib.buttons

import sqlite3


db = sqlite3.connect('siap.db')
cur = db.cursor()

def create(parent):
    return surat_masuk(parent)

[wxID_SURAT_MASUK, wxID_SURAT_MASUKDARI, wxID_SURAT_MASUKINPUT_KETERANGAN, 
 wxID_SURAT_MASUKINPUT_NOMOR_SURAT, wxID_SURAT_MASUKINPUT_PERIHAL, 
 wxID_SURAT_MASUKKEPADA, wxID_SURAT_MASUKKOTAK_SURAT_MASUK, 
 wxID_SURAT_MASUKLABEL_ISI_SINGKAT_SURAT, wxID_SURAT_MASUKLABEL_KETERANGAN, 
 wxID_SURAT_MASUKLABEL_NOMOR_SURAT_MASUK, wxID_SURAT_MASUKLABEL_TANGGAL_SURAT, 
 wxID_SURAT_MASUKLABEL_TUJUAN_SURAT, wxID_SURAT_MASUKMENU, 
 wxID_SURAT_MASUKPERIHAL, wxID_SURAT_MASUKRICHTEXTCTRL1, 
 wxID_SURAT_MASUKSIMPAN, wxID_SURAT_MASUKTANGGAL, wxID_SURAT_MASUKTUJUAN, 
] = [wx.NewId() for _init_ctrls in range(18)]

class surat_masuk(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_SURAT_MASUK, name=u'surat_masuk',
              parent=prnt, pos=wx.Point(439, 244), size=wx.Size(858, 400),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Surat Masuk')
        self.SetClientSize(wx.Size(850, 370))
        self.Center(wx.BOTH)
        self.SetBackgroundColour(wx.Colour(192, 192, 192))

        self.label_nomor_surat_masuk = wx.StaticText(id=wxID_SURAT_MASUKLABEL_NOMOR_SURAT_MASUK,
              label=u'Nomor Surat Masuk', name=u'label_nomor_surat_masuk',
              parent=self, pos=wx.Point(40, 48), size=wx.Size(122, 17),
              style=0)

        self.label_tanggal_surat = wx.StaticText(id=wxID_SURAT_MASUKLABEL_TANGGAL_SURAT,
              label=u'Tanggal Surat', name=u'label_tanggal_surat', parent=self,
              pos=wx.Point(40, 80), size=wx.Size(81, 17), style=0)

        self.label_tujuan_surat = wx.StaticText(id=wxID_SURAT_MASUKLABEL_TUJUAN_SURAT,
              label=u'Dari', name=u'label_tujuan_surat', parent=self,
              pos=wx.Point(40, 112), size=wx.Size(76, 17), style=0)

        self.label_isi_singkat_surat = wx.StaticText(id=wxID_SURAT_MASUKLABEL_ISI_SINGKAT_SURAT,
              label=u'Isi Singkat Surat', name=u'label_isi_singkat_surat',
              parent=self, pos=wx.Point(40, 144), size=wx.Size(97, 17),
              style=0)

        self.label_keterangan = wx.StaticText(id=wxID_SURAT_MASUKLABEL_KETERANGAN,
              label=u'Disposisi', name=u'label_keterangan', parent=self,
              pos=wx.Point(40, 280), size=wx.Size(88, 17), style=0)

        self.input_nomor_surat = wx.TextCtrl(id=wxID_SURAT_MASUKINPUT_NOMOR_SURAT,
              name=u'input_nomor_surat', parent=self, pos=wx.Point(168, 40),
              size=wx.Size(312, 25), style=0, value=u'')

        self.dari = wx.TextCtrl(id=wxID_SURAT_MASUKDARI, name=u'dari',
              parent=self, pos=wx.Point(168, 104), size=wx.Size(312, 25),
              style=0, value=u'')

        self.input_keterangan = wx.TextCtrl(id=wxID_SURAT_MASUKINPUT_KETERANGAN,
              name=u'input_keterangan', parent=self, pos=wx.Point(168, 280),
              size=wx.Size(656, 25), style=0, value=u'')

        self.kotak_surat_masuk = wx.StaticBox(id=wxID_SURAT_MASUKKOTAK_SURAT_MASUK,
              label=u'Surat masuk Input', name=u'kotak_surat_masuk',
              parent=self, pos=wx.Point(8, 16), size=wx.Size(832, 304),
              style=0)

        self.tanggal = wx.DatePickerCtrl(id=wxID_SURAT_MASUKTANGGAL,
              name=u'tanggal', parent=self, pos=wx.Point(168, 72),
              size=wx.Size(168, 26), style=wx.DP_SHOWCENTURY)

        self.richTextCtrl1 = wx.richtext.RichTextCtrl(id=wxID_SURAT_MASUKRICHTEXTCTRL1,
              parent=self, pos=wx.Point(168, 144), size=wx.Size(656, 128),
              style=wx.richtext.RE_MULTILINE, value='')

        self.tujuan = wx.StaticText(id=wxID_SURAT_MASUKTUJUAN, label=u'Kepada',
              name=u'tujuan', parent=self, pos=wx.Point(488, 112),
              size=wx.Size(48, 15), style=0)

        self.kepada = wx.TextCtrl(id=wxID_SURAT_MASUKKEPADA, name=u'kepada',
              parent=self, pos=wx.Point(552, 104), size=wx.Size(272, 25),
              style=0, value='')

        self.perihal = wx.StaticText(id=wxID_SURAT_MASUKPERIHAL,
              label=u'Perihal', name=u'perihal', parent=self, pos=wx.Point(488,
              48), size=wx.Size(44, 15), style=0)

        self.input_perihal = wx.TextCtrl(id=wxID_SURAT_MASUKINPUT_PERIHAL,
              name=u'input_perihal', parent=self, pos=wx.Point(552, 40),
              size=wx.Size(272, 25), style=0, value='')

        self.simpan = wx.Button(id=wxID_SURAT_MASUKSIMPAN, label=u'Simpan',
              name=u'simpan', parent=self, pos=wx.Point(280, 336),
              size=wx.Size(144, 23), style=0)

        self.menu = wx.Button(id=wxID_SURAT_MASUKMENU, label=u'Kembali Ke Menu',
              name=u'menu', parent=self, pos=wx.Point(432, 336),
              size=wx.Size(176, 23), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnTombol_ke_menu_suratButton(self, event):
        
        self.Close()
        self.Destroy()

    def OnTombol_simpanButton(self, event):
        inputsuratmasuk = str(self.input_nomor_surat.GetValue())
        inputtanggal = str(self.tanggal.GetValue())
        inputdari = str(self.dari.GetValue())
        inputkepada = str(self.kepada.GetValue())
        inputperihal = str(self.input_perihal.GetValue())
        inputketerangan = str(self.richTextCtrl1.GetValue())
        inputdisposisi = str(self.input_keterangan.GetValue())
        add_surat = "INSERT INTO suratmasuk (keterangan, no_surat, tanggal, dari, kepada, perihal,disposisi) VALUES('"+(inputketerangan)+"', '"+(inputsuratmasuk)+"', '"+(inputtanggal)+"', '"+(inputdari)+"', '"+(inputkepada)+"', '"+(inputperihal)+"', '"+(inputdisposisi)+"')"
        cur.execute(add_surat)
        self.input_nomor_surat.Clear()
        
        self.dari.Clear()
        self.kepada.Clear()
        self.input_perihal.Clear()
        self.richTextCtrl1.Clear()
        self.input_keterangan.Clear()
        self.pesan = wx.MessageDialog(self,"Data Surat Masuk Disimpan","Konfirmasi",wx.OK) 
        self.pesan.ShowModal()
