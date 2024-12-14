def count_safe_reports(reports, dampner=False):
    '''
    Counts the number of reports that are safe. A report is safe if it's levels are all gradually increasing or 
    gradually decreasing, and each level differs by no more than 3. If the dampner is on, a report is considered safe if
    removing one level would make it a safe report.
    
    Inputs:
    - reports: a list of reports, where each report is a list of levels represented as integers
    - dampner: a boolean for whether the dampner is on or off
    
    Outputs:
    - the number of safe reports
    '''
    safe_reports = 0
    for report in reports:
        if dampner: # Try removing every element for a brute force solution
            for level_index in range(len(report)):
                if is_report_safe(report[0:level_index] + report[level_index + 1:]):
                    safe_reports += 1
                    break
        else:
            if is_report_safe(report):
                safe_reports += 1

    return safe_reports

def is_report_safe(report):
    '''
    Checks if one report is safe. A report is safe if it's levels are all gradually increasing or gradually decreasing, 
    and each level differs by no more than 3. 
    
    Inputs:
    - report: one report represented as a list of levels represented as integers
    
    Outputs:
    - whether or not a report is safe
    '''
    safe = True
    increasing = False
    if report[1] - report[0] > 0:
        increasing = True
    prev = report[0]
    
    for level in report[1:]:
        if increasing:
            if level - prev <= 0:
                return False
        else:
            if level - prev >= 0:
                return False 
        
        if abs(level - prev) > 3:
            return False

        prev = level
    
    return True

reports = []
f = open("day2.txt", "r")
for line in f:
    report = line.split()
    report = [int(level) for level in report]
    reports.append(report)

print("Safe reports: " + str(count_safe_reports(reports)))
print("Safe reports with dampner: " + str(count_safe_reports(reports, dampner=True)))