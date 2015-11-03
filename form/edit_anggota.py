#Boa:Dialog:edit_anggota
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
    return edit_anggota(parent)

[wxID_EDIT_ANGGOTA, wxID_EDIT_ANGGOTABUTTON1, wxID_EDIT_ANGGOTABUTTON2, 
 wxID_EDIT_ANGGOTACARI_KK, wxID_EDIT_ANGGOTADESA, wxID_EDIT_ANGGOTADOKUMEN, 
 wxID_EDIT_ANGGOTADOKUMEN1, wxID_EDIT_ANGGOTADOKUMEN2, 
 wxID_EDIT_ANGGOTADOKUMEN3, wxID_EDIT_ANGGOTADOKUMEN4, 
 wxID_EDIT_ANGGOTADOKUMEN5, wxID_EDIT_ANGGOTADOKUMEN6, 
 wxID_EDIT_ANGGOTADOKUMEN7, wxID_EDIT_ANGGOTADOKUMEN8, 
 wxID_EDIT_ANGGOTAGAMBAR, wxID_EDIT_ANGGOTAINPUT_ALAMAT, 
 wxID_EDIT_ANGGOTAINPUT_AYAH, wxID_EDIT_ANGGOTAINPUT_DUSUN, 
 wxID_EDIT_ANGGOTAINPUT_IBU, wxID_EDIT_ANGGOTAINPUT_NAMA, 
 wxID_EDIT_ANGGOTAINPUT_NIK, wxID_EDIT_ANGGOTAINPUT_NO, 
 wxID_EDIT_ANGGOTAINPUT_NO_KK, wxID_EDIT_ANGGOTAINPUT_RT, 
 wxID_EDIT_ANGGOTAINPUT_RW, wxID_EDIT_ANGGOTAINPUT_TEMPAT_LAHIR, 
 wxID_EDIT_ANGGOTAISIPENDUDUK, wxID_EDIT_ANGGOTAKABUPATEN, 
 wxID_EDIT_ANGGOTAKECAMATAN, wxID_EDIT_ANGGOTAKEMBALI, 
 wxID_EDIT_ANGGOTALABEL_AGAMA, wxID_EDIT_ANGGOTALABEL_ALAMAT, 
 wxID_EDIT_ANGGOTALABEL_DIFABELITAS, wxID_EDIT_ANGGOTALABEL_DUSUN, 
 wxID_EDIT_ANGGOTALABEL_GOLONGAN_DARAH, wxID_EDIT_ANGGOTALABEL_JENIS_KELAMIN, 
 wxID_EDIT_ANGGOTALABEL_KEWARGANEGARAAN, wxID_EDIT_ANGGOTALABEL_KONTRASEPSI, 
 wxID_EDIT_ANGGOTALABEL_NAMA_AYAH, wxID_EDIT_ANGGOTALABEL_NAMA_IBU, 
 wxID_EDIT_ANGGOTALABEL_NAMA_LENGKAP, wxID_EDIT_ANGGOTALABEL_NOMOR_KK, 
 wxID_EDIT_ANGGOTALABEL_PEKERJAAN, wxID_EDIT_ANGGOTALABEL_PEKERJAAN_LAINNYA, 
 wxID_EDIT_ANGGOTALABEL_PENDIDIKAN_TEMPUH, 
 wxID_EDIT_ANGGOTALABEL_PENDIDIKAN_TERAKHIR, 
 wxID_EDIT_ANGGOTALABEL_RESIKO_KEHAMILAN, wxID_EDIT_ANGGOTALABEL_SHDK, 
 wxID_EDIT_ANGGOTALABEL_STATUS_KEPENDUDUKAN, 
 wxID_EDIT_ANGGOTALABEL_STATUS_PERKAWINAN, 
 wxID_EDIT_ANGGOTALABEL_STATUS_TINGGAL, wxID_EDIT_ANGGOTALABEL_TANGGAL_LAHIR, 
 wxID_EDIT_ANGGOTALABEL_TEMPAT_LAHIR, wxID_EDIT_ANGGOTALEBEL_NIK, 
 wxID_EDIT_ANGGOTANAMA_KK, wxID_EDIT_ANGGOTAPILIHAN_AGAMA, 
 wxID_EDIT_ANGGOTAPILIHAN_DIFABELITAS, 
 wxID_EDIT_ANGGOTAPILIHAN_GOLONGAN_DARAH, 
 wxID_EDIT_ANGGOTAPILIHAN_JENIS_KELAMIN, wxID_EDIT_ANGGOTAPILIHAN_KEHAMILAN, 
 wxID_EDIT_ANGGOTAPILIHAN_KONTRASEPSI, wxID_EDIT_ANGGOTAPILIHAN_PEKERJAAN, 
 wxID_EDIT_ANGGOTAPILIHAN_PEKERJAAN_LAINNYA, 
 wxID_EDIT_ANGGOTAPILIHAN_PENDIDIKAN_DITEMPUH, 
 wxID_EDIT_ANGGOTAPILIHAN_PENDIDIKAN_TERAKHIR, wxID_EDIT_ANGGOTAPILIHAN_SHDK, 
 wxID_EDIT_ANGGOTAPILIHAN_STATUS, 
 wxID_EDIT_ANGGOTAPILIHAN_STATUS_KEPENDUDUKAN, 
 wxID_EDIT_ANGGOTAPILIHAN_STATUS_TINGGAL, 
 wxID_EDIT_ANGGOTAPILIHAN_WARGANEGARA, wxID_EDIT_ANGGOTAPROPINSI, 
 wxID_EDIT_ANGGOTASIMPANGAMBAR, wxID_EDIT_ANGGOTASTATICTEXT1, 
 wxID_EDIT_ANGGOTASTATICTEXT10, wxID_EDIT_ANGGOTASTATICTEXT11, 
 wxID_EDIT_ANGGOTASTATICTEXT12, wxID_EDIT_ANGGOTASTATICTEXT2, 
 wxID_EDIT_ANGGOTASTATICTEXT3, wxID_EDIT_ANGGOTASTATICTEXT4, 
 wxID_EDIT_ANGGOTASTATICTEXT5, wxID_EDIT_ANGGOTASTATICTEXT6, 
 wxID_EDIT_ANGGOTASTATICTEXT7, wxID_EDIT_ANGGOTASTATICTEXT8, 
 wxID_EDIT_ANGGOTASTATICTEXT9, wxID_EDIT_ANGGOTATANGGAL_LAHIR, 
 wxID_EDIT_ANGGOTATGLLAHIR, wxID_EDIT_ANGGOTATOMBOL_CARI, 
 wxID_EDIT_ANGGOTATOMBOL_HAPUS_DATA, 
] = [wx.NewId() for _init_ctrls in range(88)]

class edit_anggota(wx.Dialog):
    def _init_coll_isipenduduk_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT,
              heading='Nomor NIK', width=150)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT,
              heading='Nomor KK', width=250)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT,
              heading='Nama Lengkap', width=260)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_LEFT, heading='Alamat',
              width=180)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_EDIT_ANGGOTA, name=u'edit_anggota',
              parent=prnt, pos=wx.Point(456, 167), size=wx.Size(824, 530),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Edit Anggota Keluarga')
        self.SetClientSize(wx.Size(816, 500))
        self.Center(wx.BOTH)
        self.SetBackgroundColour(wx.Colour(192, 192, 192))

        self.label_nomor_kk = wx.StaticText(id=wxID_EDIT_ANGGOTALABEL_NOMOR_KK,
              label=u'Nomor KK', name=u'label_nomor_kk', parent=self,
              pos=wx.Point(8, 126), size=wx.Size(168, 17), style=0)

        self.input_no_kk = wx.TextCtrl(id=wxID_EDIT_ANGGOTAINPUT_NO_KK,
              name=u'input_no_kk', parent=self, pos=wx.Point(91, 124),
              size=wx.Size(240, 21), style=wx.TE_READONLY, value=u'')

        self.input_alamat = wx.TextCtrl(id=wxID_EDIT_ANGGOTAINPUT_ALAMAT,
              name=u'input_alamat', parent=self, pos=wx.Point(91, 145),
              size=wx.Size(240, 21), style=wx.TE_READONLY, value=u'')

        self.input_dusun = wx.TextCtrl(id=wxID_EDIT_ANGGOTAINPUT_DUSUN,
              name=u'input_dusun', parent=self, pos=wx.Point(91, 166),
              size=wx.Size(192, 21), style=wx.TE_READONLY, value=u'')

        self.label_alamat = wx.StaticText(id=wxID_EDIT_ANGGOTALABEL_ALAMAT,
              label=u'Alamat', name=u'label_alamat', parent=self,
              pos=wx.Point(8, 148), size=wx.Size(47, 12), style=0)

        self.label_dusun = wx.StaticText(id=wxID_EDIT_ANGGOTALABEL_DUSUN,
              label=u'Dusun', name=u'label_dusun', parent=self, pos=wx.Point(8,
              167), size=wx.Size(64, 11), style=0)

        self.input_nik = wx.TextCtrl(id=wxID_EDIT_ANGGOTAINPUT_NIK,
              name=u'input_nik', parent=self, pos=wx.Point(115, 188),
              size=wx.Size(200, 21), style=0, value=u'')

        self.lebel_nik = wx.StaticText(id=wxID_EDIT_ANGGOTALEBEL_NIK,
              label=u'N I K *', name=u'lebel_nik', parent=self, pos=wx.Point(8,
              190), size=wx.Size(40, 17), style=0)

        self.label_nama_lengkap = wx.StaticText(id=wxID_EDIT_ANGGOTALABEL_NAMA_LENGKAP,
              label=u'Nama Lengkap', name=u'label_nama_lengkap', parent=self,
              pos=wx.Point(8, 210), size=wx.Size(80, 13), style=0)

        self.input_nama = wx.TextCtrl(id=wxID_EDIT_ANGGOTAINPUT_NAMA,
              name=u'input_nama', parent=self, pos=wx.Point(115, 209),
              size=wx.Size(200, 22), style=0, value=u'')

        self.label_jenis_kelamin = wx.StaticText(id=wxID_EDIT_ANGGOTALABEL_JENIS_KELAMIN,
              label=u'Jenis Kelamin', name=u'label_jenis_kelamin', parent=self,
              pos=wx.Point(8, 233), size=wx.Size(80, 13), style=0)

        self.pilihan_jenis_kelamin = wx.ComboBox(choices=['L', 'P'],
              id=wxID_EDIT_ANGGOTAPILIHAN_JENIS_KELAMIN,
              name=u'pilihan_jenis_kelamin', parent=self, pos=wx.Point(115,
              231), size=wx.Size(200, 21), style=0)

        self.input_tempat_lahir = wx.TextCtrl(id=wxID_EDIT_ANGGOTAINPUT_TEMPAT_LAHIR,
              name=u'input_tempat_lahir', parent=self, pos=wx.Point(115, 252),
              size=wx.Size(200, 22), style=0, value=u'')

        self.label_tempat_lahir = wx.StaticText(id=wxID_EDIT_ANGGOTALABEL_TEMPAT_LAHIR,
              label=u'Tempat Lahir', name=u'label_tempat_lahir', parent=self,
              pos=wx.Point(8, 254), size=wx.Size(80, 13), style=0)

        self.label_tanggal_lahir = wx.StaticText(id=wxID_EDIT_ANGGOTALABEL_TANGGAL_LAHIR,
              label=u'Tanggal Lahir', name=u'label_tanggal_lahir', parent=self,
              pos=wx.Point(8, 276), size=wx.Size(80, 17), style=0)

        self.label_golongan_darah = wx.StaticText(id=wxID_EDIT_ANGGOTALABEL_GOLONGAN_DARAH,
              label=u'Golongan Darah', name=u'label_golongan_darah',
              parent=self, pos=wx.Point(8, 300), size=wx.Size(88, 17), style=0)

        self.tanggal_lahir = wx.TextCtrl(id=wxID_EDIT_ANGGOTATANGGAL_LAHIR,
              name=u'tanggal_lahir', parent=self, pos=wx.Point(115, 274),
              size=wx.Size(200, 22), style=0)

        self.pilihan_golongan_darah = wx.ComboBox(choices=['A', 'AB', 'B', 'O',
              'A+', 'A-', 'AB+', 'AB-', 'B+', 'B-', 'O+', 'O-', 'Tidak tahu'],
              id=wxID_EDIT_ANGGOTAPILIHAN_GOLONGAN_DARAH,
              name=u'pilihan_golongan_darah', parent=self, pos=wx.Point(115,
              296), size=wx.Size(80, 21), style=0)

        self.label_agama = wx.StaticText(id=wxID_EDIT_ANGGOTALABEL_AGAMA,
              label=u'Agama', name=u'label_agama', parent=self, pos=wx.Point(8,
              319), size=wx.Size(48, 13), style=0)

        self.pilihan_agama = wx.ComboBox(choices=['Islam', 'Kristen Protestan',
              'Kristen Katolik', 'Hindu', 'Budha', 'Konghuchu',
              'Aliran Kepercayaan', 'Agama Lainnya'],
              id=wxID_EDIT_ANGGOTAPILIHAN_AGAMA, name=u'pilihan_agama',
              parent=self, pos=wx.Point(115, 316), size=wx.Size(200, 21),
              style=0)

        self.label_kewarganegaraan = wx.StaticText(id=wxID_EDIT_ANGGOTALABEL_KEWARGANEGARAAN,
              label=u'Kewarganegaraan', name=u'label_kewarganegaraan',
              parent=self, pos=wx.Point(8, 341), size=wx.Size(104, 13),
              style=0)

        self.pilihan_warganegara = wx.ComboBox(choices=['WNI', 'WNA'],
              id=wxID_EDIT_ANGGOTAPILIHAN_WARGANEGARA,
              name=u'pilihan_warganegara', parent=self, pos=wx.Point(115, 337),
              size=wx.Size(200, 21), style=0)

        self.label_pendidikan_terakhir = wx.StaticText(id=wxID_EDIT_ANGGOTALABEL_PENDIDIKAN_TERAKHIR,
              label=u'Pendidikan Terakhir', name=u'label_pendidikan_terakhir',
              parent=self, pos=wx.Point(8, 363), size=wx.Size(101, 17),
              style=0)

        self.pilihan_pendidikan_terakhir = wx.ComboBox(choices=['Tidak/Belum Sekolah',
              'Tidak Tamat SD/Sederajat', 'Tamat SD/Sederajat',
              'SLTP/Sederajat', 'SLTA/Sederajat', 'Diploma I/II',
              'Akademi/Diploma III/S. Muda', 'Diploma IV/Strata I', 'Strata II',
              'Strata III', 'Pendidikan Non Formal'],
              id=wxID_EDIT_ANGGOTAPILIHAN_PENDIDIKAN_TERAKHIR,
              name=u'pilihan_pendidikan_terakhir', parent=self,
              pos=wx.Point(115, 358), size=wx.Size(200, 21), style=0)

        self.label_pendidikan_tempuh = wx.StaticText(id=wxID_EDIT_ANGGOTALABEL_PENDIDIKAN_TEMPUH,
              label=u'Pendidikan Saat Ini ', name=u'label_pendidikan_tempuh',
              parent=self, pos=wx.Point(8, 384), size=wx.Size(95, 13), style=0)

        self.pilihan_pendidikan_ditempuh = wx.ComboBox(choices=['PAUD sederajat',
              'TK Sederajat', 'SD Sederajat', 'SLTP Sederajat',
              'SLTA Sederajat', 'D1 Sederajat', 'D2 Sederajat', 'D3 Sederajat' ,
              'S1 Sederajat' , 'S2 Sederajat' , 'S3 Sederajat' ,
              'Pendidikan Non Formal'],
              id=wxID_EDIT_ANGGOTAPILIHAN_PENDIDIKAN_DITEMPUH,
              name=u'pilihan_pendidikan_ditempuh', parent=self,
              pos=wx.Point(115, 379), size=wx.Size(200, 21), style=0)

        self.label_pekerjaan = wx.StaticText(id=wxID_EDIT_ANGGOTALABEL_PEKERJAAN,
              label=u'Pekerjaan Utama', name=u'label_pekerjaan', parent=self,
              pos=wx.Point(7, 404), size=wx.Size(93, 17), style=0)

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
              id=wxID_EDIT_ANGGOTAPILIHAN_PEKERJAAN, name=u'pilihan_pekerjaan',
              parent=self, pos=wx.Point(115, 400), size=wx.Size(200, 21),
              style=0)

        self.label_pekerjaan_lainnya = wx.StaticText(id=wxID_EDIT_ANGGOTALABEL_PEKERJAAN_LAINNYA,
              label=u'Pekerjaan Lainnya', name=u'label_pekerjaan_lainnya',
              parent=self, pos=wx.Point(6, 424), size=wx.Size(101, 17),
              style=0)

        self.pilihan_pekerjaan_lainnya = wx.ComboBox(choices=['Berdagang',
              'Bertani', 'Berkebun', 'Jasa  profesional  tukang', 'Seniman',
              'Lainnya'], id=wxID_EDIT_ANGGOTAPILIHAN_PEKERJAAN_LAINNYA,
              name=u'pilihan_pekerjaan_lainnya', parent=self, pos=wx.Point(115,
              421), size=wx.Size(200, 21), style=0)

        self.label_status_perkawinan = wx.StaticText(id=wxID_EDIT_ANGGOTALABEL_STATUS_PERKAWINAN,
              label=u'Status Perkawinan', name=u'label_status_perkawinan',
              parent=self, pos=wx.Point(7, 444), size=wx.Size(100, 16),
              style=0)

        self.pilihan_status = wx.ComboBox(choices=['Belum Kawin', 'Kawin',
              'Cerai Mati', 'Cerai Hidup'], parent=self, pos=wx.Point(116, 442),
              size=wx.Size(198, 21), style=0)

        self.label_status_kependudukan = wx.StaticText(id=wxID_EDIT_ANGGOTALABEL_STATUS_KEPENDUDUKAN,
              label=u'Status Kependudukan', name=u'label_status_kependudukan',
              parent=self, pos=wx.Point(322, 193), size=wx.Size(112, 18),
              style=0)

        self.pilihan_status_kependudukan = wx.ComboBox(choices=['Penduduk Tetap',
              'Penduduk Sementara', 'Penduduk Pindah/Pindahan'],
              id=wxID_EDIT_ANGGOTAPILIHAN_STATUS_KEPENDUDUKAN,
              name=u'pilihan_status_kependudukan', parent=self,
              pos=wx.Point(454, 189), size=wx.Size(200, 21), style=0)

        self.label_status_tinggal = wx.StaticText(id=wxID_EDIT_ANGGOTALABEL_STATUS_TINGGAL,
              label=u'Status Tinggal', name=u'label_status_tinggal',
              parent=self, pos=wx.Point(322, 214), size=wx.Size(88, 19),
              style=0)

        self.pilihan_status_tinggal = wx.ComboBox(choices=['Tinggal Tetap',
              'Tinggal Di Luar Desa*', 'Tinggal Di Luar Kota/Kabupaten',
              'Tinggal Di Luar Propinsi', 'Tinggal Di Luar Negeri'],
              id=wxID_EDIT_ANGGOTAPILIHAN_STATUS_TINGGAL,
              name=u'pilihan_status_tinggal', parent=self, pos=wx.Point(454,
              210), size=wx.Size(200, 21), style=0)

        self.label_difabelitas = wx.StaticText(id=wxID_EDIT_ANGGOTALABEL_DIFABELITAS,
              label=u'Penyandang Difabelitas', name=u'label_difabelitas',
              parent=self, pos=wx.Point(322, 233), size=wx.Size(120, 14),
              style=0)

        self.pilihan_difabelitas = wx.ComboBox(choices=['Tidak Cacat',
              'Cacat Fisik', 'Cacat Netra / Buta', 'Cacat Rungu/Wicara',
              'Cacat Mental/Jiwa', 'Cacat Fisik/Mental', 'Cacat Lainnya'],
              id=wxID_EDIT_ANGGOTAPILIHAN_DIFABELITAS,
              name=u'pilihan_difabelitas', parent=self, pos=wx.Point(454, 231),
              size=wx.Size(200, 21), style=0)

        self.label_kontrasepsi = wx.StaticText(id=wxID_EDIT_ANGGOTALABEL_KONTRASEPSI,
              label=u'Penggunaan Kontrasepsi', name=u'label_kontrasepsi',
              parent=self, pos=wx.Point(324, 254), size=wx.Size(128, 14),
              style=0)

        self.pilihan_kontrasepsi = wx.ComboBox(choices=['Pil', 'Suntik', 'IUD',
              'Kondom', 'Implant', 'MOP'],
              id=wxID_EDIT_ANGGOTAPILIHAN_KONTRASEPSI,
              name=u'pilihan_kontrasepsi', parent=self, pos=wx.Point(454, 252),
              size=wx.Size(200, 21), style=0)

        self.label_shdk = wx.StaticText(id=wxID_EDIT_ANGGOTALABEL_SHDK,
              label=u'SHDK', name=u'label_shdk', parent=self, pos=wx.Point(661,
              347), size=wx.Size(27, 13), style=0)

        self.pilihan_shdk = wx.ComboBox(choices=['Anak', 'Istri', 'Suami',
              'Mertua', 'Menantu', 'Famili lain', 'Lainnya'],
              id=wxID_EDIT_ANGGOTAPILIHAN_SHDK, name=u'pilihan_shdk',
              parent=self, pos=wx.Point(658, 364), size=wx.Size(150, 21),
              style=0)

        self.label_nama_ayah = wx.StaticText(id=wxID_EDIT_ANGGOTALABEL_NAMA_AYAH,
              label=u'Nama Ayah', name=u'label_nama_ayah', parent=self,
              pos=wx.Point(661, 387), size=wx.Size(152, 13), style=0)

        self.input_ayah = wx.TextCtrl(id=wxID_EDIT_ANGGOTAINPUT_AYAH,
              name=u'input_ayah', parent=self, pos=wx.Point(659, 403),
              size=wx.Size(149, 21), style=0, value=u'')

        self.label_nama_ibu = wx.StaticText(id=wxID_EDIT_ANGGOTALABEL_NAMA_IBU,
              label=u'Nama Ibu', name=u'label_nama_ibu', parent=self,
              pos=wx.Point(663, 425), size=wx.Size(160, 17), style=0)

        self.input_ibu = wx.TextCtrl(id=wxID_EDIT_ANGGOTAINPUT_IBU,
              name=u'input_ibu', parent=self, pos=wx.Point(659, 441),
              size=wx.Size(149, 21), style=0, value=u'')

        self.label_resiko_kehamilan = wx.StaticText(id=wxID_EDIT_ANGGOTALABEL_RESIKO_KEHAMILAN,
              label=u'Resiko Kehamilan', name=u'label_resiko_kehamilan',
              parent=self, pos=wx.Point(323, 276), size=wx.Size(88, 17),
              style=0)

        self.pilihan_kehamilan = wx.ComboBox(choices=['Resiko Tinggi',
              'Tidak Resiko Tinggi'], id=wxID_EDIT_ANGGOTAPILIHAN_KEHAMILAN,
              name=u'pilihan_kehamilan', parent=self, pos=wx.Point(454, 273),
              size=wx.Size(200, 21), style=0)

        self.tombol_hapus_data = wx.Button(id=wxID_EDIT_ANGGOTATOMBOL_HAPUS_DATA,
              label=u'Hapus Data', name=u'tombol_hapus_data', parent=self,
              pos=wx.Point(504, 471), size=wx.Size(144, 24), style=0)
        self.tombol_hapus_data.Bind(wx.EVT_BUTTON,
              self.OnTombol_hapus_dataButton,
              id=wxID_EDIT_ANGGOTATOMBOL_HAPUS_DATA)

        self.kembali = wx.Button(id=wxID_EDIT_ANGGOTAKEMBALI,
              label=u'Kembali Ke Menu', name=u'kembali', parent=self,
              pos=wx.Point(656, 471), size=wx.Size(152, 25), style=0)
        self.kembali.Bind(wx.EVT_BUTTON, self.OnKembaliButton,
              id=wxID_EDIT_ANGGOTAKEMBALI)

        self.dokumen = wx.StaticText(id=wxID_EDIT_ANGGOTADOKUMEN,
              label=u'Kepemilikan Dokumen', name=u'dokumen', parent=self,
              pos=wx.Point(322, 297), size=wx.Size(106, 17), style=0)

        self.isipenduduk = wx.ListCtrl(id=wxID_EDIT_ANGGOTAISIPENDUDUK,
              name=u'isipenduduk', parent=self, pos=wx.Point(8, 8),
              size=wx.Size(800, 112), style=wx.LC_REPORT)
        self._init_coll_isipenduduk_Columns(self.isipenduduk)
        self.isipenduduk.Bind(wx.EVT_LIST_ITEM_SELECTED,
              self.OnIsipendudukListItemSelected,
              id=wxID_EDIT_ANGGOTAISIPENDUDUK)

        self.staticText1 = wx.StaticText(id=wxID_EDIT_ANGGOTASTATICTEXT1,
              label=u'Nomor Induk Kependudukan', name='staticText1',
              parent=self, pos=wx.Point(450, 128), size=wx.Size(136, 17),
              style=0)

        self.cari_kk = wx.TextCtrl(id=wxID_EDIT_ANGGOTACARI_KK, name=u'cari_kk',
              parent=self, pos=wx.Point(592, 128), size=wx.Size(120, 21),
              style=0, value='')

        self.tombol_cari = wx.Button(id=wxID_EDIT_ANGGOTATOMBOL_CARI,
              label=u'Cari', name=u'tombol_cari', parent=self, pos=wx.Point(720,
              128), size=wx.Size(85, 24), style=0)
        self.tombol_cari.Bind(wx.EVT_BUTTON, self.OnTombol_cariButton,
              id=wxID_EDIT_ANGGOTATOMBOL_CARI)

        self.input_rt = wx.TextCtrl(id=wxID_EDIT_ANGGOTAINPUT_RT,
              name=u'input_rt', parent=self, pos=wx.Point(309, 166),
              size=wx.Size(56, 21), style=0, value=u'')

        self.input_rw = wx.TextCtrl(id=wxID_EDIT_ANGGOTAINPUT_RW,
              name=u'input_rw', parent=self, pos=wx.Point(391, 166),
              size=wx.Size(56, 21), style=0, value=u'')

        self.staticText2 = wx.StaticText(id=wxID_EDIT_ANGGOTASTATICTEXT2,
              label=u'RT', name='staticText2', parent=self, pos=wx.Point(288,
              171), size=wx.Size(16, 16), style=0)

        self.staticText3 = wx.StaticText(id=wxID_EDIT_ANGGOTASTATICTEXT3,
              label=u'RW', name='staticText3', parent=self, pos=wx.Point(369,
              171), size=wx.Size(19, 17), style=0)

        self.dokumen1 = wx.ComboBox(choices=['Akta Kelahiran'],
              id=wxID_EDIT_ANGGOTADOKUMEN1, name=u'dokumen1', parent=self,
              pos=wx.Point(454, 294), size=wx.Size(200, 21), style=0, value='')

        self.dokumen3 = wx.ComboBox(choices=['Akta Cerai'],
              id=wxID_EDIT_ANGGOTADOKUMEN3, name=u'dokumen3', parent=self,
              pos=wx.Point(454, 315), size=wx.Size(200, 21), style=0, value='')

        self.dokumen5 = wx.ComboBox(choices=['KTP Sementara'],
              id=wxID_EDIT_ANGGOTADOKUMEN5, name=u'dokumen5', parent=self,
              pos=wx.Point(454, 378), size=wx.Size(200, 21), style=0, value='')

        self.dokumen7 = wx.ComboBox(choices=['VISA'],
              id=wxID_EDIT_ANGGOTADOKUMEN7, name=u'dokumen7', parent=self,
              pos=wx.Point(454, 420), size=wx.Size(200, 21), style=0, value='')

        self.dokumen2 = wx.ComboBox(choices=['Akta Nikah'],
              id=wxID_EDIT_ANGGOTADOKUMEN2, name=u'dokumen2', parent=self,
              pos=wx.Point(454, 336), size=wx.Size(200, 21), style=0, value='')

        self.dokumen4 = wx.ComboBox(choices=['Akta Kematian'],
              id=wxID_EDIT_ANGGOTADOKUMEN4, name=u'dokumen4', parent=self,
              pos=wx.Point(454, 357), size=wx.Size(200, 21), style=0, value='')

        self.dokumen6 = wx.ComboBox(choices=['KITAS'],
              id=wxID_EDIT_ANGGOTADOKUMEN6, name=u'dokumen6', parent=self,
              pos=wx.Point(454, 399), size=wx.Size(200, 21), style=0, value='')

        self.dokumen8 = wx.ComboBox(choices=['Paspor'],
              id=wxID_EDIT_ANGGOTADOKUMEN8, name=u'dokumen8', parent=self,
              pos=wx.Point(454, 441), size=wx.Size(200, 21), style=0, value='')

        self.tgllahir = wx.TextCtrl(id=wxID_EDIT_ANGGOTATGLLAHIR,
              name=u'tgllahir', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(112, 27), style=0, value=u'')

        self.nama_kk = wx.TextCtrl(id=wxID_EDIT_ANGGOTANAMA_KK, name=u'nama_kk',
              parent=self, pos=wx.Point(563, 168), size=wx.Size(243, 21),
              style=wx.TE_READONLY, value=u'')

        self.staticText5 = wx.StaticText(id=wxID_EDIT_ANGGOTASTATICTEXT5,
              label=u'Nama Kepala Keluarga', name='staticText5', parent=self,
              pos=wx.Point(452, 168), size=wx.Size(107, 15), style=0)

        self.gambar = wx.TextCtrl(id=wxID_EDIT_ANGGOTAGAMBAR, name=u'gambar',
              parent=self, pos=wx.Point(657, 293), size=wx.Size(152, 21),
              style=0, value=u'')

        self.simpangambar = wx.TextCtrl(id=wxID_EDIT_ANGGOTASIMPANGAMBAR,
              name=u'simpangambar', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(152, 24), style=0, value=u'/opt/sidesa/penduduk')

        self.button1 = wx.Button(id=wxID_EDIT_ANGGOTABUTTON1,
              label=u'Upload Photo', name='button1', parent=self,
              pos=wx.Point(657, 317), size=wx.Size(152, 24), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_EDIT_ANGGOTABUTTON1)

        self.propinsi = wx.TextCtrl(id=wxID_EDIT_ANGGOTAPROPINSI,
              name=u'propinsi', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(152, 24), style=0, value=u'')

        self.kabupaten = wx.TextCtrl(id=wxID_EDIT_ANGGOTAKABUPATEN,
              name=u'kabupaten', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(152, 24), style=0, value=u'')

        self.kecamatan = wx.TextCtrl(id=wxID_EDIT_ANGGOTAKECAMATAN,
              name=u'kecamatan', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(152, 24), style=0, value=u'')

        self.desa = wx.TextCtrl(id=wxID_EDIT_ANGGOTADESA, name=u'desa',
              parent=self, pos=wx.Point(-100, -100), size=wx.Size(152, 24),
              style=0, value=u'')

        self.input_no = wx.TextCtrl(id=wxID_EDIT_ANGGOTAINPUT_NO,
              name=u'input_no', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(56, 27), style=wx.TE_READONLY, value=u'')

        self.button2 = wx.Button(id=wxID_EDIT_ANGGOTABUTTON2,
              label=u'Update Data', name='button2', parent=self,
              pos=wx.Point(352, 471), size=wx.Size(144, 24), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnTombol_tambah_dataButton,
              id=wxID_EDIT_ANGGOTABUTTON2)

        self.staticText4 = wx.StaticText(id=wxID_EDIT_ANGGOTASTATICTEXT4,
              label=u'1.', name='staticText4', parent=self, pos=wx.Point(432,
              296), size=wx.Size(10, 13), style=0)

        self.staticText6 = wx.StaticText(id=wxID_EDIT_ANGGOTASTATICTEXT6,
              label=u'2.', name='staticText6', parent=self, pos=wx.Point(432,
              318), size=wx.Size(10, 13), style=0)

        self.staticText7 = wx.StaticText(id=wxID_EDIT_ANGGOTASTATICTEXT7,
              label=u'3.', name='staticText7', parent=self, pos=wx.Point(432,
              340), size=wx.Size(10, 13), style=0)

        self.staticText8 = wx.StaticText(id=wxID_EDIT_ANGGOTASTATICTEXT8,
              label=u'4.', name='staticText8', parent=self, pos=wx.Point(432,
              360), size=wx.Size(10, 13), style=0)

        self.staticText9 = wx.StaticText(id=wxID_EDIT_ANGGOTASTATICTEXT9,
              label=u'5.', name='staticText9', parent=self, pos=wx.Point(432,
              381), size=wx.Size(10, 13), style=0)

        self.staticText10 = wx.StaticText(id=wxID_EDIT_ANGGOTASTATICTEXT10,
              label=u'6.', name='staticText10', parent=self, pos=wx.Point(432,
              402), size=wx.Size(10, 13), style=0)

        self.staticText11 = wx.StaticText(id=wxID_EDIT_ANGGOTASTATICTEXT11,
              label=u'7.', name='staticText11', parent=self, pos=wx.Point(432,
              424), size=wx.Size(10, 13), style=0)

        self.staticText12 = wx.StaticText(id=wxID_EDIT_ANGGOTASTATICTEXT12,
              label=u'8.', name='staticText12', parent=self, pos=wx.Point(433,
              444), size=wx.Size(11, 13), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.dataprofil()
        self.awal()  
    
    def awal(self):
        self.IsiList()
        self.loadgambar()
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
        self.dokumen1.SetValue('')
        self.dokumen2.SetValue('')
        self.dokumen3.SetValue('')
        self.dokumen4.SetValue('')
        self.dokumen5.SetValue('')
        self.dokumen6.SetValue('')
        self.dokumen7.SetValue('')
        self.dokumen8.SetValue('')
        self.gambar.SetValue('')
        self.cari_kk.SetValue('')
        self.nama_kk.SetValue('')
        self.input_no.SetValue('')
        self.simpangambar.SetValue('penduduk/')    
        
                       
    def IsiList(self):
        self.isipenduduk.DeleteAllItems()      
        sql = "SELECT * FROM penduduk WHERE shdk<>'Kepala Keluarga' AND kematian='Tidak' "
        cur.execute(sql) 
        hasil = cur.fetchall() 
        nokk = self.isipenduduk.GetItemCount() 
        for i in hasil : 
            self.isipenduduk.InsertStringItem(nokk, "%s"%i[1]) 
            self.isipenduduk.SetStringItem(nokk,1,"%s"%i[16]) 
            self.isipenduduk.SetStringItem(nokk,2,"%s"%i[2])
            self.isipenduduk.SetStringItem(nokk,3,"%s"%i[21])
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
            self.dokumen1.SetValue(str(hasil[41]))
            self.dokumen2.SetValue(str(hasil[42]))
            self.dokumen3.SetValue(str(hasil[43]))
            self.dokumen4.SetValue(str(hasil[44]))
            self.dokumen5.SetValue(str(hasil[45]))
            self.dokumen6.SetValue(str(hasil[46]))
            self.dokumen7.SetValue(str(hasil[47]))
            self.dokumen8.SetValue(str(hasil[48]))
            self.gambar.SetValue(str(hasil[57]))
            self.input_no.SetValue(str(hasil[0]))
            self.onView()
            
        else : 
            self.pesan = wx.MessageDialog(self,"Data Tidak Ada","Konfirmasi",wx.OK) 
            self.pesan.ShowModal() 
            self.cari_kk.Clear()
            self.cari_kk.SetFocus()
        
   
    def OnTombol_kembali_kemenuButton(self, event):
        self.main=data_penduduk.create(None)
        self.main.Show()
        self.Close()
        self.Destroy()
    
    def loadgambar(self):
        self.PhotoMaxSize = 100
        img = wx.EmptyImage(100,100)
        self.imageCtrl = wx.StaticBitmap(self, wx.ID_ANY, wx.BitmapFromImage(img),wx.Point(680, 190))
  
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
        tgllahir = str(self.tanggal_lahir.GetValue())
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
        namakk = str(self.nama_kk.GetValue())
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
        nom = str(self.input_no.GetValue())
        
        #dataprofilget
        propinsi = str(self.propinsi.GetValue())
        kabupaten = str(self.kabupaten.GetValue())
        kecamatan = str(self.kecamatan.GetValue())
        desa = str(self.desa.GetValue())
        
        if filepath == '':
            add_keluarga="UPDATE penduduk SET nik='"+nik+"', nama='"+nama+"', jk='"+jk+"', tmpt_lahir='"+tmplahir+"', tgl_lahir='"+tgllahir+"', umur='"+''+"', gdr='"+gdr+"', agama='"+agama+"', status='"+status+"', shdk='"+shdk+"', shdrt='"+''+"', pddk_akhir='"+pddkakhir+"', pekerjaan='"+pekerjaan+"', nama_ibu='"+ibu+"', nama_ayah='"+ayah+"', no_kk='"+nokk+"', nama_kep_kel='"+namakk+"', petugas='"+''+"', pekerjaan_lain='"+pekerjaanlain+"', nama_petugas='', alamat='"+alamat+"', nama_prop='"+propinsi+"', nama_kab='"+kabupaten+"', nama_kec='"+kecamatan+"', nama_kel='"+desa+"', rt='"+rt+"', rw='"+rw+"', warganegara='"+warganegara+"', nama_dusun='"+dusun+"', kemiskinan='Tidak Miskin', pddk_saat_ini='"+pddktempuh+"', status_pddk='"+statuskependudukan+"', status_tgl='"+statustinggal+"', difabelitas='"+difabelitas+"', kontrasepsi='"+kontrasepsi+"', resiko='"+kehamilan+"', kelahiran='"+''+"', kematian='Tidak', kejadianlain='"+''+"', pindah='"+''+"', dok1='"+dok1+"', dok2='"+dok2+"', dok3='"+dok3+"', dok4='"+dok4+"', dok5='"+dok5+"', dok6='"+dok6+"', dok7='"+dok7+"', dok8='"+dok8+"', promis1='', promis2='',promis3='', promis4='', promis5='', promis6='', promis7='', promis8='', photo='"+gbr+"blank.jpg', keterangan='' WHERE no='"+nom+"'"        
            cur.execute(add_keluarga)
            db.commit()
            self.pesan = wx.MessageDialog(self,"Data Sudah Terupdate","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.awal()
        
        elif filepath == gbr+nik+'.jpg':
            add_keluarga="UPDATE penduduk SET nik='"+nik+"', nama='"+nama+"', jk='"+jk+"', tmpt_lahir='"+tmplahir+"', tgl_lahir='"+tgllahir+"', umur='', gdr='"+gdr+"', agama='"+agama+"', status='"+status+"', shdk='"+shdk+"', shdrt='', pddk_akhir='"+pddkakhir+"', pekerjaan='"+pekerjaan+"', nama_ibu='"+ibu+"', nama_ayah='"+ayah+"', no_kk='"+nokk+"', nama_kep_kel='"+namakk+"', petugas='', pekerjaan_lain='"+pekerjaanlain+"', nama_petugas='', alamat='"+alamat+"', nama_prop='"+propinsi+"', nama_kab='"+kabupaten+"', nama_kec='"+kecamatan+"', nama_kel='"+desa+"', rt='"+rt+"', rw='"+rw+"', warganegara='"+warganegara+"', nama_dusun='"+dusun+"', kemiskinan='Tidak Miskin', pddk_saat_ini='"+pddktempuh+"', status_pddk='"+statuskependudukan+"', status_tgl='"+statustinggal+"', difabelitas='"+difabelitas+"', kontrasepsi='"+kontrasepsi+"', resiko='"+kehamilan+"', kelahiran='', kematian='Tidak', kejadianlain='', pindah='', dok1='"+dok1+"', dok2='"+dok2+"', dok3='"+dok3+"', dok4='"+dok4+"', dok5='"+dok5+"', dok6='"+dok6+"', dok7='"+dok7+"', dok8='"+dok8+"', promis1='', promis2='',promis3='', promis4='', promis5='', promis6='', promis7='', promis8='', photo='"+gbr+nik+".jpg', keterangan='' WHERE no='"+nom+"'"        
            cur.execute(add_keluarga)
            db.commit()
            self.pesan = wx.MessageDialog(self,"Data Sudah Terupdate","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.awal()
        
        elif filepath == gbr+'blank.jpg':
            add_keluarga="UPDATE penduduk SET nik='"+nik+"' , nama='"+nama+"' , jk='"+jk+"', tmpt_lahir='"+tmplahir+"', tgl_lahir='"+tgllahir+"', umur='', gdr='"+gdr+"', agama='"+agama+"', status='"+status+"', shdk='"+shdk+"', shdrt='', pddk_akhir='"+pddkakhir+"', pekerjaan='"+pekerjaan+"', nama_ibu='"+ibu+"', nama_ayah='"+ayah+"', no_kk='"+nokk+"', nama_kep_kel='"+namakk+"', petugas='"+''+"', pekerjaan_lain='"+pekerjaanlain+"', nama_petugas='"+''+"', alamat='"+alamat+"', nama_prop='"+propinsi+"', nama_kab='"+kabupaten+"', nama_kec='"+kecamatan+"', nama_kel='"+desa+"', rt='"+rt+"', rw='"+rw+"', warganegara='"+warganegara+"', nama_dusun='"+dusun+"', kemiskinan='Tidak Miskin', pddk_saat_ini='"+pddktempuh+"', status_pddk='"+statuskependudukan+"', status_tgl='"+statustinggal+"', difabelitas='"+difabelitas+"', kontrasepsi='"+kontrasepsi+"', resiko='"+kehamilan+"', kelahiran='', kematian='Tidak', kejadianlain='', pindah='', dok1='"+dok1+"', dok2='"+dok2+"', dok3='"+dok3+"', dok4='"+dok4+"', dok5='"+dok5+"', dok6='"+dok6+"', dok7='"+dok7+"', dok8='"+dok8+"', promis1='', promis2='',promis3='', promis4='', promis5='', promis6='', promis7='', promis8='', photo='"+gbr+"blank.jpg', keterangan='' WHERE no = '"+nom+"'"        
            cur.execute(add_keluarga)
            db.commit()
            self.pesan = wx.MessageDialog(self,"Data Sudah Tersimpan","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.awal()        
            
        else:
            shutil.copy2(filepath, gbr+nik+'.jpg')
            add_keluarga="UPDATE penduduk SET nik='"+nik+"', nama='"+nama+"', jk='"+jk+"', tmpt_lahir='"+tmplahir+"', tgl_lahir='"+tgllahir+"', umur='', gdr='"+gdr+"', agama='"+agama+"', status='"+status+"', shdk='"+shdk+"', shdrt='', pddk_akhir='"+pddkakhir+"', pekerjaan='"+pekerjaan+"', nama_ibu='"+ibu+"', nama_ayah='"+ayah+"', no_kk='"+nokk+"', nama_kep_kel='"+namakk+"', petugas='', pekerjaan_lain='"+pekerjaanlain+"', nama_petugas='', alamat='"+alamat+"', nama_prop='"+propinsi+"', nama_kab='"+kabupaten+"', nama_kec='"+kecamatan+"', nama_kel='"+desa+"', rt='"+rt+"', rw='"+rw+"', warganegara='"+warganegara+"', nama_dusun='"+dusun+"', kemiskinan='Tidak Miskin', pddk_saat_ini='"+pddktempuh+"', status_pddk='"+statuskependudukan+"', status_tgl='"+statustinggal+"', difabelitas='"+difabelitas+"', kontrasepsi='"+kontrasepsi+"', resiko='"+kehamilan+"', kelahiran='', kematian='Tidak', kejadianlain='', pindah='', dok1='"+dok1+"', dok2='"+dok2+"', dok3='"+dok3+"', dok4='"+dok4+"', dok5='"+dok5+"', dok6='"+dok6+"', dok7='"+dok7+"', dok8='"+dok8+"', promis1='', promis2='',promis3='', promis4='', promis5='', promis6='', promis7='', promis8='', photo='"+gbr+nik+".jpg', keterangan='' WHERE no='"+nom+"'"        
            cur.execute(add_keluarga)
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
        self.currentItem = event.m_itemIndex 
        b=self.isipenduduk.GetItem(self.currentItem).GetText() 
        self.cari_kk.SetValue(b) 
        self.Isi_Object()
        event.Skip()

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

    def OnTombol_hapus_dataButton(self, event):
        nom = str(self.input_no.GetValue())
        hapus="DELETE FROM penduduk WHERE no='"+nom+"'"
        cur.execute(hapus)
        db.commit()
        self.pesan = wx.MessageDialog(self,"Data Sudah Dihapus","Konfirmasi",wx.OK) 
        self.pesan.ShowModal()
        self.awal()

