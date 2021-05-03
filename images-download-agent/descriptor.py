import re
import json

def descriptor(data_table, regex, output):
  
  matches = re.finditer(regex, data_table, re.MULTILINE)  
  
  for matchNum, match in enumerate(matches, start=1):
    match = match.groupdict()
    
    
    with open(output, 'a') as f:
      f.write(json.dumps(match, indent=4))