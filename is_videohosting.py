import re


def is_video_hosting(url):
    return is_youtube_url(url) or is_vimeo_url(url) or is_rutube_url(url) or is_vk_url(url)


def is_youtube_url(url):
    pattern = r'(https?://)?(www\.)?youtube\.com(\w+)?'
    match = re.search(pattern, url)
    return match is not None


def is_vimeo_url(url):
    pattern = r'(https?://)?(www\.)?vimeo\.com(\w+)?'
    match = re.search(pattern, url)
    return match is not None


def is_rutube_url(url):
    pattern = r'(https?://)?(www\.)?rutube\.ru(\w+)?'
    match = re.search(pattern, url)
    return match is not None


def is_vk_url(url):
    pattern = r'(https?://)?(www\.)?vk\.com/video(\w+)?'
    match = re.search(pattern, url)
    return match is not None


print(is_video_hosting("https://rutube.ru/video/3b8f5254b444bbadca71712d29a95d4a/"))
