import os
import xml.etree.ElementTree as ET
import csv

# Path to the data directory
data_dir = 'programming/assignment-1/data'

# Dictionary to store aggregated time for each classname
class_times = {}

# Parse each XML file in the data directory
for filename in os.listdir(data_dir):
    if filename.endswith('.xml'):
        tree = ET.parse(os.path.join(data_dir, filename))
        root = tree.getroot()
        classname = root.attrib.get('name')
        total_time = sum(float(testcase.attrib.get('time')) for testcase in root.findall('.//testcase'))
        if classname in class_times:
            class_times[classname] += total_time
        else:
            class_times[classname] = total_time

# Distribute classnames into 5 groups based on total time
group_count = 5
groups = [[] for _ in range(group_count)]
group_times = [0] * group_count

# Sort classnames by total time in descending order
sorted_classes = sorted(class_times.items(), key=lambda item: item[1], reverse=True)

# Distribute classes to groups to balance the total time in each group
for classname, time in sorted_classes:
    min_group = group_times.index(min(group_times))
    groups[min_group].append((classname, time))
    group_times[min_group] += time

# Write output to CSV
with open('output.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['classname', 'time', 'groupNo'])
    for group_no, group in enumerate(groups, 1):
        for classname, time in group:
            csvwriter.writerow([classname, time, group_no])

print("Output written to output.csv")
