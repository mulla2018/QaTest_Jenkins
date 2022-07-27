import time
import requests

import json
URL = "https://reqres.in/api/users?page={2}"


res = requests.get(URL)

print(res.json())