# Based on the Locust examples/browse_docs_test.py
# Find all the examples under https://github.com/locustio/locust
#
# This locust test script example will simulate a user
# browsing the Locust documentation on https://docs.locust.io/

from locust import HttpUser, TaskSet, between, run_single_user, task

import random

from pyquery import PyQuery


class BrowseDocumentation(TaskSet):
    def on_start(self):
        # assume all users arrive at the index page
        self.index_page()
        self.urls_on_current_page = self.toc_urls

    @task(10)
    def index_page(self):
        r = self.client.get("/")
        pq = PyQuery(r.content)
        link_elements = pq(".toctree-wrapper a.internal")
        self.toc_urls = [l.attrib["href"] for l in link_elements]

    @task(50)
    def load_page(self, url=None):
        url = random.choice(self.toc_urls)
        r = self.client.get(url)
        pq = PyQuery(r.content)
        link_elements = pq("a.internal")
        self.urls_on_current_page = [l.attrib["href"] for l in link_elements]

    @task(30)
    def load_sub_page(self):
        url = random.choice(self.urls_on_current_page)
        self.client.get(url)


class BrowseDocumentationUser(HttpUser):
    tasks = [BrowseDocumentation]
    host = "https://docs.locust.io/en/latest/"

    # we assume someone who is browsing the Locust docs,
    # generally has a quite long waiting time (between
    # 20 and 600 seconds), since there's a bunch of text
    # on each page
    wait_time = between(20, 600)


# if launched directly, e.g. "python tests/browse_docs_test.py", not "locust -f tests/browse_docs_test.py"
# This allows for `breakpoint()` for debugging
if __name__ == "__main__":
    run_single_user(BrowseDocumentationUser)
