import requests   # type: ignore

def convert_currency(amount, from_currency, to_currency):  
    api_url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"  
    response = requests.get(api_url)  
    data = response.json()  
    rate = data["rates"].get(to_currency, "Invalid Currency")  
    return amount * rate if rate != "Invalid Currency" else "Invalid Conversion"  

def convert_gold(amount, unit):  
    gold_rates = {"gram": 7500, "tola": 87500}  
    return amount * gold_rates.get(unit, "Invalid Unit")