import re


def auto():
    content = dict()
    with open('./assets/potential-contacts.txt','r') as file:
        email_finder = r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)'
        
        formated_numbers = r'[\+\d]?(\d{3}[-\.\s]\d{2,3}[-\.\s]\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]\d{4}|\d{3}[-\.\s]\d{4})'

        regex = re.compile(email_finder)
        content = file.read()
        
        email_address = regex.findall(content)
        
        regex = re.compile(formated_numbers)
        
        
        
        phone_numbers_ = \
            " ".join(regex.findall(content)) \
            .replace(')','-') \
            .replace('(','') \
            .replace('.','-')

        
        
        phone_numbers = open("./results/phone_numbers.txt", "w+")
       
        
        
        
        phone_numbers_ = phone_numbers_.split()
        phone_numbers_.sort()
        
        strs = " ".join(phone_numbers_)
        from itertools import groupby
        phone_numbers_ = [num for num,v in groupby(strs.split())]
        
        
        strs = " ".join(email_address)
        email_address = [email for email,v in groupby(strs.split())]
        emails = open("./results/emails.txt", "w+")
        for email in email_address: 
            emails.write(email + '\n')
        for num in phone_numbers_: 
            phone_numbers.write(num + '\n')
auto()
