from csr import CSR, CSREntry
from api_calls import get_csr, get_match_list_json

class HaloInfinite:
    def __init__(self, name, gamertag, token, season, api_version):
        self.name = name
        self.gamertag = gamertag
        self.token = token
        self.season = season
        self.version = api_version
        self.attr = {}
        if not self.update_csr():
            return


    def update_csr(self):
        try:
            response = get_csr(self.gamertag, self.token, self.season, self.version)
            csr = CSR(response)
            self.attr['crossplay'] = csr.playlists['crossplay']
            self.attr['controller'] = csr.playlists['controller']
            self.attr['mnk'] = csr.playlists['mnk']
            return True
        finally:
            return


