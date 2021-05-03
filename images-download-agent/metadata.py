import requests
from bs4 import BeautifulSoup
from descriptor import descriptor


url = "https://docs.opendata.aws/noaa-goes16/cics-readme.html"
response = requests.get(url)
soup_object = BeautifulSoup(response.content, "html.parser")
data_table = str(soup_object.find('li'))
data_table

regex = r"(?P<keys>[^>]*) - (?P<valeus>[^<]*)"
output = 'keys_values.json'
tableKeysValues = descriptor(data_table, regex, output)

regexDescription = r"- (?P<sensorDescription>[^>]*) Level (?P<levelDescription>\S+) (?P<channelDescription>[^<]*)"
output = 'description.json'
tableDescriptions = descriptor((data_table), regexDescription, output)

regexId = r"(?P<sensorId>[^>]*)-(?P<levelId>.*)-(?P<channelId>[^<]*)"
output = 'Ids.json'
tableIds = descriptor((data_table), regexId, output)