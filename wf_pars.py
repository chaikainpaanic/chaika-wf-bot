import requests
import json

def user_stats(name):
    s = requests.Session()
    message_str = ""
    stats = {}

    for i in range(1,4):
        r = s.get("http://api.warface.ru/user/stat/", params={'name' : name, 'server' : i})
        r_j = json.loads(r.text)

        try:
            stats["clan_name"] = r_j["clan_name"]
        except:
            stats["clan_name"] = "Нет"

        try:
            if(r_j["message"] == "Пользователь не найден"):
                message_str = "Пользователь не найден"
            elif(r_j["message"] == "Персонаж неактивен"):
                message_str = "Персонаж неактивен"
                break
            elif(r_j["message"] == "Игрок скрыл свою статистику"):
                message_str = "Игрок скрыл свою статистику"
                break
            else:
                message_str = ""
                break
        except:
            stats["nickname"] = r_j["nickname"]

            stats["server"] = i
            stats["rank_id"] = r_j["rank_id"]

            stats["playtime_h"] = r_j["playtime_h"]
            stats["playtime_m"] = r_j["playtime_m"]

            stats["kills"] = r_j["kills"]
            stats["death"] = r_j["death"]
            stats["friendly_kills"] = r_j["friendly_kills"]
            stats["pvp"] = r_j["pvp"]
            stats["pvp_wins"] = r_j["pvp_wins"]
            stats["pvp_lost"] = r_j["pvp_lost"]
            stats["pvp_all"] = r_j["pvp_all"]

            stats["pve_all"] = r_j["pve_all"]
            stats["pve_friendly_kills"] = r_j["pve_friendly_kills"]
            stats["pve_kills"] = r_j["pve_kills"]
            stats["pve_death"] = r_j["pve_death"]
            stats["pve"] = r_j["pve"]
            stats["pve_wins"] = r_j["pve_wins"]
            stats["pve_lost"] = r_j["pve_lost"]

            stats["favoritPVP"] = r_j["favoritPVP"]
            stats["favoritPVE"] = r_j["favoritPVE"]

            
            message_str = ""
            break
        

    if message_str == "":
        return stats
    else:
        return message_str

