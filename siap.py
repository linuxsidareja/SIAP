#!/usr/bin/env python
#Boa:App:BoaApp
#-------------------------------------------------------------------------------
#Sistem Informasi dan Administrasi Perdesaan
#pengembang johandri@ictwatch.id
#-------------------------------------------------------------------------------


import wx

import mulai

modules ={u'apbdesa': [0, '', u'form/apbdesa.py'],
 u'bankdesa': [0, '', u'form/bankdesa.py'],
 u'edit_anggota': [0, '', u'form/edit_anggota.py'],
 u'edit_kejadian_kelahiran': [0, '', u'form/edit_kejadian_kelahiran.py'],
 u'edit_kejadian_kematian': [0, '', u'form/edit_kejadian_kematian.py'],
 u'edit_kejadian_lain': [0, '', u'form/edit_kejadian_lain.py'],
 u'edit_kejadian_pindah': [0, '', u'form/edit_kejadian_pindah.py'],
 u'edit_kk': [0, '', u'form/edit_kk.py'],
 u'edit_profil': [0, '', u'form/edit_profil.py'],
 u'importdata': [0, '', u'form/importdata.py'],
 u'input_data_kemiskinan': [0, '', u'form/input_data_kemiskinan.py'],
 u'input_indikator_kemiskinan': [0, '', u'form/input_indikator_kemiskinan.py'],
 u'input_profil': [0, '', u'form/input_profil.py'],
 u'inputdatart': [0, '', u'form/inputdatart.py'],
 u'jabatan': [0, '', u'form/jabatan.py'],
 u'kaspajak': [0, '', u'form/kaspajak.py'],
 u'kaspembantu': [0, '', u'form/kaspembantu.py'],
 u'kasumum': [0, '', u'form/kasumum.py'],
 u'kejadian_kelahiran': [0, '', u'form/kejadian_kelahiran.py'],
 u'kejadian_kematian': [0, '', u'form/kejadian_kematian.py'],
 u'kejadian_lain': [0, '', u'form/kejadian_lain.py'],
 u'kejadian_pindah': [0, '', u'form/kejadian_pindah.py'],
 u'kk_sementara': [0, '', u'form/kk_sementara.py'],
 u'kk_tetap': [0, '', u'form/kk_tetap.py'],
 u'kunci': [0, '', u'form/kunci.py'],
 u'laporanrkp': [0, '', u'form/laporanrkp.py'],
 u'laporanrpjmdes': [0, '', u'form/laporanrpjmdes.py'],
 u'lihatpendapatan': [0, '', u'form/lihatpendapatan.py'],
 u'mulai': [1, 'Main frame of Application', u'mulai.py'],
 u'namapejabat': [0, '', u'form/namapejabat.py'],
 u'pecah_keluarga': [0, '', u'form/pecah_keluarga.py'],
 u'pemasukanapbdesa': [0, '', u'form/pemasukanapbdesa.py'],
 u'pembangunandesa': [0, '', u'form/pembangunandesa.py'],
 u'pemberdayaanmasyarakat': [0, '', u'form/pemberdayaanmasyarakat.py'],
 u'pembinaankemasyarakatan': [0, '', u'form/pembinaankemasyarakatan.py'],
 u'pembuatan_surat_keluar': [0, '', u'form/pembuatan_surat_keluar.py'],
 u'pendapatanaslidesa': [0, '', u'form/pendapatanaslidesa.py'],
 u'pendapatanlainlain': [0, '', u'form/pendapatanlainlain.py'],
 u'pendapatantransfer': [0, '', u'form/pendapatantransfer.py'],
 u'penerimaanpembiayaan': [0, '', u'form/penerimaanpembiayaan.py'],
 u'pengeluaranpembiayaan': [0, '', u'form/pengeluaranpembiayaan.py'],
 u'penyelenggaraandesa': [0, '', u'form/penyelenggaraandesa.py'],
 u'permintaanbayar': [0, '', u'form/permintaanbayar.py'],
 u'potensi_ekonomi': [0, '', u'form/potensi_ekonomi.py'],
 u'potensi_pariwisata': [0, '', u'form/potensi_pariwisata.py'],
 u'potensi_pertahanan': [0, '', u'form/potensi_pertahanan.py'],
 u'rab': [0, '', u'form/rab.py'],
 u'realisasiapb1': [0, '', u'form/realisasiapb1.py'],
 u'realisasiapb2': [0, '', u'form/realisasiapb2.py'],
 u'rkppembangunandesa': [0, '', u'form/rkppembangunandesa.py'],
 u'rkppemberdayaanmasyarakat': [0, '', u'form/rkppemberdayaanmasyarakat.py'],
 u'rkppembinaankemasyarakatan': [0, '', u'form/rkppembinaankemasyarakatan.py'],
 u'rkppenyelenggarandesa': [0, '', u'form/rkppenyelenggarandesa.py'],
 u'rkptakterduga': [0, '', u'form/rkptakterduga.py'],
 u'rpjmpembangunandesa': [0, '', u'form/rpjmpembangunandesa.py'],
 u'rpjmpemberdayaanmasyarakat': [0, '', u'form/rpjmpemberdayaanmasyarakat.py'],
 u'rpjmpembinaankemasyarakatan': [0,
                                  '',
                                  u'form/rpjmpembinaankemasyarakatan.py'],
 u'rpjmpenyelenggaraandesa': [0, '', u'form/rpjmpenyelenggaraandesa.py'],
 u'rpjmtakterduga': [0, '', u'form/rpjmtakterduga.py'],
 u'sinkron_data': [0, '', u'form/sinkron_data.py'],
 u'surat_masuk': [0, '', u'form/surat_masuk.py'],
 u'tahunrpjmdes': [0, '', u'form/tahunrpjmdes.py'],
 u'takterduga': [0, '', u'form/takterduga.py'],
 u'tambah_anggota_keluarga': [0, '', u'form/tambah_anggota_keluarga.py'],
 u'tanggungbelanja': [0, '', u'form/tanggungbelanja.py'],
 u'tentang': [0, '', u'form/tentang.py']}

class LoginDialog(wx.Dialog):
    """
    Class to define login dialog
    """
 
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Dialog.__init__(self, None,size=wx.Size(200, 150), title="Login SIAP")
 
        # user info
        
        # pass info
        p_sizer = wx.BoxSizer(wx.HORIZONTAL)
 
        p_lbl = wx.StaticText(self, label="Password:")
        p_sizer.Add(p_lbl, 0, wx.ALL|wx.CENTER, 5)
        self.password = wx.TextCtrl(self, style=wx.TE_PASSWORD|wx.TE_PROCESS_ENTER)
        p_sizer.Add(self.password, 0, wx.ALL, 5)
 
        main_sizer = wx.BoxSizer(wx.VERTICAL)
       
        main_sizer.Add(p_sizer, 0, wx.ALL, 5)
 
        btn = wx.Button(self, label="Login")
        btn.Bind(wx.EVT_BUTTON, self.onLogin)
        main_sizer.Add(btn, 0, wx.ALL|wx.CENTER, 5)
 
        self.SetSizer(main_sizer)
 
    #----------------------------------------------------------------------
    def onLogin(self, event):
        """
        Check credentials and login
        """
        stupid_password = "abcd"
        user_password = self.password.GetValue()
        if user_password == stupid_password:
            self.main = mulai.create(None)
            self.main.Show()
            self.Destroy()
        else:
            print "Username or password is incorrect!"

class BoaApp(wx.App):
    def OnInit(self):
        #self.main = mulai.create(None)
        #self.main.Show()
        #self.SetTopWindow(self.main)
        Login = LoginDialog()
        Login.Show()
        return True
        

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()