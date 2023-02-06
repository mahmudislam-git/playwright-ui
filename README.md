
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
```

## To Record Tests using Playwright

```
playWright codegen <your application url>

```

## Run the Tests

```
pytest --settings=settings_qa tests --headed --slowmo  12000

```

## Open the SQLite DB to fetch the resource monitoring data from pytest-monitor

```
sqlite3 .pymon
sqlite> select ITEM,ITEM_START_TIME,TOTAL_TIME ,USER_TIME,CPU_USAGE,MEM_USAGE from TEST_METRICS;

```



