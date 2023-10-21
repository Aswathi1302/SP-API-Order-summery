from urllib import response
import requests
import json

client_id = ' amzn1.application-oa2-client.64bad907bd8946e88947458c7a045b1c'
client_secret = 'amzn1.oa2-cs.v1.091feb164954acb3a122f87a8d827b0adccc4ac53e301ffb43ccf98320baa2c7'
auth_url = f'https://api.amazon.com/auth/o2/token'
orders_url = f'https://sellingpartnerapi-eu.amazon.com'

dict={'refreshtoken':'Atzr|IwEBIBYeugCiSJwL0pMF_RkpPW9V3mGA8smZkiNssF1gcYhddJ2G1e6DtXXNwtwSwsg1Hm_8EzTK2JqB0ABP4vR0r6X96OlzTlVZAiFROCgH7u45_c-l4p4VVSYut63RQhRcsYVAl9K4EmH8XhY2gx9IRu8y4gGdeLDCa_cKL28ENIpmM4MANM5WEdYVqEbYXjwE_g0NX-LfCqBBgc-08MBV9TA0eWLOmzg4a-4q8Pwp0Rp-ECHwsa7Lxy6NWmiCSmL3l0OO4ADVvw9tzfrfkrgJGMM88IzAN-gV7C-daAS86FcjBvOpouPwU3rKcj9ploFDj9s','lwa_app_id':'amzn1.application-oa2-client.64bad907bd8946e88947458c7a045b1c',
'lwa_client_secret':'amzn1.oa2-cs.v1.091feb164954acb3a122f87a8d827b0adccc4ac53e301ffb43ccf98320baa2c7'}
token_response = requests.post(
    "https://api.amazon.com/auth/o2/token",
    data={
        "grant_type": "refresh_token",
        "refresh_token": dict["refreshtoken"],
        "client_id": dict["lwa_app_id"],
        "client_secret": dict["lwa_client_secret"],
    },
)
access_token = token_response.json()["access_token"]


def retrieve_order_data(access_token):
    orders = requests.get(
        orders_url
        + "/orders/v0/orders"
        + "?MarketplaceIds=A21TJRUUN4KGV&CreatedAfter=2019-01-01",
        headers={
            "x-amz-access-token": access_token,
        },
    )

    if orders.status_code == 200:
        return orders.json()
    else:
        raise Exception(f"Failed to retrieve order data: {orders.status_code} - {orders.text}")

def generate_order_summaries(orders):
    orders = orders["payload"]["Orders"]
    for order in orders:
        print("Order ID:", order["AmazonOrderId"])
        print("Purchase Date:", order.get("PurchaseDate", "N/A"))
        print("Sales Channel:", order.get("SalesChannel", "N/A"))
        print("Order Status:", order["OrderStatus"])
        payment_method_details = order.get("PaymentMethodDetails", [])
        if payment_method_details:
            print("Payment Method:", payment_method_details[0])
        else:
            print("Payment Method: N/A")

        order_total = order.get("OrderTotal")
        if order_total:
            print("Order Total:", f"{order_total['CurrencyCode']} {order_total['Amount']}")
        else:
            print("Order Total: N/A")

        product_quantity = order.get("NumberOfItemsUnshipped")
        if product_quantity:
            print("Product Quantity:", product_quantity)
        else:
            print("Product Quantity: N/A")

        print()

def main():
    try:
        order_data = retrieve_order_data(access_token)
        generate_order_summaries(order_data)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    main()
