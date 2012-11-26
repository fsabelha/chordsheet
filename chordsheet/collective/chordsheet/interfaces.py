from zope.interface import Interface
from plone.theme.interfaces import IDefaultPloneLayer


class IChordSheet(Interface):
    '''
    Interface for the ChordSheet class.
    '''

class IChordSheetSpecific(IDefaultPloneLayer):
    '''
    Marker interface that defines a Zope 3 skin layer for this product.
    '''
