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
```
```
curl http://localhost:8181
curl http://localhost:8181/ping
```
