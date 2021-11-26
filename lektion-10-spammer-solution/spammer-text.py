import utils

utils.hello()

secret_marketing_data = utils.file_reader('emails.txt')

emails = secret_marketing_data.split(";")

fixed_emails = utils.fix_email_list(emails)

new_file_contents = ", ".join(fixed_emails) # Skapar en str av en list, använder komma som separator

utils.file_writer('refined.txt', new_file_contents)

print(", ".join(fixed_emails)) 