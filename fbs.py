import requests, json, os, sys

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
\t    \ \  \_______/   \ \  \   \   \   \ \  \______/
\t     \ \  \_________  \ \  \   \   \   \ \  \ 
\t      \ \   ________\  \ \  \___\   \   \ \  \______
\t       \ \  \_______/   \ \   ____   \   \ \______  \ 
\t        \ \  \           \ \  \   \   \   \_______\  \ 
\t         \ \  \           \ \  \___\   \      _____\  \ 
\t          \ \__\           \ \ _________\    /\________\        
\t           \/__/            \/__________/    \_________/

Author : Denol Ganz
Team   : Indonesian Sad Cyber
    """

def get_userid(token):
    url = "https://graph.facebook.com/me?access_token=%s" % token
    res = requests.get(url)
    info = json.loads(res.text)
    return info["id"]

def turn_shield(token, enable = True):
    uid = get_userid(token)
    data = 'variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutation' % (enable, str(uid))
    headers = {"Content-Type" : "application/x-www-form-urlencoded", "Authorization" : "OAuth %s" % token}
    url = "https://graph.facebook.com/graphql"
    res = requests.post(url, data = data, headers = headers)
    print("\033[94mDone!!!")



banner()
print warna.biru+"""
Sudah Punya Token?
s = sudah
b = belum
"""
nanya=raw_input("---> ")
if nanya == "s":
    USER_TOKEN=raw_input(warna.oren+"Input Token : ")
    print """
    [1] Aktifkan
    [2] Nonaktifkan
    """
    a=raw_input("Pilih : ")
    if a == "1" or a == "01":
        SHIELD_ENABLE="true"
        turn_shield(USER_TOKEN, SHIELD_ENABLE)
    elif a == "2" or a == "02":
        SHIELD_ENABLE="false"
        turn_shield(USER_TOKEN, SHIELD_ENABLE)
elif nanya == "b":
    user=raw_input(warna.oren+'Username/Email : ')
    passw=raw_input(warna.oren+'Password : ')
    get = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+user+'&locale=en_US&password='+passw+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
    up = get.content
    pu = json.loads(up)
    if "session_key" in up:
        print warna.merah+'Token : '+ warna.hijau + pu["access_token"]
        open(user+'-token.txt', 'a').write(pu["access_token"])
        USER_TOKEN=""+pu['access_token']+""
        print """
        [1] Aktifkan
        [2] Nonaktifkan
        """
        b=raw_input("---> ")
        if b == "1":
            SHIELD_ENABLE="true"
            turn_shield(USER_TOKEN, SHIELD_ENABLE)
        elif b == "2":
            SHIELD_ENABLE="false"
            turn_shield(USER_TOKEN, SHIELD_ENABLE)
    else:
        print 'maaf username/password salah'
