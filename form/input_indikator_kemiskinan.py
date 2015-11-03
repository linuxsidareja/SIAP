#Boa:Frame:indikator
#-------------------------------------------------------------------------------
#Sistem Informasi dan Administrasi Perdesaan
#pengembang johandri@ictwatch.id
#-------------------------------------------------------------------------------

import wx
import wx.lib.buttons


def create(parent):
    return indikator(parent)

[wxID_INDIKATOR, wxID_INDIKATORBUTTON1, wxID_INDIKATORBUTTON2, 
 wxID_INDIKATORBUTTON3, wxID_INDIKATORINPUT_INDIKATOR1, 
 wxID_INDIKATORINPUT_INDIKATOR10, wxID_INDIKATORINPUT_INDIKATOR11, 
 wxID_INDIKATORINPUT_INDIKATOR12, wxID_INDIKATORINPUT_INDIKATOR2, 
 wxID_INDIKATORINPUT_INDIKATOR3, wxID_INDIKATORINPUT_INDIKATOR4, 
 wxID_INDIKATORINPUT_INDIKATOR5, wxID_INDIKATORINPUT_INDIKATOR6, 
 wxID_INDIKATORINPUT_INDIKATOR7, wxID_INDIKATORINPUT_INDIKATOR8, 
 wxID_INDIKATORINPUT_INDIKATOR9, wxID_INDIKATORSTATICTEXT1, 
 wxID_INDIKATORSTATICTEXT10, wxID_INDIKATORSTATICTEXT11, 
 wxID_INDIKATORSTATICTEXT12, wxID_INDIKATORSTATICTEXT2, 
 wxID_INDIKATORSTATICTEXT3, wxID_INDIKATORSTATICTEXT4, 
 wxID_INDIKATORSTATICTEXT5, wxID_INDIKATORSTATICTEXT6, 
 wxID_INDIKATORSTATICTEXT7, wxID_INDIKATORSTATICTEXT8, 
 wxID_INDIKATORSTATICTEXT9, 
] = [wx.NewId() for _init_ctrls in range(28)]

class indikator(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_INDIKATOR, name=u'indikator',
              parent=prnt, pos=wx.Point(401, 212), size=wx.Size(935, 464),
              style=wx.DEFAULT_FRAME_STYLE,
              title=u'Input Indikator Kemiskinan')
        self.SetClientSize(wx.Size(927, 434))
        self.Center(wx.BOTH)
        self.SetBackgroundColour(wx.Colour(192, 192, 192))

        self.staticText1 = wx.StaticText(id=wxID_INDIKATORSTATICTEXT1,
              label=u'1.', name='staticText1', parent=self, pos=wx.Point(32,
              16), size=wx.Size(12, 17), style=0)

        self.input_indikator1 = wx.TextCtrl(id=wxID_INDIKATORINPUT_INDIKATOR1,
              name=u'input_indikator1', parent=self, pos=wx.Point(56, 16),
              size=wx.Size(840, 25), style=0, value=u'')

        self.staticText2 = wx.StaticText(id=wxID_INDIKATORSTATICTEXT2,
              label=u'2.', name='staticText2', parent=self, pos=wx.Point(32,
              48), size=wx.Size(12, 17), style=0)

        self.input_indikator2 = wx.TextCtrl(id=wxID_INDIKATORINPUT_INDIKATOR2,
              name=u'input_indikator2', parent=self, pos=wx.Point(56, 48),
              size=wx.Size(840, 25), style=0, value=u'')

        self.staticText3 = wx.StaticText(id=wxID_INDIKATORSTATICTEXT3,
              label=u'3.', name='staticText3', parent=self, pos=wx.Point(32,
              80), size=wx.Size(12, 17), style=0)

        self.input_indikator3 = wx.TextCtrl(id=wxID_INDIKATORINPUT_INDIKATOR3,
              name=u'input_indikator3', parent=self, pos=wx.Point(56, 80),
              size=wx.Size(840, 25), style=0, value=u'')

        self.staticText4 = wx.StaticText(id=wxID_INDIKATORSTATICTEXT4,
              label=u'4.', name='staticText4', parent=self, pos=wx.Point(32,
              112), size=wx.Size(12, 17), style=0)

        self.input_indikator4 = wx.TextCtrl(id=wxID_INDIKATORINPUT_INDIKATOR4,
              name=u'input_indikator4', parent=self, pos=wx.Point(56, 112),
              size=wx.Size(840, 25), style=0, value=u'')

        self.staticText5 = wx.StaticText(id=wxID_INDIKATORSTATICTEXT5,
              label=u'5.', name='staticText5', parent=self, pos=wx.Point(32,
              144), size=wx.Size(12, 17), style=0)

        self.input_indikator5 = wx.TextCtrl(id=wxID_INDIKATORINPUT_INDIKATOR5,
              name=u'input_indikator5', parent=self, pos=wx.Point(56, 144),
              size=wx.Size(840, 25), style=0, value=u'')

        self.staticText6 = wx.StaticText(id=wxID_INDIKATORSTATICTEXT6,
              label=u'6.', name='staticText6', parent=self, pos=wx.Point(32,
              176), size=wx.Size(12, 17), style=0)

        self.input_indikator6 = wx.TextCtrl(id=wxID_INDIKATORINPUT_INDIKATOR6,
              name=u'input_indikator6', parent=self, pos=wx.Point(56, 176),
              size=wx.Size(840, 25), style=0, value=u'')

        self.staticText7 = wx.StaticText(id=wxID_INDIKATORSTATICTEXT7,
              label=u'7.', name='staticText7', parent=self, pos=wx.Point(32,
              208), size=wx.Size(12, 17), style=0)

        self.input_indikator7 = wx.TextCtrl(id=wxID_INDIKATORINPUT_INDIKATOR7,
              name=u'input_indikator7', parent=self, pos=wx.Point(56, 208),
              size=wx.Size(840, 25), style=0, value=u'')

        self.staticText8 = wx.StaticText(id=wxID_INDIKATORSTATICTEXT8,
              label=u'8.', name='staticText8', parent=self, pos=wx.Point(32,
              240), size=wx.Size(12, 17), style=0)

        self.input_indikator8 = wx.TextCtrl(id=wxID_INDIKATORINPUT_INDIKATOR8,
              name=u'input_indikator8', parent=self, pos=wx.Point(56, 240),
              size=wx.Size(840, 25), style=0, value=u'')

        self.staticText9 = wx.StaticText(id=wxID_INDIKATORSTATICTEXT9,
              label=u'9.', name='staticText9', parent=self, pos=wx.Point(32,
              272), size=wx.Size(12, 17), style=0)

        self.input_indikator9 = wx.TextCtrl(id=wxID_INDIKATORINPUT_INDIKATOR9,
              name=u'input_indikator9', parent=self, pos=wx.Point(56, 272),
              size=wx.Size(840, 25), style=0, value=u'')

        self.input_indikator10 = wx.TextCtrl(id=wxID_INDIKATORINPUT_INDIKATOR10,
              name=u'input_indikator10', parent=self, pos=wx.Point(56, 304),
              size=wx.Size(840, 25), style=0, value=u'')

        self.input_indikator11 = wx.TextCtrl(id=wxID_INDIKATORINPUT_INDIKATOR11,
              name=u'input_indikator11', parent=self, pos=wx.Point(56, 336),
              size=wx.Size(840, 25), style=0, value=u'')

        self.input_indikator12 = wx.TextCtrl(id=wxID_INDIKATORINPUT_INDIKATOR12,
              name=u'input_indikator12', parent=self, pos=wx.Point(56, 368),
              size=wx.Size(840, 25), style=0, value=u'')

        self.staticText10 = wx.StaticText(id=wxID_INDIKATORSTATICTEXT10,
              label=u'10.', name='staticText10', parent=self, pos=wx.Point(24,
              304), size=wx.Size(21, 15), style=0)

        self.staticText11 = wx.StaticText(id=wxID_INDIKATORSTATICTEXT11,
              label=u'11.', name='staticText11', parent=self, pos=wx.Point(24,
              336), size=wx.Size(21, 15), style=0)

        self.staticText12 = wx.StaticText(id=wxID_INDIKATORSTATICTEXT12,
              label=u'12.', name='staticText12', parent=self, pos=wx.Point(24,
              368), size=wx.Size(21, 15), style=0)

        self.button1 = wx.Button(id=wxID_INDIKATORBUTTON1, label=u'Simpan',
              name='button1', parent=self, pos=wx.Point(272, 400),
              size=wx.Size(128, 23), style=0)

        self.button2 = wx.Button(id=wxID_INDIKATORBUTTON2, label=u'Rubah Data',
              name='button2', parent=self, pos=wx.Point(408, 400),
              size=wx.Size(136, 23), style=0)

        self.button3 = wx.Button(id=wxID_INDIKATORBUTTON3,
              label=u'Kembali Kemenu', name='button3', parent=self,
              pos=wx.Point(552, 400), size=wx.Size(152, 23), style=0)
        self.button3.Bind(wx.EVT_BUTTON, self.OnButton3Button,
              id=wxID_INDIKATORBUTTON3)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnTombol_simpan_dataButton(self, event):
        inputindikator1 = str(self.input_indikator1.GetValue())
        inputindikator2 = str(self.input_indikator2.GetValue())
        inputindikator3 = str(self.input_indikator3.GetValue())
        inputindikator4 = str(self.input_indikator4.GetValue())
        inputindikator5 = str(self.input_indikator5.GetValue())
        inputindikator6 = str(self.input_indikator6.GetValue())
        inputindikator7 = str(self.input_indikator7.GetValue())
        inputindikator8 = str(self.input_indikator8.GetValue())
        inputindikator9 = str(self.input_indikator9.GetValue())
        inputindikator10 = str(self.input_indikator10.GetValue())
        inputindikator11 = str(self.input_indikator11.GetValue())
        

    
        

    def OnButton3Button(self, event):
        self.Close()
        self.Destroy()
