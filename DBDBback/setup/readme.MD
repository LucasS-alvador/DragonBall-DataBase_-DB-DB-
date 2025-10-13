# Setup:

1) Activate the virtual environment:
LINUX:
```
source setup/venv/bin/activate
```
WINDOWS: 
```
.\venv\Scripts\Activate
```

If there is not a virtual environment ("venv" folder), create it:
```
cd setup
python3 -m venv venv

After creation, active it:

LINUX:
```
source venv/bin/activate
```

WINDOWS:
```
.\venv\Scripts\Activate
```

Install the libraries:
```
pip3 install -r requirements.txt
```
* Alternatively, you can install libraries by hand:
```
pip3 install flask
pip3 install flask_sqlalchemy
pip3 install flask_cors
pip3 install pytest
```
* Maintenance: *when necessary*, generate new requirements:
```
pip3 freeze > requirements.txt
```
2) Configure environment variables PYTHONPATH and MY_DB   

Linux/macOS
```
export PYTHONPATH=/home/friend/02-gitlab/prog25/web/python/flask/01-back-persons-cars:$PYTHONPATH
export MY_DB="SQLITE"
```
Windows
```
export PYTHONPATH=C:\02-gitlab\prog25\web\python\flask\01-back-persons-cars\setup;PYTHONPATH%
export MY_DB="SQLITE"
```

If executing Powershell:
```
$env:PYTHONPATH = "C:\02-gitlab\prog25\web\python\flask\01-back-persons-cars\setup"
$env:MY_DB="SQLITE"
```

3) You can remove the database.db file and re-create the database:
```
rm src/database.db
python3 setup/create_database.py
```

4) Run the backend tests:

Goto the "tests" folder

Run:
```
pytest -s
```
5) If tests are ok, you can run the backend :-)

In folder "src", run:
```
flask run --debug
```
6) Call the backend, in the web browser:

localhost:5000

export PYTHONPATH=C:\Users\discente\Music\DragonBalls\prog25\web\python\flask\01-back-persons-cars\setup;%PYTHONPATH%
export MY_DB="SQLITE"

C:\Users\discente\Music\DragonBalls\prog25\web\python\flask\01-back-persons-cars\setup
