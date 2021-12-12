#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# generated by wxGlade 0.9.6 on Thu Oct 29 22:41:10 2020
#

import numpy, matplotlib
if matplotlib.__version__ < '2.2':
    raise ValueError("Minimum Matplotlib version required: 2.2")
#
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas

import wx
import os
from shutil import make_archive

# read from glade
import gui
# read from main solver
import fiber

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade

class MyFrame(gui.MyFrame):


    def OnChooseTargetFile(self, event):  # wxGlade: MyFrame.<event_handler>
        pathname = self.showFileDialog()
        self.text_ctrl_1.SetValue(pathname)

    def OnChooseOutputFile(self, event):  # wxGlade: MyFrame.<event_handler>
        pathname = self.showFileDialog()
        self.text_ctrl_2.SetValue(pathname)

    def showFileDialog(self):
        with wx.FileDialog(self, 'Pls, select File',
                          style=wx.DD_DEFAULT_STYLE
                                | wx.DD_DIR_MUST_EXIST
                                | wx.DD_CHANGE_DIR
                          ) as dialog:
            if dialog.ShowModal() == wx.ID_CANCEL:
                return
            return dialog.GetPath()

    def OnCancel(self, event):  # wxGlade: MyFrame.<event_handler>
        self.Destroy()

    def OnExec(self, event):  # wxGlade: MyFrame.<event_handler>

        target_file = self.text_ctrl_1.GetValue()
        output_file = self.text_ctrl_2.GetValue()
        #
        #filepath = os.path.join(output_file, os.path.basename(target_file))
        #print(target_file)

        # Main Program
        # 入出力ファイルを初期設定以外にする場合は引数 inp_path out_path を指定
        theta,ecumax,ndiv,nn,ecu,esu,\
            mate1,mate2,\
            xx1,yy1,xx2,yy2,ndimx,ndimy,fc,\
            ids,nx,ny,dtx,dty,dia,fy,\
            =\
            self.read_data(target_file)

        print("------------------------------")

        obj = fiber.Fiber(xx1,xx2,yy1,yy2,mate1,mate2)
        if obj.getModel(xx1,xx2,yy1,yy2,ndimx,ndimy,fc,\
                        ids,nx,ny,dtx,dty,dia,fy):
            obj.getG(xx1,xx2,yy1,yy2)
            #obj.viewModel(0.5)
            print("Complete Model Making")
        else:
            del obj
            obj = Fiber()
            dlg = wx.MessageDialog(self, 'Erro input',
                                   'Error input',
                                   wx.OK | wx.ICON_ERROR
                                   )
            dlg.ShowModal()
            dlg.Destroy()
            print("Fail Model Making")



        ax = []
        screen = []
        ax.append( self.matplotlib_axes2 )
        ax.append( self.matplotlib_axes3 )
        ax.append( self.matplotlib_axes4 )
        screen.append( self.matplotlib_canvas2 )

        for i in range(0,len(ax)):
            ax[i].clear()
        for i in range(0,len(screen)):
            screen[i].draw()

        obj.solve(nn,theta,ecumax,ndiv,ecu,esu,ax,screen)

        #obj.solveBySt(nn,theta,0, ecu,"# Ultimate by concrete") # Conの圧縮歪み
        #obj.solveBySt(nn,theta,3,-esu,"# Ultimate by Steel Bar") # 鉄筋の引張歪み

        print("------------------------------")
        print("Complete")

    def OnCap(self,event):

        target_file = self.text_ctrl_1.GetValue()

        theta,ecumax,ndiv,nn,ecu,esu,\
            mate1,mate2,\
            xx1,yy1,xx2,yy2,ndimx,ndimy,fc,\
            ids,nx,ny,dtx,dty,dia,fy,\
            =\
            self.read_data(target_file)

        obj = fiber.Fiber(xx1,xx2,yy1,yy2,mate1,mate2)
        if obj.getModel(xx1,xx2,yy1,yy2,ndimx,ndimy,fc,\
                        ids,nx,ny,dtx,dty,dia,fy):
            obj.getG(xx1,xx2,yy1,yy2)
            #obj.viewModel(0.5)
            print("Complete Model Making")
        else:
            del obj
            obj = Fiber()
            dlg = wx.MessageDialog(self, 'Erro input',
                                   'Error input',
                                   wx.OK | wx.ICON_ERROR
                                   )
            dlg.ShowModal()
            dlg.Destroy()
            print("Fail Model Making")

        comment =\
            obj.solveBySt(nn,theta,0, ecu,"# Ultimate by Concrete") # Conの圧縮歪み
        comment +=\
            obj.solveBySt(nn,theta,3,-esu,"# Ultimate by Steel Bar") # 鉄筋の引張歪み
        self.text_ctrl_result.SetValue(comment)


    ########################################################################
    # View Conter
    def OnConter(self, event):  # wxGlade: MyFrame.<event_handler>

        # Spec
        ax     = self.matplotlib_axes
        screen = self.matplotlib_canvas
        self.matplotlib_axes.clear()
        self.matplotlib_canvas.draw()

        # Make Model
        target_file = self.text_ctrl_1.GetValue()
        theta,ecumax,ndiv,nn,ecu,esu,\
            mate1,mate2,\
            xx1,yy1,xx2,yy2,ndimx,ndimy,fc,\
            ids,nx,ny,dtx,dty,dia,fy,\
            =\
            self.read_data(target_file)

        #plt.tight_layout()
        print("------------------------------")

        obj = fiber.Fiber(xx1,xx2,yy1,yy2,mate1,mate2)
        if obj.getModel(xx1,xx2,yy1,yy2,ndimx,ndimy,fc,\
                        ids,nx,ny,dtx,dty,dia,fy):
            obj.getG(xx1,xx2,yy1,yy2)
            obj.make_cont(nn,theta,ecu,ax,screen)
            print("Complete Model Making")
        else:
            del obj
            obj = Fiber()
            dlg = wx.MessageDialog(self, 'Erro input',
                                   'Error input',
                                   wx.OK | wx.ICON_ERROR
                                   )
            dlg.ShowModal()
            dlg.Destroy()
            print("Fail Model Making")

        #self.matplotlib_canvas.draw()
        del obj
        event.Skip()

    ########################################################################
    # View Model
    def OnPlot(self, event):  # wxGlade: MyFrame.<event_handler>

        # Spec
        ax     = self.matplotlib_axes
        screen = self.matplotlib_canvas
        self.matplotlib_axes.clear()
        self.matplotlib_canvas.draw()

        # Make Model
        target_file = self.text_ctrl_1.GetValue()
        theta,ecumax,ndiv,nn,ecu,esu,\
            mate1,mate2,\
            xx1,yy1,xx2,yy2,ndimx,ndimy,fc,\
            ids,nx,ny,dtx,dty,dia,fy,\
            =\
            self.read_data(target_file)

        #plt.tight_layout()
        print("------------------------------")

        obj = fiber.Fiber(xx1,xx2,yy1,yy2,mate1,mate2)
        if obj.getModel(xx1,xx2,yy1,yy2,ndimx,ndimy,fc,\
                        ids,nx,ny,dtx,dty,dia,fy):
            obj.getG(xx1,xx2,yy1,yy2)
            obj.viewModel(0.5,ax,screen)
            print("Complete Model Making")
        else:
            del obj
            obj = Fiber()
            dlg = wx.MessageDialog(self, 'Erro input',
                                   'Error input',
                                   wx.OK | wx.ICON_ERROR
                                   )
            dlg.ShowModal()
            dlg.Destroy()
            print("Fail Model Making")

        #self.matplotlib_canvas.draw()
        del obj
        event.Skip()

    ########################################################################
    # read data
    def read_data(self,readFile):
    # Read Input File
        mate1 = []
        mate2 = []
        xx1 = []
        yy1 = []
        xx2 = []
        yy2 = []
        dtx = []
        dty = []
        ndimx = []
        ndimy = []
        fc = []
        ids = []
        nx = []
        ny = []
        dtx = []
        dty = []
        dia = []
        fy = []

        for line in open(readFile, "r"):
            # if first low = "#",  skip the line
            if line[0] == "#":
                continue
            data = line.split(",") # split line and put data into

            # read parameter
            if(data[0] == "CTLN"):
                theta   = float(data[1])
                ecumax  = float(data[2])
                ndiv    = int(data[3])
                nn      = float(data[4])
                ecu     = float(data[5])
                print(ecu)
                esu     = float(data[6])
            if(data[0] == "MATE"):
                mate1.append( int(data[1]) )
                mate2.append( float(data[2]) )
            if(data[0] == "FIBE"):
                #print(data)
                xx1.append( float(data[1]) )
                yy1.append( float(data[2]) )
                xx2.append( float(data[3]) )
                yy2.append( float(data[4]) )
                ndimx.append( int(data[5]) )
                ndimy.append( int(data[6]) )
                fc.append( int(data[7]) )
            if(data[0] == "REBA"):
                ids.append( int(data[1]) )
                nx.append( int(data[2]) )
                ny.append( int(data[3]) )
                dtx.append( float(data[4]) )
                dty.append( float(data[5]) )
                dia.append( str(data[6]).replace(' ','') )
                fy.append( int(data[7]) )
        print("Finish to read!")
        return theta,ecumax,ndiv,nn,ecu,esu,\
            mate1,mate2,\
            xx1,yy1,xx2,yy2,ndimx,ndimy,fc,\
            ids,nx,ny,dtx,dty,dia,fy

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