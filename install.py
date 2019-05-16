from pip._internal import main as pip_main
import os
import json

def pip_auto_install(package):
	return_value = os.system("pip install --user "+package+" >/dev/null 2>&1")
	if os.WEXITSTATUS(return_value)==0:
		return True
	return False


failed_packages=[]
with open('package.json') as f:
        data = json.load(f)["Dependencies"]

for package in data:
	if not pip_auto_install(package):
		failed_packages.append(package)

if(len(failed_packages)==0):
    print("success")
else:
	for package in failed_packages:
		print(package)
