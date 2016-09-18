from moisture_sensor import dweeter
from random import randint
import uuid


def test_send_something():
    """
    Tests sending valid data
    Expects a dictionary with key/value containing {"this": "succeeded"}
    """
    dweet = dweeter.Dweet(project_name=project_name, payload=payload)
    send_response = dweet.send()
    assert isinstance(send_response, dict)
    assert send_response["this"] == "succeeded"


def test_send_none():
    """
    Tests sending no data.
    Expects a dictionary containing:
            {
              "Error sending dweet": "No parameters specified."
            }
    """
    dweet = dweeter.Dweet(project_name=project_name, payload=None)
    send_response = dweet.send()
    assert isinstance(send_response, dict)
    assert send_response["Error sending dweet"] == "No parameters specified."


def test_retrieve_latest():
    """
    Tests retrieving the most recent data
    Expects a dictionary with key/value containing {"this": "succeeded"}
    """
    dweet = dweeter.Dweet(project_name=project_name, payload=None)
    retrieve_latest_response = dweet.retrieve_latest()
    assert isinstance(retrieve_latest_response, dict)
    assert retrieve_latest_response["this"] == "succeeded"


def test_retrieve_last_five():
    """
    Tests retrieving the five most recent data
    Expects:
        a dictionary with key/value containing {"this": "succeeded"}
        "with" key's value to be a list with five elements
    """
    for x in range(0, 5):
        random_payload = {
                  "Trinidad Scorpion": randint(0,2),
                  "Chocolate Scotch Bonnet": randint(0,2),
                  "Jalapeno": randint(0,2)
                }
        dweet = dweeter.Dweet(project_name=project_name, payload=random_payload)
        dweet.send()
    retrieve_last_five_responses = dweet.retrieve_last_five()
    assert isinstance(retrieve_last_five_responses, dict)
    assert retrieve_last_five_responses["this"] == "succeeded"
    assert isinstance(retrieve_last_five_responses["with"], list)
    assert len(retrieve_last_five_responses["with"]) == 5

guid = uuid.getnode()
project_name = "dweeter-test-{}".format(uuid.getnode())
payload = {
          "Trinidad Scorpion": randint(0,2),
          "Chocolate Scotch Bonnet": randint(0,2),
          "Jalapeno": randint(0,2)
        }
