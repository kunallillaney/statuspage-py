import pytest
import sys
sys.path.append('..')
from core.component import Component

c = Component()
c.name = 'test'
c.desciption = 'Testing'
import pdb; pdb.set_trace()
comp = Component.fromName('test')
# c.create()
