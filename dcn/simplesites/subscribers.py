from Acquisition import aq_base
from Products.Five.component import LocalSiteHook, HOOK_NAME
from Products.SiteAccess.AccessRule import AccessRule
from zope.interface import directlyProvides, directlyProvidedBy, alsoProvides
from ZPublisher.BeforeTraverse import registerBeforeTraverse

from plone.theme.layer import default_layers

from interfaces import IMyBrowserLayer


def siteAdded(context, event):
    """
      objectModified event on simple siteModified.
      this code from collective.editsiteswitcher.
    """

    """Add local site hook with before traverse event.

    Check to see if the current object already has a LocalSiteHook
    from Five registered. If not, then register one ourselves, going
    around ``enableSite`` since we don't want to make this object a
    full ``ISite``, but just get the ``BeforeTraverseEvent`` fired.
    """

    # import pdb; pdb.set_trace()
    base_object = aq_base(context)
    if hasattr(base_object, HOOK_NAME):
        return
    hook = AccessRule(HOOK_NAME)
    registerBeforeTraverse(base_object, hook, HOOK_NAME, 1)
    setattr(base_object, HOOK_NAME, LocalSiteHook())


def applyTheme(context, event):
    """
        Apply IMyBrowserLayer and skin to request as we traverse
    """

    # #Add our browserlayer to the request.
    # Code from plone.theme mark_layer; generalized for
    # non-skin layer
    layer_ifaces = []
    default_ifaces = []
    # We need to make sure IDefaultPloneLayer comes after
    # any other layers, even if they don't explicitly extend it.
    for layer in directlyProvidedBy(event.request):
        if layer in default_layers:
            default_ifaces.append(layer)
        else:
            layer_ifaces.append(layer)
    ifaces = [IMyBrowserLayer, ] + layer_ifaces + default_ifaces
    directlyProvides(event.request, *ifaces)

    # set the skin
    skin = context.page_structure
    if skin is not None:
        context.changeSkin(skin, event.request)

