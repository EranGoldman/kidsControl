"""Lockscreen widget."""
import sys


class lockscreen:
    """Lockscreen widget."""

    def getWidget(self, urlParameters=None):
        """Get the last Lockscreen."""
        html = "<p>Version : 0.1</p>"
        if "action" in urlParameters:
            html += urlParameters['action'][0]
        html += "<p>"+",".join(urlParameters)+"</p>"
        return html

    def getPage(self, urlParameters=None):
        """Get the page."""
        if "restart" in urlParameters:
            if urlParameters['restart']=="now":
                os.execl('server','server')
        return "default - OK"
