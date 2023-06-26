import logging

logging.basicConfig(level=logging.INFO)
delimiter = ";"
data_list_business=[]
data_list_customer=[]
num_items = 0
num_business_entries = 0
num_customer_entries = 0
defined_logging_level='logging.DEBUG'
ns = {"james": "http://www.sqills.com/james/"}
input_feed='../resources/outages.xml'
output_business_feed = '../resources/business_output_new.json'
output_customer_feed = '../resources/customer_output_new.json'
