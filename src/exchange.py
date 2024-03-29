from datetime import date
import requests
import json

def get_exchange_rate(base_currency, ex_currency):
    
    today = date.today()
    # modifies the url to access text from api, then stores the rate info
    
    url = 'https://api.exchangerate.host/timeseries?start_date='+str(today)+'&end_date='+str(today)+'&base='+base_currency+'&symbols='+ex_currency
    jsonRates= requests.get(url)
    jsonObject = json.loads(jsonRates.text)
    rates = jsonObject["rates"]
    
    value = rates[str(today)]
    ex_rate = value[ex_currency]
    return ex_rate

def change_global_currency(base_currency, ex_currency, array):
    rate = get_exchange_rate(base_currency, ex_currency)
    for x in array:
        x["Balance"] = x["Balance"]*rate
    return array

def convert_currency(base_currency, ex_currency, amount):
    rate = get_exchange_rate(base_currency, ex_currency)
    amount = amount*rate
