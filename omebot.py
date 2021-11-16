priority_weight = {"low": 1, "med":2, "high":3}
tag_types={">": "I_am", "<": "looking_for", "-": "block"}
class Block: pass

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
        raise Block
    if his_tags["I_am"] & my_tags["block"]:
        raise Block
    
    my_score = len(my_tags["looking_for"] & his_tags["I_am"])
    his_score = len(my_tags["I_am"] & his_tags["looking_for"])

    return (my_score, his_score)

def count_points_with_priority(my_tags, his_tags):
    my_final_result = 0
    his_final_result = 0
    for my_priority in ["low", "med", "high"]:
        for his_priority in ["low", "med", "high"]:
            my_result, his_result = count_points(my_tags[my_priority], his_tags[his_priority])
            my_result = my_result * priority_weight[my_priority]
            his_result = his_result * priority_weight[his_priority]
            my_final_result += my_result
            his_final_result += his_result
            print(f"{my_result} {his_result}")
    return (my_final_result, his_final_result)
        
empty_user={"low": "", "med": "", "high": ">f <h"}

def remove_tags(tags, tags_to_remove):
    tags_to_remove_dict = tags_str_to_dict(tags_to_remove)
    for tag_type in ["I_am", "looking_for", "block"]:
        tags_to_remove_dict[tag_type] = tags_dict[tag_type] - tags[tag_type]
    user[priority] = tags_dict_to_str(tags_dict)

def remove_tag_with_priority(user, tags):
    tags = tags_str_to_dict(tags)
    for priority in ["low", "med", "high"]:
        user[priority] = remove_tags(user[priority], tags)
    return user

def add_tag_with_priority(user, tags, priority):
    user = remove_tag(user, tags)
    tags = tags_str_to_dict(tags)
    print(tags)
    print(user[priority])
    user_dict = tags_str_to_dict(user[priority])
    print(user_dict)
    for tag_type in ["I_am", "looking_for", "block"]:
        user_dict[tag_type] = set.union(user_dict[tag_type], tags[tag_type])
    user[priority] = tags_dict_to_str(user[priority])
    return user

import pdb; pdb.set_trace()