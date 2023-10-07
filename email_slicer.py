def get_username(email):
    if '@' in email:
        email_index = email.index('@')
        username = email[:email_index]
        return username

def get_domain(email):
    if '@' in email:
        email_index = email.index('@')
        return email[email_index+1:]


email = input("Enter email:")
print(f"Username:{get_username(email)}\nDomain:{get_domain(email)}")