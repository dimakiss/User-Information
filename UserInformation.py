from bs4 import BeautifulSoup
import requests, ast


class UserInformation():
    def __init__(self):
        self.json_data = self.get_json()
        self.setup_parametes()

    def setup_parametes(self):

        self.IP = self.json_data['ip']
        self.hostname = self.json_data['hostname']
        self.city = self.json_data['city']
        self.region = self.json_data['region']
        self.country = self.json_data['country']
        self.org = self.json_data['org']
        self.location = self.json_data['loc']
        self.timezone = self.json_data['timezone']

    def get_json(self):

        # scrap all the users data from the site'http://ipinfo.io/json'
        # return users data as dict
        url = 'http://ipinfo.io/json'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')
        data_raw = str(soup.text).replace('\n', '')
        data = ast.literal_eval(data_raw)
        return data

    def save_to_text_file(self,file_name,file_loc=None):

        # save the json data to file name "filename" in location "file_loc"
        # if "file loc" is None, save in current folder

        if file_loc!=None:
            file_loc+="\\"
            file_name=file_loc+file_name
        with open(file_name,'w') as f:
            f.write(str(self.json_data))

    def read_from_data_file(self,file_loc):

        # update the json data and all the parametes

        with open(file_loc,'r') as f:
            data_str_format=f.read()
        data_str_format=ast.literal_eval(data_str_format)
        self.json_data=data_str_format
        self.setup_parametes()  # update the parametes


if __name__ == '__main__':
    user = UserInformation()
    
    # demonstration
    print("Your Data")
    print("ip:",user.IP)
    print("hostname:",user.hostname)
    print("city:",user.city)
    print("region:",user.region)
    print("country:",user.country)
    print("loc:",user.location)
    print("org:",user.org)
    print("timezone:",user.timezone)
