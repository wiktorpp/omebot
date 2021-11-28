priority_weight = {"low": 1, "med":2, "high":3}
tag_shorthand_to_name={">": "I_am", "<": "looking_for", "-": "block"}
class Block: pass

users=[
    {"tags_with_priority": {"low":"<f >e", "med":"", "high":""}},
    {"tags_with_priority": {"low":"<f", "med":"", "high":""}},
]

def tags_str_to_dict(input, default_prefix=None):
    input = input.split()
    output = {"I_am": set(), "looking_for": set(), "block": set()}
    for tag in input:
        try:
            output[tag_shorthand_to_name[tag[0]]].add(tag[1:])
        except KeyError:
            if default_prefix == None:
                raise ValueError
            else:
                for type_name in default_prefix:
                    output[type_name].add(tag)
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
    return (my_final_result, his_final_result)

def remove_tags(tags, tags_to_remove):
    print(("remove_tags", tags, tags_to_remove))
    tags_dict = tags_str_to_dict(tags)
    tags_to_remove_dict = tags_str_to_dict(tags_to_remove, default_prefix=["I_am", "looking_for", "block"])
    for tag_type in ["I_am", "looking_for", "block"]:
        tags_dict[tag_type] = tags_dict[tag_type] - tags_to_remove_dict[tag_type]
    tags = tags_dict_to_str(tags_dict)
    return tags

def remove_tags_with_priority(tags_with_priority, tags, priority="all"):
    if priority != "all":
        tags_with_priority[priority] = remove_tags(tags_with_priority[priority], tags)
    else:
        for priority in ["low", "med", "high"]:
            tags_with_priority[priority] = remove_tags(tags_with_priority[priority], tags)
    return tags_with_priority

def add_tags(tags, tags_to_add):
    tags_dict = tags_str_to_dict(tags)
    tags_to_add_dict = tags_str_to_dict(tags_to_add, default_prefix=["I_am", "looking_for"])
    for tag_type in ["I_am", "looking_for", "block"]:
        tags_dict[tag_type].update(tags_to_add_dict[tag_type])
    tags = tags_dict_to_str(tags_dict)
    return tags

def add_tag_with_priority(tags_with_priority, tags, priority):
    tags_with_priority = remove_tags_with_priority(tags_with_priority, tags)
    tags_with_priority[priority] = add_tags(tags_with_priority[priority], tags)
    return tags_with_priority

def search(me):
    tags_with_priority = me["tags_with_priority"]
    for user in users:
        print(count_points_with_priority(tags_with_priority, user["tags_with_priority"]))

def parse_command(command):
    pass

remove_tags(">f <f", "f")
add_tags(">f","<f")
#add_tag_with_priority({"low":">f"}, "<f", "low")
#remove_tags_with_priority({"low":">f"}, ">f", "low")
#remove_tags_with_priority({"low":">f <e", "med":"", "high":""}, ">f")
me = {"tags_with_priority": {"low":">f <e", "med":"", "high":""}}
import pdb; pdb.set_trace()