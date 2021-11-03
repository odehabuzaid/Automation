import re


def auto():
    content = dict()
    with open('./assets/potential-contacts.txt','r') as file:
        email_finder = r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)'
        
        formated_numbers = r'(\d{3}[-\.\s]\d{3}[-\.\s]\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]\d{4}|\d{3}[-\.\s]\d{4})'

        regex = re.compile(email_finder)
        content = file.read()

        email_address = regex.findall(content)
        
        regex = re.compile(formated_numbers)
        
        phone_numbers = \
            " ".join(regex.findall(content)) \
            .replace(')','-') \
            .replace('(','') \
            .replace('.','-')

        content = dict(zip(email_address,phone_numbers.split()))
        
        phone_numbers = open("./results/phone_numbers.txt", "w+")
        emails = open("./results/emails.txt", "w+")
        for k,v in content.items(): 
            phone_numbers.write(v + '\n')
            emails.write(k + '\n')
auto()
