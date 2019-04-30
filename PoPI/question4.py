def shortest_continuous_segment(s):
    '''implement the function'''
    segments = {}
    prev_number = None
    seq = 0
    for i in s:
        if prev_number == None:
            seq += 1
            prev_number = i
        elif i == prev_number:
            seq += 1
            prev_number = i
        else:
            if prev_number not in segments.keys():
                segments[prev_number] = seq
            else:
                segments[prev_number] = min(segments[prev_number], seq)
            seq = 1
            prev_number = i
    if prev_number not in segments.keys():
        segments[prev_number] = seq
    else:
        segments[prev_number] = min(segments[prev_number], seq)

    min_dict = {}
    for key, val in segments.items():
        if val == min(segments.values()):
            min_dict[key] = val

    return (max(min_dict.keys()), min(segments.values()))
