"""Screenshots widget."""


class screenshot:
    """Screenshot widget."""

    def getWidget(self):
        """Get the last screenshot."""
        # newest = max(glob.iglob('modules/screenshot/screenshots/*.png'),
        # key=os.path.getctime)
        return "<p> newest </p>"

    def getPage(self):
        """Get the page."""
        return "OK"
