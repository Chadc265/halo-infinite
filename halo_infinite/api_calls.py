import requests

__all__ = [
    "get_single_match_json",
    "get_match_list_json",
    "get_csr"
]



def get_csr(gamer_tag:str, token:str, season:int, API_VERSION:str = "0.3.8"):
    url = f'https://halo.api.stdlib.com/infinite@{API_VERSION}/stats/csrs/?gamertag={gamer_tag}&season={season}'
    headers = {f'Authorization': 'Bearer ' + token}
    r = requests.get(url, headers)
    return r.json()


def get_single_match_json(match_id:str, token:str, API_VERSION:str = "0.3.8"):
    url = f'https://halo.api.stdlib.com/infinite@{API_VERSION}/stats/matches/retrieve/?id={match_id}'
    headers = {f'Authorization': 'Bearer ' + token}
    r = requests.get(url, headers=headers)
    return r.json()

def get_match_list_json(gamer_tag:str, token:str, API_VERSION:str = "0.3.8", count:int=25, offset:int=1):
    url = f'https://halo.api.stdlib.com/infinite@{API_VERSION}/stats/matches/list/?gamertag={gamer_tag}&limit.count={count}&limit.offset={offset}&mode=matchmade'
    headers = {f'Authorization': 'Bearer ' + token}
    r = requests.get(url, headers=headers)
    return r.json()