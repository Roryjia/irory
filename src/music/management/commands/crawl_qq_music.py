# -*-coding:utf-8 -*-
# 
# Created on 2016-05-09
#      __      __
#  -  /__) _  /__) __/
#  / / (  (/ / (    /
#                  /

import re
import base64
import urllib
import os

from django.core.management.base import BaseCommand, CommandError
import requests

from music.models import Music

QQ_MUSIC_TOP100 = 'http://i.y.qq.com/v8/fcg-bin/fcg_v8_toplist_cp.fcg?' \
                  'tpl=mac&type=top&topid=26&format=json&platform=mac'
QQ_MUSIC_MP3_KEY = 'http://base.music.qq.com/fcgi-bin/fcg_musicexpress.fcg?' \
                   'json=3&guid=5695140076&g_tk=938407465&loginUin=0&hostUin=0&format=' \
                   'jsonp&inCharset=GB2312&outCharset=GB2312&notice=0&platform=yqq&' \
                   'jsonpCallback=jsonCallback&needNewCode='
headers = {
    'Host': 'i.y.qq.com',
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.86 Safari/537.36',
    'Referer': 'http://y.qq.com/',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Cookie': 'ptcz=7ebe7f97f6759653bc1fdd647c1d2b05dc3be669c0a6412f26002640b692d29e; pt2gguin=o1289521190; pgv_pvi=9952033792; qqmusic_uin=12345678; qqmusic_key=12345678; qqmusic_fromtag=30; ts_refer=music.qq.com/; ip_limit=1; ts_last=y.qq.com/; ts_uid=1835267822; pgv_info=ssid=s8743642499; ts_last=i.y.qq.com/v8/fcg-bin/fcg_play_single_song.fcg; pgv_pvid=5695140076; o_cookie=1289521190; ts_uid=1835267822',
}
QQ_MUSIC_LYRIC = 'http://i.y.qq.com/lyric/fcgi-bin/fcg_query_lyric.fcg?' \
                 'pcachetime=1461832194684&songmid={}' \
                 '&g_tk=938407465&loginUin=0&hostUin=0&format=json&inCharset=GB2312' \
                 '&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0'
QQ_MUSIC_MP3_FILE = 'http://cc.stream.qqmusic.qq.com/C200{}.m4a?vkey={}&guid=5695140076&fromtag=30'
QQ_MUSIC_ALBUM = 'http://i.gtimg.cn/music/photo/mid_album_300/{}/{}/{}.jpg'

_base_mp3 = 'media/music/mp3'
_base_image = 'media/music/image'


class Command(BaseCommand):

    help = 'A qq music crawler'
    can_import_settings = True

    def handle(self, *args, **options):
        try:
            vkey = re.findall('"key": "(\w+)"', requests.get(QQ_MUSIC_MP3_KEY).content)[0]

            music_top100_list = requests.get(QQ_MUSIC_TOP100).json()
            data = []
            for m in music_top100_list['songlist']:
                album_id = m['data']['albummid']
                song_id = m['data']['songmid']
                song_name = m['data']['songname']
                song_lyric = base64.b64decode(
                    re.findall('"lyric":"(.*)"',
                               requests.get(QQ_MUSIC_LYRIC.format(song_id), headers=headers).content)[0])
                data.append({
                    'song_id': song_id,
                    'song_name': song_name,
                    'song_mp3_url': QQ_MUSIC_MP3_FILE.format(song_id, vkey),
                    'song_mp3': u'/{}/{}.mp3'.format(_base_mp3, song_name),
                    'song_lyric': song_lyric,
                    'album_name': m['data']['albumname'],
                    'album_image_url': QQ_MUSIC_ALBUM.format(album_id[-2], album_id[-1], album_id),
                    'album_image': u'/{}/{}.jpg'.format(_base_image, song_name),
                    'singer': '/'.join([s['name'] for s in m['data']['singer']]),
                })

            from django.conf import settings

            if not os.path.exists(os.path.join(settings.BASE_DIR, _base_mp3)):
                os.mkdir(os.path.join(settings.BASE_DIR, _base_mp3))
            if not os.path.exists(os.path.join(settings.BASE_DIR, _base_image)):
                os.mkdir(os.path.join(settings.BASE_DIR, _base_image))
            for m in data:
                try:
                    Music.objects.get(song_id=m['song_id'])
                except Music.DoesNotExist:
                    print u'`{}` start download ....'.format(m['song_name'])
                    try:
                        urllib.urlretrieve(m.pop('song_mp3_url'),
                                           os.path.join(settings.BASE_DIR, _base_mp3, '{}.mp3'.format(m['song_name'])))
                        urllib.urlretrieve(m.pop('album_image_url'),
                                           os.path.join(settings.BASE_DIR, _base_image, '{}.jpg'.format(m['song_name'])))
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(u'download `{}`Have an error: `{}`'.format(m['song_name'], e)))
                        continue

                    music = Music(**m)
                    music.save()
                else:
                    continue
        except Exception as e:
            self.stdout.write(self.style.ERROR('Have an error: `{}`'.format(e)))
        else:
            self.stdout.write('Successfully crawl qq music.')
