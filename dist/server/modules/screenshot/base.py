"""Screenshots widget."""
import os
import datetime
import wx


class screenshot:
    """Screenshot widget."""

    def getFiles(self):
        """Get the file list."""
        scDir = os.path.join(os.getcwd(), 'public','modules','screenshots')
        return os.listdir(scDir)

    def get_last_file(self):
        """Get last file."""
        scDir = os.path.join(os.getcwd(), 'public', 'modules', 'screenshots')
        files = [(scDir + x) for x in os.listdir(scDir) if x.endswith(".png")]
        return max(files, key=os.path.getctime)

    def takeScreenshot(self):
        """Take a screenshot."""
        file_name = datetime.datetime.now().strftime('%Y%m%d-%H-%M-%S') + '.png'
        directory = os.path.join(os.getcwd(), 'public', 'modules', 'screenshots')
        if not os.path.exists(directory):
            os.makedirs(directory)
        filename = os.path.join(directory, file_name)
        app = wx.App()
        screen = wx.ScreenDC()

        size = screen.GetSize()
        width = size[0]
        height = size[1]
        bmp = wx.Bitmap(width, height)
        mem = wx.MemoryDC(bmp)
        mem.SelectObject(bmp)
        mem.Blit(0, 0, width, height, screen, 0, 0)
        mem.SelectObject(wx.NullBitmap)
        img = bmp.ConvertToImage()
        img.SaveFile(filename, wx.BITMAP_TYPE_PNG)
        del mem
        # bmp.SaveFile(filename, wx.BITMAP_TYPE_PNG)

        return (file_name)

    def getWidget(self, urlParameters=None):
        """Get the last screenshot."""
        scFiles = self.getFiles()
        html = ""
        if (len(scFiles) > 1):
            newest = self.get_last_file()
            html += "<img src='" + newest[2:]
            html += "' width='90%'><br>"
        else:
            html += "<p> Folder has no images</p>"
        return html

    def getPage(self, urlParameters=None):
        """Get the page."""
        html = ""
        html += "<h2> Current screenshot : </h2>"
        if "action" in urlParameters:
            if urlParameters['action'] == "oldscreenshot":
                html += "<p> action == oldscreenshot</p>"
        html += "<img src='public/modules/screenshots/" + self.takeScreenshot()
        html += "' width='90%'><br>"
        html += "<h2>Old screenshots</h2>"
        scFiles = self.getFiles()
        html += "<br>".join(scFiles)
        return html
