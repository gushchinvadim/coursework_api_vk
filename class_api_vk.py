import requests

token = ''
user_id = ''
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