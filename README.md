source venv/bin/activate

## Install Browsers
playwright install

## Set UI username and password for MacOS,Linux
export BATCH_UI_USERNAME=kingofking
export BATCH_UI_PASSOWORD=password123

## Set UI username and password for Windows
setx BATCH_UI_USERNAME "kingofking"
setx BATCH_UI_PASSOWORD "password123"

## Record the code
playWright codegen https://ecommerce-playground.lambdatest.io/

## Run test on qa env
(Don't use this, until implmentation completed) pytest --settings=settings_qa tests --headed --slowmo  12000