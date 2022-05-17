import requests
import json
import jsonpath
import jsonpath_rw_ext as jp

url = 'https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false'


def test_name():
    response = requests.get(url)
    json_response = json.loads(response.text)
    name = jsonpath.jsonpath(json_response, 'Name')
    name1 = ['Carbon credits']
    assert name == name1, "Name don't match"
    assert name is not None


def test_can_relist():
    response = requests.get(url)
    json_response = response.json()
    assert json_response['CanRelist'] is True


def test_promotions():
    response = requests.get(url)
    json_r = json.loads(response.text)
    for name in jp.match("Promotions[*].Name", json_r):
        if name == "Gallery":
            assert name == "Gallery", "Name don't exist"
            for description in jp.match("Promotions[?(@.Description=='Good position in category')].Description",
                                        json_r):
                if description == "Good position in category":
                    assert description == "Good position in category", "Description don't exist "
