module is built from 3 default files

base.py - contains the base point for the widget and the page


```python
class MODULE_NAME:
    """Short description of the widget."""

    def getWidget(self, urlParameters=None):
        """This code should return html to include in the wisget div."""
        html = "<p>Hello world</p>"
        return html

    def getPage(self, urlParameters=None):
        """This code should return the html for a full module page."""
        html = "<p>Hello world</p>"
        return html
```

cron.py - run as maintenance every periodic time - TBD

__init__.py - default module file
