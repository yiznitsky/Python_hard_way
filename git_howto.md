# Step 1: Create Repository on GitHub
> click `+` on top left of screen and select `New Repository`

#Step 2:
> Choose a **Repository name**, select `public` or `private`

#Step 3:
> Select "license"

#Step 4:
> In terminal window create **README.md**

```bash
echo "# repo name" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/yiznitsky/<repositoryname>.git
git push -u origin master
```

#Step 5: Start Committing

```bash
git add .
git commit
git push origin master
```

**Commit often!**