from bs4 import BeautifulSoup


def extract_info(html):
    soup_html = BeautifulSoup(html, "html.parser")
    confirmation_body = soup_html.find(attrs={"class": "circle-success"})
    water_mark = confirmation_body.find(attrs={"class": "watermark"})

    if water_mark:
        water_mark.decompose()

    return confirmation_body


def get_confirmation_code(html):
    soup_html = BeautifulSoup(html, "html.parser")
    confirmation_code_h3 = soup_html.find("h3")

    return confirmation_code_h3.string.strip().replace("\\n", "").replace("\\t", "")


# uncomment for testing
# print(get_confirmation_code(open("_output.html")))
