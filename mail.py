import smtplib
try:
    print('sending theemail1')
    server = smtplib.SMTP('smtp.mailtrap.io', 587)
    # server.ehlo()
    server.starttls()  # Enable TLS encryption
    # server.ehlo()
    print(2)
    server.login('breezebike669@gmail.com', 'Aayush888999@')
    print('Sendin thegmail2')

    sender = 'breezebike669@gmail.com'
    # Replace with a valid recipient email address
    recipient = 'saarock4646@gmail.com'
    message = 'Mailsent from the python'
    print('SENDING THE GMAIL3')

    server.sendmail(sender, recipient, message)
    # server.quit()
    print("Email sent successfully!")


except Exception as e:
    print("An error occurred while sending the email:", e)

