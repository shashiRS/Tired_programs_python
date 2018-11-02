import requests

url = 'https://api-us.restb.ai/vision/v1/classify'
payload = {
    # Add your client key
    'client_key': '[client-key]',
    'model_id': 'real_estate_global_v2',
    # Add the image URL you want to classify
    'image_url': 'https://demo.restb.ai/images/demo/demo-1.jpg'
}
# Make the classify request
response = requests.get(url, params=payload)
print response
# The response is formatted in JSON
json_response = response.json()
