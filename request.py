import requests

url = 'http://localhost:5000/predict'
r = requests.post(url,json={'Temp':30, 'pressure':47, 'Humidity':289, 'altitude':29})

print(r.json())