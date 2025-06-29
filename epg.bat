

git pull origin master
git add .
git commit -m update 
git push origin master
git checkout --orphan latest_branch
git add -A
git commit -am "update -*_*"
git branch -D master
git branch -m master
git push -f origin master