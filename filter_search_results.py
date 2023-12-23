from is_videohosting import is_video_hosting


def filter_results(input_list):
    new_list = [x for x in input_list if not is_video_hosting(x)]
    return new_list
