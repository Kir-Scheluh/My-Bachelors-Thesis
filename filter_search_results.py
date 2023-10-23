from is_videohosting import is_video_hosting

def filter_results(dict):
    new_dict = {'hosts': [], 'titles':[], 'links':[]}
    for i in range(len(dict['hosts'])):
        if not is_video_hosting(dict['hosts'][i]):
            new_dict['hosts'].append(dict['hosts'][i])
            new_dict['titles'].append(dict['titles'][i])
            new_dict['links'].append(dict['links'][i])
    return new_dict