def tags_str_to_dict(input):
    input = input.split()
    output = {"I_am": set(), "looking_for": set(), "block": set()}
    for tag in input:
        if tag.startswith(">"):
            output["I_am"].add(tag[1:])
        if tag.startswith("<"):
            output["looking_for"].add(tag[1:])
        if tag.startswith("-"):
            output["block"].add(tag[1:])
    return output
            

import pdb; pdb.set_trace()