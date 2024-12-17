# Quick, learn locust

## Getting Started

### Using virtual environment venv

Python virtual environments enable you to set up a Python sandbox with its
own set of packages separate from the system site-packages in which to work.

#### Create

```bash
$ python -m venv .venv
```

#### Activate

To activate on macOS and Linux.
```bash
$ source .venv/bin/activate
```

To activate on Windows.
```bash
$ .venv\Scripts\activate.bat
```

To activate on Windows with PowerShell.
```bash
$ .venv\Scripts\Activate.ps
```

#### Deactivate

When done,run:
```bash
$ deactivate
```

### Using pip to install pytest

pip is the tool used to install Python packages, and it is installed as part of
your Python installation.

Confirm pip version by running:
```bash
$ pip --version
```

You should see:
```bash
pip 24.0 from /Users/ ... /.venv/lib/python3.11/site-packages/pip (python 3.11)
```

Install locust by running:
```bash
$ pip install locust
```

Confirm the locust version by running:
```bash
$ locust --version
```

You should see:
```bash
locust 2.32.4 from /Users/ ... /.venv/lib/python3.11/site-packages/locust (python 3.11)
```

## Running the locust testing framework

Run locust with the following command:
```bash
$ locust [options] [UserClass ...]
```

Show help message and configuration info:
```bash
$ locust --help
```

Learn more from the Locust documentation:
```bash
https://docs.locust.io
```

## Hello World

1. Open the file `locustfile.py`, which is described on this _Your first test_ page: https://docs.locust.io/en/stable/quickstart.html

2. This "HttpUser" will make an HTTP request to `/hello`, then to `/world`, and then repeat.

3. In you current directory and then run the `locust` command:

```bash
$ locust
[2024-12-17 08:00:13,012] You-Machine-Name/INFO/locust.main: Starting Locust 2.32.4
[2024-12-17 08:00:13,030] You-Machine-Name/INFO/locust.main: Starting web interface at http://0.0.0.0:8089
```

NOTE: Your web interface might be reached as `localhost` instead of `0.0.0.0`.

4. Open http://0.0.0.0:8089

5. Enter the Host as `https://www.google.com` and the rest as shown here:

![Locust start new load test](Locust-start-new-load-test.jpg)

6. Click the Start button.
