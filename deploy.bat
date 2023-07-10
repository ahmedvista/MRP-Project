@echo off
cls

set "host_ip=107.174.249.53"
set "host_user=root"
set "deploy_path=/root/www/test_deploy"
set "ssh_key="C:\Users\Ahmed\id_vscode""


echo "delete old files except"
ssh -i %ssh_key% %host_user%@%host_ip% "cd %deploy_path% && ls | grep -xv "db.sqlite3" | xargs sudo rm -rf"

py -Bc "import pathlib; [p.unlink() for p in pathlib.Path('.').rglob('*.py[co]')]"
py -Bc "import pathlib; [p.rmdir() for p in pathlib.Path('.').rglob('__pycache__')]"

scp -rp -i %ssh_key% mrp/* %host_user%@%host_ip%:%deploy_path%

ssh -i %ssh_key% %host_user%@%host_ip% "python3 -m venv %deploy_path%/venv"
ssh -i %ssh_key% %host_user%@%host_ip% "%deploy_path%/venv/bin/pip install -r %deploy_path%/requirements.txt "
ssh -i %ssh_key% %host_user%@%host_ip% "%deploy_path%/venv/bin/python3 %deploy_path%/manage.py migrate --run-syncdb"

pause