# ---------------This code mainly used to print the access key by using client id and client secret----------
import requests
token_url = "https://api.amazon.com/auth/o2/token"
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}
data = {
    "client_id": "amzn1.application-oa2-client.f88b43d485904f9592f27813ff8be7cc",            
    "client_secret": "amzn1.oa2-cs.v1.8eca63bd22f065c50b1e6201e2036b97bf4752b502b7e6f18845d18635599b5a",   
    "grant_type": "client_credentials",
    "scope": "appstore::apps:readwrite"
}
response = requests.post(token_url, headers=headers, data=data)

if response.status_code == 200:
   
    access_token = response.json().get('access_token')
    print("Access Token:", access_token)
else:
 
    print("Token request failed. Status code:", response.status_code)
    print("Response content:", response.text)