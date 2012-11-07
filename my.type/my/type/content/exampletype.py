"""Definition of the Example Type content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-

from my.type.interfaces import IExampleType
from my.type.config import PROJECTNAME

ExampleTypeSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

ExampleTypeSchema['title'].storage = atapi.AnnotationStorage()
ExampleTypeSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(ExampleTypeSchema, moveDiscussion=False)


class ExampleType(base.ATCTContent):
    """Description of the Example Type"""
    implements(IExampleType)

    meta_type = "ExampleType"
    schema = ExampleTypeSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(ExampleType, PROJECTNAME)
