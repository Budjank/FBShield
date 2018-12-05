import requests
import json

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
        print("Result => "+res.text)

print "####################"
print "##### FBShield #####"
print "####################"
print ""
print "[1] Aktifkan (true)"
print "[2] Nonaktifkan (false)"
print ""
a=raw_input("Pilih : ")
if a == "1" or a == "01":
    USER_TOKEN=raw_input("Token : ")
    SHIELD_ENABLE="true"
    turn_shield(USER_TOKEN, SHIELD_ENABLE)
elif a == "2" or a == "02":
    USER_TOKEN=raw_input("Token : ")
    SHIELD_ENABLE="false"
    turn_shield(USER_TOKEN, SHIELD_ENABLE)
