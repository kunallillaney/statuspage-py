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

from __future__ import print_function
from __future__ import absolute_import
import os
from ConfigParser import SafeConfigParser

class Settings(object):
  
  def __init__(self, file_name='settings.ini'):
    self.parser = SafeConfigParser()
    file_name = os.path.join(os.path.dirname(__file__), file_name)
    try:
      self.parser.read(file_name)
    except Exception as e:
      raise
  
  @property
  def API_TOKEN(self):
    return self.parser.get('general', 'API_TOKEN')

  @property
  def SITE_HOST(self):
    return self.parser.get('general', 'SITE_HOST')

  @property
  def PAGE_ID(self):
    return self.parser.get('general', 'PAGE_ID')
