
## Installation
 ```
pip install -r requirements. txt 

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



