import pytest
import requests

ENDPOINT = "http://localhost:8080"

@pytest.mark.repeat(10)  # Run the test 10 times
def test_can_call_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200

@pytest.mark.repeat(10)  # Run the test 10 times
def test_can_create_item():
    payload = {
        "text": "apple",
        "is_done": False
    }
    response = requests.post(ENDPOINT + "/items", json=payload)
    assert response.status_code == 200
    
    #data = response.json()
    #print(data)

@pytest.mark.repeat(10)  # Run the test 10 times
def test_get_items():
    response = requests.get(ENDPOINT + "/items")
    assert response.status_code == 200
    
    #data = response.json();
    #print(data)

@pytest.mark.repeat(10)  # Run the test 10 times
def test_get_an_item():
    response = requests.get(ENDPOINT + "/items/0")
    assert response.status_code == 200
    
    #data = response.json();
    #print(data)
    
@pytest.mark.repeat(10)  # Run the test 10 times
def test_delete_an_item():
    response = requests.delete(ENDPOINT + "/items/0")
    assert response.status_code == 200
    
    #data = response.json();
    #print(data)