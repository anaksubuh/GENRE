git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/anaksubuh/GENRE.git
git push -u origin main
git reset --mixed origin/main
git add .
git commit -m "This is a new commit for what I originally planned to be amended"
git push origin main