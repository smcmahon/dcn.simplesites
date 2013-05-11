from Acquisition import aq_base
from Products.Five.component import LocalSiteHook, HOOK_NAME
from Products.SiteAccess.AccessRule import AccessRule
from ZPublisher.BeforeTraverse import registerBeforeTraverse

def siteModified(context, event):
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
    base_object = aq_base(context)
    if hasattr(base_object, HOOK_NAME):
        return
    hook = AccessRule(HOOK_NAME)
    registerBeforeTraverse(base_object, hook, HOOK_NAME, 1)
    setattr(base_object, HOOK_NAME, LocalSiteHook())


def applyTheme(context, event):
    """
        Apply skin to request as we traverse
    """

    skin = context.page_structure
    if skin is not None:
        context.changeSkin(skin, event.request)
