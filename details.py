# -----------------------------------------------This code used to print the entire order details of a customer------
import requests

client_id = ' amzn1.application-oa2-client.64bad907bd8946e88947458c7a045b1c'
client_secret = 'amzn1.oa2-cs.v1.091feb164954acb3a122f87a8d827b0adccc4ac53e301ffb43ccf98320baa2c7'
auth_url = f'https://api.amazon.com/auth/o2/token'
orders_url = f'https://sellingpartnerapi-na.amazon.com'



def retrieve_order_data( access_token="Atzr|IwEBIBYeugCiSJwL0pMF_RkpPW9V3mGA8smZkiNssF1gcYhddJ2G1e6DtXXNwtwSwsg1Hm_8EzTK2JqB0ABP4vR0r6X96OlzTlVZAiFROCgH7u45_c-l4p4VVSYut63RQhRcsYVAl9K4EmH8XhY2gx9IRu8y4gGdeLDCa_cKL28ENIpmM4MANM5WEdYVqEbYXjwE_g0NX-LfCqBBgc-08MBV9TA0eWLOmzg4a-4q8Pwp0Rp-ECHwsa7Lxy6NWmiCSmL3l0OO4ADVvw9tzfrfkrgJGMM88IzAN-gV7C-daAS86FcjBvOpouPwU3rKcj9ploFDj9s"):
    headers = {
        'Authorization': f'Bearer {access_token}',
        'x-amz-access-token': access_token,
    }

    response = requests.get(orders_url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to retrieve order data: {response.status_code} - {response.text}")

def generate_order_summaries(order_data):
    summaries = []

    for order in order_data.get('payload', []):
        order_id = order.get('amazonOrderId')
        customer_name = order['buyerInfo']['CustomerName']
        order_date=order[order_data]
        product_name=order[product_name]
        product_quantity=order[product_name]
        order_total = order['orderTotal']['amount']['value']
        assignment = order['assignment']

        summary = {
            'OrderID': order_id,
            'CustomerName': customer_name,
            'OrderDate':order_date,
            'product_name':product_name,
            'orderQuantity':product_quantity,
            'OrderTotal': order_total,
            'assignment':  assignment,
        }

        summaries.append(summary)

    return summaries
 
def main():
    try:
        access_token = "Atzr|IwEBIBYeugCiSJwL0pMF_RkpPW9V3mGA8smZkiNssF1gcYhddJ2G1e6DtXXNwtwSwsg1Hm_8EzTK2JqB0ABP4vR0r6X96OlzTlVZAiFROCgH7u45_c-l4p4VVSYut63RQhRcsYVAl9K4EmH8XhY2gx9IRu8y4gGdeLDCa_cKL28ENIpmM4MANM5WEdYVqEbYXjwE_g0NX-LfCqBBgc-08MBV9TA0eWLOmzg4a-4q8Pwp0Rp-ECHwsa7Lxy6NWmiCSmL3l0OO4ADVvw9tzfrfkrgJGMM88IzAN-gV7C-daAS86FcjBvOpouPwU3rKcj9ploFDj9s"
        order_data = retrieve_order_data(access_token)
        order_summaries = generate_order_summaries(order_data)

        for summary in order_summaries:
            print(summary)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
       

if __name__ == '__main__':
    main()
