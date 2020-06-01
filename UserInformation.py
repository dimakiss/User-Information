from bs4 import BeautifulSoup
import requests,ast


class UserInformation():
  def __init__(self):
      json_data=self.get_json()
      self.IP = json_data['ip']
      self.hostname=json_data['hostname']
      self.city = json_data['city']
      self.region = json_data['region']
      self.country = json_data['country']
      self.org = json_data['org']
      self.location=json_data['loc']
      self.timezone=json_data['timezone']

  def get_json(self):
      url = 'http://ipinfo.io/json'
      response = requests.get(url)
      soup = BeautifulSoup(response.content, 'lxml')
      # print(soup.prettify())
      data_raw = str(soup.text).replace('\n', '')
      data = ast.literal_eval(data_raw)
      return data
      
if __name__ == '__main__':
  user = UserInformation()
