# ""Alien Email""
# We need you to send a spoofed email.
# Use smtp server at '127.0.0.1', port 1025.
# Author needs to be bob-roswell-1947@ship-shape-security.com
# Recipient needs to be zultron@cyberdarkart.com
#
import smtplib

author = 'bob-roswell-1947@ship-shape-security.com'
recipient = 'zultron@cyberdarkart.com'

server = smtplib.SMTP('127.0.0.1', 1025)
server.sendmail(author, recipient, "This is a greeting from humans")
server.close()
