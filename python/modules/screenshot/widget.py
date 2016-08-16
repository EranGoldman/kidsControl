"""Screenshots widget."""
import os
import glob


class Widget:
    """Screenshot widget."""

    def getWidgetHtml():
        """Get the last screenshot."""
        newest = max(glob.iglob('*.png'), key=os.path.getctime)
        return "<p>" + newest + "</p>"
