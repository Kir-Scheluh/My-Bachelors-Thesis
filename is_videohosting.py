import re
from urllib.parse import urlparse

def get_domain_from_url(url):
    parsed_url = urlparse(url)
    if parsed_url.scheme and parsed_url.netloc:
        return parsed_url.scheme + "://" + parsed_url.netloc
    else:
        return None


def is_video_hosting(url):
    return is_youtube_url(url) or is_vimeo_url(url) or is_rutube_url(url) or is_vk_url(url)


def is_youtube_url(url):
    pattern = r'(https?://)?(www\.)?youtube\.com(\w+)?'
    url = get_domain_from_url(url)
    match = re.search(pattern, url)
    return match is not None


def is_vimeo_url(url):
    pattern = r'(https?://)?(www\.)?vimeo\.com(\w+)?'
    url = get_domain_from_url(url)
    match = re.search(pattern, url)
    return match is not None


def is_rutube_url(url):
    pattern = r'(https?://)?(www\.)?rutube\.ru(\w+)?'
    url = get_domain_from_url(url)
    match = re.search(pattern, url)
    return match is not None


def is_vk_url(url):
    pattern = r'(https?://)?(www\.)?vk\.com/video(\w+)?'
    url = get_domain_from_url(url)
    match = re.search(pattern, url)
    return match is not None

