pyinstaller --onefile login.py
xcopy /s /i /e /q /y .\apks .\dist\apks\
xcopy /s /i /e /q /y .\nomes .\dist\nomes\
xcopy /s /i /e /q /y .\vpn .\dist\vpn\