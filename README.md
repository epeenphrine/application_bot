
install all packages in requirements.txt
you can do it by:
pipenv install -r ./requirements.txt


make sure you add job urls from that you typed in indeed. Alot of the settings such as location, experience, and all that is in the url 
store it in config.py:
example:

job_urls = [
    'https://indeed.com',
    'https://indeed1.com',
    'https://indeed.com
]

to filter for jobs that stay within job board and start bringing up each link in browser 1 by 1
run manual_run.py interactive:

python -i manual_run.py \
run() \
apply() \




