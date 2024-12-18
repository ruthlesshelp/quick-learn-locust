from time import sleep
from locust import HttpUser, run_single_user, task
from pyquery import PyQuery

class TriangleApplicationUser(HttpUser):
    host = "https://testpages.eviltester.com"

    @task
    def triangle_page(self):
        get_response = self.client.get("/styled/apps/triangle/triangle001.html")
        assert get_response is not None
        sleep(5)

        breakpoint()

        pq1 = PyQuery(get_response.content)
        assert pq1 is not None

        side1_input = pq1("#side1")
        assert side1_input is not None

        side1_input.val("3")
        side1_val = side1_input.val()
        assert side1_val == '3'

        side2_input = pq1("#side2")
        assert side2_input is not None

        side2_input.val("4")
        side2_val = side2_input.val()
        assert side2_val == '4'

        side3_input = pq1("#side3")
        assert side3_input is not None

        side3_input.val("5")
        side3_val = side3_input.val()
        assert side3_val == '5'

        post_response = self.client.post(
            "/",
            data= {
                "side1": "3",
                "side2": "4",
                "side3": "5"
            }
        )

        pq2 = PyQuery(post_response.content)

        answer_text = pq2("#triangle-type").val()
        assert answer_text == 'Scalene'

# if launched directly, e.g. "python tests/triangle_application.py", not "locust -f tests/triangle_application.py"
# This allows for `breakpoint()` for debugging
if __name__ == "__main__":
    run_single_user(TriangleApplicationUser)
