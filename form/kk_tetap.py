#Boa:Frame:kk_tetap
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
    return kk_tetap(parent)

[wxID_KK_TETAP, wxID_KK_TETAPBUTTON1, wxID_KK_TETAPDESA, wxID_KK_TETAPDOKUMEN, 
 wxID_KK_TETAPDOKUMEN1, wxID_KK_TETAPDOKUMEN2, wxID_KK_TETAPDOKUMEN3, 
 wxID_KK_TETAPDOKUMEN4, wxID_KK_TETAPDOKUMEN5, wxID_KK_TETAPDOKUMEN6, 
 wxID_KK_TETAPDOKUMEN7, wxID_KK_TETAPDOKUMEN8, wxID_KK_TETAPGAMBAR, 
 wxID_KK_TETAPINPUT_ALAMAT, wxID_KK_TETAPINPUT_AYAH, wxID_KK_TETAPINPUT_DUSUN, 
 wxID_KK_TETAPINPUT_IBU, wxID_KK_TETAPINPUT_NAMA, wxID_KK_TETAPINPUT_NIK, 
 wxID_KK_TETAPINPUT_NO_KK, wxID_KK_TETAPINPUT_RT, wxID_KK_TETAPINPUT_RW, 
 wxID_KK_TETAPINPUT_TEMPAT_LAHIR, wxID_KK_TETAPISIPENDUDUK, 
 wxID_KK_TETAPKABUPATEN, wxID_KK_TETAPKECAMATAN, wxID_KK_TETAPKEMBALI, 
 wxID_KK_TETAPLABEL_AGAMA, wxID_KK_TETAPLABEL_ALAMAT, 
 wxID_KK_TETAPLABEL_DIFABELITAS, wxID_KK_TETAPLABEL_DUSUN, 
 wxID_KK_TETAPLABEL_GOLONGAN_DARAH, wxID_KK_TETAPLABEL_JENIS_KELAMIN, 
 wxID_KK_TETAPLABEL_KEWARGANEGARAAN, wxID_KK_TETAPLABEL_KONTRASEPSI, 
 wxID_KK_TETAPLABEL_NAMA_AYAH, wxID_KK_TETAPLABEL_NAMA_IBU, 
 wxID_KK_TETAPLABEL_NAMA_LENGKAP, wxID_KK_TETAPLABEL_NOMOR_KK, 
 wxID_KK_TETAPLABEL_PEKERJAAN, wxID_KK_TETAPLABEL_PEKERJAAN_LAINNYA, 
 wxID_KK_TETAPLABEL_PENDIDIKAN_TEMPUH, wxID_KK_TETAPLABEL_PENDIDIKAN_TERAKHIR, 
 wxID_KK_TETAPLABEL_STATUS_KEPENDUDUKAN, wxID_KK_TETAPLABEL_STATUS_PERKAWINAN, 
 wxID_KK_TETAPLABEL_STATUS_TINGGAL, wxID_KK_TETAPLABEL_TANGGAL_LAHIR, 
 wxID_KK_TETAPLABEL_TEMPAT_LAHIR, wxID_KK_TETAPLEBEL_NIK, 
 wxID_KK_TETAPPILIHAN_AGAMA, wxID_KK_TETAPPILIHAN_DIFABELITAS, 
 wxID_KK_TETAPPILIHAN_GOLONGAN_DARAH, wxID_KK_TETAPPILIHAN_JENIS_KELAMIN, 
 wxID_KK_TETAPPILIHAN_KEHAMILAN, wxID_KK_TETAPPILIHAN_KONTRASEPSI, 
 wxID_KK_TETAPPILIHAN_PEKERJAAN, wxID_KK_TETAPPILIHAN_PEKERJAAN_LAINNYA, 
 wxID_KK_TETAPPILIHAN_PENDIDIKAN_DITEMPUH, 
 wxID_KK_TETAPPILIHAN_PENDIDIKAN_TERAKHIR, wxID_KK_TETAPPILIHAN_SHDK, 
 wxID_KK_TETAPPILIHAN_STATUS, wxID_KK_TETAPPILIHAN_STATUS_KEPENDUDUKAN, 
 wxID_KK_TETAPPILIHAN_STATUS_TINGGAL, wxID_KK_TETAPPILIHAN_WARGANEGARA, 
 wxID_KK_TETAPPROPINSI, wxID_KK_TETAPSIMPANGAMBAR, wxID_KK_TETAPSTATICTEXT2, 
 wxID_KK_TETAPSTATICTEXT3, wxID_KK_TETAPTANGGAL_LAHIR, wxID_KK_TETAPTGLLAHIR, 
 wxID_KK_TETAPTOMBOL_TAMBAH_DATA, 
] = [wx.NewId() for _init_ctrls in range(71)]

class kk_tetap(wx.Frame):
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
        wx.Frame.__init__(self, id=wxID_KK_TETAP, name=u'kk_tetap', parent=prnt,
              pos=wx.Point(420, 82), size=wx.Size(896, 662),
              style=wx.DEFAULT_FRAME_STYLE,
              title=u'Tambah Kartu Keluarga Tetap')
        self.SetClientSize(wx.Size(888, 632))
        self.Center(wx.BOTH)
        self.SetHelpText(u'Masukan Nomor KK')
        self.SetBackgroundColour(wx.Colour(192, 192, 192))

        self.isipenduduk = wx.ListCtrl(id=wxID_KK_TETAPISIPENDUDUK,
              name=u'isipenduduk', parent=self, pos=wx.Point(16, 16),
              size=wx.Size(856, 128), style=wx.LC_REPORT)
        self._init_coll_isipenduduk_Columns(self.isipenduduk)

        self.label_nomor_kk = wx.StaticText(id=wxID_KK_TETAPLABEL_NOMOR_KK,
              label=u'Nomor KK', name=u'label_nomor_kk', parent=self,
              pos=wx.Point(13, 150), size=wx.Size(168, 17), style=0)

        self.label_alamat = wx.StaticText(id=wxID_KK_TETAPLABEL_ALAMAT,
              label=u'Alamat', name=u'label_alamat', parent=self,
              pos=wx.Point(256, 152), size=wx.Size(47, 17), style=0)

        self.label_dusun = wx.StaticText(id=wxID_KK_TETAPLABEL_DUSUN,
              label=u'Dusun', name=u'label_dusun', parent=self,
              pos=wx.Point(552, 152), size=wx.Size(144, 17), style=0)

        self.lebel_nik = wx.StaticText(id=wxID_KK_TETAPLEBEL_NIK,
              label=u'N I K *', name=u'lebel_nik', parent=self,
              pos=wx.Point(192, 192), size=wx.Size(40, 17), style=0)

        self.label_nama_lengkap = wx.StaticText(id=wxID_KK_TETAPLABEL_NAMA_LENGKAP,
              label=u'Nama Lengkap', name=u'label_nama_lengkap', parent=self,
              pos=wx.Point(192, 232), size=wx.Size(98, 17), style=0)

        self.label_jenis_kelamin = wx.StaticText(id=wxID_KK_TETAPLABEL_JENIS_KELAMIN,
              label=u'Jenis Kelamin', name=u'label_jenis_kelamin', parent=self,
              pos=wx.Point(192, 272), size=wx.Size(152, 17), style=0)

        self.label_tempat_lahir = wx.StaticText(id=wxID_KK_TETAPLABEL_TEMPAT_LAHIR,
              label=u'Tempat Lahir', name=u'label_tempat_lahir', parent=self,
              pos=wx.Point(192, 312), size=wx.Size(176, 17), style=0)

        self.label_tanggal_lahir = wx.StaticText(id=wxID_KK_TETAPLABEL_TANGGAL_LAHIR,
              label=u'Tanggal Lahir', name=u'label_tanggal_lahir', parent=self,
              pos=wx.Point(192, 352), size=wx.Size(152, 17), style=0)

        self.label_golongan_darah = wx.StaticText(id=wxID_KK_TETAPLABEL_GOLONGAN_DARAH,
              label=u'Golongan Darah', name=u'label_golongan_darah',
              parent=self, pos=wx.Point(192, 392), size=wx.Size(200, 17),
              style=0)

        self.label_agama = wx.StaticText(id=wxID_KK_TETAPLABEL_AGAMA,
              label=u'Agama', name=u'label_agama', parent=self,
              pos=wx.Point(400, 192), size=wx.Size(120, 17), style=0)

        self.label_kewarganegaraan = wx.StaticText(id=wxID_KK_TETAPLABEL_KEWARGANEGARAAN,
              label=u'Kewarganegaraan', name=u'label_kewarganegaraan',
              parent=self, pos=wx.Point(400, 232), size=wx.Size(168, 17),
              style=0)

        self.label_pendidikan_terakhir = wx.StaticText(id=wxID_KK_TETAPLABEL_PENDIDIKAN_TERAKHIR,
              label=u'Pendidikan Terakhir', name=u'label_pendidikan_terakhir',
              parent=self, pos=wx.Point(400, 272), size=wx.Size(184, 17),
              style=0)

        self.label_pendidikan_tempuh = wx.StaticText(id=wxID_KK_TETAPLABEL_PENDIDIKAN_TEMPUH,
              label=u'Pendidikan Saat Ini Ditempuh',
              name=u'label_pendidikan_tempuh', parent=self, pos=wx.Point(400,
              312), size=wx.Size(264, 17), style=0)

        self.label_pekerjaan_lainnya = wx.StaticText(id=wxID_KK_TETAPLABEL_PEKERJAAN_LAINNYA,
              label=u'Pekerjaan Lainnya', name=u'label_pekerjaan_lainnya',
              parent=self, pos=wx.Point(400, 392), size=wx.Size(168, 17),
              style=0)

        self.label_status_tinggal = wx.StaticText(id=wxID_KK_TETAPLABEL_STATUS_TINGGAL,
              label=u'Status Tinggal', name=u'label_status_tinggal',
              parent=self, pos=wx.Point(624, 272), size=wx.Size(152, 17),
              style=0)

        self.label_pekerjaan = wx.StaticText(id=wxID_KK_TETAPLABEL_PEKERJAAN,
              label=u'Pekerjaan Utama', name=u'label_pekerjaan', parent=self,
              pos=wx.Point(400, 352), size=wx.Size(200, 17), style=0)

        self.label_difabelitas = wx.StaticText(id=wxID_KK_TETAPLABEL_DIFABELITAS,
              label=u'Penyandang Difabelitas', name=u'label_difabelitas',
              parent=self, pos=wx.Point(624, 312), size=wx.Size(184, 17),
              style=0)

        self.label_status_perkawinan = wx.StaticText(id=wxID_KK_TETAPLABEL_STATUS_PERKAWINAN,
              label=u'Status Perkawinan', name=u'label_status_perkawinan',
              parent=self, pos=wx.Point(624, 192), size=wx.Size(176, 17),
              style=0)

        self.input_no_kk = wx.TextCtrl(id=wxID_KK_TETAPINPUT_NO_KK,
              name=u'input_no_kk', parent=self, pos=wx.Point(8, 168),
              size=wx.Size(240, 21), style=0, value=u'')

        self.input_alamat = wx.TextCtrl(id=wxID_KK_TETAPINPUT_ALAMAT,
              name=u'input_alamat', parent=self, pos=wx.Point(256, 168),
              size=wx.Size(288, 21), style=0, value=u'')

        self.input_dusun = wx.TextCtrl(id=wxID_KK_TETAPINPUT_DUSUN,
              name=u'input_dusun', parent=self, pos=wx.Point(552, 168),
              size=wx.Size(192, 21), style=0, value=u'')

        self.input_rt = wx.TextCtrl(id=wxID_KK_TETAPINPUT_RT, name=u'input_rt',
              parent=self, pos=wx.Point(752, 168), size=wx.Size(56, 21),
              style=0, value=u'')

        self.input_rw = wx.TextCtrl(id=wxID_KK_TETAPINPUT_RW, name=u'input_rw',
              parent=self, pos=wx.Point(816, 168), size=wx.Size(56, 21),
              style=0, value=u'')

        self.input_nik = wx.TextCtrl(id=wxID_KK_TETAPINPUT_NIK,
              name=u'input_nik', parent=self, pos=wx.Point(192, 208),
              size=wx.Size(200, 21), style=0, value=u'')

        self.input_nama = wx.TextCtrl(id=wxID_KK_TETAPINPUT_NAMA,
              name=u'input_nama', parent=self, pos=wx.Point(192, 248),
              size=wx.Size(200, 21), style=0, value=u'')

        self.pilihan_jenis_kelamin = wx.ComboBox(choices=['L', 'P'],
              id=wxID_KK_TETAPPILIHAN_JENIS_KELAMIN,
              name=u'pilihan_jenis_kelamin', parent=self, pos=wx.Point(192,
              288), size=wx.Size(200, 21), style=0)

        self.input_tempat_lahir = wx.TextCtrl(id=wxID_KK_TETAPINPUT_TEMPAT_LAHIR,
              name=u'input_tempat_lahir', parent=self, pos=wx.Point(192, 328),
              size=wx.Size(200, 25), style=0, value=u'')

        self.tanggal_lahir = wx.DatePickerCtrl(id=wxID_KK_TETAPTANGGAL_LAHIR,
              name=u'tanggal_lahir', parent=self, pos=wx.Point(192, 368),
              size=wx.Size(200, 26), style=wx.DP_DROPDOWN | wx.DP_SHOWCENTURY)
        self.tanggal_lahir.Bind(wx.EVT_DATE_CHANGED, self.OnGetDate)

        self.pilihan_golongan_darah = wx.ComboBox(choices=['A', 'AB', 'B', 'O',
              'A+', 'A-', 'AB+', 'AB-', 'B+', 'B-', 'O+', 'O-', 'Tidak tahu'],
              id=wxID_KK_TETAPPILIHAN_GOLONGAN_DARAH,
              name=u'pilihan_golongan_darah', parent=self, pos=wx.Point(192,
              408), size=wx.Size(80, 21), style=0)

        self.pilihan_agama = wx.ComboBox(choices=['Islam', 'Kristen Protestan',
              'Kristen Katolik', 'Hindu', 'Budha', 'Konghuchu',
              'Aliran Kepercayaan', 'Agama Lainnya'],
              id=wxID_KK_TETAPPILIHAN_AGAMA, name=u'pilihan_agama', parent=self,
              pos=wx.Point(400, 208), size=wx.Size(216, 21), style=0)

        self.pilihan_warganegara = wx.ComboBox(choices=['WNI', 'WNA'],
              id=wxID_KK_TETAPPILIHAN_WARGANEGARA, name=u'pilihan_warganegara',
              parent=self, pos=wx.Point(400, 248), size=wx.Size(216, 21),
              style=0)

        self.pilihan_pendidikan_terakhir = wx.ComboBox(choices=['Tidak/Belum Sekolah',
              'Tidak Tamat SD/Sederajat', 'Tamat SD/Sederajat',
              'SLTP/Sederajat', 'SLTA/Sederajat', 'Diploma I/II',
              'Akademi/Diploma III/S. Muda', 'Diploma IV/Strata I', 'Strata II',
              'Strata III', 'Pendidikan Non Formal'],
              id=wxID_KK_TETAPPILIHAN_PENDIDIKAN_TERAKHIR,
              name=u'pilihan_pendidikan_terakhir', parent=self,
              pos=wx.Point(400, 288), size=wx.Size(216, 21), style=0)

        self.pilihan_pendidikan_ditempuh = wx.ComboBox(choices=['PAUD sederajat',
              'TK Sederajat', 'SD Sederajat', 'SLTP Sederajat',
              'SLTA Sederajat', 'D1 Sederajat', 'D2 Sederajat', 'D3 Sederajat' ,
              'S1 Sederajat' , 'S2 Sederajat' , 'S3 Sederajat' ,
              'Pendidikan Non Formal'],
              id=wxID_KK_TETAPPILIHAN_PENDIDIKAN_DITEMPUH,
              name=u'pilihan_pendidikan_ditempuh', parent=self,
              pos=wx.Point(400, 328), size=wx.Size(216, 21), style=0)

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
              'Wiraswasta', 'Buruh Migran'], id=wxID_KK_TETAPPILIHAN_PEKERJAAN,
              name=u'pilihan_pekerjaan', parent=self, pos=wx.Point(400, 370),
              size=wx.Size(216, 21), style=0)

        self.pilihan_pekerjaan_lainnya = wx.ComboBox(choices=['Berdagang',
              'Bertani', 'Berkebun', 'Jasa  profesional  tukang', 'Seniman',
              'Lainnya'], id=wxID_KK_TETAPPILIHAN_PEKERJAAN_LAINNYA,
              name=u'pilihan_pekerjaan_lainnya', parent=self, pos=wx.Point(400,
              408), size=wx.Size(216, 21), style=0)

        self.pilihan_status = wx.ComboBox(choices=['Belum Kawin', 'Kawin',
              'Cerai Mati', 'Cerai Hidup'], id=wxID_KK_TETAPPILIHAN_STATUS,
              name=u'pilihan_status', parent=self, pos=wx.Point(624, 208),
              size=wx.Size(248, 21), style=0)

        self.label_status_kependudukan = wx.StaticText(id=wxID_KK_TETAPLABEL_STATUS_KEPENDUDUKAN,
              label=u'Status Kependudukan', name=u'label_status_kependudukan',
              parent=self, pos=wx.Point(624, 232), size=wx.Size(184, 17),
              style=0)

        self.pilihan_status_kependudukan = wx.ComboBox(choices=['Penduduk Tetap',
              'Penduduk Sementara', 'Penduduk Pindah/Pindahan'],
              id=wxID_KK_TETAPPILIHAN_STATUS_KEPENDUDUKAN,
              name=u'pilihan_status_kependudukan', parent=self,
              pos=wx.Point(624, 248), size=wx.Size(248, 21), style=0)

        self.pilihan_status_tinggal = wx.ComboBox(choices=['Tinggal Tetap',
              'Tinggal Di Luar Desa*', 'Tinggal Di Luar Kota/Kabupaten',
              'Tinggal Di Luar Propinsi', 'Tinggal Di Luar Negeri'],
              id=wxID_KK_TETAPPILIHAN_STATUS_TINGGAL,
              name=u'pilihan_status_tinggal', parent=self, pos=wx.Point(624,
              288), size=wx.Size(248, 21), style=0)

        self.pilihan_difabelitas = wx.ComboBox(choices=['Tidak cacat',
              'Cacat Fisik', 'Cacat Netra/Buta', 'Cacat Rungu/Wicara',
              'Cacat Mental/Jiwa', 'Cacat Fisik/Mental', 'Cacat Lainnya'],
              id=wxID_KK_TETAPPILIHAN_DIFABELITAS, name=u'pilihan_difabelitas',
              parent=self, pos=wx.Point(624, 328), size=wx.Size(248, 21),
              style=0)

        self.label_kontrasepsi = wx.StaticText(id=wxID_KK_TETAPLABEL_KONTRASEPSI,
              label=u'Penggunaan Kontrasepsi', name=u'label_kontrasepsi',
              parent=self, pos=wx.Point(624, 352), size=wx.Size(192, 17),
              style=0)

        self.pilihan_kontrasepsi = wx.ComboBox(choices=['Pil', 'Suntik', 'IUD',
              'Kondom', 'Implant', 'MOP'], id=wxID_KK_TETAPPILIHAN_KONTRASEPSI,
              name=u'pilihan_kontrasepsi', parent=self, pos=wx.Point(624, 368),
              size=wx.Size(248, 21), style=0)

        self.pilihan_kehamilan = wx.ComboBox(choices=['Resiko Tinggi',
              'Tidak Resiko Tinggi'], id=wxID_KK_TETAPPILIHAN_KEHAMILAN,
              name=u'pilihan_kehamilan', parent=self, pos=wx.Point(624, 408),
              size=wx.Size(248, 21), style=0)

        self.dokumen = wx.StaticText(id=wxID_KK_TETAPDOKUMEN,
              label=u'Kepemilikan Dokumen', name=u'dokumen', parent=self,
              pos=wx.Point(24, 440), size=wx.Size(304, 17), style=0)

        self.staticText2 = wx.StaticText(id=wxID_KK_TETAPSTATICTEXT2,
              label=u'RT', name='staticText2', parent=self, pos=wx.Point(760,
              152), size=wx.Size(24, 16), style=0)

        self.staticText3 = wx.StaticText(id=wxID_KK_TETAPSTATICTEXT3,
              label=u'RW', name='staticText3', parent=self, pos=wx.Point(824,
              152), size=wx.Size(19, 17), style=0)

        self.dokumen1 = wx.ComboBox(choices=['Akta Kelahiran'],
              id=wxID_KK_TETAPDOKUMEN1, name=u'dokumen1', parent=self,
              pos=wx.Point(24, 464), size=wx.Size(187, 21), style=0, value='')

        self.dokumen2 = wx.ComboBox(choices=['Akta Nikah'],
              id=wxID_KK_TETAPDOKUMEN2, name=u'dokumen2', parent=self,
              pos=wx.Point(24, 504), size=wx.Size(187, 21), style=0, value='')

        self.dokumen3 = wx.ComboBox(choices=['Akta Cerai'],
              id=wxID_KK_TETAPDOKUMEN3, name=u'dokumen3', parent=self,
              pos=wx.Point(224, 464), size=wx.Size(187, 21), style=0, value='')

        self.dokumen4 = wx.ComboBox(choices=['Akta Kematian'],
              id=wxID_KK_TETAPDOKUMEN4, name=u'dokumen4', parent=self,
              pos=wx.Point(224, 504), size=wx.Size(187, 21), style=0, value='')

        self.dokumen5 = wx.ComboBox(choices=['KTP Sementara'],
              id=wxID_KK_TETAPDOKUMEN5, name=u'dokumen5', parent=self,
              pos=wx.Point(424, 464), size=wx.Size(187, 21), style=0, value='')

        self.dokumen6 = wx.ComboBox(choices=['KITAS'], id=wxID_KK_TETAPDOKUMEN6,
              name=u'dokumen6', parent=self, pos=wx.Point(424, 504),
              size=wx.Size(187, 21), style=0, value='')

        self.dokumen7 = wx.ComboBox(choices=['VISA'], id=wxID_KK_TETAPDOKUMEN7,
              name=u'dokumen7', parent=self, pos=wx.Point(632, 464),
              size=wx.Size(187, 21), style=0, value='')

        self.dokumen8 = wx.ComboBox(choices=['Paspor'],
              id=wxID_KK_TETAPDOKUMEN8, name=u'dokumen8', parent=self,
              pos=wx.Point(632, 504), size=wx.Size(187, 21), style=0, value='')

        self.pilihan_shdk = wx.TextCtrl(id=wxID_KK_TETAPPILIHAN_SHDK,
              name=u'pilihan_shdk', parent=self, pos=wx.Point(24, 560),
              size=wx.Size(304, 21), style=wx.TE_READONLY,
              value=u'Kepala Keluarga')

        self.label_nama_ayah = wx.StaticText(id=wxID_KK_TETAPLABEL_NAMA_AYAH,
              label=u'Nama Ayah', name=u'label_nama_ayah', parent=self,
              pos=wx.Point(344, 536), size=wx.Size(152, 17), style=0)

        self.input_ayah = wx.TextCtrl(id=wxID_KK_TETAPINPUT_AYAH,
              name=u'input_ayah', parent=self, pos=wx.Point(344, 560),
              size=wx.Size(280, 21), style=0, value=u'')

        self.label_nama_ibu = wx.StaticText(id=wxID_KK_TETAPLABEL_NAMA_IBU,
              label=u'Nama Ibu', name=u'label_nama_ibu', parent=self,
              pos=wx.Point(632, 536), size=wx.Size(160, 17), style=0)

        self.input_ibu = wx.TextCtrl(id=wxID_KK_TETAPINPUT_IBU,
              name=u'input_ibu', parent=self, pos=wx.Point(632, 560),
              size=wx.Size(240, 21), style=0, value=u'')

        self.tombol_tambah_data = wx.Button(id=wxID_KK_TETAPTOMBOL_TAMBAH_DATA,
              label=u'Tambah Data', name=u'tombol_tambah_data', parent=self,
              pos=wx.Point(248, 600), size=wx.Size(200, 24), style=0)
        self.tombol_tambah_data.Bind(wx.EVT_BUTTON,
              self.OnTombol_tambah_dataButton,
              id=wxID_KK_TETAPTOMBOL_TAMBAH_DATA)

        self.kembali = wx.Button(id=wxID_KK_TETAPKEMBALI,
              label=u'Kembali Ke Menu', name=u'kembali', parent=self,
              pos=wx.Point(480, 600), size=wx.Size(208, 24), style=0)
        self.kembali.Bind(wx.EVT_BUTTON, self.OnKembaliButton,
              id=wxID_KK_TETAPKEMBALI)

        self.tgllahir = wx.TextCtrl(id=wxID_KK_TETAPTGLLAHIR, name=u'tgllahir',
              parent=self, pos=wx.Point(-100, -100), size=wx.Size(112, 27),
              style=0, value=u'')

        self.gambar = wx.TextCtrl(id=wxID_KK_TETAPGAMBAR, name=u'gambar',
              parent=self, pos=wx.Point(24, 368), size=wx.Size(152, 24),
              style=0, value=u'')

        self.simpangambar = wx.TextCtrl(id=wxID_KK_TETAPSIMPANGAMBAR,
              name=u'simpangambar', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(152, 24), style=0, value=u'penduduk/')

        self.button1 = wx.Button(id=wxID_KK_TETAPBUTTON1, label=u'Upload Photo',
              name='button1', parent=self, pos=wx.Point(24, 392),
              size=wx.Size(152, 24), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_KK_TETAPBUTTON1)

        self.propinsi = wx.TextCtrl(id=wxID_KK_TETAPPROPINSI, name=u'propinsi',
              parent=self, pos=wx.Point(-100, -100), size=wx.Size(152, 24),
              style=0, value=u'')

        self.kabupaten = wx.TextCtrl(id=wxID_KK_TETAPKABUPATEN,
              name=u'kabupaten', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(152, 24), style=0, value=u'')

        self.kecamatan = wx.TextCtrl(id=wxID_KK_TETAPKECAMATAN,
              name=u'kecamatan', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(152, 24), style=0, value=u'')

        self.desa = wx.TextCtrl(id=wxID_KK_TETAPDESA, name=u'desa', parent=self,
              pos=wx.Point(-100, -100), size=wx.Size(152, 24), style=0,
              value=u'')

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
        self.simpangambar.SetValue('penduduk/')
        
        
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
                add_keluarga="INSERT INTO penduduk (nik , nama , jk, tmpt_lahir, tgl_lahir, umur, gdr, agama, status, shdk, shdrt, pddk_akhir, pekerjaan, nama_ibu, nama_ayah, no_kk, nama_kep_kel, petugas, pekerjaan_lain, nama_petugas, alamat, nama_prop, nama_kab, nama_kec, nama_kel, rt, rw, warganegara, nama_dusun, kemiskinan, pddk_saat_ini, status_pddk, status_tgl, difabelitas, kontrasepsi, resiko, kelahiran, kematian, kejadianlain, pindah, dok1, dok2, dok3, dok4, dok5, dok6, dok7, dok8, promis1, promis2,promis3, promis4, promis5, promis6, promis7, promis8, photo, keterangan) VALUES('"+(nik)+"', '"+(nama)+"', '"+(jk)+"','"+(tmplahir)+"','"+(tgllahir)+"','"+''+"','"+(gdr)+"','"+(agama)+"','"+(status)+"','"+(shdk)+"','"+''+"','"+(pddkakhir)+"','"+(pekerjaan)+"','"+(ayah)+"','"+(ibu)+"','"+(nokk)+"','"+(nama)+"','"+''+"','"+(pekerjaanlain)+"','"+''+"','"+(alamat)+"','"+(propinsi)+"','"+(kabupaten)+"','"+(kecamatan)+"','"+(desa)+"','"+(rt)+"','"+(rw)+"','"+(warganegara)+"','"+(dusun)+"','Tidak Miskin','"+(pddktempuh)+"','"+(statuskependudukan)+"','"+(statustinggal)+"','"+(difabelitas)+"','"+(kontrasepsi)+"','"+(kehamilan)+"', '"+''+"', 'Tidak', '"+''+"', '"+''+"', '"+(dok1)+"', '"+(dok2)+"', '"+(dok3)+"', '"+(dok4)+"', '"+(dok5)+"', '"+(dok6)+"', '"+(dok7)+"', '"+(dok8)+"', '"+''+"', '"+''+"', '"+''+"', '"+''+"', '"+''+"', '"+''+"', '"+''+"', '"+''+"', '"+(gbr)+"blank.jpg', '"+''+"')"        
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
                add_keluarga="INSERT INTO penduduk (nik , nama , jk, tmpt_lahir, tgl_lahir, umur, gdr, agama, status, shdk, shdrt, pddk_akhir, pekerjaan, nama_ibu, nama_ayah, no_kk, nama_kep_kel, petugas, pekerjaan_lain, nama_petugas, alamat, nama_prop, nama_kab, nama_kec, nama_kel, rt, rw, warganegara, nama_dusun,  kemiskinan, pddk_saat_ini, status_pddk, status_tgl, difabelitas, kontrasepsi, resiko, kelahiran, kematian, kejadianlain, pindah, dok1, dok2, dok3, dok4, dok5, dok6, dok7, dok8, promis1, promis2,promis3, promis4, promis5, promis6, promis7, promis8, photo, keterangan) VALUES('"+(nik)+"', '"+(nama)+"', '"+(jk)+"','"+(tmplahir)+"','"+(tgllahir)+"','"+''+"','"+(gdr)+"','"+(agama)+"','"+(status)+"','"+(shdk)+"','"+''+"','"+(pddkakhir)+"','"+(pekerjaan)+"','"+(ayah)+"','"+(ibu)+"','"+(nokk)+"','"+(nama)+"','"+''+"','"+(pekerjaanlain)+"','"+''+"','"+(alamat)+"','"+(propinsi)+"','"+(kabupaten)+"','"+(kecamatan)+"','"+(desa)+"','"+(rt)+"','"+(rw)+"','"+(warganegara)+"','"+(dusun)+"','Tidak Miskin','"+(pddktempuh)+"','"+(statuskependudukan)+"','"+(statustinggal)+"','"+(difabelitas)+"','"+(kontrasepsi)+"','"+(kehamilan)+"', '"+''+"', 'Tidak', '"+''+"', '"+''+"', '"+(dok1)+"', '"+(dok2)+"', '"+(dok3)+"', '"+(dok4)+"', '"+(dok5)+"', '"+(dok6)+"', '"+(dok7)+"', '"+(dok8)+"', '"+''+"', '"+''+"', '"+''+"', '"+''+"', '"+''+"', '"+''+"', '"+''+"', '"+''+"', '"+(gbr)+(nik)+".jpg', '"+''+"')"        
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
