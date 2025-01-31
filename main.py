from fastapi import FastAPI
import platform
import requests

app = FastAPI()


ENDPOINT_MARIADB = "https://qod-api-route-vpc-test-08-workload.apps.w2rz2.rh.wwtpoc.local"
ENDPOINT_MYSQL = "https://qod-api-route-vpc-test-08-workload02.apps.w2rz2.rh.wwtpoc.local"
ENDPOINT_COCKROACHDB = "https://qod-api-route-vpc-test-08-workload03.apps.w2rz2.rh.wwtpoc.local"
ENDPOINT_MONGODB = "https://qod-api-route-vpc-test-08-workload04.apps.w2rz2.rh.wwtpoc.local"
ENDPOINT_REDIS = "https://qod-api-route-vpc-test-08-workload05.apps.w2rz2.rh.wwtpoc.local"
ENDPOINT_CASSANDRA = "https://qod-api-route-vpc-test-08-workload06.apps.w2rz2.rh.wwtpoc.local"


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


@app.get("/cockroachdb/daily")
def get_daily_quote_from_cockroachdb():
    print("This request is being served by server: " + platform.node())
    
    response = requests.get(ENDPOINT_COCKROACHDB + "/daily", verify=False)

    return response.json()


@app.get("/cockroachdb/random")
def get_random_quote_from_cockroachdb():
    print("This request is being served by server: " + platform.node())
    
    response = requests.get(ENDPOINT_COCKROACHDB + "/random", verify=False)

    return response.json()


@app.get("/mongodb/daily")
def get_daily_quote_from_mongodb():
    print("This request is being served by server: " + platform.node())
    
    response = requests.get(ENDPOINT_MONGODB + "/daily", verify=False)

    return response.json()


@app.get("/mongodb/random")
def get_random_quote_from_mongodb():
    print("This request is being served by server: " + platform.node())
    
    response = requests.get(ENDPOINT_MONGODB + "/random", verify=False)

    return response.json()
    
    
@app.get("/redis/daily")
def get_daily_quote_from_redis():
    print("This request is being served by server: " + platform.node())
    
    response = requests.get(ENDPOINT_REDIS + "/daily", verify=False)

    return response.json()


@app.get("/redis/random")
def get_random_quote_from_redis():
    print("This request is being served by server: " + platform.node())
    
    response = requests.get(ENDPOINT_REDIS + "/random", verify=False)

    return response.json()
    

@app.get("/cassandra/daily")
def get_daily_quote_from_cassandra():
    print("This request is being served by server: " + platform.node())
    
    response = requests.get(ENDPOINT_CASSANDRA + "/daily", verify=False)

    return response.json()


@app.get("/cassandra/random")
def get_random_quote_from_cassandra():
    print("This request is being served by server: " + platform.node())
    
    response = requests.get(ENDPOINT_CASSANDRA + "/random", verify=False)

    return response.json()