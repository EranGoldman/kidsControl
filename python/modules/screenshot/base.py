"""Screenshots widget."""
import os
# import glob


class screenshot:
    """Screenshot widget."""

    def getFiles(self):
        """Get the file list."""
        scDir = './public/modules/screenshots'
        return os.listdir(scDir)

    def get_last_file(self):
        """Get last file."""
        scDir = './public/modules/screenshots/'
        files = [(scDir + x) for x in os.listdir(scDir) if x.endswith(".png")]
        return max(files, key=os.path.getctime)

    def getWidget(self, urlParameters=None):
        """Get the last screenshot."""
        scFiles = self.getFiles()
        html = ""
        if (len(scFiles) > 1):
            newest = self.get_last_file()
            # print "Recently modified Docs",newest
            # newest = max(glob.iglob('./public/modules/screenshots/*.png'),
            # key=os.path.getctime)
            html += "<img src='" + newest[2:]
            html += "' width='90%'><br>"
        else:
            html += "<p> Folder has no images</p>"
        # newest = max(glob.iglob('modules/screenshot/screenshots/*.png')
        # ,key=os.path.getctime)
        return html

    def getPage(self, urlParameters=None):
        """Get the page."""
        import screenshot as sc
        html = ""
        html += "<h2> Current screenshot : </h2>"
        if "action" in urlParameters:
            if urlParameters['action'] == "oldscreenshot":
                html += "<p> action == oldscreenshot</p>"
        html += "<img src='public/modules/screenshots/" + sc.screenshot()
        html += "' width='90%'><br>"
        html += "<h2>Old screenshots</h2>"
        scFiles = self.getFiles()
        html += "<br>".join(scFiles)
        return html
