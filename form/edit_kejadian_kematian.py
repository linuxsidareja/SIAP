#Boa:Dialog:edit_kejadian_kematian
#-------------------------------------------------------------------------------
#Sistem Informasi dan Administrasi Perdesaan
#pengembang johandri@ictwatch.id
#-------------------------------------------------------------------------------

import os
import wx
import wx.lib.buttons

import sqlite3
import string
import gettext



db = sqlite3.connect('siap.db')
cur = db.cursor()

def create(parent):
    return edit_kejadian_kematian(parent)

[wxID_EDIT_KEJADIAN_KEMATIAN, wxID_EDIT_KEJADIAN_KEMATIANCARI_KK, 
 wxID_EDIT_KEJADIAN_KEMATIANDOKUMEN, wxID_EDIT_KEJADIAN_KEMATIANINPUTNO, 
 wxID_EDIT_KEJADIAN_KEMATIANINPUT_ALAMAT, 
 wxID_EDIT_KEJADIAN_KEMATIANINPUT_AYAH, 
 wxID_EDIT_KEJADIAN_KEMATIANINPUT_DUSUN, wxID_EDIT_KEJADIAN_KEMATIANINPUT_IBU, 
 wxID_EDIT_KEJADIAN_KEMATIANINPUT_NAMA, wxID_EDIT_KEJADIAN_KEMATIANINPUT_NIK, 
 wxID_EDIT_KEJADIAN_KEMATIANINPUT_NO, wxID_EDIT_KEJADIAN_KEMATIANINPUT_NO_KK, 
 wxID_EDIT_KEJADIAN_KEMATIANINPUT_RT, wxID_EDIT_KEJADIAN_KEMATIANINPUT_RW, 
 wxID_EDIT_KEJADIAN_KEMATIANINPUT_TEMPAT_LAHIR, 
 wxID_EDIT_KEJADIAN_KEMATIANISIPENDUDUK, wxID_EDIT_KEJADIAN_KEMATIANKEMBALI, 
 wxID_EDIT_KEJADIAN_KEMATIANKETERANGAN, 
 wxID_EDIT_KEJADIAN_KEMATIANLABEL_AGAMA, 
 wxID_EDIT_KEJADIAN_KEMATIANLABEL_ALAMAT, 
 wxID_EDIT_KEJADIAN_KEMATIANLABEL_DIFABELITAS, 
 wxID_EDIT_KEJADIAN_KEMATIANLABEL_DUSUN, 
 wxID_EDIT_KEJADIAN_KEMATIANLABEL_GOLONGAN_DARAH, 
 wxID_EDIT_KEJADIAN_KEMATIANLABEL_JENIS_KELAMIN, 
 wxID_EDIT_KEJADIAN_KEMATIANLABEL_KEWARGANEGARAAN, 
 wxID_EDIT_KEJADIAN_KEMATIANLABEL_KONTRASEPSI, 
 wxID_EDIT_KEJADIAN_KEMATIANLABEL_NAMA_AYAH, 
 wxID_EDIT_KEJADIAN_KEMATIANLABEL_NAMA_IBU, 
 wxID_EDIT_KEJADIAN_KEMATIANLABEL_NAMA_LENGKAP, 
 wxID_EDIT_KEJADIAN_KEMATIANLABEL_NOMOR_KK, 
 wxID_EDIT_KEJADIAN_KEMATIANLABEL_PEKERJAAN, 
 wxID_EDIT_KEJADIAN_KEMATIANLABEL_PEKERJAAN_LAINNYA, 
 wxID_EDIT_KEJADIAN_KEMATIANLABEL_PENDIDIKAN_TEMPUH, 
 wxID_EDIT_KEJADIAN_KEMATIANLABEL_PENDIDIKAN_TERAKHIR, 
 wxID_EDIT_KEJADIAN_KEMATIANLABEL_RESIKO_KEHAMILAN, 
 wxID_EDIT_KEJADIAN_KEMATIANLABEL_SHDK, 
 wxID_EDIT_KEJADIAN_KEMATIANLABEL_STATUS_KEPENDUDUKAN, 
 wxID_EDIT_KEJADIAN_KEMATIANLABEL_STATUS_PERKAWINAN, 
 wxID_EDIT_KEJADIAN_KEMATIANLABEL_STATUS_TINGGAL, 
 wxID_EDIT_KEJADIAN_KEMATIANLABEL_TANGGAL_LAHIR, 
 wxID_EDIT_KEJADIAN_KEMATIANLABEL_TEMPAT_LAHIR, 
 wxID_EDIT_KEJADIAN_KEMATIANLAPORAN, wxID_EDIT_KEJADIAN_KEMATIANLEBEL_NIK, 
 wxID_EDIT_KEJADIAN_KEMATIANNAMA_KK, wxID_EDIT_KEJADIAN_KEMATIANPILIHAN_AGAMA, 
 wxID_EDIT_KEJADIAN_KEMATIANPILIHAN_DIFABELITAS, 
 wxID_EDIT_KEJADIAN_KEMATIANPILIHAN_GOLONGAN_DARAH, 
 wxID_EDIT_KEJADIAN_KEMATIANPILIHAN_JENIS_KELAMIN, 
 wxID_EDIT_KEJADIAN_KEMATIANPILIHAN_KEHAMILAN, 
 wxID_EDIT_KEJADIAN_KEMATIANPILIHAN_KONTRASEPSI, 
 wxID_EDIT_KEJADIAN_KEMATIANPILIHAN_PEKERJAAN, 
 wxID_EDIT_KEJADIAN_KEMATIANPILIHAN_PEKERJAAN_LAINNYA, 
 wxID_EDIT_KEJADIAN_KEMATIANPILIHAN_PENDIDIKAN_DITEMPUH, 
 wxID_EDIT_KEJADIAN_KEMATIANPILIHAN_PENDIDIKAN_TERAKHIR, 
 wxID_EDIT_KEJADIAN_KEMATIANPILIHAN_SHDK, 
 wxID_EDIT_KEJADIAN_KEMATIANPILIHAN_STATUS, 
 wxID_EDIT_KEJADIAN_KEMATIANPILIHAN_STATUS_KEPENDUDUKAN, 
 wxID_EDIT_KEJADIAN_KEMATIANPILIHAN_STATUS_TINGGAL, 
 wxID_EDIT_KEJADIAN_KEMATIANPILIHAN_WARGANEGARA, 
 wxID_EDIT_KEJADIAN_KEMATIANSIMPANGAMBAR, 
 wxID_EDIT_KEJADIAN_KEMATIANSTATICTEXT1, 
 wxID_EDIT_KEJADIAN_KEMATIANSTATICTEXT2, 
 wxID_EDIT_KEJADIAN_KEMATIANSTATICTEXT3, 
 wxID_EDIT_KEJADIAN_KEMATIANSTATICTEXT4, 
 wxID_EDIT_KEJADIAN_KEMATIANSTATICTEXT5, 
 wxID_EDIT_KEJADIAN_KEMATIANSTATICTEXT6, 
 wxID_EDIT_KEJADIAN_KEMATIANSTATICTEXT7, 
 wxID_EDIT_KEJADIAN_KEMATIANTANGGALKEJADIAN, 
 wxID_EDIT_KEJADIAN_KEMATIANTANGGALKEMATIAN, 
 wxID_EDIT_KEJADIAN_KEMATIANTANGGAL_LAHIR, 
 wxID_EDIT_KEJADIAN_KEMATIANTGLKEJADIAN, 
 wxID_EDIT_KEJADIAN_KEMATIANTOMBOL_CARI, 
 wxID_EDIT_KEJADIAN_KEMATIANTOMBOL_TAMBAH_DATA, 
] = [wx.NewId() for _init_ctrls in range(73)]

class edit_kejadian_kematian(wx.Dialog):
    def _init_coll_isipenduduk_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT,
              heading='Nama Penduduk', width=150)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT,
              heading='Nomor KK', width=250)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT, heading='Alamat',
              width=260)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_LEFT, heading='Dusun',
              width=100)
        parent.InsertColumn(col=4, format=wx.LIST_FORMAT_LEFT, heading='RT',
              width=40)
        parent.InsertColumn(col=5, format=wx.LIST_FORMAT_LEFT, heading='RW',
              width=40)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_EDIT_KEJADIAN_KEMATIAN,
              name=u'edit_edit_kejadian_kematian', parent=prnt,
              pos=wx.Point(419, 99), size=wx.Size(896, 669),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Edit Kejadian Kematian')
        self.SetClientSize(wx.Size(888, 639))
        self.Center(wx.BOTH)
        self.SetBackgroundColour(wx.Colour(192, 192, 192))

        self.label_nomor_kk = wx.StaticText(id=wxID_EDIT_KEJADIAN_KEMATIANLABEL_NOMOR_KK,
              label=u'Nomor KK', name=u'label_nomor_kk', parent=self,
              pos=wx.Point(8, 152), size=wx.Size(168, 17),
              style=wx.TE_READONLY)

        self.label_alamat = wx.StaticText(id=wxID_EDIT_KEJADIAN_KEMATIANLABEL_ALAMAT,
              label=u'Alamat', name=u'label_alamat', parent=self,
              pos=wx.Point(256, 152), size=wx.Size(47, 17), style=0)

        self.label_dusun = wx.StaticText(id=wxID_EDIT_KEJADIAN_KEMATIANLABEL_DUSUN,
              label=u'Dusun', name=u'label_dusun', parent=self,
              pos=wx.Point(552, 152), size=wx.Size(144, 17), style=0)

        self.lebel_nik = wx.StaticText(id=wxID_EDIT_KEJADIAN_KEMATIANLEBEL_NIK,
              label=u'N I K *', name=u'lebel_nik', parent=self,
              pos=wx.Point(192, 192), size=wx.Size(40, 17), style=0)

        self.label_tempat_lahir = wx.StaticText(id=wxID_EDIT_KEJADIAN_KEMATIANLABEL_TEMPAT_LAHIR,
              label=u'Tempat Lahir', name=u'label_tempat_lahir', parent=self,
              pos=wx.Point(192, 312), size=wx.Size(176, 17), style=0)

        self.label_tanggal_lahir = wx.StaticText(id=wxID_EDIT_KEJADIAN_KEMATIANLABEL_TANGGAL_LAHIR,
              label=u'Tanggal Lahir', name=u'label_tanggal_lahir', parent=self,
              pos=wx.Point(192, 352), size=wx.Size(152, 17), style=0)

        self.label_golongan_darah = wx.StaticText(id=wxID_EDIT_KEJADIAN_KEMATIANLABEL_GOLONGAN_DARAH,
              label=u'Golongan Darah', name=u'label_golongan_darah',
              parent=self, pos=wx.Point(192, 392), size=wx.Size(200, 17),
              style=0)

        self.label_nama_lengkap = wx.StaticText(id=wxID_EDIT_KEJADIAN_KEMATIANLABEL_NAMA_LENGKAP,
              label=u'Nama Lengkap', name=u'label_nama_lengkap', parent=self,
              pos=wx.Point(192, 232), size=wx.Size(98, 17), style=0)

        self.label_jenis_kelamin = wx.StaticText(id=wxID_EDIT_KEJADIAN_KEMATIANLABEL_JENIS_KELAMIN,
              label=u'Jenis Kelamin', name=u'label_jenis_kelamin', parent=self,
              pos=wx.Point(192, 272), size=wx.Size(152, 17), style=0)

        self.label_agama = wx.StaticText(id=wxID_EDIT_KEJADIAN_KEMATIANLABEL_AGAMA,
              label=u'Agama', name=u'label_agama', parent=self,
              pos=wx.Point(400, 192), size=wx.Size(120, 17), style=0)

        self.input_no_kk = wx.TextCtrl(id=wxID_EDIT_KEJADIAN_KEMATIANINPUT_NO_KK,
              name=u'input_no_kk', parent=self, pos=wx.Point(8, 168),
              size=wx.Size(240, 25), style=wx.TE_READONLY, value=u'')

        self.input_alamat = wx.TextCtrl(id=wxID_EDIT_KEJADIAN_KEMATIANINPUT_ALAMAT,
              name=u'input_alamat', parent=self, pos=wx.Point(256, 168),
              size=wx.Size(288, 25), style=wx.TE_READONLY, value=u'')

        self.input_dusun = wx.TextCtrl(id=wxID_EDIT_KEJADIAN_KEMATIANINPUT_DUSUN,
              name=u'input_dusun', parent=self, pos=wx.Point(552, 168),
              size=wx.Size(192, 25), style=wx.TE_READONLY, value=u'')

        self.input_rt = wx.TextCtrl(id=wxID_EDIT_KEJADIAN_KEMATIANINPUT_RT,
              name=u'input_rt', parent=self, pos=wx.Point(752, 168),
              size=wx.Size(56, 27), style=wx.TE_READONLY, value=u'')

        self.input_rw = wx.TextCtrl(id=wxID_EDIT_KEJADIAN_KEMATIANINPUT_RW,
              name=u'input_rw', parent=self, pos=wx.Point(816, 168),
              size=wx.Size(56, 27), style=wx.TE_READONLY, value=u'')

        self.input_nik = wx.TextCtrl(id=wxID_EDIT_KEJADIAN_KEMATIANINPUT_NIK,
              name=u'input_nik', parent=self, pos=wx.Point(192, 208),
              size=wx.Size(200, 25), style=wx.TE_READONLY, value=u'')

        self.input_nama = wx.TextCtrl(id=wxID_EDIT_KEJADIAN_KEMATIANINPUT_NAMA,
              name=u'input_nama', parent=self, pos=wx.Point(192, 248),
              size=wx.Size(200, 25), style=wx.TE_READONLY, value=u'')

        self.pilihan_jenis_kelamin = wx.TextCtrl(id=wxID_EDIT_KEJADIAN_KEMATIANPILIHAN_JENIS_KELAMIN,
              name=u'pilihan_jenis_kelamin', parent=self, pos=wx.Point(192,
              288), size=wx.Size(200, 27), style=wx.TE_READONLY, value=u'')

        self.input_tempat_lahir = wx.TextCtrl(id=wxID_EDIT_KEJADIAN_KEMATIANINPUT_TEMPAT_LAHIR,
              name=u'input_tempat_lahir', parent=self, pos=wx.Point(192, 328),
              size=wx.Size(200, 25), style=wx.TE_READONLY, value=u'')

        self.tanggalkejadian = wx.TextCtrl(id=wxID_EDIT_KEJADIAN_KEMATIANTANGGALKEJADIAN,
              name=u'tanggalkejadian', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(176, 24), style=wx.TE_READONLY, value=u'')

        self.pilihan_golongan_darah = wx.TextCtrl(id=wxID_EDIT_KEJADIAN_KEMATIANPILIHAN_GOLONGAN_DARAH,
              name=u'pilihan_golongan_darah', parent=self, pos=wx.Point(192,
              408), size=wx.Size(80, 25), style=wx.TE_READONLY, value=u'')

        self.pilihan_agama = wx.TextCtrl(id=wxID_EDIT_KEJADIAN_KEMATIANPILIHAN_AGAMA,
              name=u'pilihan_agama', parent=self, pos=wx.Point(400, 208),
              size=wx.Size(216, 25), style=wx.TE_READONLY, value=u'')

        self.label_kewarganegaraan = wx.StaticText(id=wxID_EDIT_KEJADIAN_KEMATIANLABEL_KEWARGANEGARAAN,
              label=u'Kewarganegaraan', name=u'label_kewarganegaraan',
              parent=self, pos=wx.Point(400, 232), size=wx.Size(168, 17),
              style=0)

        self.pilihan_warganegara = wx.TextCtrl(name=u'pilihan_warganegara',
              parent=self, pos=wx.Point(400, 248), size=wx.Size(216, 25),
              style=wx.TE_READONLY, value=u'')

        self.label_pendidikan_terakhir = wx.StaticText(id=wxID_EDIT_KEJADIAN_KEMATIANLABEL_PENDIDIKAN_TERAKHIR,
              label=u'Pendidikan Terakhir', name=u'label_pendidikan_terakhir',
              parent=self, pos=wx.Point(400, 272), size=wx.Size(184, 17),
              style=0)

        self.pilihan_pendidikan_terakhir = wx.TextCtrl(id=wxID_EDIT_KEJADIAN_KEMATIANPILIHAN_PENDIDIKAN_TERAKHIR,
              name=u'pilihan_pendidikan_terakhir', parent=self,
              pos=wx.Point(400, 288), size=wx.Size(216, 25),
              style=wx.TE_READONLY, value=u'')

        self.label_pendidikan_tempuh = wx.StaticText(id=wxID_EDIT_KEJADIAN_KEMATIANLABEL_PENDIDIKAN_TEMPUH,
              label=u'Pendidikan Saat Ini Ditempuh',
              name=u'label_pendidikan_tempuh', parent=self, pos=wx.Point(400,
              312), size=wx.Size(264, 17), style=0)

        self.pilihan_pendidikan_ditempuh = wx.TextCtrl(id=wxID_EDIT_KEJADIAN_KEMATIANPILIHAN_PENDIDIKAN_DITEMPUH,
              name=u'pilihan_pendidikan_ditempuh', parent=self,
              pos=wx.Point(400, 328), size=wx.Size(216, 25),
              style=wx.TE_READONLY, value=u'')

        self.label_pekerjaan = wx.StaticText(id=wxID_EDIT_KEJADIAN_KEMATIANLABEL_PEKERJAAN,
              label=u'Pekerjaan Utama', name=u'label_pekerjaan', parent=self,
              pos=wx.Point(400, 352), size=wx.Size(200, 17), style=0)

        self.pilihan_pekerjaan = wx.TextCtrl(id=wxID_EDIT_KEJADIAN_KEMATIANPILIHAN_PEKERJAAN,
              name=u'pilihan_pekerjaan', parent=self, pos=wx.Point(400, 370),
              size=wx.Size(216, 25), style=wx.TE_READONLY, value=u'')

        self.label_pekerjaan_lainnya = wx.StaticText(id=wxID_EDIT_KEJADIAN_KEMATIANLABEL_PEKERJAAN_LAINNYA,
              label=u'Pekerjaan Lainnya', name=u'label_pekerjaan_lainnya',
              parent=self, pos=wx.Point(400, 392), size=wx.Size(168, 17),
              style=0)

        self.pilihan_pekerjaan_lainnya = wx.TextCtrl(id=wxID_EDIT_KEJADIAN_KEMATIANPILIHAN_PEKERJAAN_LAINNYA,
              name=u'pilihan_pekerjaan_lainnya', parent=self, pos=wx.Point(400,
              408), size=wx.Size(216, 25), style=wx.TE_READONLY, value=u'')

        self.label_status_perkawinan = wx.StaticText(id=wxID_EDIT_KEJADIAN_KEMATIANLABEL_STATUS_PERKAWINAN,
              label=u'Status Perkawinan', name=u'label_status_perkawinan',
              parent=self, pos=wx.Point(624, 192), size=wx.Size(176, 17),
              style=0)

        self.pilihan_status = wx.TextCtrl(id=wxID_EDIT_KEJADIAN_KEMATIANPILIHAN_STATUS,
              name=u'pilihan_status', parent=self, pos=wx.Point(624, 208),
              size=wx.Size(248, 25), style=wx.TE_READONLY, value=u'')

        self.label_status_kependudukan = wx.StaticText(id=wxID_EDIT_KEJADIAN_KEMATIANLABEL_STATUS_KEPENDUDUKAN,
              label=u'Status Kependudukan', name=u'label_status_kependudukan',
              parent=self, pos=wx.Point(624, 232), size=wx.Size(184, 17),
              style=0)

        self.pilihan_status_kependudukan = wx.TextCtrl(id=wxID_EDIT_KEJADIAN_KEMATIANPILIHAN_STATUS_KEPENDUDUKAN,
              name=u'pilihan_status_kependudukan', parent=self,
              pos=wx.Point(624, 248), size=wx.Size(248, 25),
              style=wx.TE_READONLY, value=u'')

        self.label_status_tinggal = wx.StaticText(id=wxID_EDIT_KEJADIAN_KEMATIANLABEL_STATUS_TINGGAL,
              label=u'Status Tinggal', name=u'label_status_tinggal',
              parent=self, pos=wx.Point(624, 272), size=wx.Size(152, 17),
              style=0)

        self.pilihan_status_tinggal = wx.TextCtrl(id=wxID_EDIT_KEJADIAN_KEMATIANPILIHAN_STATUS_TINGGAL,
              name=u'pilihan_status_tinggal', parent=self, pos=wx.Point(624,
              288), size=wx.Size(248, 25), style=wx.TE_READONLY, value=u'')

        self.label_difabelitas = wx.StaticText(id=wxID_EDIT_KEJADIAN_KEMATIANLABEL_DIFABELITAS,
              label=u'Penyandang Difabelitas', name=u'label_difabelitas',
              parent=self, pos=wx.Point(624, 312), size=wx.Size(184, 17),
              style=0)

        self.pilihan_difabelitas = wx.TextCtrl(id=wxID_EDIT_KEJADIAN_KEMATIANPILIHAN_DIFABELITAS,
              name=u'pilihan_difabelitas', parent=self, pos=wx.Point(624, 328),
              size=wx.Size(248, 25), style=wx.TE_READONLY, value=u'')

        self.label_kontrasepsi = wx.StaticText(id=wxID_EDIT_KEJADIAN_KEMATIANLABEL_KONTRASEPSI,
              label=u'Penggunaan Kontrasepsi', name=u'label_kontrasepsi',
              parent=self, pos=wx.Point(624, 352), size=wx.Size(192, 17),
              style=0)

        self.pilihan_kontrasepsi = wx.TextCtrl(id=wxID_EDIT_KEJADIAN_KEMATIANPILIHAN_KONTRASEPSI,
              name=u'pilihan_kontrasepsi', parent=self, pos=wx.Point(624, 368),
              size=wx.Size(248, 25), style=wx.TE_READONLY, value=u'')

        self.pilihan_kehamilan = wx.TextCtrl(id=wxID_EDIT_KEJADIAN_KEMATIANPILIHAN_KEHAMILAN,
              name=u'pilihan_kehamilan', parent=self, pos=wx.Point(624, 408),
              size=wx.Size(248, 25), style=wx.TE_READONLY, value=u'')

        self.laporan = wx.TextCtrl(id=wxID_EDIT_KEJADIAN_KEMATIANLAPORAN,
              name=u'laporan', parent=self, pos=wx.Point(136, 496),
              size=wx.Size(192, 27), style=0, value=u'')

        self.keterangan = wx.TextCtrl(id=wxID_EDIT_KEJADIAN_KEMATIANKETERANGAN,
              name=u'keterangan', parent=self, pos=wx.Point(416, 496),
              size=wx.Size(448, 27), style=0, value=u'')

        self.label_shdk = wx.StaticText(id=wxID_EDIT_KEJADIAN_KEMATIANLABEL_SHDK,
              label=u'Status Hubungan Dalam Keluarga', name=u'label_shdk',
              parent=self, pos=wx.Point(24, 536), size=wx.Size(320, 17),
              style=0)

        self.pilihan_shdk = wx.TextCtrl(id=wxID_EDIT_KEJADIAN_KEMATIANPILIHAN_SHDK,
              name=u'pilihan_shdk', parent=self, pos=wx.Point(24, 560),
              size=wx.Size(304, 25), style=wx.TE_READONLY, value=u'')

        self.label_nama_ayah = wx.StaticText(id=wxID_EDIT_KEJADIAN_KEMATIANLABEL_NAMA_AYAH,
              label=u'Nama Ayah', name=u'label_nama_ayah', parent=self,
              pos=wx.Point(344, 536), size=wx.Size(152, 17), style=0)

        self.input_ayah = wx.TextCtrl(id=wxID_EDIT_KEJADIAN_KEMATIANINPUT_AYAH,
              name=u'input_ayah', parent=self, pos=wx.Point(344, 560),
              size=wx.Size(280, 25), style=wx.TE_READONLY, value=u'')

        self.label_nama_ibu = wx.StaticText(id=wxID_EDIT_KEJADIAN_KEMATIANLABEL_NAMA_IBU,
              label=u'Nama Ibu', name=u'label_nama_ibu', parent=self,
              pos=wx.Point(632, 536), size=wx.Size(160, 17), style=0)

        self.input_ibu = wx.TextCtrl(id=wxID_EDIT_KEJADIAN_KEMATIANINPUT_IBU,
              name=u'input_ibu', parent=self, pos=wx.Point(632, 560),
              size=wx.Size(240, 25), style=wx.TE_READONLY, value=u'')

        self.label_resiko_kehamilan = wx.StaticText(id=wxID_EDIT_KEJADIAN_KEMATIANLABEL_RESIKO_KEHAMILAN,
              label=u'Resiko Kehamilan', name=u'label_resiko_kehamilan',
              parent=self, pos=wx.Point(624, 392), size=wx.Size(176, 17),
              style=0)

        self.tombol_tambah_data = wx.Button(id=wxID_EDIT_KEJADIAN_KEMATIANTOMBOL_TAMBAH_DATA,
              label=u'Tambah Data', name=u'tombol_tambah_data', parent=self,
              pos=wx.Point(240, 600), size=wx.Size(200, 32), style=0)
        self.tombol_tambah_data.Bind(wx.EVT_BUTTON,
              self.OnTombol_tambah_dataButton,
              id=wxID_EDIT_KEJADIAN_KEMATIANTOMBOL_TAMBAH_DATA)

        self.kembali = wx.Button(id=wxID_EDIT_KEJADIAN_KEMATIANKEMBALI,
              label=u'Kembali Ke Menu', name=u'kembali', parent=self,
              pos=wx.Point(456, 600), size=wx.Size(208, 32), style=0)
        self.kembali.Bind(wx.EVT_BUTTON, self.OnKembaliButton,
              id=wxID_EDIT_KEJADIAN_KEMATIANKEMBALI)

        self.dokumen = wx.StaticText(id=wxID_EDIT_KEJADIAN_KEMATIANDOKUMEN,
              label=u'Catatan Kejadian Kematian', name=u'dokumen', parent=self,
              pos=wx.Point(16, 440), size=wx.Size(304, 17), style=0)

        self.isipenduduk = wx.ListCtrl(id=wxID_EDIT_KEJADIAN_KEMATIANISIPENDUDUK,
              name=u'isipenduduk', parent=self, pos=wx.Point(16, 16),
              size=wx.Size(856, 104), style=wx.LC_REPORT)
        self._init_coll_isipenduduk_Columns(self.isipenduduk)
        self.isipenduduk.Bind(wx.EVT_LIST_ITEM_SELECTED,
              self.OnIsipendudukListItemSelected,
              id=wxID_EDIT_KEJADIAN_KEMATIANISIPENDUDUK)

        self.staticText1 = wx.StaticText(id=wxID_EDIT_KEJADIAN_KEMATIANSTATICTEXT1,
              label=u'Nama Lengkap', name='staticText1', parent=self,
              pos=wx.Point(400, 128), size=wx.Size(145, 17), style=0)

        self.cari_kk = wx.TextCtrl(id=wxID_EDIT_KEJADIAN_KEMATIANCARI_KK,
              name=u'cari_kk', parent=self, pos=wx.Point(552, 128),
              size=wx.Size(224, 24), style=0, value='')

        self.tombol_cari = wx.Button(id=wxID_EDIT_KEJADIAN_KEMATIANTOMBOL_CARI,
              label=u'Cari', name=u'tombol_cari', parent=self, pos=wx.Point(784,
              128), size=wx.Size(85, 24), style=0)
        self.tombol_cari.Bind(wx.EVT_BUTTON, self.OnTombol_cariButton,
              id=wxID_EDIT_KEJADIAN_KEMATIANTOMBOL_CARI)

        self.input_no = wx.TextCtrl(id=wxID_EDIT_KEJADIAN_KEMATIANINPUT_NO,
              name=u'input_no', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(56, 27), style=wx.TE_READONLY, value=u'')

        self.staticText2 = wx.StaticText(id=wxID_EDIT_KEJADIAN_KEMATIANSTATICTEXT2,
              label=u'RT', name='staticText2', parent=self, pos=wx.Point(760,
              152), size=wx.Size(24, 16), style=0)

        self.staticText3 = wx.StaticText(id=wxID_EDIT_KEJADIAN_KEMATIANSTATICTEXT3,
              label=u'RW', name='staticText3', parent=self, pos=wx.Point(824,
              152), size=wx.Size(19, 17), style=0)

        self.staticText4 = wx.StaticText(id=wxID_EDIT_KEJADIAN_KEMATIANSTATICTEXT4,
              label=u'Pemberi Laporan', name='staticText4', parent=self,
              pos=wx.Point(16, 504), size=wx.Size(118, 17), style=0)

        self.staticText5 = wx.StaticText(id=wxID_EDIT_KEJADIAN_KEMATIANSTATICTEXT5,
              label=u'Keterangan', name='staticText5', parent=self,
              pos=wx.Point(336, 504), size=wx.Size(74, 17), style=0)

        self.staticText6 = wx.StaticText(id=wxID_EDIT_KEJADIAN_KEMATIANSTATICTEXT6,
              label=u'Tanggal Kematian', name='staticText6', parent=self,
              pos=wx.Point(16, 464), size=wx.Size(106, 17), style=0)

        self.tglkejadian = wx.TextCtrl(id=wxID_EDIT_KEJADIAN_KEMATIANTGLKEJADIAN,
              name='tglkejadian', parent=self, pos=wx.Point(136, 464),
              size=wx.Size(192, 26), style=0)

        self.nama_kk = wx.TextCtrl(id=wxID_EDIT_KEJADIAN_KEMATIANNAMA_KK,
              name=u'nama_kk', parent=self, pos=wx.Point(8, 208),
              size=wx.Size(176, 24), style=wx.TE_READONLY, value=u'')

        self.staticText7 = wx.StaticText(id=wxID_EDIT_KEJADIAN_KEMATIANSTATICTEXT7,
              label=u'Nama Kepala Keluarga', name='staticText7', parent=self,
              pos=wx.Point(8, 192), size=wx.Size(135, 17), style=0)

        self.tanggalkematian = wx.TextCtrl(id=wxID_EDIT_KEJADIAN_KEMATIANTANGGALKEJADIAN,
              name=u'tanggalkejadian', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(176, 24), style=wx.TE_READONLY, value=u'')

        self.simpangambar = wx.TextCtrl(id=wxID_EDIT_KEJADIAN_KEMATIANSIMPANGAMBAR,
              name=u'simpangambar', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(152, 24), style=0, value=u'')

        self.tanggal_lahir = wx.TextCtrl(id=wxID_EDIT_KEJADIAN_KEMATIANTANGGAL_LAHIR,
              name=u'tanggal_lahir', parent=self, pos=wx.Point(192, 368),
              size=wx.Size(200, 27), style=0, value=u'')

        self.inputno = wx.TextCtrl(id=wxID_EDIT_KEJADIAN_KEMATIANINPUTNO,
              name=u'inputno', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(200, 27), style=0, value=u'')

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.awal()
    
    def awal(self):
        self.loadgambar()
        self.IsiList()
        self.input_no_kk.SetValue('')
        self.input_alamat.SetValue('')
        self.input_dusun.SetValue('')
        self.input_rt.SetValue('')
        self.input_rw.SetValue('')
        self.input_nik.SetValue('')
        self.input_nama.SetValue('')
        self.pilihan_jenis_kelamin.SetValue('')
        self.input_tempat_lahir.SetValue('')
        self.tanggal_lahir.SetValue('')
        self.pilihan_golongan_darah.SetValue('')
        self.pilihan_agama.SetValue('')
        self.pilihan_warganegara.SetValue('')
        self.pilihan_pendidikan_terakhir.SetValue('')
        self.pilihan_pendidikan_ditempuh.SetValue('')
        self.pilihan_pekerjaan.SetValue('')
        self.pilihan_pekerjaan_lainnya.SetValue('')
        self.pilihan_status.SetValue('')
        self.pilihan_status_kependudukan.SetValue('')
        self.pilihan_status_tinggal.SetValue('')
        self.pilihan_difabelitas.SetValue('')
        self.pilihan_kontrasepsi.SetValue('')
        self.pilihan_kehamilan.SetValue('')
        self.pilihan_shdk.SetValue('')
        self.input_ayah.SetValue('')
        self.input_ibu.SetValue('')
        self.laporan.SetValue('')
        self.keterangan.SetValue('')
        self.cari_kk.SetValue('')
        self.nama_kk.SetValue('')
        self.input_no.SetValue('')
            
                    
    def OnGetDate(self, event):
        selected = self.tglkejadian.GetValue()
        month = selected.Month + 1
        day = selected.Day
        year = selected.Year
        date_str = "%02d/%02d/%4d" % (month, day, year)
        self.tanggalkematian.SetValue("{}".format(date_str))
        
    def loadgambar(self):
        self.PhotoMaxSize = 130
        img = wx.EmptyImage(120,130)
        self.imageCtrl = wx.StaticBitmap(self, wx.ID_ANY, wx.BitmapFromImage(img),wx.Point(52, 251))

    def IsiList(self):
        self.isipenduduk.DeleteAllItems()    
        sql = "SELECT * FROM penduduk WHERE kematian='Ya'"
        cur.execute(sql) 
        hasil = cur.fetchall() 
        nokk = self.isipenduduk.GetItemCount() 
        for i in hasil : 
            self.isipenduduk.InsertStringItem(nokk, "%s"%i[1]) 
            self.isipenduduk.SetStringItem(nokk,1,"%s"%i[2]) 
            self.isipenduduk.SetStringItem(nokk,2,"%s"%i[21])
            self.isipenduduk.SetStringItem(nokk,3,"%s"%i[29])
            self.isipenduduk.SetStringItem(nokk,4,"%s"%i[26]) 
            self.isipenduduk.SetStringItem(nokk,5,"%s"%i[27])
            nokk = nokk + 1
    
    def Isi_Object(self) : 
        carikk=str(self.cari_kk.GetValue())
        sql="SELECT * FROM penduduk WHERE nik='%s'"%(carikk)
        cur.execute(sql)
        hasil = cur.fetchone()  
        if hasil : 
            self.input_no_kk.SetValue(str(hasil[16]))
            self.nama_kk.SetValue(str(hasil[17])) 
            self.input_alamat.SetValue(str(hasil[21]))
            self.input_dusun.SetValue(str(hasil[29]))
            self.input_rt.SetValue(str(hasil[26]))
            self.input_rw.SetValue(str(hasil[27]))
            self.input_nik.SetValue(str(hasil[1]))
            self.input_nama.SetValue(str(hasil[2]))
            self.pilihan_jenis_kelamin.SetValue(str(hasil[3]))
            self.input_tempat_lahir.SetValue(str(hasil[4]))
            self.tanggal_lahir.SetValue(str(hasil[5]))
            self.pilihan_golongan_darah.SetValue(str(hasil[7]))
            self.pilihan_agama.SetValue(str(hasil[8]))
            self.pilihan_warganegara.SetValue(str(hasil[28]))
            self.pilihan_pendidikan_terakhir.SetValue(str(hasil[12]))
            self.pilihan_pendidikan_ditempuh.SetValue(str(hasil[31]))
            self.pilihan_pekerjaan.SetValue(str(hasil[13]))
            self.pilihan_pekerjaan_lainnya.SetValue(str(hasil[19]))
            self.pilihan_status.SetValue(str(hasil[9]))
            self.pilihan_status_kependudukan.SetValue(str(hasil[32]))
            self.pilihan_status_tinggal.SetValue(str(hasil[33]))
            self.pilihan_difabelitas.SetValue(str(hasil[34]))
            self.pilihan_kontrasepsi.SetValue(str(hasil[35]))
            self.pilihan_kehamilan.SetValue(str(hasil[36]))
            self.pilihan_shdk.SetValue(str(hasil[10]))
            self.input_ayah.SetValue(str(hasil[15]))
            self.input_ibu.SetValue(str(hasil[14]))
            self.simpangambar.SetValue(str(hasil[57]))
            self.input_no.SetValue(str(hasil[0]))
            self.viewgambar()
        else : 
            self.pesan = wx.MessageDialog(self,"Data Tidak Ada","Konfirmasi",wx.OK) 
            self.pesan.ShowModal() 
            self.cari_kk.Clear()
            self.cari_kk.SetFocus()
     
    def Isi_Object2(self) :   
        carikk=str(self.cari_kk.GetValue())
        sql="SELECT * FROM peristiwakematian WHERE nomornik='%s'"%(carikk)
        cur.execute(sql)
        ada = cur.fetchone() 
        if ada:
            self.laporan.SetValue(str(ada[5]))
            self.keterangan.SetValue(str(ada[6]))
            self.tglkejadian.SetValue(str(ada[1]))
            self.inputno.SetValue(str(ada[0]))
        else : 
            self.pesan = wx.MessageDialog(self,"Data Tidak Ada","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()    
            
    def viewgambar(self):
        filepath=self.simpangambar.GetValue()
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
   
    def OnTombol_kembali_kemenuButton(self, event):
        self.main=data_penduduk.create(None)
        self.main.Show()
        self.Close()
        self.Destroy()

    def OnTombol_tambah_dataButton(self, event):
    
        nokk = str(self.input_no_kk.GetValue())
        nik = str(self.input_nik.GetValue())
        nama = str(self.input_nama.GetValue())
        mati = str(self.tanggalkematian.GetValue())
        laporan = str(self.laporan.GetValue())
        keterangan = str(self.keterangan.GetValue())
        inputno = str(self.input_no.GetValue())
                
        if laporan == '':
            self.pesan = wx.MessageDialog(self,"Nama Pelapor Jangan Kosong","Peringatan",wx.OK) 
            self.pesan.ShowModal()
        elif keterangan == '':
            self.pesan = wx.MessageDialog(self,"Keterangan Kematian Jangan Kosong","Peringatan",wx.OK) 
            self.pesan.ShowModal()    
            
        else:
            add_keluarga="UPDATE penduduk SET kematian='Ya' WHERE no='"+inputno+"'"        
            cur.execute(add_keluarga)
            db.commit()
            add_kejadian="INSERT INTO peristiwakematian (tanggalkematian, namalengkap, nomornik, nomorkk, yangmenyatakan, keterangan)  VALUES('"+(mati)+"','"+(nama)+"','"+(nik)+"','"+(nokk)+"','"+(laporan)+"','"+(keterangan)+"') "
            cur.execute(add_kejadian)
            db.commit()
            self.pesan = wx.MessageDialog(self,"Data Sudah Tersimpan","Konfirmasi",wx.OK) 
            self.pesan.ShowModal() 
            self.awal()

   
    def OnKembaliButton(self, event):

        self.Close()
        self.Destroy()

    def OnTombol_cariButton(self, event):
        self.Isi_Object()
   
    def OnIsipendudukListItemSelected(self, event):
        self.currentItem = event.m_itemIndex # mengambil no index baris yang dipilih 
        b=self.isipenduduk.GetItem(self.currentItem).GetText() # no index baris dikonversi ke text/ string 
        self.cari_kk.SetValue(b) 
        self.Isi_Object()
        self.Isi_Object2()
        event.Skip()
