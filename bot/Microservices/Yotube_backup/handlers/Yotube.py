import json

import requests

# youtube.com/account_advanced узнать id канала
from bot.General.setting_bot.config import API, id_channels

maxResults = '5'


def subscriptions(id_channels, nextPageToken=''):
    """Список подписок канала"""
    list_channel = []
    while True:
        url = f'https://youtube.googleapis.com/youtube/v3/subscriptions?part=snippet,contentDetails&maxResults={maxResults}' \
              f'&pageToken={nextPageToken}&channelId={id_channels}&key={API}'
        response = requests.get(url)
        # print(url)
        if response.status_code == 200:
            date = json.loads(response.text)
            # print(response.text)
            totalResults = date.get('pageInfo', None).get('totalResults', "0")
            nextPageToken = date.get('nextPageToken', None)

            for items in date['items']:
                title = items['snippet']['title']
                channelId = items['snippet']['resourceId']['channelId']
                name_id = {'title': title, 'channelId': channelId}
                print(name_id)
                list_channel.append(name_id)

            if nextPageToken is None:
                print("Выход")

                bonus = {'Канал автора': 'https://www.youtube.com/channel/UCEjAPx6xgJl85HDCtOoGmUw'}
                list_channel.append(bonus)

                list_user = {
                    'Yt_id': id_channels,
                    'channel_count': totalResults,
                    'channel': list_channel
                }
                # print(list_user)

                # with open(f'{id_channels}.json', 'w') as f:
                #     json.dump(list_user, f, ensure_ascii=False)
                return list_user

            # print("Следующая страница:\n")
        else:
            date = json.loads(response.text)
            a = date['error']['message']
            msg = f'Error: {response.status_code}\nОткройте свои подписки и повторите:\n' \
                  f'https://www.youtube.com/account_privacy\n message: {a}'
            print(msg)
            return msg





if __name__ == '__main__':
    subscriptions(id_channels)
