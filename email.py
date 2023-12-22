

class Email:
    has_been_read = False
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
    def mark_as_read(self):
        self.has_been_read = True

inbox = []

def populate_inbox(email_address, subject_line, email_content):
    inbox.append(Email(email_address, subject_line, email_content))

def list_emails():
    email_list = "Please choose an email to read:\n"
    for index, email in enumerate(inbox):
        email_list += f"{index + 1} -- {email.subject_line}\n"
    return email_list

def read_email(email_index):
    selected_email = inbox[email_index]
    selected_email.mark_as_read()
    print("\n"
          +f"From: {selected_email.email_address}"
          +"\n"
          +f"Subject line: {selected_email.subject_line}"
          +"\n"
          +f"Body:\n{selected_email.email_content}"
          +"\n\n"
          +"Email has been marked as read"
          )

populate_inbox(
    "groe181@gmail.com", 
    "Quick catch-up", 
    "Hi Geoff,\nAre you available for a call next Friday?\nThanks,\nJames"
    )
populate_inbox(
    "croe1711@gmail.com", 
    "Shopping List", 
    "Hi Geoff,\nPlease add potatoes to the list when you go to the shops tomorrow.\nMum"
    )
populate_inbox(
    "emily.kay@gmail.com", 
    "Next week", 
    "Geoff,\nEllie and Dan are coming around for dinner on Tuesday.\nEmily"
    )

menu = """
Choose an option:
1. Read an email
2. View unread emails
3. Quit application
"""
menu_selection = None

while menu_selection != 3:
    menu_selection = int(input(menu))
    if menu_selection == 1:
        read_email(int(input(list_emails())) - 1)
    elif menu_selection == 2:
        for email in inbox:
            if not email.has_been_read:
                print(email.subject_line)
    else:
        print("Please enter a valid option of 1, 2 or 3")
