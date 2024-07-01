from datetime import datetime
from decouple import config
from send_mail import send_smtp_email
from routeros_ssh_connector import MikrotikDevice


ROUTER_IP=config('router_ip')
USERNAME_MIK=config('username_mik')
PASSWORD_MIK=config('password_mik')



time_chris = datetime.now()
date = time_chris.date()
time = time_chris.now().time().strftime('%H-%M')

router = MikrotikDevice()
router.connect(ROUTER_IP, USERNAME_MIK, PASSWORD_MIK)


# get backup and save it into the file
identity = router.get_identity()
command = f"system/backup/save name=back-{date}-{time} password=123 encryption=aes-sha256"
try:
    router.send_command(command)
except:
    print('faild to backup')

# download the backup file to host
backup_name = f"back-{date}-{time}.backup"
router.download_file(backup_name, local_path=".")


router.disconnect()
del router


subject = "Backup-Mikrotik"
text = f"This is daily backup from your Mikrotik device  --  device-name: {identity}"
send_smtp_email(subject, time_chris, text, backup_name)