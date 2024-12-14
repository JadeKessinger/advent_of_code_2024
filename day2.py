def count_safe_reports(reports):
    '''
    Counts the number of reports that are safe. A report is safe if it's levels are all gradually increasing or 
    gradually decreasing, and each level differs by no more than 3.
    
    Inputs:
    - reports: a list of reports, where each report is a list of levels represented as integers
    
    Outputs:
    - the number of safe reports
    '''
    safe_reports = 0
    for report in reports:
        safe = True
        increasing = False
        if report[1] - report[0] > 0:
            increasing = True
        prev = report[0]
        
        for level in report[1:]:
            if increasing:
                if level - prev <= 0:
                    safe = False
            else:
                if level - prev >= 0:
                    safe = False 
            
            if abs(level - prev) > 3:
                safe = False
            
            if not safe:
                break

            prev = level
        
        if safe:
            safe_reports += 1
    
    return safe_reports

reports = []
f = open("day2.txt", "r")
for line in f:
    report = line.split()
    report = [int(level) for level in report]
    reports.append(report)

print("Safe reports: " + str(count_safe_reports(reports)))