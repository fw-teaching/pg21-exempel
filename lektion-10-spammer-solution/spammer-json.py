import json
import utils

utils.hello()

with open('emails.json') as file_handle:
    secret_marketing_data_json = file_handle.read()

emails = json.loads(secret_marketing_data_json) # Vi läser in json-texten som en python-lista och sparar i emails

fixed_emails = utils.fix_email_list(emails)

new_file_contents = json.dumps(fixed_emails, indent=4) # vi dumpar fixed_emails-listan som json i new_file_contents

with open('refined.json', 'w') as file_handle:  # w = write
    file_handle.write(new_file_contents)

print(new_file_contents) 