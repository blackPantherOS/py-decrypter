import gnupg
import os, sys
from Tkinter import Tk

# Make sure a folder or directory was specified
if len(sys.argv) == 1:
   sys.exit(1)

# Assign name of file or folder to resusable variable
filename = sys.argv[1]

# Instantiate the clipboard object
cb = Tk()
cb.withdraw()

while 1:
   while True:
      try:
         f = open(filename, "rb").read()
      except IOError:
         print 'Error: cannot open ' + filename + '. Does the file exist?'
      else:
         print "Opening " + filename
         break

   while True:
      decrypt_key = raw_input("Passphrase: ")
      try:
         gpg = gnupg.GPG(gpgbinary="gpg.exe")
      except ValueError:
         raw_input("Error: did not find gpg.exe -- is it stored in Decryptor's \n directory? Hit ENTER to exit...")
         quit
      else:
         decrypted_data = gpg.decrypt(f, passphrase=decrypt_key)
         if str(decrypted_data) == '':
            print "Decryption failed -- no data returned. Is the passphrase correct?"
            True
         else:
            cb.clipboard_clear()
            cb.clipboard_append(decrypted_data)                
            print '\n\n' + str(decrypted_data) + ' (...has been copied to clipboard)\n\n'
            os.remove(filename)
            raw_input("Clipboard will be cleared. Press ENTER to close program...")
            cb.clipboard_clear()
            cb.destroy()
            sys.exit()
            break
