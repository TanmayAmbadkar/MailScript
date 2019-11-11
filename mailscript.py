import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

MY_ADDRESS = 'tanmay.ambadkar@gmail.com'
PASSWORD = '#SaRuTaTa1'

def get_contacts(filename):
    """
    Return two lists names, emails containing names and email addresses
    read from a file specified by filename.
    """
    
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[1])
            emails.append(a_contact.split()[0])
    return names, emails

def read_template(filename):
    """
    Returns a Template object comprising the contents of the 
    file specified by filename.
    """
    
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def main():
    names, emails = get_contacts('mycontacts.txt')

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    for name, email in zip(names, emails):
        msg = MIMEMultipart()       # create a message
        print(name)
        # add in the actual person name to the message template
        # Prints out the message body for our sake

        # setup the parameters of the message
        msg['From']=MY_ADDRESS
        msg['To']=email
        msg['Subject']="Polo forest food requirements form"
        
        # add in the message body
        #msg.attach(MIMEText(message, 'plain'))
        msgText = MIMEText('Dear {},\n'.format(name))
        msg.attach(msgText)
        msgText = MIMEText('Please fill this form by 6:00pm, 12/11/2019. This form is regarding whether you will be paying for food in polo forest. Even if you don\'t want to pay, please fill the form.\n','plain')
        msg.attach(msgText)
        msgText = MIMEText('<a href="https://forms.gle/cVky919GVtZR2Gdn6">Please fill this form\n</a>','html')
        msg.attach(msgText)
        msgText = MIMEText('\nRegards,\nTanmay and Anuj', 'plain')
        msg.attach(msgText)
        s.send_message(msg)
        del msg
        
    # Terminate the SMTP session and close the connection
    s.quit()
    
if __name__ == '__main__':
    main()