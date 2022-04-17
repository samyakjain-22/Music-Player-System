import smtplib,webbrowser
print("HELLO!!!")
print("YOU CAN SEND WARNING MAIL USING THIS...")
def get_mail():
    server_available = ["hotmail", "gmail", "yahoo", "outlook"]
    while True:
        mail_id="samyakjainsam22@gmail.com" # id 
        if "@" and ".com" in mail_id:
            symbol_pos=mail_id.find("@")
            dot_pos=mail_id.find(".com")
            sp=mail_id[symbol_pos+1:dot_pos]
            if sp in server_available:
                return mail_id,sp
                break
            else:
                print(f"WE CAN NOT PROVIDE SERVICE FOR '{sp}'")
                print('ONLY SERVERS ARE ["hotmail", "gmail", "yahoo", "outlook"]')
                print("try again...")
                continue
        else:
            print("INVALID MAIL")
            print("try again...")
            continue
def set_smtp_domain(service_provider):
    if service_provider=="gmail":
        return "smtp.gmail.com"
    if service_provider == "outlook" or service_provider=="hotmail":
        return "smtp-mail.outlook.com"
    if service_provider == "yahoo":
        return "smtp.mail.yahoo.com"
usermail,service_provider=get_mail()
password="Jainsamyak@222000" #pass
while True:
    try:
        smtp_domain=set_smtp_domain(service_provider)
        connection=smtplib.SMTP(smtp_domain,587)
        connection.ehlo()
        connection.starttls()
        connection.login(usermail,password)
    except:
        if service_provider=="gmail":
            print("LOGIN UNSUCESSFULL,There are 2 possible reason!!!")
            print("1.) Wrong username or password.")
            print("2.) Your Gmail is very secure to use this.You can change it to less secure.")
            print("Do you want your mail account less secure for sometime to enable the working by opening a webpage?")
            answer=input("'yes' or 'no'? : ")
            if answer=="yes":
                webbrowser.open("https://myaccount.google.com/lesssecureapps")
                print("You can retype your email and password...")
                usermail, service_provider = get_mail()
                password = input("password : ")
                continue
            else:
                print("You can retype your email and password...")
                usermail,service_provider=get_mail()
                password=input("password : ")
                continue
        else:
            print("LOGIN UNSUCESSFULL,you may have write wrong username or password...")
            print("Please retype your email and password")
            usermail,service_provider=get_mail()
            password=input("password :")
            continue
    else:
        print("LOGIN SUCCESSFULLY!!!")
        break
reciver_address,reciver_service_provider=get_mail()
print("Please enter Subject and Message")
Subject=input("Subject : ")
Message=input("Message : ")
connection.sendmail(usermail,reciver_address,("Subject: " + str(Subject) + "\n\n" + str(Message)))
print("EMAIL SEND SUCCESSFULLY")
connection.quit()