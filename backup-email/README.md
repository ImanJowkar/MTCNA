
# send email

```
tool e-mail set from=mikrotik-zabbix port=587 server=mail.example.com tls=starttls user=zbx@example.com

tool e-mail send to="user@outlook.com" subject="zabbix-mikrotik" tls=starttls body="aseras" from="zbx@example.com" 

```

# send backup to email

```
tool e-mail send to="user@gmail.com" subject="backup-mikrotik" tls=starttls body="below is backupfile"  from="zbx@ayexample.com" file=full-backup.backup


```

# script for backup
```
:local backupName "Backup-$[system clock get date]";
:local to "imanjowkar99@gmail.com";
:local subject "backup-$[system/identity/get name]";
:local body "here is your backup file form Mikrotik router os :$[system/identity/get name] - date: $[system clock get date]";



/system backup save name=$backupName encryption=aes-sha256 password=12345
delay delay-time=3
put $to
/tool e-mail send to=$to subject=$subject body=$body file=$backupName tls=starttls from="test@example.com"

```

### create a scheduler
```
/system scheduler
add name=schedule1-backup on-event="system/script/run backup" policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon start-date=2024-06-23 \
    start-time=00:10:14
```