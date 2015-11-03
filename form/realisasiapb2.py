#Boa:Frame:realisasiapb2
#-------------------------------------------------------------------------------
#Sistem Informasi dan Administrasi Perdesaan
#pengembang johandri@ictwatch.id
#-------------------------------------------------------------------------------

import wx

def create(parent):
    return realisasiapb2(parent)

[wxID_REALISASIAPB2] = [wx.NewId() for _init_ctrls in range(1)]

class realisasiapb2(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_REALISASIAPB2, name=u'realisasiapb2',
              parent=prnt, pos=wx.Point(409, 206), size=wx.Size(919, 475),
              style=wx.DEFAULT_FRAME_STYLE,
              title=u'Realisasi APB Desa Akhir Tahun')
        self.SetClientSize(wx.Size(911, 445))
        self.Center(wx.BOTH)
        self.SetBackgroundColour(wx.Colour(192, 192, 192))

    def __init__(self, parent):
        self._init_ctrls(parent)
