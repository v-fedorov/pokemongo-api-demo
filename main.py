import requests
import re
import struct
import json
import argparse
import pokemon_pb2
import gyms_pb2

from datetime import datetime
from geopy.geocoders import GoogleV3
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)



API_URL = 'https://pgorelease.nianticlabs.com/plfe/rpc'
LOGIN_URL = 'https://sso.pokemon.com/sso/login?service=https%3A%2F%2Fsso.pokemon.com%2Fsso%2Foauth2.0%2FcallbackAuthorize'
LOGIN_OAUTH = 'https://sso.pokemon.com/sso/oauth2.0/accessToken'

SESSION = requests.session()
SESSION.headers.update({'User-Agent': 'Niantic App'})
SESSION.verify = False

DEBUG = True
COORDS_LATITUDE = 0
COORDS_LONGITUDE = 0
COORDS_ALTITUDE = 0

def f2i(float):
  return struct.unpack('<Q', struct.pack('<d', float))[0]

def f2h(float):
  return hex(struct.unpack('<Q', struct.pack('<d', float))[0])

def h2f(hex):
  return struct.unpack('<d', struct.pack('<Q', int(hex,16)))[0]

def set_location(location_name):
    geolocator = GoogleV3()
    loc = geolocator.geocode(location_name)

    print('[!] Your given location: {}'.format(loc.address))
    print('[!] lat/long/alt: {} {} {}'.format(loc.latitude, loc.longitude, loc.altitude))
    set_location_coords(loc.latitude, loc.longitude, loc.altitude)

def set_location_coords(lat, long, alt):
    global COORDS_LATITUDE, COORDS_LONGITUDE, COORDS_ALTITUDE
    COORDS_LATITUDE = f2i(lat)
    COORDS_LONGITUDE = f2i(long)
    COORDS_ALTITUDE = f2i(alt)

def get_location_coords():
    return (COORDS_LATITUDE, COORDS_LONGITUDE, COORDS_ALTITUDE)

def api_req(api_endpoint, access_token, req):
    try:
        p_req = pokemon_pb2.RequestEnvelop()
        p_req.unknown1 = 2
        p_req.rpc_id = 9092199861574434830

        p_req.requests.MergeFrom(req)

        p_req.latitude, p_req.longitude, p_req.altitude = get_location_coords()

        p_req.unknown12 = 989
        p_req.auth.provider = 'ptc'
        p_req.auth.token.contents = access_token
        p_req.auth.token.unknown13 = 59
        protobuf = p_req.SerializeToString()

        r = SESSION.post(api_endpoint, data=protobuf, verify=False)

        p_ret = pokemon_pb2.ResponseEnvelop()
        p_ret.ParseFromString(r.content)
        return p_ret
    except Exception,e:
        if DEBUG:
            print(e)
        return None

def api_req_gym(api_endpoint, access_token, req):
    try:
        p_req = gyms_pb2.RequestEnvelopGym()
        p_req.unknown1 = 2
        p_req.rpc_id = 9092199861574434830

        p_req.requests.MergeFrom(req)

        p_req.latitude, p_req.longitude, p_req.altitude = get_location_coords()

        p_req.unknown12 = 989
        p_req.auth.provider = 'ptc'
        p_req.auth.token.contents = access_token
        p_req.auth.token.unknown13 = 59
        protobuf = p_req.SerializeToString()

        r = SESSION.post(api_endpoint, data=protobuf, verify=False)

        p_ret = gyms_pb2.ResponseEnvelopGym()
        p_ret.ParseFromString(r.content)
        return p_ret
    except Exception,e:
        if DEBUG:
            print(e)
        return None


def get_api_endpoint(access_token):
    req = pokemon_pb2.RequestEnvelop()

    req1 = req.requests.add()
    req1.type = 134
    req2 = req.requests.add()
    req2.type = 126
    req3 = req.requests.add()
    req3.type = 4

    integerValue=req.four2int()
    integerValue.value=1468347297482
    req3.message=integerValue.SerializeToString()

    # req3.message.unknown4 = 1468546084127
    req4 = req.requests.add()
    req4.type = 129
    req5 = req.requests.add()
    req5.type = 5
    stringValue=req.four2string()
    stringValue.value="4a2e9bc330dae60e7b74fc85b98868ab4700802e"
    req5.message=stringValue.SerializeToString()
    # req5.message.unknown4 = "4a2e9bc330dae60e7b74fc85b98868ab4700802e"

    print req.requests[2]
    p_ret = api_req(API_URL, access_token, req.requests)

    try:
        return ('https://%s/rpc' % p_ret.api_url)
    except:
        return None


def get_gym(api_endpoint, access_token):
    req = pokemon_pb2.RequestEnvelop()

    req1 = req.requests.add()
    req1.type = 134
    stringValue=req.four2string()
    stringValue.value="4a9a35bee0e54cbebc13d3325286848e.16"
    stringValue.PlayerLatDegrees=0x404409e2ef4e0115
    stringValue.PlayerLngDegrees=0xc052c577681669cf
    stringValue.GymLatDegrees=0x404409e2ef4e0115
    stringValue.GymLngDegrees=0xc052c577681669cf


    req1.message=stringValue.SerializeToString()
    # req1.message.unknown4 = "4a9a35bee0e54cbebc13d3325286848e.16"

    return api_req(api_endpoint, access_token, req.requests)

def get_gyms(api_endpoint, access_token):
    req = gyms_pb2.RequestEnvelopGym()

    req1 = req.requests.add()
    req1.type = 106
    stringValue=req.four2string()
    stringValue.cells.append(9927817343864406016)
    stringValue.cells.append(9927817350306856960)
    stringValue.cells.append(9927817361044275200)
    stringValue.cells.append(9927817367486726144)
    stringValue.cells.append(9927817352454340608)
    stringValue.lat=0x4044087720000000
    stringValue.lon=0xc052c51060000000

    req1.message=stringValue.SerializeToString()
    # req1.message.unknown4 = "4a9a35bee0e54cbebc13d3325286848e.16"

    return api_req_gym(api_endpoint, access_token, req.requests)

def login_ptc(username, password):
    print('[!] login for: {}'.format(username))
    head = {'User-Agent': 'niantic'}
    r = SESSION.get(LOGIN_URL, headers=head)
    jdata = json.loads(r.content)
    data = {
        'lt': jdata['lt'],
        'execution': jdata['execution'],
        '_eventId': 'submit',
        'username': username,
        'password': password,
    }
    r1 = SESSION.post(LOGIN_URL, data=data, headers=head)

    ticket = None
    try:
        ticket = re.sub('.*ticket=', '', r1.history[0].headers['Location'])
    except Exception,e:
        if DEBUG:
            print(r1.json()['errors'][0])
        return None

    data1 = {
        'client_id': 'mobile-app_pokemon-go',
        'redirect_uri': 'https://www.nianticlabs.com/pokemongo/error',
        'client_secret': 'w8ScCUXJQc6kXKw8FiOhd8Fixzht18Dq3PEVkUCP5ZPxtgyWsbTvWHFLm2wNY0JR',
        'grant_type': 'refresh_token',
        'code': ticket,
    }
    r2 = SESSION.post(LOGIN_OAUTH, data=data1)
    access_token = re.sub('&expires.*', '', r2.content)
    access_token = re.sub('.*access_token=', '', access_token)

    return access_token


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", help="PTC Username", required=True)
    parser.add_argument("-p", "--password", help="PTC Password", required=True)
    parser.add_argument("-l", "--location", help="Location", required=True)
    parser.add_argument("-d", "--debug", help="Debug Mode", action='store_true')
    parser.set_defaults(DEBUG=True)
    args = parser.parse_args()

    if args.debug:
        global DEBUG
        DEBUG = True
        print('[!] DEBUG mode on')

    set_location(args.location)

    access_token = login_ptc(args.username, args.password)
    if access_token is None:
        print('[-] Wrong username/password')
        return
    print('[+] RPC Session Token: {} ...'.format(access_token[:25]))

    api_endpoint = get_api_endpoint(access_token)
    if api_endpoint is None:
        print('[-] RPC server offline')
        return
    print('[+] Received API endpoint: {}'.format(api_endpoint))

    # profile = get_profile(api_endpoint, access_token)
    # if profile is not None:
    #     print('[+] Login successful')

    #     print profile.payload[0]

    #     profile = profile.payload[0].profile
    #     print('[+] Username: {}'.format(profile.username))

    #     creation_time = datetime.fromtimestamp(int(profile.creation_time)/1000)
    #     print('[+] You are playing Pokemon Go since: {}'.format(
    #         creation_time.strftime('%Y-%m-%d %H:%M:%S'),
    #     ))

    #     for curr in profile.currency:
    #         print('[+] {}: {}'.format(curr.type, curr.amount))
    # else:
    #     print('[-] Ooops...')

    gyms = get_gyms(api_endpoint, access_token)
    if gyms is not None:
        print('[+] Login successful')

        print gyms
    else:
        print('[-] Ooops...')


    gym = get_gym(api_endpoint, access_token)
    if gym is not None:
        print('[+] Login successful')

        print gym.payload[0]
    else:
        print('[-] Ooops...')


if __name__ == '__main__':
    main()
