import smtplib

fromaddr = 'geigercounter2ss@gmail.com'
toaddrs  = 'adrian.paleacu@gmail.com'
msg = 'There was a terrible error that occured and I wanted you to know!'


# Credentials (if needed)
username = 'geigercounter2ss@gmail.com'
password = '******'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()