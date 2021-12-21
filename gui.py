#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.6 on Tue Dec 21 21:49:20 2021
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode

import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((884, 700))
        
        # Menu Bar
        self.frame_menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(wx.ID_ANY, "&New", "")
        wxglade_tmp_menu.Append(wx.ID_ANY, "&Save", "")
        wxglade_tmp_menu.Append(wx.ID_ANY, "&Export", "")
        wxglade_tmp_menu.Append(wx.ID_ANY, "&Save as", "")
        wxglade_tmp_menu.AppendSeparator()
        wxglade_tmp_menu.Append(wx.ID_ANY, "E&xit", "")
        self.frame_menubar.Append(wxglade_tmp_menu, "&File")
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(wx.ID_ANY, "&about frame2D", "")
        self.frame_menubar.Append(wxglade_tmp_menu, "&About")
        self.SetMenuBar(self.frame_menubar)
        # Menu Bar end
        
        # Tool Bar
        self.frame_toolbar = wx.ToolBar(self, -1, style=wx.TB_DEFAULT_STYLE)
        self.SetToolBar(self.frame_toolbar)
        # Tool Bar end
        self.text_ctrl_1 = wx.TextCtrl(self, wx.ID_ANY, "./sample/input.csv")
        self.button_1 = wx.Button(self, wx.ID_ANY, u"…")
        figure = self.matplotlib_figure = Figure(tight_layout=True)
        # 1x1 grid, first subplot
        self.matplotlib_axes = figure.add_subplot(111)
        self.matplotlib_canvas = FigureCanvas(self, wx.ID_ANY, figure)
        self.text_ctrl_result = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.TE_READONLY)
        figure2 = self.matplotlib_figure2 = Figure(tight_layout=True)
        # 1x1 grid, first subplot
        self.matplotlib_axes2 = figure2.add_subplot(4,1,(1,2))
        #
        #figure3 = self.matplotlib_figure3 = Figure(tight_layout=True)
        # 1x1 grid, first subplot
        self.matplotlib_axes3 = figure2.add_subplot(413)
        self.matplotlib_axes4 = figure2.add_subplot(414)
        self.matplotlib_canvas2 = FigureCanvas(self, wx.ID_ANY, figure2)
        self.text_ctrl_2 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.button_2 = wx.Button(self, wx.ID_ANY, u"…")
        self.button_5 = wx.Button(self, wx.ID_ANY, "View Model")
        self.button_7 = wx.Button(self, wx.ID_ANY, "Capacity")
        self.button_3 = wx.Button(self, wx.ID_ANY, "Run")
        self.button_6 = wx.Button(self, wx.ID_ANY, "View Conter")
        self.button_4 = wx.Button(self, wx.ID_ANY, "Cancel")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.OnChooseTargetFile, self.button_1)
        self.Bind(wx.EVT_BUTTON, self.OnChooseOutputFile, self.button_2)
        self.Bind(wx.EVT_BUTTON, self.OnPlot, self.button_5)
        self.Bind(wx.EVT_BUTTON, self.OnCap, self.button_7)
        self.Bind(wx.EVT_BUTTON, self.OnExec, self.button_3)
        self.Bind(wx.EVT_BUTTON, self.OnConter, self.button_6)
        self.Bind(wx.EVT_BUTTON, self.OnCancel, self.button_4)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("FibGet")
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(wx.Bitmap("/Users/tsuno/work/pythonApp/fiber/icon/fibGet.png", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.SetBackgroundColour(wx.Colour(47, 47, 47))
        self.SetForegroundColour(wx.Colour(0, 0, 0))
        self.frame_toolbar.Realize()
        self.matplotlib_canvas.SetMinSize((50, 50))
        self.matplotlib_canvas2.SetMinSize((100, 100))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_10 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        label_1 = wx.StaticText(self, wx.ID_ANY, "Input file", style=wx.ALIGN_CENTER)
        label_1.SetForegroundColour(wx.Colour(192, 192, 192))
        sizer_2.Add(label_1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        sizer_2.Add(self.text_ctrl_1, 2, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        sizer_2.Add(self.button_1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        sizer_1.Add(sizer_2, 0, wx.EXPAND, 0)
        sizer_10.Add(self.matplotlib_canvas, 2, wx.ALL | wx.EXPAND, 5)
        sizer_10.Add(self.text_ctrl_result, 1, wx.ALL | wx.EXPAND, 5)
        sizer_7.Add(sizer_10, 2, wx.ALL | wx.EXPAND, 0)
        sizer_3.Add(self.matplotlib_canvas2, 1, wx.ALL | wx.EXPAND, 0)
        sizer_8.Add(sizer_3, 1, wx.EXPAND, 0)
        sizer_7.Add(sizer_8, 2, wx.EXPAND, 0)
        sizer_1.Add(sizer_7, 2, wx.EXPAND, 0)
        label_3 = wx.StaticText(self, wx.ID_ANY, "Output file", style=wx.ALIGN_CENTER)
        label_3.SetForegroundColour(wx.Colour(192, 192, 192))
        sizer_4.Add(label_3, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        sizer_4.Add(self.text_ctrl_2, 2, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        sizer_4.Add(self.button_2, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        sizer_1.Add(sizer_4, 0, wx.EXPAND, 0)
        sizer_5.Add((350, 20), 5, 0, 0)
        sizer_5.Add(self.button_5, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 1)
        sizer_5.Add(self.button_7, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 1)
        sizer_5.Add(self.button_3, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 1)
        sizer_5.Add(self.button_6, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 1)
        sizer_5.Add(self.button_4, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 1)
        sizer_1.Add(sizer_5, 0, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def OnChooseTargetFile(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'OnChooseTargetFile' not implemented!")
        event.Skip()

    def OnChooseOutputFile(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'OnChooseOutputFile' not implemented!")
        event.Skip()

    def OnPlot(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'OnPlot' not implemented!")
        event.Skip()

    def OnCap(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'OnCap' not implemented!")
        event.Skip()

    def OnExec(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'OnExec' not implemented!")
        event.Skip()

    def OnConter(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'OnConter' not implemented!")
        event.Skip()

    def OnCancel(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'OnCancel' not implemented!")
        event.Skip()

# end of class MyFrame

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
