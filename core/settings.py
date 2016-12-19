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
