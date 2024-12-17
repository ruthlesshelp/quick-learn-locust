from locust import HttpUser, run_single_user, task

class TriangleApplicationUser(HttpUser):
    host = "https://testpages.eviltester.com"

    @task
    def triangle_page(self):
        res = self.client.get("/styled/apps/triangle/triangle001.html")

        breakpoint()

        assert res is not None



# if launched directly, e.g. "python tests/triangle_applicant.py", not "locust -f tests/triangle_applicant.py"
# This allows for `breakpoint()` for debugging
if __name__ == "__main__":
    run_single_user(TriangleApplicationUser)
