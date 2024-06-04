import os
import xml.etree.ElementTree as ET

def parse_xml_files(directory):
    data = []
    # Iterate through XML files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".xml"):
            tree = ET.parse(os.path.join(directory, filename))
            root = tree.getroot()
            # Parse XML and aggregate time consumed by classname
            # Implement your parsing logic here
            classname = root.find('classname').text  # Example: Replace 'classname' with the actual XML element containing the classname
            time = root.find('time').text  # Example: Replace 'time' with the actual XML element containing the time
            data.append((classname, time))
    return data

def main():
    data = parse_xml_files("data")
    # Implement logic to equally distribute `classname` by their time into 5 groups
    # Print the data in CSV format with the header `classname,time,groupNo`

if __name__ == "__main__":
    main()
