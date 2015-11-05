#Boa:Frame:menuutama
#-------------------------------------------------------------------------------
#Sistem Informasi dan Administrasi Perdesaan
#pengembang johandri@ictwatch.id
#-------------------------------------------------------------------------------

import wx
import sys
sys.path.append('form/')

import edit_anggota
import kejadian_kelahiran
import kejadian_kematian
import input_data_kemiskinan
import input_indikator_kemiskinan
import apbdesa
import potensi_ekonomi
import potensi_pertahanan
import potensi_pariwisata
import importdata
import surat_masuk
import pembuatan_surat_keluar
import kunci
import input_profil
import pemberdayaanmasyarakat
import pembinaankemasyarakatan
import takterduga
import pembangunandesa
import penyelenggaraandesa
import pendapatanaslidesa
import pendapatanlainlain
import pendapatantransfer
import lihatpendapatan
import rpjmpembangunandesa
import rpjmpemberdayaanmasyarakat
import rpjmpembinaankemasyarakatan
import rpjmpenyelenggaraandesa
import rpjmtakterduga
import rkppembangunandesa
import rkppemberdayaanmasyarakat
import rkppembinaankemasyarakatan
import rkppenyelenggarandesa
import rkptakterduga
import laporanrpjmdes
import laporanrkp
import edit_kejadian_kelahiran
import edit_kejadian_kematian
import edit_kejadian_lain
import edit_kejadian_pindah
import kejadian_pindah
import kejadian_lain
import sinkron_data
import penerimaanpembiayaan
import pengeluaranpembiayaan
import apbdesa
import rab
import kaspembantu
import permintaanbayar
import tanggungbelanja
import kasumum
import kaspajak
import bankdesa
import kk_tetap
import edit_kk
import pecah_keluarga
import kk_sementara
import tambah_anggota_keluarga
import tentang
import jabatan
import namapejabat
import inputdatart
import os

import sqlite3
db = sqlite3.connect('siap.db')

def create(parent):
    return menuutama(parent)

[wxID_MENUUTAMA, wxID_MENUUTAMASTATICBITMAP1, 
] = [wx.NewId() for _init_ctrls in range(2)]

[wxID_FRAME1MENU1ITEMS10, wxID_FRAME1MENU1ITEMS3, wxID_FRAME1MENU1ITEMS4, 
 wxID_FRAME1MENU1ITEMS5, wxID_FRAME1MENU1ITEMS6, wxID_FRAME1MENU1ITEMS7, 
 wxID_FRAME1MENU1ITEMS8, wxID_FRAME1MENU1ITEMS9, 
] = [wx.NewId() for _init_coll_menu1_Items in range(8)]

[wxID_FRAME1MENU2ITEMS0, wxID_FRAME1MENU2ITEMS1, wxID_FRAME1MENU2ITEMS2, 
 wxID_FRAME1MENU2ITEMS3, wxID_FRAME1MENU2ITEMS4, wxID_FRAME1MENU2ITEMS5, 
 wxID_FRAME1MENU2ITEMS6, 
] = [wx.NewId() for _init_coll_menu2_Items in range(7)]

[wxID_FRAME1MENU3ITEMS0, wxID_FRAME1MENU3ITEMS1, 
] = [wx.NewId() for _init_coll_menu3_Items in range(2)]

[wxID_FRAME1MENU4ITEMS0, wxID_FRAME1MENU4ITEMS1, wxID_FRAME1MENU4ITEMS2, 
 wxID_FRAME1MENU4ITEMS2, 
] = [wx.NewId() for _init_coll_menu4_Items in range(4)]

[wxID_FRAME1MENU5ITEMS0, wxID_FRAME1MENU5ITEMS1, wxID_FRAME1MENU5ITEMS2, 
] = [wx.NewId() for _init_coll_menu5_Items in range(3)]

[wxID_FRAME1MENU6ITEMS0, wxID_FRAME1MENU6ITEMS1, wxID_FRAME1MENU6ITEMS2, 
] = [wx.NewId() for _init_coll_menu6_Items in range(3)]

[wxID_FRAME1MENU7ITEMS0, wxID_FRAME1MENU7ITEMS1, wxID_FRAME1MENU7ITEMS2, 
 wxID_FRAME1MENU7ITEMS3, wxID_FRAME1MENU7ITEMS4, wxID_FRAME1MENU7ITEMS5, 
 wxID_FRAME1MENU7ITEMS6, wxID_FRAME1MENU7ITEMS7, wxID_FRAME1MENU7ITEMS8, 
] = [wx.NewId() for _init_coll_menu7_Items in range(9)]

[wxID_FRAME1MENU8ITEMS0, wxID_FRAME1MENU8ITEMS1, wxID_FRAME1MENU8ITEMS2, 
 wxID_FRAME1MENU8ITEMS3, wxID_FRAME1MENU8ITEMS4, wxID_FRAME1MENU8ITEMS5, 
 wxID_FRAME1MENU8ITEMS6, wxID_FRAME1MENU8ITEMS7, 
] = [wx.NewId() for _init_coll_menu8_Items in range(8)]

[wxID_FRAME1MENU9ITEMS0, wxID_FRAME1MENU9ITEMS1, wxID_FRAME1MENU9ITEMS2, 
 wxID_FRAME1MENU9ITEMS3, wxID_FRAME1MENU9ITEMS4, wxID_FRAME1MENU9ITEMS5, 
 wxID_FRAME1MENU9ITEMS6, wxID_FRAME1MENU9ITEMS7, 
] = [wx.NewId() for _init_coll_menu9_Items in range(8)]

[wxID_FRAME1MENU10ITEMS0, wxID_FRAME1MENU10ITEMS1, wxID_FRAME1MENU10ITEMS2, 
] = [wx.NewId() for _init_coll_menu10_Items in range(3)]

[wxID_FRAME1MENU11ITEMS0, wxID_FRAME1MENU11ITEMS1, wxID_FRAME1MENU11ITEMS2, 
] = [wx.NewId() for _init_coll_menu11_Items in range(3)]

[wxID_FRAME1MENU12ITEMS0, wxID_FRAME1MENU12ITEMS1, wxID_FRAME1MENU12ITEMS2, 
] = [wx.NewId() for _init_coll_menu12_Items in range(3)]

[wxID_FRAME1MENU13ITEMS0, wxID_FRAME1MENU13ITEMS1, wxID_FRAME1MENU13ITEMS2, 
] = [wx.NewId() for _init_coll_menu13_Items in range(3)]

[wxID_FRAME1MENU14ITEMS0, wxID_FRAME1MENU14ITEMS1, wxID_FRAME1MENU14ITEMS2, 
] = [wx.NewId() for _init_coll_menu14_Items in range(3)]

[wxID_FRAME1MENU15ITEMS0, wxID_FRAME1MENU15ITEMS1, wxID_FRAME1MENU15ITEMS2, 
] = [wx.NewId() for _init_coll_menu15_Items in range(3)]

[wxID_FRAME1MENU16ITEMS0, wxID_FRAME1MENU16ITEMS1, wxID_FRAME1MENU16ITEMS2, 
] = [wx.NewId() for _init_coll_menu16_Items in range(3)]

[wxID_FRAME1MENU17ITEMS0, wxID_FRAME1MENU17ITEMS1, 
] = [wx.NewId() for _init_coll_menu17_Items in range(2)]

[wxID_FRAME1ADMINISTRASIDANKEUANGANITEMS0, 
 wxID_FRAME1ADMINISTRASIDANKEUANGANITEMS1, 
 wxID_FRAME1ADMINISTRASIDANKEUANGANITEMS2, 
 wxID_FRAME1ADMINISTRASIDANKEUANGANITEMS3, 
 wxID_FRAME1ADMINISTRASIDANKEUANGANITEMS4, 
 wxID_FRAME1ADMINISTRASIDANKEUANGANITEMS5, 
 wxID_FRAME1ADMINISTRASIDANKEUANGANITEMS6, 
] = [wx.NewId() for _init_coll_administrasidankeuangan_Items in range(7)]

[wxID_MENUUTAMARPJMDESCETAKRPJMDES, 
 wxID_MENUUTAMARPJMDESRPJMBIDPENYELENGGARAN, 
 wxID_MENUUTAMARPJMDESRPJMPEMBDESA, wxID_MENUUTAMARPJMDESRPJMPEMBERDAYAAN, 
 wxID_MENUUTAMARPJMDESRPJMPEMBINAAN, wxID_MENUUTAMARPJMDESRPJMTAKTERDUGA, 
] = [wx.NewId() for _init_coll_rpjmdes_Items in range(6)]

[wxID_MENUUTAMAPERSURATANLPJDESA, wxID_MENUUTAMAPERSURATANPERDES, 
 wxID_MENUUTAMAPERSURATANSURATKELUAR, wxID_MENUUTAMAPERSURATANSURATMASUK, 
] = [wx.NewId() for _init_coll_persuratan_Items in range(4)]

[wxID_FRAME1MENUPOTENSIITEMS0, wxID_FRAME1MENUPOTENSIITEMS1, 
] = [wx.NewId() for _init_coll_menupotensi_Items in range(2)]

[wxID_MENUUTAMAPOTENSIEKONOMI, wxID_MENUUTAMAPOTENSIPERTAHANAN, 
 wxID_MENUUTAMAPOTENSISOSIALBUDAYA, 
] = [wx.NewId() for _init_coll_potensi_Items in range(3)]

[wxID_MENUUTAMAISIANGGOTAPERUBAHANANGGOTA, 
 wxID_MENUUTAMAISIANGGOTATAMBAHANGGOTAKELUARGA, 
] = [wx.NewId() for _init_coll_isianggota_Items in range(2)]

[wxID_MENUUTAMAISIKKEDITKK, wxID_MENUUTAMAISIKKKKSEMENTARA, 
 wxID_MENUUTAMAISIKKPECAHKK, wxID_MENUUTAMAISIKKTAMBAHKK, 
] = [wx.NewId() for _init_coll_isikk_Items in range(4)]

[wxID_MENUUTAMAKEMATIANRUBAH, wxID_MENUUTAMAKEMATIANTAMBAH, 
] = [wx.NewId() for _init_coll_kematian_Items in range(2)]

[wxID_MENUUTAMASTATISTIKADMINISTRASI, wxID_MENUUTAMASTATISTIKKEMISKINAN, 
 wxID_MENUUTAMASTATISTIKPENDUDUK, 
] = [wx.NewId() for _init_coll_statistik_Items in range(3)]

[wxID_MENUUTAMAMUTASIRUBAH, wxID_MENUUTAMAMUTASITAMBAH, 
] = [wx.NewId() for _init_coll_mutasi_Items in range(2)]

[wxID_MENUUTAMARKPLAPORANRKP, wxID_MENUUTAMARKPRKPPEMBANGUNAN, 
 wxID_MENUUTAMARKPRKPPEMBERDAYAAN, wxID_MENUUTAMARKPRKPPEMBINAAN, 
 wxID_MENUUTAMARKPRKPPENYELENGGARAN, wxID_MENUUTAMARKPRKPTAKTERDUGA, 
] = [wx.NewId() for _init_coll_rkp_Items in range(6)]

[wxID_FRAME1PROFILITEMS10, wxID_FRAME1PROFILITEMS3, wxID_FRAME1PROFILITEMS4, 
 wxID_FRAME1PROFILITEMS5, wxID_FRAME1PROFILITEMS6, wxID_FRAME1PROFILITEMS7, 
 wxID_FRAME1PROFILITEMS8, wxID_FRAME1PROFILITEMS9, 
] = [wx.NewId() for _init_coll_profil_Items in range(8)]

[wxID_MENUUTAMAKELAHIRANRUBAH, wxID_MENUUTAMAKELAHIRANTAMBAH, 
] = [wx.NewId() for _init_coll_kelahiran_Items in range(2)]

[wxID_MENUUTAMAISIPROFILDATAOL, wxID_MENUUTAMAISIPROFILEDITPROFILDESA, 
 wxID_MENUUTAMAISIPROFILINPUTPROFILDESA, wxID_MENUUTAMAISIPROFILITEMS5, 
 wxID_MENUUTAMAISIPROFILITEMS6, wxID_MENUUTAMAISIPROFILPASSWORD, 
] = [wx.NewId() for _init_coll_isiprofil_Items in range(6)]

[wxID_MENUUTAMAKODEREKENINGBIDANGPEMBANGUNAN, 
 wxID_MENUUTAMAKODEREKENINGBIDANGPEMBERDAYAAN, 
 wxID_MENUUTAMAKODEREKENINGBIDANGPEMBINAAN, 
 wxID_MENUUTAMAKODEREKENINGBIDANGPENYELENGGARAAN, 
 wxID_MENUUTAMAKODEREKENINGBIDANGTAKTERDUGA, 
 wxID_MENUUTAMAKODEREKENINGPEMBIAYAAN1, wxID_MENUUTAMAKODEREKENINGPEMBIAYAAN2, 
 wxID_MENUUTAMAKODEREKENINGPENDAPATANASLIDESA, 
 wxID_MENUUTAMAKODEREKENINGPENDAPATANLAINLAIN, 
 wxID_MENUUTAMAKODEREKENINGPENDAPATANTRANSFER, 
] = [wx.NewId() for _init_coll_koderekening_Items in range(10)]

[wxID_MENUUTAMAMENUPROFILDANPENDUDUKITEMS10, 
 wxID_MENUUTAMAMENUPROFILDANPENDUDUKITEMS4, 
 wxID_MENUUTAMAMENUPROFILDANPENDUDUKITEMS5, 
 wxID_MENUUTAMAMENUPROFILDANPENDUDUKITEMS6, 
 wxID_MENUUTAMAMENUPROFILDANPENDUDUKITEMS7, 
 wxID_MENUUTAMAMENUPROFILDANPENDUDUKITEMS8, 
 wxID_MENUUTAMAMENUPROFILDANPENDUDUKITEMS9, 
 wxID_MENUUTAMAMENUPROFILDANPENDUDUKKELUAR, 
] = [wx.NewId() for _init_coll_menuprofildanpenduduk_Items in range(8)]

[wxID_MENUUTAMAMENUADMINISTRASIDANKEUANGANITEMS0, 
 wxID_MENUUTAMAMENUADMINISTRASIDANKEUANGANITEMS2, 
 wxID_MENUUTAMAMENUADMINISTRASIDANKEUANGANITEMS3, 
 wxID_MENUUTAMAMENUADMINISTRASIDANKEUANGANITEMS4, 
 wxID_MENUUTAMAMENUADMINISTRASIDANKEUANGANITEMS5, 
 wxID_MENUUTAMAMENUADMINISTRASIDANKEUANGANITEMS6, 
] = [wx.NewId() for _init_coll_menuadministrasidankeuangan_Items in range(6)]

[wxID_MENUUTAMAAPBDESABELANJAAPBDESA, wxID_MENUUTAMAAPBDESAPENERIMAANAPBDESA, 
 wxID_MENUUTAMAAPBDESARAB, 
] = [wx.NewId() for _init_coll_apbdesa_Items in range(3)]

[wxID_MENUUTAMAKEUANGANITEMS0, wxID_MENUUTAMAKEUANGANITEMS1, 
 wxID_MENUUTAMAKEUANGANITEMS2, wxID_MENUUTAMAKEUANGANITEMS3, 
 wxID_MENUUTAMAKEUANGANITEMS4, wxID_MENUUTAMAKEUANGANITEMS5, 
] = [wx.NewId() for _init_coll_keuangan_Items in range(6)]

[wxID_MENUUTAMAMENUPOTENSIDANSTATISTIKITEMS0] = [wx.NewId() for _init_coll_menupotensidanstatistik_Items in range(1)]

[wxID_MENUUTAMAKEMISKINANDATAKEMISKINAN] = [wx.NewId() for _init_coll_kemiskinan_Items in range(1)]

[wxID_MENUUTAMAPEMBUKUANITEMS0] = [wx.NewId() for _init_coll_pembukuan_Items in range(1)]

[wxID_MENUUTAMABANTUANITEMS0] = [wx.NewId() for _init_coll_bantuan_Items in range(1)]

class menuutama(wx.Frame):
    def _init_coll_MenuAtas_Menus(self, parent):
        # generated method, don't edit

        parent.Append(menu=self.menuprofildanpenduduk,
              title=u'Profil Dan Kependudukan')
        parent.Append(menu=self.menupotensidanstatistik, title=u'Potensi Desa')
        parent.Append(menu=self.menuadministrasidankeuangan,
              title=u'Administrasi Dan Keuangan')
        parent.Append(menu=self.bantuan, title=u'Bantuan')

    def _init_coll_kelahiran_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='', id=wxID_MENUUTAMAKELAHIRANTAMBAH,
              kind=wx.ITEM_NORMAL, text=u'Tambah Kelahiran')
        parent.Append(help='', id=wxID_MENUUTAMAKELAHIRANRUBAH,
              kind=wx.ITEM_NORMAL, text=u'Perubahan Kelahiran')
        self.Bind(wx.EVT_MENU, self.OnKelahiranTambahMenu,
              id=wxID_MENUUTAMAKELAHIRANTAMBAH)
        self.Bind(wx.EVT_MENU, self.OnKelahiranRubahMenu,
              id=wxID_MENUUTAMAKELAHIRANRUBAH)

    def _init_coll_bantuan_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='', id=wxID_MENUUTAMABANTUANITEMS0,
              kind=wx.ITEM_NORMAL, text=u'Tentang SIAP')
        self.Bind(wx.EVT_MENU, self.OnBantuanItems0Menu,
              id=wxID_MENUUTAMABANTUANITEMS0)

    def _init_coll_pembukuan_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='', id=wxID_MENUUTAMAPEMBUKUANITEMS0,
              kind=wx.ITEM_NORMAL, text=u'Daftar Inventaris')
        self.Bind(wx.EVT_MENU, self.OnPembukuanItems0Menu,
              id=wxID_MENUUTAMAPEMBUKUANITEMS0)

    def _init_coll_menuadministrasidankeuangan_Items(self, parent):
        # generated method, don't edit

        parent.AppendMenu(help='',
              id=wxID_MENUUTAMAMENUADMINISTRASIDANKEUANGANITEMS0,
              submenu=self.persuratan, text=u'Administrasi Surat')
        parent.AppendMenu(help='',
              id=wxID_MENUUTAMAMENUADMINISTRASIDANKEUANGANITEMS2,
              submenu=self.koderekening, text=u'Master Kode Rekening')
        parent.AppendMenu(help='',
              id=wxID_MENUUTAMAMENUADMINISTRASIDANKEUANGANITEMS3,
              submenu=self.rpjmdes, text=u'RPJMDesa')
        parent.AppendMenu(help='',
              id=wxID_MENUUTAMAMENUADMINISTRASIDANKEUANGANITEMS4,
              submenu=self.rkp, text=u'RKP Desa')
        parent.AppendMenu(help='',
              id=wxID_MENUUTAMAMENUADMINISTRASIDANKEUANGANITEMS5,
              submenu=self.apbdesa, text=u'APBD Desa')
        parent.AppendMenu(help='',
              id=wxID_MENUUTAMAMENUADMINISTRASIDANKEUANGANITEMS6,
              submenu=self.keuangan, text=u'Administrasi Keuangan')

    def _init_coll_kematian_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='', id=wxID_MENUUTAMAKEMATIANTAMBAH,
              kind=wx.ITEM_NORMAL, text=u'Tambah Data Kematian')
        parent.Append(help='', id=wxID_MENUUTAMAKEMATIANRUBAH,
              kind=wx.ITEM_NORMAL, text=u'Perubahan Data Kematian')
        self.Bind(wx.EVT_MENU, self.OnKematianTambahMenu,
              id=wxID_MENUUTAMAKEMATIANTAMBAH)
        self.Bind(wx.EVT_MENU, self.OnKematianRubahMenu,
              id=wxID_MENUUTAMAKEMATIANRUBAH)

    def _init_coll_kemiskinan_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='', id=wxID_MENUUTAMAKEMISKINANDATAKEMISKINAN,
              kind=wx.ITEM_NORMAL, text=u'Data Kemiskinan')
        self.Bind(wx.EVT_MENU, self.OnKemiskinanDatakemiskinanMenu,
              id=wxID_MENUUTAMAKEMISKINANDATAKEMISKINAN)

    def _init_coll_potensi_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='', id=wxID_MENUUTAMAPOTENSIEKONOMI,
              kind=wx.ITEM_NORMAL, text='Ekonomi')
        parent.Append(help='', id=wxID_MENUUTAMAPOTENSISOSIALBUDAYA,
              kind=wx.ITEM_NORMAL, text='Sosial Budaya')
        parent.Append(help='', id=wxID_MENUUTAMAPOTENSIPERTAHANAN,
              kind=wx.ITEM_NORMAL, text='Pertahanan')
        self.Bind(wx.EVT_MENU, self.OnPotensiItems0Menu,
              id=wxID_MENUUTAMAPOTENSIEKONOMI)
        self.Bind(wx.EVT_MENU, self.OnPotensiItems1Menu,
              id=wxID_MENUUTAMAPOTENSISOSIALBUDAYA)
        self.Bind(wx.EVT_MENU, self.OnPotensiItems2Menu,
              id=wxID_MENUUTAMAPOTENSIPERTAHANAN)

    def _init_coll_koderekening_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='', id=wxID_MENUUTAMAKODEREKENINGPENDAPATANASLIDESA,
              kind=wx.ITEM_NORMAL, text='Pendapatan Asli Desa')
        parent.Append(help='', id=wxID_MENUUTAMAKODEREKENINGPENDAPATANTRANSFER,
              kind=wx.ITEM_NORMAL, text='Pendapatan Transfer')
        parent.Append(help='', id=wxID_MENUUTAMAKODEREKENINGPENDAPATANLAINLAIN,
              kind=wx.ITEM_NORMAL, text='Pendapatan Lain-lain')
        parent.AppendSeparator()
        parent.Append(help='',
              id=wxID_MENUUTAMAKODEREKENINGBIDANGPENYELENGGARAAN,
              kind=wx.ITEM_NORMAL,
              text='Bidang Penyelenggaraan Pemerintah Desa')
        parent.Append(help='', id=wxID_MENUUTAMAKODEREKENINGBIDANGPEMBANGUNAN,
              kind=wx.ITEM_NORMAL, text='Bidang Pelaksanaan Pembangunan Desa')
        parent.Append(help='', id=wxID_MENUUTAMAKODEREKENINGBIDANGPEMBINAAN,
              kind=wx.ITEM_NORMAL, text='Bidang Pembinaan Kemasyarakatan')
        parent.Append(help='', id=wxID_MENUUTAMAKODEREKENINGBIDANGPEMBERDAYAAN,
              kind=wx.ITEM_NORMAL, text='Bidang Pemberdayaan Kemasyarakatan')
        parent.Append(help='', id=wxID_MENUUTAMAKODEREKENINGBIDANGTAKTERDUGA,
              kind=wx.ITEM_NORMAL, text='Bidang Tak Terduga')
        parent.AppendSeparator()
        parent.Append(help='', id=wxID_MENUUTAMAKODEREKENINGPEMBIAYAAN1,
              kind=wx.ITEM_NORMAL, text=u'Pembiayaan Penerimaan')
        parent.Append(help='', id=wxID_MENUUTAMAKODEREKENINGPEMBIAYAAN2,
              kind=wx.ITEM_NORMAL, text=u'Pembiayaan Pengeluaran')
        self.Bind(wx.EVT_MENU, self.OnKoderekeningPendapatanaslidesaMenu,
              id=wxID_MENUUTAMAKODEREKENINGPENDAPATANASLIDESA)
        self.Bind(wx.EVT_MENU, self.OnKoderekeningPendapatantransferMenu,
              id=wxID_MENUUTAMAKODEREKENINGPENDAPATANTRANSFER)
        self.Bind(wx.EVT_MENU, self.OnKoderekeningPendapatanlainlainMenu,
              id=wxID_MENUUTAMAKODEREKENINGPENDAPATANLAINLAIN)
        self.Bind(wx.EVT_MENU, self.OnKoderekeningBidangpenyelenggaraanMenu,
              id=wxID_MENUUTAMAKODEREKENINGBIDANGPENYELENGGARAAN)
        self.Bind(wx.EVT_MENU, self.OnKoderekeningBidangpembangunanMenu,
              id=wxID_MENUUTAMAKODEREKENINGBIDANGPEMBANGUNAN)
        self.Bind(wx.EVT_MENU, self.OnKoderekeningBidangpembinaanMenu,
              id=wxID_MENUUTAMAKODEREKENINGBIDANGPEMBINAAN)
        self.Bind(wx.EVT_MENU, self.OnKoderekeningBidangpemberdayaanMenu,
              id=wxID_MENUUTAMAKODEREKENINGBIDANGPEMBERDAYAAN)
        self.Bind(wx.EVT_MENU, self.OnKoderekeningBidangtakterdugaMenu,
              id=wxID_MENUUTAMAKODEREKENINGBIDANGTAKTERDUGA)
        self.Bind(wx.EVT_MENU, self.OnKoderekeningPembiayaan1Menu,
              id=wxID_MENUUTAMAKODEREKENINGPEMBIAYAAN1)
        self.Bind(wx.EVT_MENU, self.OnKoderekeningPembiayaan2Menu,
              id=wxID_MENUUTAMAKODEREKENINGPEMBIAYAAN2)

    def _init_coll_rpjmdes_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='', id=wxID_MENUUTAMARPJMDESRPJMBIDPENYELENGGARAN,
              kind=wx.ITEM_NORMAL,
              text='Bidang Penyelenggaraan Pemerintah Desa')
        parent.Append(help='', id=wxID_MENUUTAMARPJMDESRPJMPEMBDESA,
              kind=wx.ITEM_NORMAL, text='Bidang Pelaksanaan Pembangunan Desa')
        parent.Append(help='', id=wxID_MENUUTAMARPJMDESRPJMPEMBINAAN,
              kind=wx.ITEM_NORMAL, text='Bidang Pembinaan Kemasyarakatan')
        parent.Append(help='', id=wxID_MENUUTAMARPJMDESRPJMPEMBERDAYAAN,
              kind=wx.ITEM_NORMAL, text='Bidang Pemberdayaan Kemasyarakatan')
        parent.Append(help='', id=wxID_MENUUTAMARPJMDESRPJMTAKTERDUGA,
              kind=wx.ITEM_NORMAL, text='Bidang Tak Terduga')
        parent.Append(help='', id=wxID_MENUUTAMARPJMDESCETAKRPJMDES,
              kind=wx.ITEM_NORMAL, text=u'Cetak RPJMDesa')
        self.Bind(wx.EVT_MENU, self.OnRpjmdesRpjmbidpenyelenggaranMenu,
              id=wxID_MENUUTAMARPJMDESRPJMBIDPENYELENGGARAN)
        self.Bind(wx.EVT_MENU, self.OnRpjmdesRpjmpembdesaMenu,
              id=wxID_MENUUTAMARPJMDESRPJMPEMBDESA)
        self.Bind(wx.EVT_MENU, self.OnRpjmdesRpjmpembinaanMenu,
              id=wxID_MENUUTAMARPJMDESRPJMPEMBINAAN)
        self.Bind(wx.EVT_MENU, self.OnRpjmdesRpjmpemberdayaanMenu,
              id=wxID_MENUUTAMARPJMDESRPJMPEMBERDAYAAN)
        self.Bind(wx.EVT_MENU, self.OnRpjmdesRpjmtakterdugaMenu,
              id=wxID_MENUUTAMARPJMDESRPJMTAKTERDUGA)
        self.Bind(wx.EVT_MENU, self.OnRpjmdesCetakrpjmdesMenu,
              id=wxID_MENUUTAMARPJMDESCETAKRPJMDES)

    def _init_coll_persuratan_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='', id=wxID_MENUUTAMAPERSURATANSURATMASUK,
              kind=wx.ITEM_NORMAL, text='Surat Masuk')
        parent.Append(help='', id=wxID_MENUUTAMAPERSURATANSURATKELUAR,
              kind=wx.ITEM_NORMAL, text='Surat Keluar')
        parent.Append(help='', id=wxID_MENUUTAMAPERSURATANPERDES,
              kind=wx.ITEM_NORMAL, text='Penyusunan PERDES')
        parent.Append(help='', id=wxID_MENUUTAMAPERSURATANLPJDESA,
              kind=wx.ITEM_NORMAL, text='Penyusunan LPJ Desa')
        self.Bind(wx.EVT_MENU, self.OnPersuratanItems0Menu,
              id=wxID_MENUUTAMAPERSURATANSURATMASUK)
        self.Bind(wx.EVT_MENU, self.OnPersuratanItems1Menu,
              id=wxID_MENUUTAMAPERSURATANSURATKELUAR)
        self.Bind(wx.EVT_MENU, self.OnPersuratanItems2Menu,
              id=wxID_MENUUTAMAPERSURATANPERDES)

    def _init_coll_keuangan_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='', id=wxID_MENUUTAMAKEUANGANITEMS0,
              kind=wx.ITEM_NORMAL, text=u'Kas Pembantu Kegiatan')
        parent.Append(help='', id=wxID_MENUUTAMAKEUANGANITEMS1,
              kind=wx.ITEM_NORMAL, text=u'Surat Permintaan Pembayaran')
        parent.Append(help='', id=wxID_MENUUTAMAKEUANGANITEMS2,
              kind=wx.ITEM_NORMAL, text=u'Tanggung Jawab Belanja')
        parent.Append(help='', id=wxID_MENUUTAMAKEUANGANITEMS3,
              kind=wx.ITEM_NORMAL, text=u'Buku Kas Umum')
        parent.Append(help='', id=wxID_MENUUTAMAKEUANGANITEMS4,
              kind=wx.ITEM_NORMAL, text=u'Buku Kas Pembantu Pajak')
        parent.Append(help='', id=wxID_MENUUTAMAKEUANGANITEMS5,
              kind=wx.ITEM_NORMAL, text=u'Buku Bank Desa')
        self.Bind(wx.EVT_MENU, self.OnKeuanganItems0Menu,
              id=wxID_MENUUTAMAKEUANGANITEMS0)
        self.Bind(wx.EVT_MENU, self.OnKeuanganItems1Menu,
              id=wxID_MENUUTAMAKEUANGANITEMS1)
        self.Bind(wx.EVT_MENU, self.OnKeuanganItems2Menu,
              id=wxID_MENUUTAMAKEUANGANITEMS2)
        self.Bind(wx.EVT_MENU, self.OnKeuanganItems3Menu,
              id=wxID_MENUUTAMAKEUANGANITEMS3)
        self.Bind(wx.EVT_MENU, self.OnKeuanganItems4Menu,
              id=wxID_MENUUTAMAKEUANGANITEMS4)
        self.Bind(wx.EVT_MENU, self.OnKeuanganItems5Menu,
              id=wxID_MENUUTAMAKEUANGANITEMS5)

    def _init_coll_statistik_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='', id=wxID_MENUUTAMASTATISTIKPENDUDUK,
              kind=wx.ITEM_NORMAL, text='Penduduk')
        parent.Append(help='', id=wxID_MENUUTAMASTATISTIKKEMISKINAN,
              kind=wx.ITEM_NORMAL, text='Kemiskinan')
        parent.Append(help='', id=wxID_MENUUTAMASTATISTIKADMINISTRASI,
              kind=wx.ITEM_NORMAL, text='Administrasi')
        self.Bind(wx.EVT_MENU, self.OnStatistikItems0Menu,
              id=wxID_MENUUTAMASTATISTIKPENDUDUK)
        self.Bind(wx.EVT_MENU, self.OnStatistikItems1Menu,
              id=wxID_MENUUTAMASTATISTIKKEMISKINAN)
        self.Bind(wx.EVT_MENU, self.OnStatistikItems2Menu,
              id=wxID_MENUUTAMASTATISTIKADMINISTRASI)

    def _init_coll_isianggota_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='', id=wxID_MENUUTAMAISIANGGOTATAMBAHANGGOTAKELUARGA,
              kind=wx.ITEM_NORMAL, text=u'Tambah Anggota Keluarga')
        parent.Append(help='', id=wxID_MENUUTAMAISIANGGOTAPERUBAHANANGGOTA,
              kind=wx.ITEM_NORMAL, text=u'Perubahan Anggota Keluarga')
        self.Bind(wx.EVT_MENU, self.OnIsianggotaTambahanggotakeluargaMenu,
              id=wxID_MENUUTAMAISIANGGOTATAMBAHANGGOTAKELUARGA)
        self.Bind(wx.EVT_MENU, self.OnIsianggotaPerubahananggotaMenu,
              id=wxID_MENUUTAMAISIANGGOTAPERUBAHANANGGOTA)

    def _init_coll_mutasi_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='', id=wxID_MENUUTAMAMUTASITAMBAH,
              kind=wx.ITEM_NORMAL, text=u'Tambah Data Mutasi')
        parent.Append(help='', id=wxID_MENUUTAMAMUTASIRUBAH,
              kind=wx.ITEM_NORMAL, text=u'Perubahan Data Mutasi')
        self.Bind(wx.EVT_MENU, self.OnMutasiItems0Menu,
              id=wxID_MENUUTAMAMUTASITAMBAH)
        self.Bind(wx.EVT_MENU, self.OnMutasiItems1Menu,
              id=wxID_MENUUTAMAMUTASIRUBAH)

    def _init_coll_menupotensidanstatistik_Items(self, parent):
        # generated method, don't edit

        parent.AppendMenu(help='',
              id=wxID_MENUUTAMAMENUPOTENSIDANSTATISTIKITEMS0,
              submenu=self.potensi, text=u'Potensi Desa')

    def _init_coll_apbdesa_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='', id=wxID_MENUUTAMAAPBDESAPENERIMAANAPBDESA,
              kind=wx.ITEM_NORMAL, text=u'Penerimaan APB DESA')
        parent.Append(help='', id=wxID_MENUUTAMAAPBDESABELANJAAPBDESA,
              kind=wx.ITEM_NORMAL, text=u'Belanja APB DESA')
        parent.AppendSeparator()
        parent.Append(help='', id=wxID_MENUUTAMAAPBDESARAB, kind=wx.ITEM_NORMAL,
              text=u'Penyusunan RAB')
        self.Bind(wx.EVT_MENU, self.OnApbdesaPenerimaanapbdesaMenu,
              id=wxID_MENUUTAMAAPBDESAPENERIMAANAPBDESA)
        self.Bind(wx.EVT_MENU, self.OnApbdesaBelanjaapbdesaMenu,
              id=wxID_MENUUTAMAAPBDESABELANJAAPBDESA)
        self.Bind(wx.EVT_MENU, self.OnApbdesaRabMenu,
              id=wxID_MENUUTAMAAPBDESARAB)

    def _init_coll_rkp_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='', id=wxID_MENUUTAMARKPRKPPENYELENGGARAN,
              kind=wx.ITEM_NORMAL,
              text='Bidang Penyelenggaraan Pemerintah Desa')
        parent.Append(help='', id=wxID_MENUUTAMARKPRKPPEMBANGUNAN,
              kind=wx.ITEM_NORMAL, text='Bidang Pelaksanaan Pembangunan Desa')
        parent.Append(help='', id=wxID_MENUUTAMARKPRKPPEMBINAAN,
              kind=wx.ITEM_NORMAL, text='Bidang Pembinaan Kemasyarakatan')
        parent.Append(help='', id=wxID_MENUUTAMARKPRKPPEMBERDAYAAN,
              kind=wx.ITEM_NORMAL, text='Bidang Pemberdayaan Kemasyarakatan')
        parent.Append(help='', id=wxID_MENUUTAMARKPRKPTAKTERDUGA,
              kind=wx.ITEM_NORMAL, text='Bidang Tak Terduga')
        parent.Append(help='', id=wxID_MENUUTAMARKPLAPORANRKP,
              kind=wx.ITEM_NORMAL, text=u'Laporan RKP')
        self.Bind(wx.EVT_MENU, self.OnRkpRkppenyelenggaranMenu,
              id=wxID_MENUUTAMARKPRKPPENYELENGGARAN)
        self.Bind(wx.EVT_MENU, self.OnRkpRkppembangunanMenu,
              id=wxID_MENUUTAMARKPRKPPEMBANGUNAN)
        self.Bind(wx.EVT_MENU, self.OnRkpRkppembinaanMenu,
              id=wxID_MENUUTAMARKPRKPPEMBINAAN)
        self.Bind(wx.EVT_MENU, self.OnRkpRkppemberdayaanMenu,
              id=wxID_MENUUTAMARKPRKPPEMBERDAYAAN)
        self.Bind(wx.EVT_MENU, self.OnRkpRkptakterdugaMenu,
              id=wxID_MENUUTAMARKPRKPTAKTERDUGA)
        self.Bind(wx.EVT_MENU, self.OnRkpLaporanrkpMenu,
              id=wxID_MENUUTAMARKPLAPORANRKP)

    def _init_coll_isikk_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='', id=wxID_MENUUTAMAISIKKTAMBAHKK,
              kind=wx.ITEM_NORMAL, text=u'Tambah Kepala Keluarga')
        parent.Append(help='', id=wxID_MENUUTAMAISIKKEDITKK,
              kind=wx.ITEM_NORMAL, text=u'Perubahan Kepala Keluarga')
        parent.Append(help='', id=wxID_MENUUTAMAISIKKPECAHKK,
              kind=wx.ITEM_NORMAL, text=u'Pecah Kepala Keluarga')
        parent.Append(help='', id=wxID_MENUUTAMAISIKKKKSEMENTARA,
              kind=wx.ITEM_NORMAL, text=u'Tambah KK Sementara')
        self.Bind(wx.EVT_MENU, self.OnIsikkTambahkkMenu,
              id=wxID_MENUUTAMAISIKKTAMBAHKK)
        self.Bind(wx.EVT_MENU, self.OnIsikkEditkkMenu,
              id=wxID_MENUUTAMAISIKKEDITKK)
        self.Bind(wx.EVT_MENU, self.OnIsikkPecahkkMenu,
              id=wxID_MENUUTAMAISIKKPECAHKK)
        self.Bind(wx.EVT_MENU, self.OnIsikkKksementaraMenu,
              id=wxID_MENUUTAMAISIKKKKSEMENTARA)

    def _init_coll_menuprofildanpenduduk_Items(self, parent):
        # generated method, don't edit

        parent.AppendMenu(help='', id=wxID_MENUUTAMAMENUPROFILDANPENDUDUKITEMS4,
              submenu=self.isiprofil, text=u'Profil Desa')
        parent.AppendSeparator()
        parent.AppendMenu(help='', id=wxID_MENUUTAMAMENUPROFILDANPENDUDUKITEMS6,
              submenu=self.isikk, text=u'Kepala Keluarga')
        parent.AppendMenu(help='', id=wxID_MENUUTAMAMENUPROFILDANPENDUDUKITEMS5,
              submenu=self.isianggota, text=u'Anggota Keluarga')
        parent.AppendMenu(help='', id=wxID_MENUUTAMAMENUPROFILDANPENDUDUKITEMS8,
              submenu=self.kelahiran, text=u'Data Kelahiran')
        parent.AppendMenu(help='', id=wxID_MENUUTAMAMENUPROFILDANPENDUDUKITEMS7,
              submenu=self.kematian, text=u'Data Kematian')
        parent.AppendMenu(help='', id=wxID_MENUUTAMAMENUPROFILDANPENDUDUKITEMS9,
              submenu=self.mutasi, text=u'Data Mutasi')
        parent.AppendMenu(help='',
              id=wxID_MENUUTAMAMENUPROFILDANPENDUDUKITEMS10,
              submenu=self.kemiskinan, text=u'Data Kemiskinan')
        parent.AppendSeparator()
        parent.Append(help='', id=wxID_MENUUTAMAMENUPROFILDANPENDUDUKKELUAR,
              kind=wx.ITEM_NORMAL, text='Keluar Program')
        self.Bind(wx.EVT_MENU, self.OnMenuprofildanpendudukKeluarMenu,
              id=wxID_MENUUTAMAMENUPROFILDANPENDUDUKKELUAR)

    def _init_coll_isiprofil_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='', id=wxID_MENUUTAMAISIPROFILPASSWORD,
              kind=wx.ITEM_NORMAL, text=u'Password')
        parent.Append(help='', id=wxID_MENUUTAMAISIPROFILINPUTPROFILDESA,
              kind=wx.ITEM_NORMAL, text=u'Profil Desa')
        parent.Append(help='', id=wxID_MENUUTAMAISIPROFILEDITPROFILDESA,
              kind=wx.ITEM_NORMAL, text=u'Input Jabatan')
        parent.Append(help='', id=wxID_MENUUTAMAISIPROFILITEMS5,
              kind=wx.ITEM_NORMAL, text=u'Input Pejabat/Staf Desa')
        parent.Append(help='', id=wxID_MENUUTAMAISIPROFILITEMS6,
              kind=wx.ITEM_NORMAL, text=u'Input Ketua RT/RW/Dusun')
        parent.AppendSeparator()
        parent.Append(help='', id=wxID_MENUUTAMAISIPROFILDATAOL,
              kind=wx.ITEM_NORMAL, text=u'Data Untuk Online')
        self.Bind(wx.EVT_MENU, self.OnIsiprofilPasswordMenu,
              id=wxID_MENUUTAMAISIPROFILPASSWORD)
        self.Bind(wx.EVT_MENU, self.OnIsiprofilInputprofildesaMenu,
              id=wxID_MENUUTAMAISIPROFILINPUTPROFILDESA)
        self.Bind(wx.EVT_MENU, self.OnIsiprofilEditprofildesaMenu,
              id=wxID_MENUUTAMAISIPROFILEDITPROFILDESA)
        self.Bind(wx.EVT_MENU, self.OnIsiprofilDataolMenu,
              id=wxID_MENUUTAMAISIPROFILDATAOL)
        self.Bind(wx.EVT_MENU, self.OnIsiprofilItems5Menu,
              id=wxID_MENUUTAMAISIPROFILITEMS5)
        self.Bind(wx.EVT_MENU, self.OnIsiprofilItems6Menu,
              id=wxID_MENUUTAMAISIPROFILITEMS6)

    def _init_utils(self):
        # generated method, don't edit
        self.MenuAtas = wx.MenuBar()

        self.menuprofildanpenduduk = wx.Menu(title='')

        self.kemiskinan = wx.Menu(title='')

        self.persuratan = wx.Menu(title='')

        self.potensi = wx.Menu(title='')

        self.statistik = wx.Menu(title='')

        self.koderekening = wx.Menu(title='')

        self.rpjmdes = wx.Menu(title='')

        self.rkp = wx.Menu(title='')

        self.isiprofil = wx.Menu(title='')

        self.isikk = wx.Menu(title='')

        self.isianggota = wx.Menu(title='')

        self.kelahiran = wx.Menu(title='')

        self.kematian = wx.Menu(title='')

        self.mutasi = wx.Menu(title='')

        self.menupotensidanstatistik = wx.Menu(title='')

        self.menuadministrasidankeuangan = wx.Menu(title=u'')

        self.pembukuan = wx.Menu(title='')

        self.apbdesa = wx.Menu(title=u'')

        self.keuangan = wx.Menu(title='')

        self.bantuan = wx.Menu(title=u'')

        self._init_coll_MenuAtas_Menus(self.MenuAtas)
        self._init_coll_menuprofildanpenduduk_Items(self.menuprofildanpenduduk)
        self._init_coll_kemiskinan_Items(self.kemiskinan)
        self._init_coll_persuratan_Items(self.persuratan)
        self._init_coll_potensi_Items(self.potensi)
        self._init_coll_statistik_Items(self.statistik)
        self._init_coll_koderekening_Items(self.koderekening)
        self._init_coll_rpjmdes_Items(self.rpjmdes)
        self._init_coll_rkp_Items(self.rkp)
        self._init_coll_isiprofil_Items(self.isiprofil)
        self._init_coll_isikk_Items(self.isikk)
        self._init_coll_isianggota_Items(self.isianggota)
        self._init_coll_kelahiran_Items(self.kelahiran)
        self._init_coll_kematian_Items(self.kematian)
        self._init_coll_mutasi_Items(self.mutasi)
        self._init_coll_menupotensidanstatistik_Items(self.menupotensidanstatistik)
        self._init_coll_menuadministrasidankeuangan_Items(self.menuadministrasidankeuangan)
        self._init_coll_pembukuan_Items(self.pembukuan)
        self._init_coll_apbdesa_Items(self.apbdesa)
        self._init_coll_keuangan_Items(self.keuangan)
        self._init_coll_bantuan_Items(self.bantuan)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_MENUUTAMA, name=u'menuutama',
              parent=prnt, pos=wx.Point(463, 86), size=wx.Size(810, 658),
              style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL,
              title=u'MENU UTAMA SIAP VERSI 1.0 (BETA)')
        self._init_utils()
        self.SetClientSize(wx.Size(802, 628))
        self.SetMenuBar(self.MenuAtas)
        self.SetWindowVariant(wx.WINDOW_VARIANT_NORMAL)
        self.SetAutoLayout(False)
        self.SetBackgroundColour(wx.Colour(192, 192, 192))
        self.Center(wx.BOTH)
        self.SetForegroundColour(wx.Colour(255, 255, 255))
        self.SetIcon(wx.Icon(u'C:/Users/perintis/Documents/PelatihanSidekam/siap/png/icon.ico',
              wx.BITMAP_TYPE_ICO))

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap(u'png/depan.jpg',
              wx.BITMAP_TYPE_JPEG), id=wxID_MENUUTAMASTATICBITMAP1,
              name='staticBitmap1', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(802, 628), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnMenuprofildanpendudukKeluarMenu(self, event):
        self.Close()
        self.Destroy()
        db.commit()

    def OnIsikkTambahkkMenu(self, event):
        self.main=kk_tetap.create(None)
        self.main.Show()

    def OnIsikkEditkkMenu(self, event):
        self.main=edit_kk.create(None)
        self.main.Show()

    def OnIsiprofilImportdatacsvMenu(self, event):
        self.main=importdata.create(None)
        self.main.Show()

    def OnIsikkPecahkkMenu(self, event):
        self.main=pecah_keluarga.create(None)
        self.main.Show()

    def OnIsikkKksementaraMenu(self, event):
        self.main=kk_sementara.create(None)
        self.main.Show()

    def OnIsianggotaTambahanggotakeluargaMenu(self, event):
        self.main=tambah_anggota_keluarga.create(None)
        self.main.Show()

    def OnIsianggotaPerubahananggotaMenu(self, event):
        self.main=edit_anggota.create(None)
        self.main.Show()

    def OnRpjmdesRpjmbidpenyelenggaranMenu(self, event):
        self.main=rpjmpenyelenggaraandesa.create(None)
        self.main.Show()

    def OnRpjmdesRpjmpembdesaMenu(self, event):
        self.main=rpjmpembangunandesa.create(None)
        self.main.Show()

    def OnRpjmdesRpjmpembinaanMenu(self, event):
        self.main=rpjmpembinaankemasyarakatan.create(None)
        self.main.Show()

    def OnRpjmdesRpjmpemberdayaanMenu(self, event):
        self.main=rpjmpemberdayaanmasyarakat.create(None)
        self.main.Show()

    def OnRpjmdesRpjmtakterdugaMenu(self, event):
        self.main=rpjmtakterduga.create(None)
        self.main.Show()

    def OnRkpRkppenyelenggaranMenu(self, event):
        self.main=rkppenyelenggarandesa.create(None)
        self.main.Show()

    def OnRkpRkppembangunanMenu(self, event):
        self.main=rkppembangunandesa.create(None)
        self.main.Show()


    def OnRkpRkppembinaanMenu(self, event):
        self.main=rkppembinaankemasyarakatan.create(None)
        self.main.Show()


    def OnRkpRkppemberdayaanMenu(self, event):
        self.main=rkppemberdayaanmasyarakat.create(None)
        self.main.Show()


    def OnRkpRkptakterdugaMenu(self, event):
        self.main=rpjmtakterduga.create(None)
        self.main.Show()

    def OnKoderekeningPendapatanaslidesaMenu(self, event):
        self.main=pendapatanaslidesa.create(None)
        self.main.Show()


    def OnKoderekeningPendapatantransferMenu(self, event):
        self.main=pendapatantransfer.create(None)
        self.main.Show()


    def OnKoderekeningPendapatanlainlainMenu(self, event):
        self.main=pendapatanlainlain.create(None)
        self.main.Show()


    def OnKoderekeningLihatpendapatanMenu(self, event):
        self.main=lihatpendapatan.create(None)
        self.main.Show()


    def OnKoderekeningBidangpenyelenggaraanMenu(self, event):
        self.main=penyelenggaraandesa.create(None)
        self.main.Show()


    def OnKoderekeningBidangpembangunanMenu(self, event):
        self.main=pembangunandesa.create(None)
        self.main.Show()


    def OnKoderekeningBidangpembinaanMenu(self, event):
        self.main=pembinaankemasyarakatan.create(None)
        self.main.Show()


    def OnKoderekeningBidangpemberdayaanMenu(self, event):
        self.main=pemberdayaanmasyarakat.create(None)
        self.main.Show()

    def OnKoderekeningBidangtakterdugaMenu(self, event):
        self.main=takterduga.create(None)
        self.main.Show()

    def OnRpjmdesCetakrpjmdesMenu(self, event):
        self.main=laporanrpjmdes.create(None)
        self.main.Show()

    def OnRkpLaporanrkpMenu(self, event):
        self.main=laporanrkp.create(None)
        self.main.Show()

    def OnIsiprofilPasswordMenu(self, event):
        self.main=kunci.create(None)
        self.main.Show()

    def OnIsiprofilInputprofildesaMenu(self, event):
        self.main=input_profil.create(None)
        self.main.Show()

    def OnIsiprofilEditprofildesaMenu(self, event):
        self.main=jabatan.create(None)
        self.main.Show()

    def OnMutasiItems0Menu(self, event):
        self.main=kejadian_pindah.create(None)
        self.main.Show()

    def OnMutasiItems1Menu(self, event):
        self.main=edit_kejadian_pindah.create(None)
        self.main.Show()

    def OnMutasiItems2Menu(self, event):
        event.Skip()

    def OnIsianggotaItems2Menu(self, event):
        event.Skip()

    def OnStatistikItems0Menu(self, event):
        event.Skip()

    def OnStatistikItems1Menu(self, event):
        event.Skip()

    def OnStatistikItems2Menu(self, event):
        event.Skip()

    def OnPersuratanItems0Menu(self, event):
        self.main=surat_masuk.create(None)
        self.main.Show()

    def OnPersuratanItems1Menu(self, event):
        self.main=pembuatan_surat_keluar.create(None)
        self.main.Show()

    def OnPersuratanItems2Menu(self, event):
        event.Skip()

    def OnKelahiranTambahMenu(self, event):
        self.main=kejadian_kelahiran.create(None)
        self.main.Show()

    def OnKelahiranRubahMenu(self, event):
        self.main=edit_kejadian_kelahiran.create(None)
        self.main.Show()

    def OnKelahiranLaporanMenu(self, event):
        event.Skip()

    def OnPotensiItems0Menu(self, event):
        self.main=potensi_ekonomi.create(None)
        self.main.Show()

    def OnPotensiItems1Menu(self, event):
        self.main=potensi_pariwisata.create(None)
        self.main.Show()

    def OnPotensiItems2Menu(self, event):
        self.main=potensi_pertahanan.create(None)
        self.main.Show()

    def OnKemiskinanIndikatorkemiskinanMenu(self, event):
        self.main=input_indikator_kemiskinan.create(None)
        self.main.Show()

    def OnKemiskinanDatakemiskinanMenu(self, event):
        self.main=input_data_kemiskinan.create(None)
        self.main.Show()

    def OnKematianTambahMenu(self, event):
        self.main=kejadian_kematian.create(None)
        self.main.Show()


    def OnKematianRubahMenu(self, event):
        self.main=edit_kejadian_kematian.create(None)
        self.main.Show()

    def OnKematianLaporanMenu(self, event):
        event.Skip()

    def OnPembukuanItems0Menu(self, event):
        event.Skip()

    def OnIsiprofilDataolMenu(self, event):
        self.main=sinkron_data.create(None)
        self.main.Show()

    def OnKoderekeningPembiayaan1Menu(self, event):
        self.main=penerimaanpembiayaan.create(None)
        self.main.Show()

    def OnKoderekeningPembiayaan2Menu(self, event):
        self.main=pengeluaranpembiayaan.create(None)
        self.main.Show()

    def OnApbdesaPenerimaanapbdesaMenu(self, event):
        event.Skip()

    def OnApbdesaBelanjaapbdesaMenu(self, event):
        self.main=apbdesa.create(None)
        self.main.Show()

    def OnApbdesaRabMenu(self, event):
        self.main=rab.create(None)
        self.main.Show()

    def OnKeuanganItems0Menu(self, event):
        self.main=kaspembantu.create(None)
        self.main.Show()

    def OnKeuanganItems1Menu(self, event):
        self.main=permintaanbayar.create(None)
        self.main.Show()
        
    def OnKeuanganItems2Menu(self, event):
        self.main=tanggungbelanja.create(None)
        self.main.Show()

    def OnKeuanganItems3Menu(self, event):
        self.main=kasumum.create(None)
        self.main.Show()

    def OnKeuanganItems4Menu(self, event):
        self.main=kaspajak.create(None)
        self.main.Show()

    def OnKeuanganItems5Menu(self, event):
        self.main=bankdesa.create(None)
        self.main.Show()

    def OnBantuanItems0Menu(self, event):
        self.main=tentang.create(None)
        self.main.Show()

   
    def OnIsiprofilItems5Menu(self, event):
        self.main=namapejabat.create(None)
        self.main.Show()


    def OnIsiprofilItems6Menu(self, event):
        self.main=inputdatart.create(None)
        self.main.Show()


    
