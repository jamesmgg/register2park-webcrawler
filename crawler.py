import requests
import utils

class Crawler:
    def __init__(self):
        self.HOME_PAGE_URL = "https://www.register2park.com/register.php?width=1680&height=1050"
        self.REGISTER_URL = "https://www.register2park.com/register-vehicle-process?width=1680&height=1050"
        self.REGISTER_POST_BODY = {
            "vehicleApt": -1,  # APT_NUMBER_GOES_HERE
            "vehicleMake": "<VEHICLE_MAKE>",
            "vehicleModel": "<VEHICLE_MODEL>",
            "vehicleLicensePlate": "<VEHICLE_LICENSE_PLATES>",
            "propertyIdSelected": -1, # PROPERTY_NUMBER (get it inspecting network requests when registering manually)
            "propertySource": "parking - snap"
        }
        self.session = requests.Session()
        self.results = {}

        self.session.headers.update({
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
        })

    def _get(self, url):
        print(f"GET: {url}")
        r = self.session.get(url)
        print(f"status_code={r.status_code}")
        r.raise_for_status()
        return r

    def _post(self, url, body):
        print(f"POST: {url}")
        r = self.session.post(url, data=body)
        print(f"status_code={r.status_code}")
        r.raise_for_status()
        return r

    def home_page(self):
        return self._get(self.HOME_PAGE_URL)

    def register(self):
        return self._post(self.REGISTER_URL, self.REGISTER_POST_BODY)

    def run(self):
        home_page_resp = self.home_page()
        register_resp = self.register()

        return register_resp
