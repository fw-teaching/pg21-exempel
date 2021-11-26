
def hello():
    """Prints hello"""
    print("Hello from module")

def fix_email_list(email_list):
    """Removes non-valid arcada-adresses from list of emails"""
    fixed_emails = [email.lower().strip() for email in email_list if "@arcada.fi" in email.lower()]
    fixed_emails.sort()
    return fixed_emails

def file_reader(filename):
    """Reads a text file and returns its contents"""
    with open(filename) as file_handle:
        file_contents = file_handle.read()
    return file_contents

def file_writer(filename, contents):
    """Writes contents to a text file """
    with open(filename, 'w') as file_handle:
        file_handle.write(contents)