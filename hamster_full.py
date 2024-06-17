import requests, json, time, sys, random
from colorama import init
from termcolor import colored

init()
action = input("what do you want : (upgrade, recive) ")
session = requests.Session()
proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}

min_roi = 72
# set , proxies=proxies, verify=False
for_input = 50 #int(input("Please enter how many times do you want to upgrade : "))
#break_time = 15 #int(input("How long wait between upgrades : "))
mahdi_token = '1717578287677FKZrpIPCgMS7DaiIfqSvYXJePECPs4mvirmm6wq7DGiMLu8GwUYTb2MtpOBmPQaE332286435'
mahdi2_token = '1717738045449lzu0v95kWohiDbaRVMlAGLNwjOg49Z0HzK3CbOFhMo5VVkoC7fM0sVYY4GrgwKJQ7154155704'
mom_token = '1717738237089ipd6FT3vEP0wpVhETxLVjAyY60jZdb12XsVRRgXmjRaPax0JsIS9L6TGJq9LcgL6115169669'
yosaf_token = '1717748014626gJzyGDkbomiDZHldDBRRwtWA2A2oims4gTmqUTliyRPXGfAb19VUZQKpQVOUdygW6378481367'
zahra_token = '1718631666871FVbL2Kmiv3SLkm9ZmaPv4DMfeUg5hLOLjLx9rlxZKEknZ17EoFZyw6FVxwxNmTaj374377885'
tokens = {'mahdi' : mahdi_token, 'mahdi2' : mahdi2_token, 'mom' : mom_token, 'yosaf' : yosaf_token, 'zahra' : zahra_token}
tok_names = {1 : 'mahdi', 2 : "mahdi2", 3 : 'mom', 4 : 'yosaf' , 5 : 'zahra'}
'''uncomment if want to use select method'''
#print(f'{time.strftime('%X')} [+] Loading registerd Database  ......')
#for i in range(len(tokens)):
#    print(f"{i+1} : {tok_names[i+1]}")
#selected_token = int(input(f'{time.strftime('%X')} [+] Now Select user to start action : '))
#token = tokens[selected_token]
token = None
print(time.strftime('%X') + f' - [+] Establish initial connection  ......')
time.sleep(1)

def countdown_timer(seconds):
    # Print initial message
    while seconds >= 0:
        # Print the countdown
        print(f"Time remaining: {seconds} seconds", end='\r')
        
        # Blink effect
        if seconds % 2 == 0:
            print(" " * 30, end='\r')
        else:
            print(f"Time remaining: {seconds} seconds", end='\r')
        
        sys.stdout.flush()
        time.sleep(1)
        
        seconds -= 1

def calculate(upgrade_list, account_balance):
    min = {}
    upgrade_obj = upgrade_list['upgradesForBuy']
    for item in upgrade_obj:
        if item['profitPerHour'] == 0 or item['price'] == 0 or item['profitPerHourDelta'] == 0 or item['isAvailable'] == False or item['isExpired'] == True or account_balance < item['price']:
            continue
        if 'cooldownSeconds' in item and item['cooldownSeconds']:
            continue
        ratio = item['profitPerHourDelta'] / item['price']
        roi = item['price'] / item['profitPerHourDelta']
        last_ratio = roi / ratio
        
        if len(min) == 0:
            min = item
            min['ratio'] = ratio
            min['roi'] = roi
            min['last_ratio'] = last_ratio
        
        if last_ratio < min['last_ratio']:
            min = item
            min['ratio'] = ratio
            min['roi'] = roi
            min['last_ratio'] = last_ratio
    return min

def remove(string):
    return string.replace(" ", "")

def clicker():
    clicker_url = 'https://hamsterkombat.io/clicker/'
    headers_clicker = {
    'Host': 'hamsterkombat.io',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'iframe',
    'Sec-Ch-Ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Linux"',
    'Referer': 'https://web.telegram.org/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,fa;q=0.8',
    'Priority': 'u=0, i',
    }
    clicker_status = session.get(clicker_url, headers=headers_clicker, timeout=20)

def authme(token_local):
    authme_url = 'https://api.hamsterkombat.io/auth/me-telegram'
    headers_authme = {
    'Host': 'api.hamsterkombat.io',
    'Content-Length': '0',
    'Sec-Ch-Ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Authorization': f'Bearer {token_local}',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Sec-Ch-Ua-Platform': '"Linux"',
    'Accept': '*/*',
    'Origin': 'https://hamsterkombat.io',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://hamsterkombat.io/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,fa;q=0.8',
    'Priority': 'u=1, i',
    'Connection': 'close'
    }
    session.post(authme_url, headers=headers_authme, timeout=20)

def config(token_local):
    config_url = 'https://api.hamsterkombat.io/clicker/config'
    headers_config = {
    'Host': 'api.hamsterkombat.io',
    'Content-Length': '0',
    'Sec-Ch-Ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Authorization': f'Bearer {token_local}',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Sec-Ch-Ua-Platform': '"Linux"',
    'Accept': '*/*',
    'Origin': 'https://hamsterkombat.io',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://hamsterkombat.io/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,fa;q=0.8',
    'Priority': 'u=1, i',
    'Connection': 'close'
        }
    session.post(config_url, headers=headers_config, timeout=20)
    return None

def sync(token_local):
    sync_url = 'https://api.hamsterkombat.io/clicker/sync'
    headers_sync = {
    'Host': 'api.hamsterkombat.io',
    'Content-Length': '0',
    'Sec-Ch-Ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Authorization': f'Bearer {token_local}',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Sec-Ch-Ua-Platform': '"Linux"',
    'Accept': '*/*',
    'Origin': 'https://hamsterkombat.io',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://hamsterkombat.io/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,fa;q=0.8',
    'Priority': 'u=1, i',
    'Connection': 'close'
}
    sync_ret = session.post(sync_url, headers=headers_sync, timeout=20)
    return sync_ret

def get_data(token_local):
    data_recive = False
    while not data_recive:
        print(time.strftime('%X') + ' - [+] Sending Request to server ......')
        time.sleep(1)
        print(time.strftime('%X') + ' - [+] Getting data from Server ......')
        time.sleep(1)
        get_url = 'https://api.hamsterkombat.io/clicker/upgrades-for-buy'

        headers = {
            'Host': 'api.hamsterkombat.io',
            'Content-Length': '0',
            'Sec-Ch-Ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Authorization': f'Bearer {token_local}',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
            'Sec-Ch-Ua-Platform': '"Linux"',
            'Accept': '*/*',
            'Origin': 'https://hamsterkombat.io',
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://hamsterkombat.io/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9,fa;q=0.8',
            'Priority': 'u=1, i',
            'Connection': 'close'
            }
        try:
            response = session.post(get_url, headers=headers, timeout=20)
            res_test = response.json()
            print(time.strftime('%X') + ' - [+] Data recived from server ......')
            time.sleep(1)
            return res_test
        except:
            print(colored(time.strftime('%X') + f' - [-] Unable to reach server ......','red'))


    print(time.strftime('%X') + ' - [+] Data recived from server ......')
    time.sleep(1)
    return res_test

def send_data(init_balance, token_local):
    upgrade_url = 'https://api.hamsterkombat.io/clicker/buy-upgrade'
    balance = init_balance
    for i in range(for_input):
        res_test = get_data(token_local)
        print(time.strftime('%X') + ' - [+] Start calculating for best upgrade ......')
        time.sleep(1)
        min = calculate(res_test,balance)
        print(time.strftime('%X') + ' - [+] Calculate complete ......')
        time.sleep(1)
        print(time.strftime('%X') + f' - [+] The best upgrade is : ' + colored(f'{min["name"]}', 'green') + f' - with ROI : {int(min["roi"])} Hours')
        time.sleep(1)
        if int(min['roi']) > min_roi:
            print(time.strftime('%X') + f' - [-] {colored(f"Roi larger Than {min_roi} H", "red")}')
            sys.exit(1)
        print(time.strftime('%X') + ' - [+] Generate new Timestamp for anti-blocking ......')
        time.sleep(1)
        current_timestamp = int(time.time() * 1000)
        print(time.strftime('%X') + ' - [+] Timestamp calculated ......')
        time.sleep(1)

        data = {"upgradeId": f"{min['id']}","timestamp": current_timestamp}
        content_len = len(str(remove(str(data))))
        headers = {
            'Host': 'api.hamsterkombat.io',
            'Content-Length': f'{content_len}',
            'Sec-Ch-Ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Sec-Ch-Ua-Mobile': '?0',
            'Authorization': f'Bearer {token_local}',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
            'Sec-Ch-Ua-Platform': '"Linux"',
            'Origin': 'https://hamsterkombat.io',
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://hamsterkombat.io/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9,fa;q=0.8',
            'Priority': 'u=1, i',
            'Connection': 'close'
                }

        print(time.strftime('%X') + ' - [+] Now sending upgrade to server ......')
        time.sleep(1)

    
        try:
            response = session.post(upgrade_url, headers=headers, data=json.dumps(data), timeout=20)
            print(time.strftime('%X') + ' - [+] Data send complete , Waiting for respons ......')
        except:
            try :
                response = session.post(upgrade_url, headers=headers, data=json.dumps(data), timeout=20)
                print(time.strftime('%X') + ' - [+] Data send complete , Waiting for respons ......')
            except:
                print(colored(f'[-] Unable to send post to server ......', 'red'))
                print(colored('[-] Failed to send data ......', 'red'))
                print(colored('[-] Retring in 5 Again ......','red'))
                countdown_timer(5)
                sys.exit(2)
        res_json = response.json()
        if response.status_code == 200 :
            print(colored(time.strftime('%X') + ' - [+] Successful ......', 'green'))
            passive_earn = res_json['clickerUser']['earnPassivePerHour']
            print(time.strftime('%X') + f" - [+] New Passive earn : " + f'{passive_earn:,}')
            balance = int(res_json['clickerUser']['balanceCoins'])
            print(time.strftime('%X') + f" - [+] Balance is  {balance:,}......")


        else :
            print(colored(time.strftime('%X') + f' - [+] Failed ......','red'))
        break_time = random.randint(10, 20)
        countdown_timer(break_time)

def just_send(token_send,tok):
    clicker()
    authme(token_send)
    config(token_send)
    sync_return = sync(token_send)
    balance = int(sync_return.json()['clickerUser']['balanceCoins'])
    print(time.strftime('%X') + f' - [+] The initial balance of {colored(tok, "blue")} is : ' + f'{balance:,}')
    
def receive_coins():
    counter = 1
    while True:
        for tok in tokens:
            users = {}
            users[tok] = False
            token = tokens[tok]
            print(time.strftime('%X') + f' - [+] trying {counter} time')
            while not users[tok]:
                try:
                    just_send(token, tok)
                    session.close()
                    users[tok] = True
                except:
                    print(colored(time.strftime('%X') + ' - [-] Failed to establish connection ......', 'red'))
                    print(colored(time.strftime('%X') + ' [-] Retring in 5 Again ......','red'))
                    countdown_timer(5)
        counter += 1
        countdown_timer(3600)    
    
def upgrade():
    print(tok_names.values())
    selected_token = input("select which user do you want to upgrade? : ")
    token = tokens[selected_token]
    counter = 1
    establish = False
    while not establish:
        try:
            clicker()
            authme(tokens[selected_token])
            config(tokens[selected_token])
            sync_return = sync(tokens[selected_token])
            balance = int(sync_return.json()['clickerUser']['balanceCoins'])
            print(time.strftime('%X') + f' - [+] The initial balance is : ' + f'{balance:,}')
            establish = True
        except:
            print(colored(time.strftime('%X') + ' - [-] Failed to establish connection ......', 'red'))
            
    while True:
        send_data(balance,tokens[selected_token])
        countdown_timer(10)  
        
        
if action == 'recive':
    receive_coins()
if action == 'upgrade':
    upgrade()
