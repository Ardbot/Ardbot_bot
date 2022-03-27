import json

import requests

# youtube.com/account_advanced узнать id канала
from bot.General.setting_bot.config import API, id_channels

maxResults = '50'


def list_subs_channel(id_channels, nextPageToken=''):
    """Список подписок канала"""
    list_channel = []
    while True:
        url = f'https://youtube.googleapis.com/youtube/v3/subscriptions?part=snippet,contentDetails&maxResults={maxResults}' \
              f'&pageToken={nextPageToken}&channelId={id_channels}&key={API}'
        # f'&pageToken={nextPageToken}&channelId={id_channels}&key={API}'
        response = requests.get(url)
        # print(response.text)
        # print(url)
        date = json.loads(response.text)
        if response.status_code == 200:
            # print(response.text)
            totalResults = date.get('pageInfo', None).get('totalResults', "0")
            nextPageToken = date.get('nextPageToken', None)
            # mes = date.get('error', '0')

            for items in date['items']:
                title = items['snippet']['title']
                channelId = items['snippet']['resourceId']['channelId']
                url_channel = 'https://www.youtube.com/channel/' + channelId
                name_id = {'title': title, 'channelId': channelId, 'url_youtube': url_channel}

                print(name_id)
                list_channel.append(name_id)

            if nextPageToken is None:
                print("Выход")

                bonus = {"title": "Ard_bot",
                         "channelId": "UCEjAPx6xgJl85HDCtOoGmUw",
                         'url_youtube': 'https://www.youtube.com/channel/UCEjAPx6xgJl85HDCtOoGmUw',
                         'telegram': 'https://t.me/ardbot_teh',
                         'zen': 'https://zen.yandex.ru/id/5ee7044064d6731cc9e1ddda'
                         }
                list_channel.insert(2, bonus)

                list_user = {
                    'status_code': response.status_code,
                    'Yt_id': id_channels,
                    'instruction': 'https://t.me/ardbot_teh/12',
                    'channel_count': totalResults,
                    'channel': list_channel
                }

                return list_user
        else:
            msg = {'status_code': response.status_code,
                   'error': f'Откройте свои подписки или проверьте адрес:\n,'
                            f'https://www.youtube.com/account_privacy\n'
                            f'https://www.youtube.com/channel/{id_channels}\n',
                   'message': date.get('error').get('message')
                   }
            return msg


def channels(id_channels2='UC__hk2pt088MDmH-f1dzMcw', API2='AIzaSyBvJBNM9_q_zQJTLgKlWLXTmlwMc3KKv8s'):
    url = f'https://youtube.googleapis.com/youtube/v3/channels?part=snippet%2CcontentDetails%2Cstatistics&id={id_channels2}&key={API2}'
    response = requests.get(url)
    print(url)
    print(response.text)


def tg_log(tg_id, id_channels, status_code=0):
    tg_log = {
        'tg_id': tg_id,
        'id_channels': id_channels,
        'status_code': status_code

    }
    with open(f'log.json', 'a') as f:
        json.dump(tg_log, f, ensure_ascii=False, indent=2)


# def ping_channel(id_channels):
#     url= f'https://youtube.googleapis.com/youtube/v3/channels?part=snippet&id={id_channels}&key={API}'
#     response = requests.get(url)
#     print(response.status_code)
#     print(response.text)

# https://www.googleapis.com/youtube/v3/videos?part=statistics&id=mxnTXNwZzlo&key=AIzaSyBvJBNM9_q_zQJTLgKlWLXTmlwMc3KKv8s


if __name__ == '__main__':
    list_subs_channel(id_channels)
    # ping_channel(id_channels)
    # channels()
