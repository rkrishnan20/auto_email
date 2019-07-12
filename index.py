import smtplib as sb
import sys

args = sys.argv
server = sb.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login("rahulkrishnan6199", "10%Nerd90%Boss")
msg = "Hi Philip, \n" 
text = input()
msg += text
msg += "\nBest, \nRahul"
server.sendmail("rahulkrishnan6199@gmail.com", "rkrishn2@terpmail.umd.edu", msg)

