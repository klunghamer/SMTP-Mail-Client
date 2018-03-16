from socket import *
import ssl
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ("smtp.gmail.com", 465) #Fill in start #Fill in end
# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket = ssl.wrap_socket(clientSocket)
clientSocket.connect(mailserver)
#Fill in end
recv = clientSocket.recv(1024)
print recv
if recv[:3] != '220':
    print '220 reply not received from server.'
# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
    print '250 reply not received from server.'


#gmail authentication
clientSocket.send('AUTH LOGIN a2VsbHkubHVuZ2hhbWVyQGdtYWlsLmNvbQ==\r\n') #encoded email
recv1 = clientSocket.recv(1024)
print recv1
clientSocket.send('cGFnamJteHNxdm5zbXlsaA==\r\n') #encoded app password
recv1 = clientSocket.recv(1024)
print recv1

# Send MAIL FROM command and print server response.
# Fill in start
mailFrom = "MAIL FROM: <kelly.lunghamer@gmail.com>\r\n"
clientSocket.send(mailFrom)
recv1 = clientSocket.recv(1024)
print recv1
# Fill in end
# Send RCPT TO command and print server response.
# Fill in start
rcptTo = "RCPT TO: <kgl277@nyu.edu>\r\n"
clientSocket.send(rcptTo)
recv2 = clientSocket.recv(1024)
print recv2
# Fill in end
# Send DATA command and print server response.
# Fill in start
data = "DATA\r\n"
clientSocket.send(data)
recv3 = clientSocket.recv(1024)
print recv3
# Fill in end
# Send message data.
# Fill in start
clientSocket.send(msg)
# Fill in end
# Message ends with a single period.
# Fill in start
clientSocket.send(endmsg)
# Fill in end
# Send QUIT command and get server response.
# Fill in start
quit = "QUIT\r\n"
clientSocket.send(quit)
recv4 = clientSocket.recv(1024)
print recv4
# Fill in end
