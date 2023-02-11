import pywhatkit

# Asks a user to type a phonenumber to message
# Note, use international syntax, 
# for example a US number would be +17576243392
print("\n")
print("Type a number to message:")
number = '+5585994199015'

# Asks for user to type a message
print("\n")
print("Type a message:")
message = 'Ola'

# Send a WhatsApp Message to the contact instantly (gives 10s to load web client before sending)
pywhatkit.sendwhatmsg_instantly(number, message, 10)