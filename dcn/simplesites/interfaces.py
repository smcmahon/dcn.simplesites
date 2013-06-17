from zope.interface import Interface


class IMyBrowserLayer(Interface):
    """
        Marker applied to request when we traverse into a simple site.
    """