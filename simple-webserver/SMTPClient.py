from socket import *
msg = '\r\n I love computer networks!'
endmsg = '\r\n.\r\n'
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = "" # put in your own
# Create socket called clientSocket and establish a TCP connection with mailserver

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 25))

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
# Send MAIL FROM command and print server response.

mailFromCommand = 'MAIL FROM: someone@gmail.com\r\n'
clientSocket.send(mailFromCommand)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
	print '250 reply not received from server.'

# Send RCPT TO command and print server response.
rcptToCommand = 'RCPT TO: adoan91@gmail.com\r\n'
clientSocket.send(rcptToCommand)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
	print '250 reply not received from server.'
# Send DATA command and print server response.
dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '354':
	print '354 reply not received from server.'
# Send message data.
message = "SUBJECT: Test Subject\n"
# Message ends with a single period.
clientSocket.send(message + msg + endmsg)
# Send QUIT command and get server response.
quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand)
recv1 = clientSocket.recv(1024)
print recv1
