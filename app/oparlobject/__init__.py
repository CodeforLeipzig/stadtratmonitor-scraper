from ..abstract.oparl import *

from .object.object import OparlObject
from .object.factory import OparlFactory
from .property import converter

converter.ConverterConnector.oparl_factory = OparlFactory


class Consultation(OparlObject, AbcConsultation, factory=OparlFactory): ...
class Location(OparlObject, AbcLocation, factory=OparlFactory): ...
class MainFile(OparlObject, AbcMainFile, factory=OparlFactory): ...
class Membership(OparlObject, AbcMembership, factory=OparlFactory): ...
class Organization(OparlObject, AbcOrganization, factory=OparlFactory): ...
class Paper(OparlObject, AbcPaper, factory=OparlFactory): ...
class Person(OparlObject, AbcPerson, factory=OparlFactory): ...
