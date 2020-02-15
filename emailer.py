import boto3
from botocore.exceptions import ClientError

SENDER = "SOME_NAME <youremail@gmail.com>"

# Replace recipient@example.com with a "To" address. If your account
# is still in the sandbox, this address must be verified.
RECIPIENT = "recipient_email@gmail.com"

AWS_REGION = "us-east-1"

# The character encoding for the email.
CHARSET = "UTF-8"

# Create a new SES resource and specify a region.
client = boto3.client('ses', region_name=AWS_REGION)


def send_confirmation_email(request_html, request_text, subject):
    # Try to send the email.
    try:
        response = _send_email(request_html, request_text, subject)
    # Display an error if something goes wrong.
    except ClientError as e:
        print(e)
        _send_email(None, str(e), "Register2Park Failure! -- AWS errors")
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])


def _send_email(body_html, body_text, subject):
    message_config = {
        'Body': {
            'Text': {
                'Charset': CHARSET,
                'Data': body_text,
            },
        },
        'Subject': {
            'Charset': CHARSET,
            'Data': subject,
        },
    }

    if body_html:
        # set body_html if it exists
        message_config['Body'].update({
            'Html': {
                'Charset': CHARSET,
                'Data': body_html,
            },
        })

    return client.send_email(
        Destination={
            'ToAddresses': [
                RECIPIENT,
            ],
        },
        Message=message_config,
        Source=SENDER,
    )
