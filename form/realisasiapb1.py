#Boa:Frame:realisasiapb1
#-------------------------------------------------------------------------------
#Sistem Informasi dan Administrasi Perdesaan
#pengembang johandri@ictwatch.id
#-------------------------------------------------------------------------------

import wx

def create(parent):
    return realisasiapb1(parent)

[wxID_REALISASIAPB1] = [wx.NewId() for _init_ctrls in range(1)]

class realisasiapb1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_REALISASIAPB1, name=u'realisasiapb1',
              parent=prnt, pos=wx.Point(409, 206), size=wx.Size(919, 475),
              style=wx.DEFAULT_FRAME_STYLE,
              title=u'Realisasi APB Desa Semester 1')
        self.SetClientSize(wx.Size(911, 445))
        self.Center(wx.BOTH)
        self.SetBackgroundColour(wx.Colour(192, 192, 192))

    def __init__(self, parent):
        self._init_ctrls(parent)
