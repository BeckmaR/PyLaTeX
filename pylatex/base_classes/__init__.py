# flake8: noqa

from .errors import PyLaTeXError, TableError
from .latex_object import LatexObject
from .containers import Container, Environment
from .command import CommandBase, Command, Options, Arguments
from .table import TabularBase
from .section import SectionBase
from .float import Float

# Old names of the base classes for backwards compatibility
BaseLaTeXClass = LatexObject
BaseLaTeXContainer = Container
BaseLaTeXNamedContainer = Environment
