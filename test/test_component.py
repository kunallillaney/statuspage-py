# Copyright 2016 Kunal Lillaney (http://kunallillaney.github.io)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest
import sys
sys.path.append('..')
from core.component import Component

class Test_Component:

  def setup_class(self):
    self.component = Component()
    self.component.name = 'Test_Name_1'
    self.component.description = 'Test_Description_1'

  def teardown_class(self):
    pass

  def test_create_component(self):
    self.component.create()
    
  def test_get_component(self):
    component = Component.fromName('Test_Name_1')
    assert(component.name == self.component.name)
    assert(component.id == self.component.id)
    assert(component.description == self.component.description)

  def test_delete_component(self):
    self.component.delete()
    try:
      component = Component.fromName('Test_Name_1')
    except ValueError as e:
      assert(e.message == 'Component does not exist')
