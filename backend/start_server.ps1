cd .\venv\Scripts
.\activate
Write-Host "Venv activated." -ForegroundColor DarkGreen 
cd ..\..\Courses\
Write-Host "Enviroment variables set. Starting server..." -ForegroundColor DarkRed 
python manage.py runserver