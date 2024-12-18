def sum_middle_of_valid_updates(rules, updates):
    result = 0
    rules_dict = create_rules_dict(rules)
    updates = parse_updates(updates)
    for update in updates:
        if is_update_valid(rules_dict, update):
            result += update[int((len(update) - 1) / 2)]
    return result

def is_update_valid(rules_dict, update):
    if get_invalid_page(rules_dict, update) == None:
        return True
    else:
        return False

def get_invalid_page(rules_dict, update):
    for page_index in range(len(update)):
        page = update[page_index]
        
        if page in rules_dict:
            (before_page_rules, after_page_rules) = rules_dict[page]
            pages_before = update[0:page_index]
            pages_after = update[page_index + 1:]

            for before_page_rule in before_page_rules:
                if before_page_rule in pages_before:
                    return (page, "should be before", before_page_rule)
            
            for after_page_rule in after_page_rules:
                if after_page_rule in pages_after:
                    return (page, "should be after", after_page_rule)
    
    return None

def create_rules_dict(rules):
    rules_dict = {}
    for rule in rules:
        x = int(rule[0:rule.index("|")])
        y = int(rule[rule.index("|")+1:])
        if x not in rules_dict:
            rules_dict[x] = ([y],[])
        else:
            rules_dict[x][0].append(y)
        if y not in rules_dict:
            rules_dict[y] = ([],[x])
        else:
            rules_dict[y][1].append(x)
    
    return rules_dict

def parse_updates(updates):
    parsed_updates = []
    for update in updates:
        parsed_update = []
        while "," in update:
            page = int(update[0:update.index(",")])
            parsed_update.append(page)

            update = update[update.index(",") + 1:]
        parsed_update.append(int(update))
        parsed_updates.append(parsed_update)
    return parsed_updates

def sum_middle_of_corrected_invalid_updates(rules, updates):
    rules_dict = create_rules_dict(rules)
    updates = parse_updates(updates)
    
    invalid_updates = []
    for update in updates:
        if not is_update_valid(rules_dict, update):
            invalid_updates.append(update)

    result = 0
    for update in invalid_updates:
        corrected_update = correct_invalid_update(rules_dict, update)
        result += int(corrected_update[int((len(corrected_update) - 1) / 2)])

    return result

def correct_invalid_update(rules_dict, update):
    while not is_update_valid(rules_dict, update):
        (page, before_or_after, rule_page) = get_invalid_page(rules_dict, update)
        original_page_index = update.index(page)
        if before_or_after == "should be before":
            update.insert(update.index(rule_page), page)
            update = update[0:original_page_index+1] + update[original_page_index+2:]
        elif before_or_after == "should be after":
            update.insert(update.index(rule_page)+1, page)
            update = update[0:original_page_index] + update[original_page_index+1:]
    return update       

f = open("inputs/day05.txt", "r")
rule_lines = True
rules = []
updates = []
for line in f:
    if rule_lines:
        if line != "\n":
            rules.append(line)
        else:
            rule_lines = False
    else:
        updates.append(line)

print("Sum of the middle page in valid updates: " + str(sum_middle_of_valid_updates(rules, updates)))
print("Sum of the middle page in corrected invalid updates: " + str(sum_middle_of_corrected_invalid_updates(rules, updates)))
