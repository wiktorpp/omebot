def tags_str_to_dict(input):
    input = input.split()
    output = {"I_am": set(), "looking_for": set(), "block": set()}
    for tag in input:
        if tag.startswith(">"):
            output["I_am"].add(tag[1:])
        elif tag.startswith("<"):
            output["looking_for"].add(tag[1:])
        elif tag.startswith("-"):
            output["block"].add(tag[1:])
        else:
            raise ValueError
    return output

def tags_dict_to_str(input):
    output=""
    for tag in input["I_am"]:
        output += f">{tag} "
    for tag in input["looking_for"]:
        output += f"<{tag} "
    for tag in input["block"]:
        output += f"-{tag} "
    return output

def count_points(my_tags, his_tags):
    my_tags = tags_str_to_dict(my_tags)
    his_tags = tags_str_to_dict(his_tags)

    if my_tags["I_am"] & his_tags["block"]:
        return None
    if his_tags["I_am"] & my_tags["block"]:
        return None
    
    my_score = len(my_tags["looking_for"] & his_tags["I_am"])
    his_score = len(my_tags["I_am"] & his_tags["looking_for"])

    return (my_score, his_score)

import pdb; pdb.set_trace()