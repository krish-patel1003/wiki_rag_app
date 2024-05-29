## How to run locally

#### Create virtual environment
```bash
python -m venv env
```

#### Activate virtual environment
For Windows
```bash
 .\env\Scripts\activate
```

#### Install Requirements
```bash
pip install -r requirements.txt
```

#### Run FastAPI server
```bash
fastapi dev ./app/main.py
```

Go to http://127.0.0.1:8000/docs and Try the GET API to Ask you question.
