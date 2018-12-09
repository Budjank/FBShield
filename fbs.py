import requests, json, os, sys, hashlib

n = []

class warna:
    ungu = '\033[95m'
    biru = '\033[94m'
    hijau = '\033[92m'
    oren = '\033[93m'
    merah = '\033[91m'

def banner():
    print warna.merah + """
\t     ____________     ___________      ___________
\t    /\    _______\   /\   ____   \    /\   _______\ 
\t    \ \  \_______/   \ \  \ \ \   \   \ \  \______/
\t     \ \  \_________  \ \  \ \ \   \   \ \  \ 
\t      \ \   ________\  \ \  \_\_\   \   \ \  \______
\t       \ \  \_______/   \ \   ____   \   \ \______  \ 
\t        \ \  \           \ \  \ \ \   \   \_______\  \ 
\t         \ \  \           \ \  \_\_\   \      _____\  \ 
\t          \ \__\           \ \ _________\    /\________\        
\t           \/__/            \/__________/    \_________/

Author : Denol Ganz
Team   : Indonesian Sad Cyber
    """

def get_userid(token):
    url = "https://graph.facebook.com/me?access_token=%s" % token
    res = requests.get(url)
    info = json.loads(res.text)
    nick = info['name']
    n.append(info['name'])
    return info["id"]

def turn_shield(token, enable = True):
    uid = get_userid(token)
    data = 'variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutation' % (enable, str(uid))
    headers = {"Content-Type" : "application/x-www-form-urlencoded", "Authorization" : "OAuth %s" % token}
    url = "https://graph.facebook.com/graphql"
    res = requests.post(url, data = data, headers = headers)
    if '"is_shielded":true' in res.text:
        print warna.hijau+"Pelindung Profile Aktif"
    elif '"is_shielded":false' in res.text:
        print warna.biru+"Pelindung Profile Nonaktif"
    else:
        print warna.merah+"Error"

banner()
print warna.biru+"""
Sudah Punya Token?
s = sudah
b = belum
"""
nanya=raw_input(warna.oren+"---> ")
if nanya == "s" or nanya == "S":
    print warna.hijau+"Input Token"
    USER_TOKEN=raw_input(warna.oren+"---> ")
    print warna.biru+"""
    [1] Aktifkan
    [2] Nonaktifkan
    """
    a=raw_input(warna.oren+"---> ")
    if a == "1" or a == "01":
        SHIELD_ENABLE="true"
        turn_shield(USER_TOKEN, SHIELD_ENABLE)
    elif a == "2" or a == "02":
        SHIELD_ENABLE="false"
        turn_shield(USER_TOKEN, SHIELD_ENABLE)
elif nanya == "b" or nanya == "B":
    print warna.merah+"Username"
    usr = raw_input(warna.oren+"---> ");
    print warna.merah+"Password"
    pwd = raw_input(warna.oren+"---> ");
    API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32';
    data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":usr,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"};sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+usr+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.0'+API_SECRET
    x = hashlib.new('md5')
    x.update(sig)
    data.update({'sig':x.hexdigest()})
    req = requests.get('https://api.facebook.com/restserver.php',params=data)
    lol = json.loads(req.text)
    if "session_key" in lol:
        print warna.merah+"Token => "+warna.hijau+lol['access_token']
        USER_TOKEN=""+lol['access_token']+""
        print warna.biru+"""
        [1] Aktifkan
        [2] Nonaktifkan
        """
        b=raw_input(warna.oren+"---> ")
        if b == "1" or b == "01":
            SHIELD_ENABLE="true"
            turn_shield(USER_TOKEN, SHIELD_ENABLE)
        elif b == "2" or b == "02":
            SHIELD_ENABLE="false"
            turn_shield(USER_TOKEN, SHIELD_ENABLE)
    else:
        print warna.merah+"Gagal Login"
