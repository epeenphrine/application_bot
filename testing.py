from datetime import datetime
from datetime import timedelta
import time
import winsound
import webbrowser
import json

with open ('jobs_applied_to.json') as f:
    decent_jobs = json.load(f)

title = 'engineer'
link = 'google.com'
applied = False

dict_list = []

print(len(decent_jobs))

jobs_status = { 'title' : title, 'link' : link, 'applied': applied}
jobs_status1 = {'title': 'mcddonalds', 'link': 'yolo.com', 'applied': True}
print(jobs_status['title'])
dict_list.append(jobs_status)
dict_list.append(jobs_status1)
for i in range(0, len(dict_list)):
    job = dict_list[i]
    if False in job.values():
        print(job)
        job['applied'] = True
        dict_list[i] = job


print(dict_list)