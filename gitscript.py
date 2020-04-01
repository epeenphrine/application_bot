import os

commit_message = input('commit mesage: ')

os.system(f"git add . && git reset config.py && git status && git commit -m '{commit_message}' ")

print('commit made')