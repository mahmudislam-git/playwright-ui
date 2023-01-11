source venv/bin/activate

playwright install

playWright codegen https://ecommerce-playground.lambdatest.io/
 

pytest tests --headed --slowmo  12000