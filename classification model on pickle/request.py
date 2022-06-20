import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'age':22.573729142097473, 'interest':17.96922325097786})
print(r.json())