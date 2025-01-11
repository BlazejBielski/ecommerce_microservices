import requests

def get_user_details(user_id):
    try:
        response = requests.get(f"http://auth-service/users/{user_id}/")
        if response.status_code == 200:
            return response.json()
        return {"error": f"User {user_id} not found"}
    except requests.RequestException as e:
        return {"error": f"Failed to connect to auth_service: {str(e)}"}

def verify_product(product_id):
    try:
        response = requests.get(f"http://product-service/products/{product_id}/")
        return response.status_code == 200
    except requests.RequestException as e:
        return False
