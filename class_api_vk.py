import requests
import vk_api
import tqdm
import time
import os
token = 'vk1.a.gHadVng3UMHB8zjFfL2Trpb8dwycGarTLO6QmAQE1rPe6XOMrWqiV6EDcqMhZa4JZtETkRvUVNdLGL9kfWmcccZTDprCtZbVLRmseKbjKUF3_3vUrRvDkFqKct9fOgfMarhO3NciZELAcM9vGXC-pWepzzW9wE9ejTu6sRbFO6bH1lBKtYXlkqdQ5RhpsGWS'
user_id = '807916537'
class VKAPIClient:
    API_BASE_URL = 'https://api.vk.com/method'
    def __init__(self, token, user_id):
        self.token = token
        self.user_id = user_id

    def get_common_params(self):
        return {
            'access_token': self.token,
            'v': '5.199'
        }

    def get_status(self):
      params = self.get_common_params()
      params.update({'user_id': self.user_id})
      response = requests.get(
          f'{self.API_BASE_URL}/status.get', params=params)
      return response.json()

if __name__ == '__main__':

    vk_client = VKAPIClient(token, user_id)
    print(vk_client.get_status())