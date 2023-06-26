#!/usr/bin/env python3
from lxml import etree
from functions import *
from config import *
import os
from datetime import *

# All variables are extracted from config.py which is imported on main.py
# All Functions are defined in functions.py which is imported on main.py

if os.path.isfile(input_feed) and os.path.getsize(input_feed) == 0:
   logging.error("input file is empty")
elif not os.path.isfile(input_feed):
     logging.error("Input file does not exist")
else:       
     input_xml = etree.parse(input_feed)
     root = input_xml.getroot()
     for item in root.findall('channel/item'):
         num_items += 1
         try: 
             location = get_xml_locations(item,"james:locations",ns,delimiter)    
             des_json = get_xml_text(item,"description",ns)
             start_date,end_date = get_xml_des(item,des_json,ns)    
             status = get_xml_status(start_date,end_date)
             title = get_xml_text(item,"title",ns)
             postal_code = get_xml_text(item,"james:postalCodes",ns)
             data = {
                     "endDate" : end_date,
                     "title"   : title,
                     "postalCodes" : postal_code,
                     "status" : status,
                     "startDate" : start_date,
                     "description" : des_json
                     }
 
             if 'ZMST' in location or 'ZMOH' in location:
                 num_business_entries += 1
                 logging.debug('%s - %s - %s - %s - %s ',"business",location,start_date,end_date,status)
                 data_list_business.append(data)
             else:
                 num_customer_entries += 1
                 logging.debug('%s - %s - %s - %s - %s',"customer",location,start_date,end_date,status)
                 data_list_customer.append(data)
         except Exception as e:
                 logging.error("Error processing item: %s", e)
     logging.info('%s - %s',"Total records processed",num_items) 
     logging.info('%s - %s',"Total records for business",num_business_entries)
     logging.info('%s - %s',"Total records for customer",num_customer_entries)

#Dump data in json files

dump_json(data_list_business,output_business_feed)
dump_json(data_list_customer,output_customer_feed)
