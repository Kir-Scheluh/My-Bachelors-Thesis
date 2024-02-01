import re

def filter_results(input_list):
    new_list = [x for x in input_list if not is_video_hosting(x)]
    return new_list

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
