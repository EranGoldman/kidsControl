"""Screenshots widget."""


class default:
    """Screenshot widget."""

    def getWidget(self, urlParameters=None):
        """Get the last screenshot."""
        html = "<p>Version : 0.1</p>"
        if "action" in urlParameters:
            html += urlParameters['action'][0]
        html += "<p>"+",".join(urlParameters)+"</p>"
        return html

    def getPage(self, urlParameters=None):
        """Get the page."""
        return "default - OK"
