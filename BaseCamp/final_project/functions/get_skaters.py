def get_skaters(events):
    skaters_dict = {}
    for event in events:
        for result in event["results"]:
            skater = result["skater"]
            skaters_dict[skater["id"]] = skater

    skaters_list = list(skaters_dict.values())
    return skaters_list
