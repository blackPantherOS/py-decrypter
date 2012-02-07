Python GPG Decrypter
====================

This Python script is used as a Windows executable to decrypt encrypted GPG files through drag and drop. It outputs the decrypted text to the Windows command prompt, copies the text to the clipboard and deletes the encrypted file when finished executing.


Build with PyInstaller
----------------------

1. Download and install [Python Windows Installer](http://www.python.org/download/).
2. Download and install [pywin32](http://sourceforge.net/projects/pywin32/files/pywin32/Build216/pywin32-216.win32-py2.7.exe/download) (Python for Windows extensions).
3. Download and unpack [PyInstaller](http://www.pyinstaller.org/) (https://github.com/pyinstaller/pyinstaller) to the Python folder (ie - `C:\Python27`).
4. Copy decrypter.py into the pyinstaller folder (ie - `C:\Python27\pyinstaller\decrypter.py`).
5. Launch the Windows Command Prompt and `cd` into the PyInstaller folder - `cd C:\Python27\`.
6. Run `Configure.py`.
7. Run `Makespec.py decrypter.py --onefile -K`.
8. Run `Build.py decrypter/decrypter.spec`.


End User Instructions
---------------------

### Setup - Import Secret Key

1. Download and install [Gpg4win](http://www.gpg4win.org/download.html) with Kleopatra
2. Open Kleopatra by going to Programs > Gpg4win > Kleopatra.
3. Import your secret key into Kleopatra by clicking the Import Certificates button and selecting the proper key file.
4. Close Kleopatra.
5. Download the [decrypter app](https://github.com/downloads/CollegePlus/py_decrypter/decrypter-1.0.exe).
 
### Decrypting Files
 
1. Drag and drop any GPG encrypted file onto the decrypter-x.x.exe file.
2. Enter your passphrase if required.
3. Paste the clipboard contents into a text field or text area before closing the decrypter-x.x.exe app.
4. Close the app and repeat steps 1 through 3 for each additional file you wish to decrypt.