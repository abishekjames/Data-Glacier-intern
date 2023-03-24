import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'Year':2023})
r = requests.post(url,json={'Present_Price':6})
r = requests.post(url,json={'Kms_Driven':60000})
r = requests.post(url,json={'Fuel_Type_Petrol':1})
r = requests.post(url,json={'Owner':1})
r = requests.post(url,json={'Seller_Type_Individual':1})
r = requests.post(url,json={'Transmission_Mannual':1})
print(r.json())