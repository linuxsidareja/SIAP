#Boa:Frame:kk_sementara
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
import shutil


db = sqlite3.connect('siap.db')
cur = db.cursor()

def create(parent):
    return kk_sementara(parent)

[wxID_KK_SEMENTARA, wxID_KK_SEMENTARABUTTON1, wxID_KK_SEMENTARADESA, 
 wxID_KK_SEMENTARADOKUMEN, wxID_KK_SEMENTARADOKUMEN1, 
 wxID_KK_SEMENTARADOKUMEN2, wxID_KK_SEMENTARADOKUMEN3, 
 wxID_KK_SEMENTARADOKUMEN4, wxID_KK_SEMENTARADOKUMEN5, 
 wxID_KK_SEMENTARADOKUMEN6, wxID_KK_SEMENTARADOKUMEN7, 
 wxID_KK_SEMENTARADOKUMEN8, wxID_KK_SEMENTARAGAMBAR, 
 wxID_KK_SEMENTARAINPUT_ALAMAT, wxID_KK_SEMENTARAINPUT_AYAH, 
 wxID_KK_SEMENTARAINPUT_DUSUN, wxID_KK_SEMENTARAINPUT_IBU, 
 wxID_KK_SEMENTARAINPUT_NAMA, wxID_KK_SEMENTARAINPUT_NIK, 
 wxID_KK_SEMENTARAINPUT_NO_KK, wxID_KK_SEMENTARAINPUT_RT, 
 wxID_KK_SEMENTARAINPUT_RW, wxID_KK_SEMENTARAINPUT_TEMPAT_LAHIR, 
 wxID_KK_SEMENTARAISIPENDUDUK, wxID_KK_SEMENTARAKABUPATEN, 
 wxID_KK_SEMENTARAKECAMATAN, wxID_KK_SEMENTARAKEMBALI, 
 wxID_KK_SEMENTARALABEL_AGAMA, wxID_KK_SEMENTARALABEL_ALAMAT, 
 wxID_KK_SEMENTARALABEL_DIFABELITAS, wxID_KK_SEMENTARALABEL_DUSUN, 
 wxID_KK_SEMENTARALABEL_GOLONGAN_DARAH, wxID_KK_SEMENTARALABEL_JENIS_KELAMIN, 
 wxID_KK_SEMENTARALABEL_KEWARGANEGARAAN, wxID_KK_SEMENTARALABEL_KONTRASEPSI, 
 wxID_KK_SEMENTARALABEL_NAMA_AYAH, wxID_KK_SEMENTARALABEL_NAMA_IBU, 
 wxID_KK_SEMENTARALABEL_NAMA_LENGKAP, wxID_KK_SEMENTARALABEL_NOMOR_KK, 
 wxID_KK_SEMENTARALABEL_PEKERJAAN, wxID_KK_SEMENTARALABEL_PEKERJAAN_LAINNYA, 
 wxID_KK_SEMENTARALABEL_PENDIDIKAN_TEMPUH, 
 wxID_KK_SEMENTARALABEL_PENDIDIKAN_TERAKHIR, 
 wxID_KK_SEMENTARALABEL_STATUS_KEPENDUDUKAN, 
 wxID_KK_SEMENTARALABEL_STATUS_PERKAWINAN, 
 wxID_KK_SEMENTARALABEL_STATUS_TINGGAL, wxID_KK_SEMENTARALABEL_TANGGAL_LAHIR, 
 wxID_KK_SEMENTARALABEL_TEMPAT_LAHIR, wxID_KK_SEMENTARALEBEL_NIK, 
 wxID_KK_SEMENTARAPILIHAN_AGAMA, wxID_KK_SEMENTARAPILIHAN_DIFABELITAS, 
 wxID_KK_SEMENTARAPILIHAN_GOLONGAN_DARAH, 
 wxID_KK_SEMENTARAPILIHAN_JENIS_KELAMIN, wxID_KK_SEMENTARAPILIHAN_KEHAMILAN, 
 wxID_KK_SEMENTARAPILIHAN_KONTRASEPSI, wxID_KK_SEMENTARAPILIHAN_PEKERJAAN, 
 wxID_KK_SEMENTARAPILIHAN_PEKERJAAN_LAINNYA, 
 wxID_KK_SEMENTARAPILIHAN_PENDIDIKAN_DITEMPUH, 
 wxID_KK_SEMENTARAPILIHAN_PENDIDIKAN_TERAKHIR, wxID_KK_SEMENTARAPILIHAN_SHDK, 
 wxID_KK_SEMENTARAPILIHAN_STATUS, 
 wxID_KK_SEMENTARAPILIHAN_STATUS_KEPENDUDUKAN, 
 wxID_KK_SEMENTARAPILIHAN_STATUS_TINGGAL, 
 wxID_KK_SEMENTARAPILIHAN_WARGANEGARA, wxID_KK_SEMENTARAPROPINSI, 
 wxID_KK_SEMENTARASIMPANGAMBAR, wxID_KK_SEMENTARASTATICTEXT2, 
 wxID_KK_SEMENTARASTATICTEXT3, wxID_KK_SEMENTARATANGGAL_LAHIR, 
 wxID_KK_SEMENTARATGLLAHIR, wxID_KK_SEMENTARATOMBOL_TAMBAH_DATA, 
] = [wx.NewId() for _init_ctrls in range(71)]

class kk_sementara(wx.Dialog):
    def _init_coll_isipenduduk_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT,
              heading='Nomor KK', width=150)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT,
              heading='Nama Kepala Keluarga', width=250)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT, heading='Alamat',
              width=230)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_LEFT, heading='Dusun',
              width=120)
        parent.InsertColumn(col=4, format=wx.LIST_FORMAT_LEFT, heading='RT',
              width=40)
        parent.InsertColumn(col=5, format=wx.LIST_FORMAT_LEFT, heading='RW',
              width=40)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_KK_SEMENTARA, name=u'kk_sementara',
              parent=prnt, pos=wx.Point(424, 114), size=wx.Size(888, 654),
              style=wx.DEFAULT_FRAME_STYLE,
              title=u'Tambah Kartu Keluarga Sementara')
        self.SetClientSize(wx.Size(880, 624))
        self.Center(wx.BOTH)
        self.SetHelpText(u'Masukan Nomor KK')
        self.SetBackgroundColour(wx.Colour(192, 192, 192))

        self.isipenduduk = wx.ListCtrl(id=wxID_KK_SEMENTARAISIPENDUDUK,
              name=u'isipenduduk', parent=self, pos=wx.Point(8, 8),
              size=wx.Size(864, 176), style=wx.LC_REPORT)
        self._init_coll_isipenduduk_Columns(self.isipenduduk)

        self.label_nomor_kk = wx.StaticText(id=wxID_KK_SEMENTARALABEL_NOMOR_KK,
              label=u'Nomor KK', name=u'label_nomor_kk', parent=self,
              pos=wx.Point(8, 192), size=wx.Size(80, 14), style=0)

        self.label_alamat = wx.StaticText(id=wxID_KK_SEMENTARALABEL_ALAMAT,
              label=u'Alamat', name=u'label_alamat', parent=self,
              pos=wx.Point(256, 189), size=wx.Size(47, 15), style=0)

        self.label_dusun = wx.StaticText(id=wxID_KK_SEMENTARALABEL_DUSUN,
              label=u'Dusun', name=u'label_dusun', parent=self,
              pos=wx.Point(552, 190), size=wx.Size(144, 13), style=0)

        self.lebel_nik = wx.StaticText(id=wxID_KK_SEMENTARALEBEL_NIK,
              label=u'N I K *', name=u'lebel_nik', parent=self,
              pos=wx.Point(192, 231), size=wx.Size(40, 17), style=0)

        self.label_nama_lengkap = wx.StaticText(id=wxID_KK_SEMENTARALABEL_NAMA_LENGKAP,
              label=u'Nama Lengkap', name=u'label_nama_lengkap', parent=self,
              pos=wx.Point(192, 271), size=wx.Size(98, 17), style=0)

        self.label_jenis_kelamin = wx.StaticText(id=wxID_KK_SEMENTARALABEL_JENIS_KELAMIN,
              label=u'Jenis Kelamin', name=u'label_jenis_kelamin', parent=self,
              pos=wx.Point(192, 311), size=wx.Size(152, 17), style=0)

        self.label_tempat_lahir = wx.StaticText(id=wxID_KK_SEMENTARALABEL_TEMPAT_LAHIR,
              label=u'Tempat Lahir', name=u'label_tempat_lahir', parent=self,
              pos=wx.Point(192, 351), size=wx.Size(176, 17), style=0)

        self.label_tanggal_lahir = wx.StaticText(id=wxID_KK_SEMENTARALABEL_TANGGAL_LAHIR,
              label=u'Tanggal Lahir', name=u'label_tanggal_lahir', parent=self,
              pos=wx.Point(192, 391), size=wx.Size(152, 17), style=0)

        self.label_golongan_darah = wx.StaticText(id=wxID_KK_SEMENTARALABEL_GOLONGAN_DARAH,
              label=u'Golongan Darah', name=u'label_golongan_darah',
              parent=self, pos=wx.Point(192, 431), size=wx.Size(200, 17),
              style=0)

        self.label_agama = wx.StaticText(id=wxID_KK_SEMENTARALABEL_AGAMA,
              label=u'Agama', name=u'label_agama', parent=self,
              pos=wx.Point(400, 231), size=wx.Size(120, 17), style=0)

        self.label_kewarganegaraan = wx.StaticText(id=wxID_KK_SEMENTARALABEL_KEWARGANEGARAAN,
              label=u'Kewarganegaraan', name=u'label_kewarganegaraan',
              parent=self, pos=wx.Point(400, 271), size=wx.Size(168, 17),
              style=0)

        self.label_pendidikan_terakhir = wx.StaticText(id=wxID_KK_SEMENTARALABEL_PENDIDIKAN_TERAKHIR,
              label=u'Pendidikan Terakhir', name=u'label_pendidikan_terakhir',
              parent=self, pos=wx.Point(400, 311), size=wx.Size(184, 17),
              style=0)

        self.label_pendidikan_tempuh = wx.StaticText(id=wxID_KK_SEMENTARALABEL_PENDIDIKAN_TEMPUH,
              label=u'Pendidikan Saat Ini Ditempuh',
              name=u'label_pendidikan_tempuh', parent=self, pos=wx.Point(400,
              351), size=wx.Size(168, 17), style=0)

        self.label_pekerjaan_lainnya = wx.StaticText(id=wxID_KK_SEMENTARALABEL_PEKERJAAN_LAINNYA,
              label=u'Pekerjaan Lainnya', name=u'label_pekerjaan_lainnya',
              parent=self, pos=wx.Point(400, 431), size=wx.Size(168, 17),
              style=0)

        self.label_status_tinggal = wx.StaticText(id=wxID_KK_SEMENTARALABEL_STATUS_TINGGAL,
              label=u'Status Tinggal', name=u'label_status_tinggal',
              parent=self, pos=wx.Point(624, 310), size=wx.Size(152, 13),
              style=0)

        self.label_pekerjaan = wx.StaticText(id=wxID_KK_SEMENTARALABEL_PEKERJAAN,
              label=u'Pekerjaan Utama', name=u'label_pekerjaan', parent=self,
              pos=wx.Point(400, 391), size=wx.Size(200, 17), style=0)

        self.label_difabelitas = wx.StaticText(id=wxID_KK_SEMENTARALABEL_DIFABELITAS,
              label=u'Penyandang Difabelitas', name=u'label_difabelitas',
              parent=self, pos=wx.Point(624, 352), size=wx.Size(184, 13),
              style=0)

        self.label_status_perkawinan = wx.StaticText(id=wxID_KK_SEMENTARALABEL_STATUS_PERKAWINAN,
              label=u'Status Perkawinan', name=u'label_status_perkawinan',
              parent=self, pos=wx.Point(624, 231), size=wx.Size(176, 17),
              style=0)

        self.input_no_kk = wx.TextCtrl(id=wxID_KK_SEMENTARAINPUT_NO_KK,
              name=u'input_no_kk', parent=self, pos=wx.Point(8, 207),
              size=wx.Size(240, 21), style=0, value=u'')

        self.input_alamat = wx.TextCtrl(id=wxID_KK_SEMENTARAINPUT_ALAMAT,
              name=u'input_alamat', parent=self, pos=wx.Point(256, 207),
              size=wx.Size(288, 21), style=0, value=u'')

        self.input_dusun = wx.TextCtrl(id=wxID_KK_SEMENTARAINPUT_DUSUN,
              name=u'input_dusun', parent=self, pos=wx.Point(552, 207),
              size=wx.Size(192, 21), style=0, value=u'')

        self.input_rt = wx.TextCtrl(id=wxID_KK_SEMENTARAINPUT_RT,
              name=u'input_rt', parent=self, pos=wx.Point(752, 207),
              size=wx.Size(56, 21), style=0, value=u'')

        self.input_rw = wx.TextCtrl(id=wxID_KK_SEMENTARAINPUT_RW,
              name=u'input_rw', parent=self, pos=wx.Point(816, 207),
              size=wx.Size(56, 21), style=0, value=u'')

        self.input_nik = wx.TextCtrl(id=wxID_KK_SEMENTARAINPUT_NIK,
              name=u'input_nik', parent=self, pos=wx.Point(192, 247),
              size=wx.Size(200, 21), style=0, value=u'')

        self.input_nama = wx.TextCtrl(id=wxID_KK_SEMENTARAINPUT_NAMA,
              name=u'input_nama', parent=self, pos=wx.Point(192, 287),
              size=wx.Size(200, 25), style=0, value=u'')

        self.pilihan_jenis_kelamin = wx.ComboBox(choices=['L', 'P'],
              id=wxID_KK_SEMENTARAPILIHAN_JENIS_KELAMIN,
              name=u'pilihan_jenis_kelamin', parent=self, pos=wx.Point(192,
              327), size=wx.Size(200, 21), style=0)

        self.input_tempat_lahir = wx.TextCtrl(id=wxID_KK_SEMENTARAINPUT_TEMPAT_LAHIR,
              name=u'input_tempat_lahir', parent=self, pos=wx.Point(192, 367),
              size=wx.Size(200, 21), style=0, value=u'')

        self.tanggal_lahir = wx.DatePickerCtrl(id=wxID_KK_SEMENTARATANGGAL_LAHIR,
              name=u'tanggal_lahir', parent=self, pos=wx.Point(192, 407),
              size=wx.Size(200, 26), style=wx.DP_DROPDOWN|wx.DP_SHOWCENTURY)
        self.tanggal_lahir.Bind(wx.EVT_DATE_CHANGED, self.OnGetDate)

        self.pilihan_golongan_darah = wx.ComboBox(choices=['A', 'AB', 'B', 'O',
              'A+', 'A-', 'AB+', 'AB-', 'B+', 'B-', 'O+', 'O-', 'Tidak tahu'],
              id=wxID_KK_SEMENTARAPILIHAN_GOLONGAN_DARAH,
              name=u'pilihan_golongan_darah', parent=self, pos=wx.Point(192,
              447), size=wx.Size(80, 21), style=0)

        self.pilihan_agama = wx.ComboBox(choices=['Islam', 'Kristen Protestan',
              'Kristen Katolik', 'Hindu', 'Budha', 'Konghuchu',
              'Aliran Kepercayaan', 'Agama Lainnya'],
              id=wxID_KK_SEMENTARAPILIHAN_AGAMA, name=u'pilihan_agama',
              parent=self, pos=wx.Point(400, 247), size=wx.Size(216, 21),
              style=0)

        self.pilihan_warganegara = wx.ComboBox(choices=['WNI', 'WNA'],
              id=wxID_KK_SEMENTARAPILIHAN_WARGANEGARA,
              name=u'pilihan_warganegara', parent=self, pos=wx.Point(400, 287),
              size=wx.Size(216, 21), style=0)

        self.pilihan_pendidikan_terakhir = wx.ComboBox(choices=['Tidak/Belum Sekolah',
              'Tidak Tamat SD/Sederajat', 'Tamat SD/Sederajat',
              'SLTP/Sederajat', 'SLTA/Sederajat', 'Diploma I/II',
              'Akademi/Diploma III/S. Muda', 'Diploma IV/Strata I', 'Strata II',
              'Strata III', 'Pendidikan Non Formal'],
              id=wxID_KK_SEMENTARAPILIHAN_PENDIDIKAN_TERAKHIR,
              name=u'pilihan_pendidikan_terakhir', parent=self,
              pos=wx.Point(400, 327), size=wx.Size(216, 21), style=0)

        self.pilihan_pendidikan_ditempuh = wx.ComboBox(choices=['PAUD sederajat',
              'TK Sederajat', 'SD Sederajat', 'SLTP Sederajat',
              'SLTA Sederajat', 'D1 Sederajat', 'D2 Sederajat', 'D3 Sederajat' ,
              'S1 Sederajat' , 'S2 Sederajat' , 'S3 Sederajat' ,
              'Pendidikan Non Formal'],
              id=wxID_KK_SEMENTARAPILIHAN_PENDIDIKAN_DITEMPUH,
              name=u'pilihan_pendidikan_ditempuh', parent=self,
              pos=wx.Point(400, 367), size=wx.Size(216, 21), style=0)

        self.pilihan_pekerjaan = wx.ComboBox(choices=['Belum/Tidak Bekerja',
              'Mengurus Rumah Tangga', 'Pelajar/Mahasiswa', 'Pensiunan',
              'Pegawai Negeri Sipil', 'Tentara Nasional Indonesia',
              'Kepolisian RI', 'Perdagangan', 'Petani/Pekebun', 'Peternak',
              'Nelayan/Perikanan', 'Industri', 'Konstruksi', 'Transportasi',
              'Karyawan Swasta', 'Karyawan BUMN', 'Karyawan BUMD',
              'Karyawan Honorer', 'Buruh Harian Lepas', 'Buruh Tani/Perkebunan',
              'Buruh Nelayan/Perikanan', 'Buruh Peternakan',
              'Pembantu Rumah Tangga', 'Tukang Cukur', 'Tukang Listrik',
              'Tukang Batu', 'Tukang Kayu', 'Tukang Sol Sepatu',
              'Tukang Las/Pandai Besi', 'Tukang Jahit', 'Penata Rambut',
              'Penata Rias', 'Penata Busana', 'Mekanik', 'Tukang Gigi',
              'Seniman', 'Tabib', 'Paraji', 'Perancang Busana', 'Penterjemah',
              'Imam Masjid', 'Pendeta', 'Pastur', 'Wartawan', 'Ustadz/Mubaligh',
              'Juru Masak', 'Promotor Acara', 'Anggota DPR-RI', 'Anggota DPD',
              'Anggota BPK', 'Presiden', 'Wakil Presiden',
              'Anggota Mahkamah Konstitusi', 'Anggota Kabinet/Kementerian',
              'Duta Besar', 'Gubernur', 'Wakil Gubernur', 'Bupati',
              'Wakil Bupati', 'Walikota', 'Wakil Walikota',
              'Anggota DPRD Propinsi', 'Anggota DPRD Kabupaten/Kota', 'Dosen',
              'Guru', 'Pilot', 'Pengacara', 'Notaris', 'Arsitek', 'Akuntan',
              'Konsultan', 'Dokter', 'Bidan', 'Perawat', 'Apoteker',
              'Psikiater/Psikolog', 'Penyiar Televisi', 'Penyiar Radio',
              'Pelaut', 'Peneliti', 'Sopir', 'Pialang', 'Paranormal',
              'Pedagang', 'Perangkat Desa', 'Kepala Desa', 'Biarawati',
              'Wiraswasta', 'Buruh Migran'],
              id=wxID_KK_SEMENTARAPILIHAN_PEKERJAAN, name=u'pilihan_pekerjaan',
              parent=self, pos=wx.Point(400, 409), size=wx.Size(216, 21),
              style=0)

        self.pilihan_pekerjaan_lainnya = wx.ComboBox(choices=['Berdagang',
              'Bertani', 'Berkebun', 'Jasa  profesional  tukang', 'Seniman',
              'Lainnya'], id=wxID_KK_SEMENTARAPILIHAN_PEKERJAAN_LAINNYA,
              name=u'pilihan_pekerjaan_lainnya', parent=self, pos=wx.Point(400,
              447), size=wx.Size(216, 21), style=0)

        self.pilihan_status = wx.ComboBox(choices=['Belum Kawin', 'Kawin',
              'Cerai Mati', 'Cerai Hidup'], id=wxID_KK_SEMENTARAPILIHAN_STATUS,
              name=u'pilihan_status', parent=self, pos=wx.Point(624, 247),
              size=wx.Size(248, 21), style=0)

        self.label_status_kependudukan = wx.StaticText(id=wxID_KK_SEMENTARALABEL_STATUS_KEPENDUDUKAN,
              label=u'Status Kependudukan', name=u'label_status_kependudukan',
              parent=self, pos=wx.Point(624, 271), size=wx.Size(184, 17),
              style=0)

        self.pilihan_status_kependudukan = wx.ComboBox(choices=['Penduduk Tetap',
              'Penduduk Sementara', 'Penduduk Pindah/Pindahan'],
              id=wxID_KK_SEMENTARAPILIHAN_STATUS_KEPENDUDUKAN,
              name=u'pilihan_status_kependudukan', parent=self,
              pos=wx.Point(624, 287), size=wx.Size(248, 21), style=0)

        self.pilihan_status_tinggal = wx.ComboBox(choices=['Tinggal Tetap',
              'Tinggal Di Luar Desa*', 'Tinggal Di Luar Kota/Kabupaten',
              'Tinggal Di Luar Propinsi', 'Tinggal Di Luar Negeri'],
              id=wxID_KK_SEMENTARAPILIHAN_STATUS_TINGGAL,
              name=u'pilihan_status_tinggal', parent=self, pos=wx.Point(624,
              327), size=wx.Size(248, 21), style=0)

        self.pilihan_difabelitas = wx.ComboBox(choices=['Tidak Cacat',
              'Cacat Fisik', 'Cacat Netra/Buta', 'Cacat Rungu/Wicara',
              'Cacat Mental/Jiwa', 'Cacat Fisik/Mental', 'Cacat Lainnya'],
              id=wxID_KK_SEMENTARAPILIHAN_DIFABELITAS,
              name=u'pilihan_difabelitas', parent=self, pos=wx.Point(624, 368),
              size=wx.Size(248, 21), style=0)

        self.label_kontrasepsi = wx.StaticText(id=wxID_KK_SEMENTARALABEL_KONTRASEPSI,
              label=u'Penggunaan Kontrasepsi', name=u'label_kontrasepsi',
              parent=self, pos=wx.Point(624, 391), size=wx.Size(192, 17),
              style=0)

        self.pilihan_kontrasepsi = wx.ComboBox(choices=['Pil', 'Suntik', 'IUD',
              'Kondom', 'Implant', 'MOP'],
              id=wxID_KK_SEMENTARAPILIHAN_KONTRASEPSI,
              name=u'pilihan_kontrasepsi', parent=self, pos=wx.Point(624, 407),
              size=wx.Size(248, 21), style=0)

        self.pilihan_kehamilan = wx.ComboBox(choices=['Resiko Tinggi',
              'Tidak Resiko Tinggi'], id=wxID_KK_SEMENTARAPILIHAN_KEHAMILAN,
              name=u'pilihan_kehamilan', parent=self, pos=wx.Point(624, 447),
              size=wx.Size(248, 21), style=0)

        self.dokumen = wx.StaticText(id=wxID_KK_SEMENTARADOKUMEN,
              label=u'Kepemilikan Dokumen', name=u'dokumen', parent=self,
              pos=wx.Point(24, 479), size=wx.Size(304, 12), style=0)

        self.staticText2 = wx.StaticText(id=wxID_KK_SEMENTARASTATICTEXT2,
              label=u'RT', name='staticText2', parent=self, pos=wx.Point(760,
              191), size=wx.Size(24, 16), style=0)

        self.staticText3 = wx.StaticText(id=wxID_KK_SEMENTARASTATICTEXT3,
              label=u'RW', name='staticText3', parent=self, pos=wx.Point(824,
              191), size=wx.Size(19, 17), style=0)

        self.dokumen1 = wx.ComboBox(choices=['Akta Kelahiran'],
              id=wxID_KK_SEMENTARADOKUMEN1, name=u'dokumen1', parent=self,
              pos=wx.Point(24, 497), size=wx.Size(187, 21), style=0, value='')

        self.dokumen2 = wx.ComboBox(choices=['Akta Nikah'],
              id=wxID_KK_SEMENTARADOKUMEN2, name=u'dokumen2', parent=self,
              pos=wx.Point(24, 521), size=wx.Size(187, 21), style=0, value='')

        self.dokumen3 = wx.ComboBox(choices=['Akta Cerai'],
              id=wxID_KK_SEMENTARADOKUMEN3, name=u'dokumen3', parent=self,
              pos=wx.Point(241, 497), size=wx.Size(187, 21), style=0, value='')

        self.dokumen4 = wx.ComboBox(choices=['Akta Kematian'],
              id=wxID_KK_SEMENTARADOKUMEN4, name=u'dokumen4', parent=self,
              pos=wx.Point(241, 521), size=wx.Size(187, 21), style=0, value='')

        self.dokumen5 = wx.ComboBox(choices=['KTP Sementara'],
              id=wxID_KK_SEMENTARADOKUMEN5, name=u'dokumen5', parent=self,
              pos=wx.Point(464, 497), size=wx.Size(187, 21), style=0, value='')

        self.dokumen6 = wx.ComboBox(choices=['KITAS'],
              id=wxID_KK_SEMENTARADOKUMEN6, name=u'dokumen6', parent=self,
              pos=wx.Point(464, 521), size=wx.Size(187, 21), style=0, value='')

        self.dokumen7 = wx.ComboBox(choices=['VISA'],
              id=wxID_KK_SEMENTARADOKUMEN7, name=u'dokumen7', parent=self,
              pos=wx.Point(684, 497), size=wx.Size(187, 21), style=0, value='')

        self.dokumen8 = wx.ComboBox(choices=['Paspor'],
              id=wxID_KK_SEMENTARADOKUMEN8, name=u'dokumen8', parent=self,
              pos=wx.Point(684, 521), size=wx.Size(187, 21), style=0, value='')

        self.pilihan_shdk = wx.TextCtrl(id=wxID_KK_SEMENTARAPILIHAN_SHDK,
              name=u'pilihan_shdk', parent=self, pos=wx.Point(24, 560),
              size=wx.Size(304, 21), style=wx.TE_READONLY,
              value=u'Kepala Keluarga')

        self.label_nama_ayah = wx.StaticText(id=wxID_KK_SEMENTARALABEL_NAMA_AYAH,
              label=u'Nama Ayah', name=u'label_nama_ayah', parent=self,
              pos=wx.Point(344, 544), size=wx.Size(152, 13), style=0)

        self.input_ayah = wx.TextCtrl(id=wxID_KK_SEMENTARAINPUT_AYAH,
              name=u'input_ayah', parent=self, pos=wx.Point(344, 560),
              size=wx.Size(280, 21), style=0, value=u'')

        self.label_nama_ibu = wx.StaticText(id=wxID_KK_SEMENTARALABEL_NAMA_IBU,
              label=u'Nama Ibu', name=u'label_nama_ibu', parent=self,
              pos=wx.Point(632, 544), size=wx.Size(160, 14), style=0)

        self.input_ibu = wx.TextCtrl(id=wxID_KK_SEMENTARAINPUT_IBU,
              name=u'input_ibu', parent=self, pos=wx.Point(632, 560),
              size=wx.Size(240, 21), style=0, value=u'')

        self.tombol_tambah_data = wx.Button(id=wxID_KK_SEMENTARATOMBOL_TAMBAH_DATA,
              label=u'Tambah Data', name=u'tombol_tambah_data', parent=self,
              pos=wx.Point(248, 592), size=wx.Size(200, 24), style=0)
        self.tombol_tambah_data.Bind(wx.EVT_BUTTON,
              self.OnTombol_tambah_dataButton,
              id=wxID_KK_SEMENTARATOMBOL_TAMBAH_DATA)

        self.kembali = wx.Button(id=wxID_KK_SEMENTARAKEMBALI,
              label=u'Kembali Ke Menu', name=u'kembali', parent=self,
              pos=wx.Point(480, 592), size=wx.Size(208, 24), style=0)
        self.kembali.Bind(wx.EVT_BUTTON, self.OnKembaliButton,
              id=wxID_KK_SEMENTARAKEMBALI)

        self.tgllahir = wx.TextCtrl(id=wxID_KK_SEMENTARATGLLAHIR,
              name=u'tgllahir', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(112, 27), style=0, value=u'')

        self.gambar = wx.TextCtrl(id=wxID_KK_SEMENTARAGAMBAR, name=u'gambar',
              parent=self, pos=wx.Point(24, 407), size=wx.Size(152, 21),
              style=0, value=u'')

        self.simpangambar = wx.TextCtrl(id=wxID_KK_SEMENTARASIMPANGAMBAR,
              name=u'simpangambar', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(152, 24), style=0, value=u'/opt/sidesa/penduduk')

        self.button1 = wx.Button(id=wxID_KK_SEMENTARABUTTON1,
              label=u'Upload Photo', name='button1', parent=self,
              pos=wx.Point(24, 431), size=wx.Size(152, 24), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_KK_SEMENTARABUTTON1)

        self.propinsi = wx.TextCtrl(id=wxID_KK_SEMENTARAPROPINSI,
              name=u'propinsi', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(152, 24), style=0, value=u'')

        self.kabupaten = wx.TextCtrl(id=wxID_KK_SEMENTARAKABUPATEN,
              name=u'kabupaten', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(152, 24), style=0, value=u'')

        self.kecamatan = wx.TextCtrl(id=wxID_KK_SEMENTARAKECAMATAN,
              name=u'kecamatan', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(152, 24), style=0, value=u'')

        self.desa = wx.TextCtrl(id=wxID_KK_SEMENTARADESA, name=u'desa',
              parent=self, pos=wx.Point(-100, -100), size=wx.Size(152, 24),
              style=0, value=u'')

    def __init__(self, parent):
        self._init_ctrls(parent)
        
        self.dataprofil()
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
        self.tgllahir.SetValue('')
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
        self.pilihan_shdk.SetValue('Kepala Keluarga')
        self.input_ayah.SetValue('')
        self.input_ibu.SetValue('')
        self.dokumen1.SetValue('')
        self.dokumen2.SetValue('')
        self.dokumen3.SetValue('')
        self.dokumen4.SetValue('')
        self.dokumen5.SetValue('')
        self.dokumen6.SetValue('')
        self.dokumen7.SetValue('')
        self.dokumen8.SetValue('')
        self.gambar.SetValue('')
        self.simpangambar.SetValue('/opt/sidesa/penduduk/')
        
        
    def OnGetDate(self, event):
        selected = self.tanggal_lahir.GetValue()
        month = selected.Month + 1
        day = selected.Day
        year = selected.Year
        date_str = "%02d/%02d/%4d" % (month, day, year)
        self.tgllahir.SetValue("{}".format(date_str))
                    
    def IsiList(self):
        self.isipenduduk.DeleteAllItems()       
        sql = "SELECT * FROM penduduk WHERE shdk='Kepala Keluarga' AND kematian='Tidak'"
        cur.execute(sql) 
        hasil = cur.fetchall() 
        nokk = self.isipenduduk.GetItemCount() 
        for i in hasil : 
            self.isipenduduk.InsertStringItem(nokk, "%s"%i[16]) 
            self.isipenduduk.SetStringItem(nokk,1,"%s"%i[17]) 
            self.isipenduduk.SetStringItem(nokk,2,"%s"%i[21])
            self.isipenduduk.SetStringItem(nokk,3,"%s"%i[29])
            self.isipenduduk.SetStringItem(nokk,4,"%s"%i[26]) 
            self.isipenduduk.SetStringItem(nokk,5,"%s"%i[27])
            nokk = nokk + 1

    def loadgambar(self):
        self.PhotoMaxSize = 100
        img = wx.EmptyImage(100,100)
        self.imageCtrl = wx.StaticBitmap(self, wx.ID_ANY, wx.BitmapFromImage(img),wx.Point(52, 251))
  
    def dataprofil(self) : 
        sql="SELECT * FROM identitas WHERE no=1"
        cur.execute(sql)
        hasil = cur.fetchone()  
        if hasil : 
            self.propinsi.SetValue(str(hasil[18]))
            self.kabupaten.SetValue(str(hasil[17])) 
            self.kecamatan.SetValue(str(hasil[16]))
            self.desa.SetValue(str(hasil[15]))
            
        else : 
            self.pesan = wx.MessageDialog(self,"Cek Data Profil","Konfirmasi",wx.OK) 
            self.pesan.ShowModal() 
            
            
    def OnTombol_tambah_dataButton(self, event):
    
        nokk = str(self.input_no_kk.GetValue())
        nik = str(self.input_nik.GetValue())
        nama = str(self.input_nama.GetValue())
        tmplahir = str(self.input_tempat_lahir.GetValue())
        jk = str(self.pilihan_jenis_kelamin.GetValue())
        tgllahir = str(self.tgllahir.GetValue())
        gdr = str(self.pilihan_golongan_darah.GetValue())
        agama = str(self.pilihan_agama.GetValue())
        warganegara = str(self.pilihan_warganegara.GetValue())
        pddkakhir = str(self.pilihan_pendidikan_terakhir.GetValue())
        pddktempuh = str(self.pilihan_pendidikan_ditempuh.GetValue())
        pekerjaan = str(self.pilihan_pekerjaan.GetValue())
        pekerjaanlain = str(self.pilihan_pekerjaan_lainnya.GetValue())
        status = str(self.pilihan_status.GetValue())
        statuskependudukan = str(self.pilihan_status_kependudukan.GetValue())
        statustinggal = str(self.pilihan_status_tinggal.GetValue())
        difabelitas = str(self.pilihan_difabelitas.GetValue())
        kontrasepsi = str(self.pilihan_kontrasepsi.GetValue())
        shdk = str(self.pilihan_shdk.GetValue())
        ayah = str(self.input_ayah.GetValue())
        ibu = str(self.input_ibu.GetValue())
        kehamilan = str(self.pilihan_kehamilan.GetValue())
        alamat = str(self.input_alamat.GetValue())
        dusun = str(self.input_dusun.GetValue())
        rt = str(self.input_rt.GetValue())
        rw = str(self.input_rw.GetValue())
        dok1 = str(self.dokumen1.GetValue())
        dok2 = str(self.dokumen2.GetValue())
        dok3 = str(self.dokumen3.GetValue())
        dok4 = str(self.dokumen4.GetValue())
        dok5 = str(self.dokumen5.GetValue())
        dok6 = str(self.dokumen6.GetValue())
        dok7 = str(self.dokumen7.GetValue())
        dok8 = str(self.dokumen8.GetValue())
        gbr = str(self.simpangambar.GetValue())
        filepath = str(self.gambar.GetValue())
        #dataprofilget
        propinsi = str(self.propinsi.GetValue())
        kabupaten = str(self.kabupaten.GetValue())
        kecamatan = str(self.kecamatan.GetValue())
        desa = str(self.desa.GetValue())
        
        if nokk == '':
            self.pesan = wx.MessageDialog(self,"Nomor Kartu Keluarga Jangan Kosong","Peringatan",wx.OK) 
            self.pesan.ShowModal()
        elif nik == '':
            self.pesan = wx.MessageDialog(self,"NIK Tidak Boleh Kosong","Peringatan",wx.OK) 
            self.pesan.ShowModal()
        elif nama == '':
            self.pesan = wx.MessageDialog(self,"Nama Tidak Boleh Kosong","Peringatan",wx.OK) 
            self.pesan.ShowModal()    
        elif filepath == '':
            sql="SELECT * FROM penduduk WHERE nik='"+(nik)+"' OR no_kk='"+(nokk)+"'"
            cur.execute(sql)
            hasil = cur.fetchone()  
            if hasil:
                self.pesan = wx.MessageDialog(self,"Nomor NIK / Nomor KK Sudah Ada","Konfirmasi",wx.OK) 
                self.pesan.ShowModal()
            else:
                add_keluarga="INSERT INTO penduduk (nik , nama , jk, tmpt_lahir, tgl_lahir, umur, gdr, agama, status, shdk, shdrt, pddk_akhir, pekerjaan, nama_ibu, nama_ayah, no_kk, nama_kep_kel, petugas, pekerjaan_lain, nama_petugas, alamat, nama_prop, nama_kab, nama_kec, nama_kel, rt, rw, warganegara, nama_dusun, kemiskinan, pddk_saat_ini, status_pddk, status_tgl, difabelitas, kontrasepsi, resiko, kelahiran, kematian, kejadianlain, pindah, dok1, dok2, dok3, dok4, dok5, dok6, dok7, dok8, promis1, promis2,promis3, promis4, promis5, promis6, promis7, promis8, photo, keterangan) VALUES('"+(nik)+"', '"+(nama)+"', '"+(jk)+"','"+(tmplahir)+"','"+(tgllahir)+"','"+''+"','"+(gdr)+"','"+(agama)+"','"+(status)+"','"+(shdk)+"','"+''+"','"+(pddkakhir)+"','"+(pekerjaan)+"','"+(ibu)+"','"+(ayah)+"','SMT-"+(nokk)+"','"+(nama)+"','"+''+"','"+(pekerjaanlain)+"','"+''+"','"+(alamat)+"','"+(propinsi)+"','"+(kabupaten)+"','"+(kecamatan)+"','"+(desa)+"','"+(rt)+"','"+(rw)+"','"+(warganegara)+"','"+(dusun)+"','Tidak Miskin','"+(pddktempuh)+"','"+(statuskependudukan)+"','"+(statustinggal)+"','"+(difabelitas)+"','"+(kontrasepsi)+"','"+(kehamilan)+"', '"+''+"', 'Tidak', '"+''+"', '"+''+"', '"+(dok1)+"', '"+(dok2)+"', '"+(dok3)+"', '"+(dok4)+"', '"+(dok5)+"', '"+(dok6)+"', '"+(dok7)+"', '"+(dok8)+"', '"+''+"', '"+''+"', '"+''+"', '"+''+"', '"+''+"', '"+''+"', '"+''+"', '"+''+"', '"+(gbr)+"blank.jpg', '"+''+"')"        
                cur.execute(add_keluarga)
                db.commit()
                self.pesan = wx.MessageDialog(self,"Data Sudah Tersimpan","Konfirmasi",wx.OK) 
                self.pesan.ShowModal()
                self.awal()
            
        else:
            sql="SELECT * FROM penduduk WHERE nik='"+(nik)+"' OR no_kk='"+(nokk)+"'"
            cur.execute(sql)
            hasil = cur.fetchone()  
            if hasil:
                self.pesan = wx.MessageDialog(self,"Nomor NIK / Nomor KK Sudah Ada","Konfirmasi",wx.OK) 
                self.pesan.ShowModal()
            else:
                shutil.copy2(filepath, gbr+nik+'.jpg')
                add_keluarga="INSERT INTO penduduk (nik , nama , jk, tmpt_lahir, tgl_lahir, umur, gdr, agama, status, shdk, shdrt, pddk_akhir, pekerjaan, nama_ibu, nama_ayah, no_kk, nama_kep_kel, petugas, pekerjaan_lain, nama_petugas, alamat, nama_prop, nama_kab, nama_kec, nama_kel, rt, rw, warganegara, nama_dusun,  kemiskinan, pddk_saat_ini, status_pddk, status_tgl, difabelitas, kontrasepsi, resiko, kelahiran, kematian, kejadianlain, pindah, dok1, dok2, dok3, dok4, dok5, dok6, dok7, dok8, promis1, promis2,promis3, promis4, promis5, promis6, promis7, promis8, photo, keterangan) VALUES('"+(nik)+"', '"+(nama)+"', '"+(jk)+"','"+(tmplahir)+"','"+(tgllahir)+"','"+''+"','"+(gdr)+"','"+(agama)+"','"+(status)+"','"+(shdk)+"','"+''+"','"+(pddkakhir)+"','"+(pekerjaan)+"','"+(ibu)+"','"+(ayah)+"','SMT-"+(nokk)+"','"+(nama)+"','"+''+"','"+(pekerjaanlain)+"','"+''+"','"+(alamat)+"','"+(propinsi)+"','"+(kabupaten)+"','"+(kecamatan)+"','"+(desa)+"','"+(rt)+"','"+(rw)+"','"+(warganegara)+"','"+(dusun)+"','Tidak Miskin','"+(pddktempuh)+"','"+(statuskependudukan)+"','"+(statustinggal)+"','"+(difabelitas)+"','"+(kontrasepsi)+"','"+(kehamilan)+"', '"+''+"', 'Tidak', '"+''+"', '"+''+"', '"+(dok1)+"', '"+(dok2)+"', '"+(dok3)+"', '"+(dok4)+"', '"+(dok5)+"', '"+(dok6)+"', '"+(dok7)+"', '"+(dok8)+"', '"+''+"', '"+''+"', '"+''+"', '"+''+"', '"+''+"', '"+''+"', '"+''+"', '"+''+"', '"+(gbr)+(nik)+".jpg', '"+''+"')"        
                cur.execute(add_keluarga)
                db.commit()
                self.pesan = wx.MessageDialog(self,"Data Sudah Tersimpan","Konfirmasi",wx.OK) 
                self.pesan.ShowModal()
                self.awal()
           

    def OnKembaliButton(self, event):
        self.Close()
        self.Destroy()

    def OnButton1Button(self, event):
        wildcard = "JPG PNG BMP File (*.jpg)|*.jpg"
        dialog = wx.FileDialog(None, "Ambil File",
                               wildcard=wildcard,
                               style=wx.OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            self.gambar.SetValue(dialog.GetPath())
        dialog.Destroy()
        self.onView()
        
    def onView(self):
        filepath = self.gambar.GetValue()
        img = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
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
