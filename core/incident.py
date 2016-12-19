from util.rest import *
from settings import Settings
settings = Settings()

class Incident(object):

  def __init__(self):
    self._name = None
    self._status = None
    self._message = None
    self._impact_override = None
    self._component_ids = None
    self._wants_twitter_update = None

  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self, value):
    self._name = value

  @property
  def status(self):
    return self._status

  @status.setter
  def status(self, value):
    self._status = value

  @property
  def message(self):
    return self._message

  @message.setter
  def message(self, value):
    self._message = value

  @property
  def wants_twitter_update(self):
    return self._wants_twitter_update

  @wants_twitter_update.setter
  def wants_twitter_update(self, value):
    self._wants_twitter_update = value

  @staticmethod
  def list():
    # url format : GET /pages/[page_id]/incidents.json
    url = 'https://{}/pages/{}/Incidents.json'.format(settings.SITE_HOST, settings.PAGE_ID)
    try:
      response = getUrl(url)
      assert(response.status_code == 200)
    except AssertionError as e:
      raise ValueError("Could not fetch incident list. Returned status code {}. Content {}".format(response.status_code, response.content))
    for incident in response.json():
      yield(Incident.fromDict(incident))


class ScheduledIncident(Incident):

  def __init__(self):
    self._scheduled_for = None
    self._scheduled_until = None
    self._scheduled_remind_prior = None
    self._scheduled_auto_in_progress = None
    self._scheduled_auto_completed = None

  def create(self):
    # url format : POST /pages/[page_id]/incidents.json
    url = 'https://{}/pages/{}/incidents.json'.format(settings.SITE_HOST, settings.PAGE_ID)
    component_ids_list = []
    for component in self._component_ids:
      component_ids_list.append(component)
    data = {
            'incident': {
                'name': self.name,
                'status': self.status,
                'message': self.message,
                'wants_twitter_update': self.wants_twitter_update,
                'component_ids': component_ids_list
                }
           }

    try:
      response = postUrl(url, data)
      assert(response.status_code == 201)
    except AssertionError as e:
      raise ValueError("Could not create incident. Returned status code {}. Content {}".format(response.status_code, response.content))
