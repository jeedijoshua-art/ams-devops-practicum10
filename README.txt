AMS — Practicum 10: Developing a DevOps Pipeline

PROJECT CONTENTS
----------------
attendance.py                         AMS attendance-status module
tests/test_attendance.py              Automated unit tests (19 cases)
requirements.txt                      Python test dependencies
.github/workflows/devops-pipeline.yml GitHub Actions CI/CD workflow
Dockerfile                            Container build and test instructions

LOCAL SETUP (macOS)
-------------------
1. Open Terminal in this extracted project folder.

2. Create and activate a virtual environment:
   python3 -m venv .venv
   source .venv/bin/activate

3. Install dependencies:
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   python -m pip install flake8 bandit pip-audit

4. Run the same checks locally:
   flake8 attendance.py tests --max-line-length=100
   bandit -q -r attendance.py
   pip-audit -r requirements.txt
   pytest --cov=attendance --cov-report=term-missing --cov-fail-under=90

5. Build and run the Docker test image (Docker Desktop must be installed/running):
   docker build -t ams-devops-demo .
   docker run --rm ams-devops-demo

GITHUB DEMONSTRATION
--------------------
1. Create an empty GitHub repository named ams-devops-practicum10.
2. In this extracted folder, initialize and push the project:

   git init
   git add .
   git commit -m "Add AMS DevOps pipeline"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/ams-devops-practicum10.git
   git push -u origin main

3. Open the repository on GitHub and select Actions.
4. Open "AMS DevOps Pipeline" to show the workflow stages and logs.
5. To demonstrate automatic triggering, edit a harmless comment in attendance.py,
   commit, and push again. The workflow should start automatically.

IMPORTANT
---------
This is a focused, runnable AMS attendance-status module created to demonstrate
the pipeline described in Practicum 10. It is not the complete production AMS
application and does not connect to its database, authentication, or live attendance
records.

The GitHub Actions workflow is configured, but it will only execute after the
project is pushed to a GitHub repository. Local checks and GitHub-hosted CI are
separate executions. Do not claim a remote pipeline passed until the Actions run
shows green success.
