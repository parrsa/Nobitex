import requests

URL = "https://testnetapi.nobitex.net"

def login(username, password):
    file_save_token = open("token.txt", "w")
    header = {"Content-Type": "application/json"}
    try:
        response = requests.post(
            url=URL + '/auth/login/',
            headers=header,
            json={
                "username": username,
                "password": password,
                "remeber": "yes"
                }
        )
        # print(response.status_code)
        response.raise_for_status()
        if response.status_code == 200:
            login_token = response.json()["key"]
            file_save_token.write(login_token)
            file_save_token.close()
            print(f"Your Token: \n{login_token}")
            # print(f"status code = {response.status_code}")
    except requests.exceptions.HTTPError as error1:
        if response.status_code == 403:
            print(f"Your password or username isn't correct. \n{error1}")
        else:
            print(f"ERROR! \n{error1}")
    except requests.exceptions.RequestException as error2:
        print(f"ERROR! \n{error2}")

def profile():
    open_token = open("token.txt", "r")
    token = open_token.read()
    header = {"Authorization": "Token " + token}
    try:
        response = requests.post(
            url=URL + "/users/profile",
            headers=header
        )
        response.raise_for_status()
        if response.status_code == 200:
            print(f"Profile: \n{response.json()}")
            open_token.close()
            # print(f"status code = {response.status_code}")
    except requests.exceptions.RequestException as error2:
        print(f"ERROR! \n{error2}")

def list_of_orders(type = "sell", srcCurrency = None, dstCurrency = "usdt"):
    #type : "buy" or "sell"
    #srcCurrency : Source Currency
    #dstCurrency : Destination Currency
    header = {"content-type" : "application/json"}
    try:
        response = requests.post(
            url = URL + "/market/orders/list",
            headers = header,
            json = {
                "oreder" : "-price",
                "type" : type,
                "srcCurrency" : srcCurrency,
                "dstCurrency" : dstCurrency
            }
        )
        response.raise_for_status()
        if response.status_code == 200:
            print(f"List of Order: \n{response.json()}")
            # print(f"status code = {response.status_code}")
    except requests.exceptions.RequestException as error2:
        print(f"ERROR! \n{error2}")
        
def list_of_trades(srcCurrency, dstCurrency, myTradesOnly = "no"):
    # srcCurrency : Source Currency
    # dstCurrency : Destination Currency
    #myTradesOnly : Show personal trading list ("yes" or "no")
    header = {"content-type" : "application/json"}
    try:
        response = requests.post(
            url = URL + "/market/trades/list",
            headers = header,
            json = {
                "srcCurrency" : srcCurrency,
                "dstCurrency" : dstCurrency,
                "myTradesOnly" : myTradesOnly
            }
        )
        response.raise_for_status()
        if response.status_code == 200:
            print(f"List of Trades: \n{response.json()}")
            # print(f"status code = {response.status_code}")
    except requests.exceptions.RequestException as error2:
        print(f"ERROR! \n{error2}")
def nobitex_statistics(srcCurrency, dstCurrency):
    # srcCurrency : Source Currency
    # dstCurrency : Destination Currency
    header = {"content-type": "application/json"}
    try:
        response = requests.post(
            url = URL + "/market/stats",
            headers = header,
            json = {
                "srcCurrency": srcCurrency,
                "dstCurrency": dstCurrency
            }
        )
        response.raise_for_status()
        if response.status_code == 200:
            print(f"Nobitex Market Statistics: \n{response.json()}")
    except requests.exceptions.RequestException as error2:
        print(f"ERROR! \n{error2}")

def OHLC(symbol, resolution, from_, to):
    #symbol : جفت ارز
    #resolution : Candle Time Frame
    #from_ : The Beginning Time of The Interval
    #to : The Ending Time of The Interval
    from_ = int(from_)
    to = int(to)
    header = {"content-type": "application/json"}
    try:
        response = requests.get(
            url = URL + "/market/udf/history",
            headers = header,
            json = {
                "symbol" : symbol,
                "resolution" : resolution,
                "from" : from_,
                "to" : to
            }
        )
        response.raise_for_status()
        if response.status_code == 200:
            # print(response.status_code)
            print(response.json())
    except requests.exceptions.RequestException as error2:
        print(f"ERROR! \n{error2}")

def global_statistics():
    #Statistics of Binance and Kraken
    try:
        response = requests.post(URL + "/market/global-stats")
        response.raise_for_status()
        if response.status_code == 200:
            print(response.json())
    except requests.exceptions.RequestException as error2:
        print(f"ERROR! \n{error2}")

def login_attempts():
    open_token = open("token.txt", "r")
    token = open_token.read()
    header = {"Authorization": "Token " + token}
    try:
        response = requests.post(
            url=URL + "/users/login-attempts",
            headers = header
        )
        response.raise_for_status()
        if response.status_code == 200:
            print(f"Your login history: \n{response.json()}")
            open_token.close()
            # print(f"status code = {response.status_code}")
    except requests.exceptions.RequestException as error2:
        print(f"ERROR! \n{error2}")

def referral_code():
    open_token = open("token.txt", "r")
    token = open_token.read()
    header = {"Authorization": "Token " + token}
    try:
        response = requests.post(
            url=URL + "/users/get-referral-code",
            headers=header
        )
        response.raise_for_status()
        if response.status_code == 200:
            print(f"Your referral code: \n{response.json()['referralCode']}")
            open_token.close()
            # print(f"status code = {response.status_code}")
    except requests.exceptions.RequestException as error2:
        print(f"ERROR! \n{error2}")

def add_card_number(card_number, bank_name):
    open_token = open("token.txt", "r")
    token = open_token.read()
    header = {"Authorization": "Token " + token,
              "content-type": "application/json"}
    open_token.close()
    try:
        response = requests.post(
            url=URL + "/users/cards-add",
            headers=header,
            json={
                "number": card_number,
                "bank": bank_name
            }
        )
        response.raise_for_status()
        if response.status_code == 200:
            print(f"Completed. \n{response.json()}")
            print(response.status_code)
    except requests.exceptions.RequestException as error2:
        print(f"ERROR! \n{error2}")

def add_account_number(account_number, shaba_number, bank_name):
    open_token = open("token.txt", "r")
    token = open_token.read()
    header = {"Authorization": "Token " + token,
              "content-type": "application/json"}
    open_token.close()
    try:
        response = requests.post(
            url=URL + "/users/accounts-add",
            headers=header,
            json={
                "number": account_number,
                "shaba": shaba_number,
                "bank": bank_name
            }
        )
        response.raise_for_status()
        if response.status_code == 200:
            print(f"Completed. \n{response.json()}")
            print(response.status_code)
    except requests.exceptions.RequestException as error2:
        print(f"ERROR! \n{error2}")

def limitations():
    open_token = open("token.txt", "r")
    token = open_token.read()
    header = {"Authorization": "Token " + token}
    try:
        response = requests.post(
            url=URL + "/users/limitations",
            headers=header
        )
        response.raise_for_status()
        if response.status_code == 200:
            print(f"Your limitaions: \n{response.json()}")
            open_token.close()
            # print(f"status code = {response.status_code}")
    except requests.exceptions.RequestException as error2:
        print(f"ERROR! \n{error2}")

def wallets_list():
    open_token = open("token.txt", "r")
    token = open_token.read()
    header = {"Authorization": "Token " + token}
    try:
        response = requests.post(
            url=URL + "/users/wallets/list",
            headers=header
        )
        response.raise_for_status()
        if response.status_code == 200:
            print(f"Your wallets list: \n{response.json()}")
            open_token.close()
            # print(f"status code = {response.status_code}")
    except requests.exceptions.RequestException as error2:
        print(f"ERROR! \n{error2}")

def wallets_balance(currency):
    open_token = open("token.txt", "r")
    token = open_token.read()
    header = {"Authorization": "Token " + token,
              "content-type": "application/json"}
    open_token.close()
    try:
        response = requests.post(
            url=URL + "/users/wallets/balance",
            headers=header,
            json={
                "currency": currency
            }
        )
        response.raise_for_status()
        if response.status_code == 200:
            print(f"Your wallet balance: \n{response.json()['balance']} {currency}")
            # print(response.status_code)
    except requests.exceptions.RequestException as error2:
        print(f"ERROR! \n{error2}")

# login("miladazami120@gmail.com", "Sa3257121600")
# profile()
# list_of_orders("buy")
# list_of_trades("btc", "rls")
# nobitex_statistics("btc", "usdt")
##### OHLC("btcusdt, "D", "1567424381", "1567395581")
# print(global_statistics())
# login_attempts()
# referral_code()
##### add_card_number("5041721011111111", "رسالت")
##### add_account_number("5041721011111111", "IR111111111111111111111111", "رسالت")
## profile()
# limitations()
# wallets_list()
# wallets_balance("ltc")