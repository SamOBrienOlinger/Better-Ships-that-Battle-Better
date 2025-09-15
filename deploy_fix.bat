@echo off
echo Adding runtime.txt file...
git add runtime.txt

echo Committing changes...
git commit -m "Add Python runtime specification and fix Django dependencies"

echo Pushing to Heroku...
git push heroku main

echo Checking if Django is installed...
heroku run pip show django

echo Running migrations...
heroku run python better_ships_that_battle_better/manage.py migrate

echo Deployment complete! Opening your app...
heroku open

pause
