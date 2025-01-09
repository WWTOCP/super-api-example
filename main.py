from fastapi import FastAPI
import platform
import requests

app = FastAPI()


ENDPOINT_MARIADB = "https://qod-api-route-vpc-test-08-workload.apps.workload3.rh.wwtpoc.local"
ENDPOINT_MYSQL = "https://qod-api-route-vpc-test-08-workload02.apps.workload3.rh.wwtpoc.local"
ENDPOINT_COCKROACHDB = "https://qod-api-route-vpc-test-08-workload03.apps.workload3.rh.wwtpoc.local"
ENDPOINT_MONGODB = "https://qod-api-route-vpc-test-08-workload04.apps.workload3.rh.wwtpoc.local"
ENDPOINT_CASSANDRA = "https://qod-api-route-vpc-test-08-workload05.apps.workload3.rh.wwtpoc.local"
ENDPOINT_REDIS = "https://qod-api-route-vpc-test-08-workload06.apps.workload3.rh.wwtpoc.local"


@app.get("/")
def root():
    print("This request is being served by server: " + platform.node())

    return {"Hello": "Superman"}


@app.get("/mariadb/daily")
def get_daily_quote_from_mariadb():
    print("This request is being served by server: " + platform.node())
    
    response = requests.get(ENDPOINT_MARIADB + "/daily", verify=False)

    return response.json()


@app.get("/mariadb/random")
def get_random_quote_from_mariadb():
    print("This request is being served by server: " + platform.node())
    
    response = requests.get(ENDPOINT_MARIADB + "/random", verify=False)

    return response.json()
    

@app.get("/mysql/daily")
def get_daily_quote_from_mysql():
    print("This request is being served by server: " + platform.node())
    
    response = requests.get(ENDPOINT_MYSQL + "/daily", verify=False)

    return response.json()


@app.get("/mysql/random")
def get_random_quote_from_mysql():
    print("This request is being served by server: " + platform.node())
    
    response = requests.get(ENDPOINT_MYSQL + "/random", verify=False)

    return response.json()
