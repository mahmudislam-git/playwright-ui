
## Installation
 ```
pip install -r requirements.txt 

```

## Set UI Username and Password
### For MacOS or LinuxOS
```
export BATCH_UI_USERNAME=<Enter your UI username>
export BATCH_UI_PASSOWORD=<Enter your UI password>
```
### For Windows
```
setx BATCH_UI_USERNAME "<Enter your UI username>"
setx BATCH_UI_PASSOWORD "<Enter your UI password>"

setx TWILIO_ACCOUNT_SID "twilio_account_sid"
setx TWILIO_AUTH_TOKEN "twilio auth token"
setx FROM_TWILIO_PHONE_NUMBER "from twilio phone number" 
setx TO_PHONE_NUMBER "receiver phone number" 
```

## To Record Tests using Playwright

```
playWright codegen <your application url>

```

## Run the Tests with pytest-monitoring tool enabled 

```
pytest --settings=settings_qa tests --headed --slowmo  12000

```

## Run the Tests with monitoring tool enabled 

```
cd /playwright-ui

~/playwright-ui/venv/bin/python ~/utils/cpu_memory_monitoring.py

pytest --settings=settings_qa tests --headed --slowmo  12000

```

## Open the SQLite DB to fetch the resource monitoring data from pytest-monitor

```
Documentation : https://pytest-monitor.readthedocs.io/en/latest/introduction.html#use-cases

sqlite3 .pymon
sqlite> select ITEM,ITEM_START_TIME,TOTAL_TIME ,USER_TIME,CPU_USAGE,MEM_USAGE from TEST_METRICS;

```



