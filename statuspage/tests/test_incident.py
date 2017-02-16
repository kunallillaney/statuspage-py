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
from statuspage.core.incident import RealtimeIncident

class Test_Realtime_Incident:

  def setup_class(self):
    self.incident = RealtimeIncident()
    self.incident.name = 'Test_Incident_Name_1'
    self.incident.message = 'Test_Incident_Message_1'

  def teardown_class(self):
    pass

  def test_create_incident(self):
    self.incident.create()
    
  def test_get_incident(self):
    incident = RealtimeIncident.fromName('Test_Incident_Name_1')
    assert(incident.name == self.incident.name)
    assert(incident.id == self.incident.id)
    assert(incident.message == self.incident.message)

  def test_delete_incident(self):
    self.incident.delete()
    try:
      incident = RealtimeIncident.fromName('Test_Incident_Name_1')
    except ValueError as e:
      assert(e.message == 'Incident does not exist')
