# Browse Documentation Test

For this example, you will need to install _PyQuery_

```bash
$ pip install pyquery
```

## Description

Based on the Locust `examples/browse_docs_test.py`

You can find all the examples under https://github.com/locustio/locust


## Running Selenium

```bash
docker run -e SE_NODE_SESSION_TIMEOUT=60 -e SE_NODE_MAX_SESSIONS=5 -p 4444:4444 -p 7900:7900 --shm-size="2g" --rm seleniarm/standalone-chromium
```

## Running the Test

Our `tests/browser_docs_test.py` Locust script will simulate a user browsing the Locust documentation on https://docs.locust.io/

In you current directory, run the `locust` command:

```bash
$ locust -f tests/browser_docs_test.py
```

