from locale import currency
import requests
import json
url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

currency_1="INR"
currency_2="USD"
amount="1000"

querystring = {"from":currency_1,"to":currency_2,"amount":amount}

headers = {
	"X-RapidAPI-Key": "9c00287bdemshfc1ad72b6f24442p1e9d15jsncaef870b865e",
	"X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
}

response = requests.request("GET",url,headers=headers,params=querystring)
data=json.loads(response.text)
converted_amount=data["result"]["convertedAmount"]
formatted="{:,.2f}".format(converted_amount)

print(converted_amount,formatted)
