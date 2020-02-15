from crawler import Crawler
from emailer import send_confirmation_email
import utils


def lambda_handler(event, context):
    crawler = Crawler()
    register_resp = crawler.run()
    register_html = utils.extract_info(register_resp.content)
    register_text = register_resp.text
    register_confirmation_code = utils.get_confirmation_code(register_resp.content)

    if "circle-success" in register_text:
        email_html = "<html><body style=\"background-color: black\">{}</body></html>".format(register_html)
        print("Successfully registered and sending email")
        send_confirmation_email(email_html, register_text, f"Register2Park Success ({register_confirmation_code})!")
    else:
        error_message = "Register2Park Confirmation Failed!"

        print(register_html)
        send_confirmation_email(None, error_message, error_message)

# lambda_handler(None, None)
