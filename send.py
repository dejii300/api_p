import requests

headers = {}
headers['Authorization'] = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc1NjA4NTA3LCJpYXQiOjE2NzU2MDc2OTEsImp0aSI6IjRlMDYyMzhiOTNmMjQ2Y2E5MGViZTQzMWQ1ZDI5ZTYyIiwidXNlcl9pZCI6MX0.44NKqVaMfDW-9R7MxECBvia8pkzLD6uQ1JgaKiA1yag'
r = requests.get('http://127.0.0.1:8000/programmers', headers=headers)
print(r.text)