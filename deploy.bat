rd /S /Q dist\server
pyinstaller -F -D -c --onefile python\server.spec
xcopy python\modules\* dist\server\modules\ /SQ
xcopy python\public\* dist\server\public\ /SQ