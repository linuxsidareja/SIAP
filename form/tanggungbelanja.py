#Boa:Frame:tanggungbelanja
#-------------------------------------------------------------------------------
#Sistem Informasi dan Administrasi Perdesaan
#pengembang johandri@ictwatch.id
#-------------------------------------------------------------------------------

import wx

def create(parent):
    return tanggungbelanja(parent)

[wxID_TANGGUNGBELANJA] = [wx.NewId() for _init_ctrls in range(1)]

class tanggungbelanja(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_TANGGUNGBELANJA,
              name=u'tanggungbelanja', parent=prnt, pos=wx.Point(409, 194),
              size=wx.Size(919, 475), style=wx.DEFAULT_FRAME_STYLE,
              title=u'Pernyataan Tanggung Jawab Belanja')
        self.SetClientSize(wx.Size(911, 445))
        self.Center(wx.BOTH)
        self.SetBackgroundColour(wx.Colour(192, 192, 192))

    def __init__(self, parent):
        self._init_ctrls(parent)
