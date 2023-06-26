Please note below points while executing script

1. Current solution is written in python version 3.11.4
2. Poetry is used as packaging tool ,plea
3. This can be used for larger datasets a summary is shown with debug level info which gives total number of input records,business records and customer records.
4. To avoid complexity all functions  are placed in funtions.py and configs are placed in config.py,this is to make quick and better understanding of parsing
5. I have used config.py to configure input file ,output files ,which is standerd 

Procedure to test or execure script.

1. Below is the structure of files

DataStreamingTeamAssessment
|-- README.md
|-- poetry.lock
|-- pyproject.toml
|-- resources
|   |-- business_outages.json
|   |-- business_output_new.json
|   |-- customer_outages.json
|   |-- customer_output_new.json
|   `-- outages.xml
`-- src
    |-- __pycache__
    |   |-- config.cpython-311.pyc
    |   `-- functions.cpython-311.pyc
    |-- config.py
    |-- functions.py
    `-- main.py

2. Install poetry using below ,if any issues please google since local machines have been stuffed with unwanted libraries

pip install --user poetry #
echo 'export PATH=${HOME}/.local/bin:${PATH}' >> ~/.profile
source ~/.profile

3. Go to location DataStreamingTeamAssessment and perform poetry install

poetry install should show result like below

 Configuration file exists at /Users/mgopathi01/Library/Preferences/pypoetry, reusing this directory.
 Consider moving TOML configuration files to /Users/mgopathi01/Library/Application Support/pypoetry, as support for the legacy directory will be removed in an upcoming release.
 Updating dependencies
 Resolving dependencies... (0.2s)
 Package operations: 1 install, 0 updates, 0 removals

   • Installing lxml (4.9.2)

 Writing lock file


4. After poetry install you can do "poetry shell" to use virtual environment pyproject.toml will install all project requirement dependencies
   if any issues delete poetry.lock and do poetry install again


5.Go to src location and execute main.py file like below

/Users/mgopathi01/TEST/DataStreamingTeamAssessment/src
Mohans-MacBook-Air:src mgopathi01$ ./main.py 
INFO:root:Total records processed - 123
INFO:root:Total records for business - 71
INFO:root:Total records for customer - 52
Mohans-MacBook-Air:src mgopathi01$ 

6. output : from same location ie.,DataStreamingTeamAssessment/src  execute ls -lrt ../resources/*new.json to check output files

ls -lrt ../resources/*new.json
 ../resources/business_output_new.json
 ../resources/customer_output_new.json

7. please note result  can be different from original split files ,since previously "current time" used made possible
to get some records with dates from file in feature ,but with current date time comparision there will be no feature records



Tests performed:

1.Input file is empty or no input file: Go to config.py and change filename or mention a filename which is empty
./main.py 
ERROR:root:Input file does not exist
ERROR:root:No Data to write for - ../resources/business_output_new.json
ERROR:root:No Data to write for - ../resources/customer_output_new.json

./main.py
ERROR:root:input file is empty
ERROR:root:No Data to write for - ../resources/business_output_new.json
ERROR:root:No Data to write for - ../resources/customer_output_new.json

2.Make changes in xml file like a tag doesnt exist for an item it works fine
since it been handled.

couple of tests can be performed by making changed to input xml file


Improvements Required:

1. A Better logic can be possible if more insights are known about possible cases or changes in xml file
   so that a dict can be maintained to reuse functions ie., get tags automatically from xml files and 
   perform a loop on all tags with out mentioning them explicitly
2. Monitoring: A better log handler can be used to send logs to carbonite or any api like pushgateway for prometheus
   so that there can be a trend shown on any visualization tool like grafana. we can run in docker and restrict
   memory and cpu ,so that other application running on server can not be effected if there huge files to be processed
   we can make an arrengement to send notification via grafana (using docker statistics from node exporter)
3. please free to fill points ,i am happy to make any changes which are usefull to this project

