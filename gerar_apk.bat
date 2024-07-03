pyinstaller --onefile --name Criador_v7.0.7 --icon=./vpn/logo.ico login.py
xcopy /s /i /e /q /y .\apks .\dist\apks\
xcopy /s /i /e /q /y .\nomes .\dist\nomes\
xcopy /s /i /e /q /y .\vpn .\dist\vpn\
xcopy /s /i /e /q /y .\platform-tools .\dist\platform-tools\