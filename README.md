## Run python app using UV
```
git clone https://github.com/mir-owahed/python-flask-app.git
cd python-flask-app/
code .
uv venv
source .venv/bin/activate

uv init
uv add flask
uv add -r requirements.txt 
uv run app.py 


python3 -V
pip3 -V
which python3
```
```
curl http://localhost:8181
curl http://localhost:8181/ping
```
## Write API using fastapi
## FastAPI project setup using 'uv'
```
mkdir fastapi-project
cd fastapi-project/
code .
mir@DESKTOP-JASRD4A:~/fastapi-project$ uv init
Initialized project `fastapi-project`
mir@DESKTOP-JASRD4A:~/fastapi-project$ uv venv
Using CPython 3.12.3 interpreter at: /usr/bin/python3.12
Creating virtual environment at: .venv
Activate with: source .venv/bin/activate
mir@DESKTOP-JASRD4A:~/fastapi-project$ source .venv/bin/activate
(fastapi-project) mir@DESKTOP-JASRD4A:~/fastapi-project$ uv pip install "fastapi[standard]"
(fastapi-project) mir@DESKTOP-JASRD4A:~/fastapi-project$ uv run fastapi dev main.py

```
access docs from browser
```
http://localhost:8000/docs
http://localhost:8000/redoc
```
```
curl http://localhost:8000/

```
