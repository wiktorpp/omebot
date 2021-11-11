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

def tags_dict_to_str(input):
    output=""
    for tag in input["I_am"]:
        output += f">{tag} "
    for tag in input["looking_for"]:
        output += f"<{tag} "
    for tag in input["block"]:
        output += f"-{tag} "
    return output

import pdb; pdb.set_trace()