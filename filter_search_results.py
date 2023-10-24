from is_videohosting import is_video_hosting


def filter_results(input_dict):
    new_dict = {'hosts': [], 'titles': [], 'links': []}
    for i in range(len(input_dict['hosts'])):
        if not is_video_hosting(input_dict['hosts'][i]):
            new_dict['hosts'].append(input_dict['hosts'][i])
            new_dict['titles'].append(input_dict['titles'][i])
            new_dict['links'].append(input_dict['links'][i])
    return new_dict
