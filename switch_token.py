import requests
import vk_api
import tqdm
class VK:
    def __init__(self, access_token, user_id, version='5.131'):
        self.token = access_token
        self.id = user_id
        self.version = version
        self.params = {'access_token': self.token, 'v':
        self.version}
    def users_info(self):
        url = 'https://api.vk.com/method/users.get'
        params = {'user_ids': self.id}
        response = requests.get(url, params={**self.params,
        **params})
        return response.json()
access_token = 'vk1.a.gHadVng3UMHB8zjFfL2Trpb8dwycGarTLO6QmAQE1rPe6XOMrWqiV6EDcqMhZa4JZtETkRvUVNdLGL9kfWmcccZTDprCtZbVLRmseKbjKUF3_3vUrRvDkFqKct9fOgfMarhO3NciZELAcM9vGXC-pWepzzW9wE9ejTu6sRbFO6bH1lBKtYXlkqdQ5RhpsGWS' # токен полученный из инструкции
user_id = '807916537' # идентификатор пользователя vk
vk = VK(access_token, user_id)
print(vk.users_info())