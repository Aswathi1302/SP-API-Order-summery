# ------------This code is used to print order details in JSON formate--------
import json
from urllib import response
import datetime
import requests
import urllib.parse 


tocken_response=requests.post(
    "https://api.amazon.com/auth/o2/token",
    data= {
        "grant_type": "refresh_tocken",
        "refresh_tocken":["refresh_tocken"],
        "client_id":" amzn1.application-oa2-client.64bad907bd8946e88947458c7a045b1c",
        "client_secret":"amzn1.oa2-cs.v1.091feb164954acb3a122f87a8d827b0adccc4ac53e301ffb43ccf98320baa2c7",
    },
)

access_token = "Atzr|IwEBIBYeugCiSJwL0pMF_RkpPW9V3mGA8smZkiNssF1gcYhddJ2G1e6DtXXNwtwSwsg1Hm_8EzTK2JqB0ABP4vR0r6X96OlzTlVZAiFROCgH7u45_c-l4p4VVSYut63RQhRcsYVAl9K4EmH8XhY2gx9IRu8y4gGdeLDCa_cKL28ENIpmM4MANM5WEdYVqEbYXjwE_g0NX-LfCqBBgc-08MBV9TA0eWLOmzg4a-4q8Pwp0Rp-ECHwsa7Lxy6NWmiCSmL3l0OO4ADVvw9tzfrfkrgJGMM88IzAN-gV7C-daAS86FcjBvOpouPwU3rKcj9ploFDj9s"
marketplace_id="ATVPDKIKX0DER"

request_params = {
        "MarketplaceIds": marketplace_id,
        "CreatedAfter": "2023-01-01T00:00:00Z"
    }
base_url = "https://sellingpartnerapi-na.amazon.com"  
url = f"{base_url}/orders/v0/orders?{urllib.parse.urlencode(request_params)}" 

orders = requests.get(url, headers={"x-amz-access-token": access_token})

headers={
        "x-amz-access-tocken":access_token,
    }  
 

print(json.dumps(orders.json(indent=2)))