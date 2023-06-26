import re
import json
from datetime import *
from config import *
import logging
#logging.basicConfig(level=logging.INFO)

def split_if_delimiter_present(string, delimiter):
    if string is None:
        return []
    delimiter_count = string.count(delimiter)
    if delimiter_count >= 1:
        return string.split(delimiter)
    else:
        return [string]

def get_xml_locations(item,tag,ns,delimiter):
       value = item.find(tag, ns).text
       array = split_if_delimiter_present(value, delimiter)
       return array

def get_xml_text(item,tag,ns):
       element_text = item.find(tag, ns)
       if element_text is not None:
          value = item.find(tag, ns).text
          return value
       else:
          return "xml tag is null" 
def get_xml_des(item,tag,ns):
       value = item.find("description", ns).text
       starttijd_match = re.search(r"Starttijd:\s*(.*?)&nbsp;", value)
       starttijd = starttijd_match.group(1) if starttijd_match else None
       eindtijd_match = re.search(r"Eindtijd:\s*(.*?)&nbsp;", value)
       eindtijd = eindtijd_match.group(1) if eindtijd_match else None
       return starttijd ,eindtijd
def get_xml_status(start_date,end_date):
    now = datetime.now()
    status = "Actueel" if end_date == "onbekend" or datetime.strptime(end_date, "%Y-%m-%d %H:%M") > now else \
             "Gepland" if start_date is not None and datetime.strptime(start_date, "%Y-%m-%d %H:%M") > now else \
             "Opgelost" if datetime.strptime(end_date, "%Y-%m-%d %H:%M") < now else None
    return status

def dump_json(data_json,output_file):
    if len(data_json) == 0:
       logging.error('%s - %s',"No Data to write for",output_file)
    else:
        with open(output_file, "w") as file:
             json.dump(data_json, file, indent=4)
