import pytest
import requests

ENDPOINT = "http://localhost:8080"

@pytest.mark.repeat(10)  # Run the test 10 times
def test_can_call_endpoint():
    if "https" in ENDPOINT.lower():
        response = requests.get(ENDPOINT, verify=False)
    else:
        response = requests.get(ENDPOINT)

    assert response.status_code == 200

@pytest.mark.repeat(10)  # Run the test 10 times
def test_get_daily_quote_from_mariadb():
    if "https" in ENDPOINT.lower():
        response = requests.get(ENDPOINT + "/mariadb/daily", verify=False)
    else:
        response = requests.get(ENDPOINT + "/mariadb/daily")
    
    data = response.json();
    print(data)

    assert response.status_code == 200
    
@pytest.mark.repeat(10)  # Run the test 10 times
def test_get_random_quote_from_mariadb():
    if "https" in ENDPOINT.lower():
        response = requests.get(ENDPOINT + "/mariadb/random", verify=False)
    else:
        response = requests.get(ENDPOINT + "/mariadb/random")
    
    data = response.json();
    print(data)

    assert response.status_code == 200

@pytest.mark.repeat(10)  # Run the test 10 times
def test_get_daily_quote_from_mysql():
    if "https" in ENDPOINT.lower():
        response = requests.get(ENDPOINT + "/mysql/daily", verify=False)
    else:
        response = requests.get(ENDPOINT + "/mysql/daily")
    
    data = response.json();
    print(data)

    assert response.status_code == 200
    
@pytest.mark.repeat(10)  # Run the test 10 times
def test_get_random_quote_from_mysql():
    if "https" in ENDPOINT.lower():
        response = requests.get(ENDPOINT + "/mysql/random", verify=False)
    else:
        response = requests.get(ENDPOINT + "/mysql/random")
    
    data = response.json();
    print(data)

    assert response.status_code == 200