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
def test_can_create_item():
    payload = {
        "text": "apple",
        "is_done": False
    }
    
    if "https" in ENDPOINT.lower():
        response = requests.post(ENDPOINT + "/items", json=payload, verify=False)
    else:
        response = requests.post(ENDPOINT + "/items", json=payload)
    assert response.status_code == 200
    
    #data = response.json()
    #print(data)

@pytest.mark.repeat(10)  # Run the test 10 times
def test_get_items():
    if "https" in ENDPOINT.lower():
        response = requests.get(ENDPOINT + "/items", verify=False)
    else:
        response = requests.get(ENDPOINT + "/items")
    assert response.status_code == 200
    
    #data = response.json();
    #print(data)

@pytest.mark.repeat(10)  # Run the test 10 times
def test_get_an_item():
    if "https" in ENDPOINT.lower():
        response = requests.get(ENDPOINT + "/items/0", verify=False)
    else:
        response = requests.get(ENDPOINT + "/items/0")
    assert response.status_code == 200
    
    #data = response.json();
    #print(data)
    
@pytest.mark.repeat(10)  # Run the test 10 times
def test_delete_an_item():
    if "https" in ENDPOINT.lower():
        response = requests.delete(ENDPOINT + "/items/0", verify=False)
    else:
        response = requests.delete(ENDPOINT + "/items/0")
    assert response.status_code == 200
    
    #data = response.json();
    #print(data)