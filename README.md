# Student Task & Note Manager API

A small API for creating personal tasks and keeping them organized. It uses FastAPI, SQLite, and SQLAlchemy.

## Get started

You’ll need Python 3.10 or newer. From the project folder, create and activate a virtual environment, then install the dependencies:

```bash
python -m venv venv
```

On Windows:

```powershell
.\venv\Scripts\activate
```

On macOS or Linux:

```bash
source venv/bin/activate
```

Install the packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project folder and add a long, random secret for signing login tokens:

```env
SECRET_KEY=replace-this-with-a-long-random-secret
```

Keep `.env` private; it should not be committed to Git.

## Run the API

From the project folder, start the development server:

```bash
uvicorn app.main:app --reload
```

Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to try the endpoints.

## Using the API

`POST /register` creates an account. Send a name, email, and password.
`POST /login` checks your credentials and returns a bearer token.
`POST /tasks` creates a task. Include the login token as a bearer token.
`GET /tasks` lists the signed-in user’s tasks.

Tasks can have a `pending` or `completed` status. Each user can only see and manage their own tasks.

## Run the tests

```bash
pytest
```
