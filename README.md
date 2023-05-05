# Your first Flask application

## Creating the environment

1. Open terminal
2. Clone the GitHub repository with examples: `git clone git@github.com:wsbwt/flask-intro.git`
3. Open folder with projects: `cd flask-intro`
4. Create the Python virtual environment: `python -m venv .venv`
5. Activate the Python virtual environment: (see Notices below)
6. If the environment is activated you should see `(.venv)` at the start of the line!
7. Update pip installer: `python -m pip install --upgrade pip`
8. Install required libraries: `pip install -r requirements.txt`
9. You can also start Visual Studio Code to edit apps: `code .` (watch the dot). 

   VSCode should recognize virtual environment and use it (see: bottom right corner).

### Notices

- If you use **MacOS** or **Linux**, in step 5 use command `.venv/bin/activate`
- If you use **CMD** (Command line) in **Windows**:
  - In terminal
- If you use **PowerShell** in **Windows**:
  - In the new window run command: `Set-ExecutionPolicy RemoteSigned -Scope Process`
  - In step 5 use command: `.\venv\Scripts\Activate.ps1`
- In Windows *do not use* Git Bash window.

## Running your application

You can test your app using command eg.: `python app1.py`

If everything has been installed correctly you should see:

```text
 * Serving Flask app "app1" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 123-456-789
 * Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)
```

When you start the browser and open page (`http://127.0.0.1:8080` lub `http://localhost:8080`) the browser should display results from the Flask application. You can stop your application in console with `Ctrl+C`.

In these examples we use port **8080** instead of the default Flask port **5000** to allow the preview of application when started in AWS Cloud9 environment.
