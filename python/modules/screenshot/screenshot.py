# coding=utf-8
"""This script take screenshot and saves it int eh screenshots folder."""
import datetime
import wx
import os


def screenshot():
    """Take a screenshot."""
    # folder_name = datetime.date.today().strftime('%Y-%m-%d')
    file_name = datetime.datetime.now().strftime('%Y%m%d-%H-%M-%S') + '.png'
    # print (folder_name)
    # print(file_name)
    directory = os.path.join('./public/modules/screenshots')
    # print(directory)
    # folder_name)
    # if os.path.exists(directory):
    #    os.makedirs(directory)
    filename = os.path.join(directory, file_name)
    # print(filename)
    app = wx.App()
    screen = wx.ScreenDC()

    size = screen.GetSize()
    width = size[0]
    height = size[1]
    bmp = wx.EmptyBitmap(width, height)
    mem = wx.MemoryDC(bmp)
    mem.SelectObject(bmp)
    mem.Blit(0, 0, width, height, screen, 0, 0)
    mem.SelectObject(wx.NullBitmap)
    img = bmp.ConvertToImage()
    img.SaveFile(filename, wx.BITMAP_TYPE_PNG)
    del mem
    # bmp.SaveFile(filename, wx.BITMAP_TYPE_PNG)

    return (file_name)

# print(screenshot())
