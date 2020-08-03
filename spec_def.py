import requests
import json

def spec_one(name, server, stat):
    s = requests.Session()
    r = s.get("http://api.warface.ru/user/stat/", params={'name' : name, 'server' : server})
    r_j = json.loads(r.text)

    str_to_search = r_j["full_response"]

    array_to_search = str_to_search.split('\n')
    i_to_return = 0
    for i in array_to_search:
        try:
            if i.index(stat) >= 0:
                i_to_return = i[i.index("=")+2:]
                break
        except:
            pass
    
    return int(i_to_return)