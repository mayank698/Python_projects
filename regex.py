import re
pattern = "\w+:\s\d+"
employee_logins_string = "1001 bmoreno: 12 Marketing 1002 tshah: 7 Human Resources 1003 sgilmore: 5 Finance"
print(re.findall(pattern, employee_logins_string))

with open("list.txt","r") as file:
    file_read=file.read()
fileToString=file_read.split(" ")
print(file_read)
print(fileToString)
#print(type(file_read))
#pattern2="\d*\.\d*\.\d*\.\d"
#print(re.findall(pattern2,file_read))