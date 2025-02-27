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