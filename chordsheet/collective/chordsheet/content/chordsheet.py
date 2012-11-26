from zope.interface import implements
from Products.Archetypes import atapi
from collective.chordsheet import chordsheetMessageFactory as _
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata
from collective.chordsheet.interfaces import IChordSheet
from collective.chordsheet import config

schema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

  atapi.TextField('description',
           required = 0,           
           widget = atapi.RichWidget(label = ('Notes and Mapping')),
            ), 

  atapi.StringField('composer',
            searchable = 1,
            required = 0,
            widget = atapi.StringWidget(label = _(u'Composer')),
            ),

  atapi.TextField('body',
            searchable = 1,
            required = 1,
            allowable_content_types = ('text/plain',
                                       'text/structured',
                                       'text/html',),
            default_output_type = 'text/x-html-safe',
            widget = atapi.RichWidget(label = _(u'Chords'), 
                                      allow_buttons = ('HELLO_EDITOR',)),
           ),

  atapi.StringField('copyright',
       	    searchable = 1,
       	    required = 0,
       	    widget = atapi.StringWidget(label = ('Copyright')),
            ),

  atapi.StringField('ccli',
       	    searchable = 1,
       	    required = 0,
       	    widget = atapi.StringWidget(label = ('CCLI Number')),
            ),


))

class ChordSheet(base.ATCTContent):
    '''An Archetype for a ChordSheet application'''

    implements(IChordSheet)

    schema = schema

atapi.registerType(ChordSheet, config.PROJECTNAME)
