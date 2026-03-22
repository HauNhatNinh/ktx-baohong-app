import urllib.request
import json

url = "http://localhost:5000/api/quen-mat-khau"
payload = json.dumps({
    "vai_tro": "sinhvien",
    "tai_khoan": "K225480106077",
    "xac_minh": "K225480106077@tnut.edu.vn"
}).encode('utf-8')
headers = {'Content-Type': 'application/json'}

try:
    req = urllib.request.Request(url, data=payload, headers=headers)
    with urllib.request.urlopen(req) as response:
        print("Status Code:", response.status)
        print("Response JSON:", response.read().decode())
except urllib.error.HTTPError as e:
    print("HTTP Error:", e.code, e.read().decode())
except Exception as e:
    print("Error:", e)
