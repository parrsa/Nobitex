import requests

URL = "https://testnetapi.nobitex.net"

def login(username, password, remember = "no"):
    # For long time tokens(30 days), word "yes" must be entered after username and password.
    # otherwise the program sends word "no" by default and receives four-hours tokens.
    file_save_token = open("token.txt", "w")
    header = {"Content-Type": "application/json"}
    try:
        response = requests.post(
            url = URL + '/auth/login/',
            headers = header,
            json = {
                "username": username,
                "password": password,
                "remeber": remember
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
    except requests.exceptions.RequestException as error:
        if response.status_code == 403:
            print(f"Your password or username isn't correct. \n{error}")
        elif response.status_code == 429:
            print(f"You need to log in with Iran's IP. \n{error}")
        else:
            print(f"ERROR! \n{error}")

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

def list_of_orders(type, srcCurrency = None, dstCurrency = "usdt", order = "-price"):
    # Use this function to get the list of orders.
    # The program shows the price from high to low by default.
    # For showing from low to high, word " price" should be entered for order variable.
    # type : "buy" or "sell"
    # srcCurrency : Source Currency
    # dstCurrency : Destination Currency
    header = {"content-type": "application/json/"}
    try:
        response = requests.post(
            url = URL + "/market/orders/list",
            headers = header,
            json = {
                "order": order,
                "type": type,
                "srcCurrency": srcCurrency,
                "dstCurrency": dstCurrency
            }
        )
        response.raise_for_status()
        if response.status_code == 200:
            print(f"List of Orders: \n{response.json()}")
            # print(f"status code = {response.status_code}")
    except requests.exceptions.RequestException as error:
        print(f"ERROR! \n{error}")
        
def list_of_trades(srcCurrency, dstCurrency, myTradesOnly = "no"):
    # Use this function to get the list of trades.
    # srcCurrency : Source Currency
    # dstCurrency : Destination Currency
    # myTradesOnly : Show personal trading list ("yes" or "no")
    header = {"content-type": "application/json"}
    try:
        response = requests.post(
            url = URL + "/market/trades/list",
            headers = header,
            json = {
                "srcCurrency": srcCurrency,
                "dstCurrency": dstCurrency,
                "myTradesOnly": myTradesOnly
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

def transactions_lits(wallet_ID):
    wallet_ID = int(wallet_ID)
    open_token = open("token.txt", "r")
    token = open_token.read()
    header = {"Authorization": "Token " + token,
              "content-type": "application/json"}
    open_token.close()
    try:
        response = requests.post(
            url=URL + "/users/wallets/transactions/list",
            headers=header,
            json={
                "wallet": wallet_ID
            }
        )
        response.raise_for_status()
        if response.status_code == 200:
            print(f"Your transactions list: \n{response.json()}")
            # print(response.status_code)
    except requests.exceptions.RequestException as error2:
        print(f"ERROR! \n{error2}")

def deposit_withdraw(wallet_ID):
    open_token = open("token.txt", "r")
    token = open_token.read()
    header = {"Authorization": "Token " + token,
              "content-type": "application/json"}
    open_token.close()
    try:
        response = requests.post(
            url=URL + "/users/wallets/deposits/list",
            headers=header,
            json={
                "wallet": wallet_ID
            }
        )
        response.raise_for_status()
        if response.status_code == 200:
            print(f"List of deposits and withdrawals: \n{response.json()}")
            # print(response.status_code)
    except requests.exceptions.RequestException as error2:
        print(f"ERROR! \n{error2}")

def generate_address(wallet_ID):
    open_token = open("token.txt", "r")
    token = open_token.read()
    header = {"Authorization": "Token " + token,
              "content-type": "application/json"}
    open_token.close()
    try:
        response = requests.post(
            url=URL + "/users/wallets/generate-address",
            headers=header,
            json={
                "wallet": wallet_ID
            }
        )
        response.raise_for_status()
        if response.status_code == 200:
            print(f"Your block chain address: \n{response.json()}")
            # print(response.status_code)
    except requests.exceptions.RequestException as error2:
        print(f"ERROR! \n{error2}")

def order(type, srcCurrency, dstCurrency, amount, price, execution = "limit"):
    # type : "buy" or "sell"
    # srcCurrency : Source Currency
    # dstCurrency : Destination Currency
    # amount = The amount you want to buy
    # price = Price to buy
    # execution = "limit" or "market"
    price = int(price)
    open_token = open("token.txt", "r")
    token = open_token.read()
    header = {"Authorization": "token " + token,
              "content-type": "application/json"}
    open_token.close()
    try:
        response = requests.post(
            url=URL + "/market/orders/add",
            headers=header,
            json={
                "type": type,
                "execution": execution,
                "srcCurrency": srcCurrency,
                "dstCurrency": dstCurrency,
                "amount": amount,
                "price": price
            }
        )
        response.raise_for_status()
        if response.status_code == 200:
            print(response.json())
            # print(response.status_code)
    except requests.exceptions.RequestException as error2:
        print(f"ERROR! \n{error2}")


