import pytest
import requests
import platform

ENDPOINT = "http://localhost:8080"

@pytest.mark.repeat(10)  # Run the test 10 times
def test_can_call_endpoint():
    if "https" in ENDPOINT.lower():
        response = requests.get(ENDPOINT, verify=False)
    else:
        response = requests.get(ENDPOINT)
    
    print("This request is being served by server: " + platform.node())

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
    
    print("This request is being served by server: " + platform.node())
    
    #data = response.json()
    #print(data)
    
    assert response.status_code == 200

@pytest.mark.repeat(10)  # Run the test 10 times
def test_get_items():
    if "https" in ENDPOINT.lower():
        response = requests.get(ENDPOINT + "/items", verify=False)
    else:
        response = requests.get(ENDPOINT + "/items")
    
    print("This request is being served by server: " + platform.node())
    
    #data = response.json();
    #print(data)

    assert response.status_code == 200
    
@pytest.mark.repeat(10)  # Run the test 10 times
def test_get_an_item():
    if "https" in ENDPOINT.lower():
        response = requests.get(ENDPOINT + "/items/0", verify=False)
    else:
        response = requests.get(ENDPOINT + "/items/0")
    
    print("This request is being served by server: " + platform.node())
    
    #data = response.json();
    #print(data)

    assert response.status_code == 200
    
@pytest.mark.repeat(10)  # Run the test 10 times
def test_delete_an_item():
    if "https" in ENDPOINT.lower():
        response = requests.delete(ENDPOINT + "/items/0", verify=False)
    else:
        response = requests.delete(ENDPOINT + "/items/0")
    
    print("This request is being served by server: " + platform.node())
    
    #data = response.json();
    #print(data)

    assert response.status_code == 200