# coding: utf-8
from __future__ import unicode_literals

import re

from .common import InfoExtractor


class NaughtyMachinimaIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?naughtymachinima\.com/video/(?P<id>[0-9]+)/.*?'
    _TESTS = [
        {
            'url': 'https://www.naughtymachinima.com/video/43551/family-rules-ep-11-part-1',
            'md5': '115cc3094704076eb7943a6a37bf603f',
            'info_dict': {
                'id': '43551',
                'ext': 'mp4',
                'title': 'Family Rules, ep.11 (part 1)',
                'uploader': 'BlackSheepOvca',
                'thumbnail': 'https://www.naughtymachinima.com/media/videos/tmb1/43551/default.jpg',
            }
        },
        {
            'url': 'https://www.naughtymachinima.com/video/10819/lollipop-effect-2',
            'md5': 'aaf5c5412431c65c85b6d141e14804d1',
            'info_dict': {
                'id': '10819',
                'ext': 'mp4',
                'title': 'Lollipop Effect 2',
                'uploader': 'Rikolo',
                'thumbnail': 'https://www.naughtymachinima.com/media/videos/tmb/10819/default.jpg',
            }
        },
        {
            'url': 'https://www.naughtymachinima.com/video/51399/alli-x-jenny-futa',
            'md5': 'c8d8794b69c590608b5e8b0e1d6ebbde',
            'info_dict': {
                'id': '51399',
                'ext': 'mp4',
                'title': 'Alli x Jenny Futa',
                'uploader': 'Sophitia95',
                'thumbnail': 'https://www.naughtymachinima.com/media/videos/tmb1/51399/default.jpg',
            }
        }
    ]

    def _real_extract(self, url):
        video_id = self._match_id(url)
        webpage = self._download_webpage(url, video_id)

        title = self._og_search_title(webpage)

        video_sources = re.findall(
            r'<source[^>]+src=["\'](.+?)["\'][^>]+label=["\'](.+?)["\'][^>]+(?:res=|res =)["\'](.+?)["\']', webpage
        )

        formats = []

        for source in video_sources:
            formats.append(
                {
                    'url': source[0],
                    'format': 'Website classifies format as %s' % source[1],
                    'height': int(source[2])
                }
            )

        uploader = self._html_search_regex(r'<div class="pull-left user-container">.*?<span>(.*?)</span>', webpage, 'uploader')

        thumbnail = self._og_search_thumbnail(webpage)

        return {
            'id': video_id,
            'title': title,
            'formats': formats,
            'thumbnail': thumbnail,
            'uploader': uploader,
            # TODO more properties (see youtube_dl/extractor/common.py)
        }