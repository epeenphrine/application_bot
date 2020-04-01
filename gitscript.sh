read -p "enter commit message: " commitmessage
git add . && git reset config.py && git status && git commit -m '$commitmessage'