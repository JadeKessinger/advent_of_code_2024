def sum_middle_of_valid_updates(rules, updates):
    result = 0
    rules_dict = create_rules_dict(rules)
    updates = parse_updates(updates)
    for update in updates:
        if is_update_valid(rules_dict, update):
            result += int(update[int((len(update) - 1) / 2)])
    return result

def is_update_valid(rules_dict, update):
    for page_index in range(len(update)):
        page = update[page_index]
        
        if page in rules_dict:
            (page_before_rules, page_after_rules) = rules_dict[page]
            pages_before = update[0:page_index]
            pages_after = update[page_index + 1:]

            for page_before_rule in page_before_rules:
                if page_before_rule in pages_before:
                    return False
            
            for page_after_rule in page_after_rules:
                if page_after_rule in pages_after:
                    return False
    
    return True

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
        

f = open("day5.txt", "r")
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
