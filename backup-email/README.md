
# send email

tool e-mail set from=mikrotik-zabbix port=587 server=mail.example.com tls=starttls user=zbx@example.com

tool e-mail send to="user@outlook.com" subject="zabbix-mikrotik" tls=starttls body="aseras" from="zbx@example.com" 



# send backup to email

tool e-mail send to="user@gmail.com" subject="backup-mikrotik" tls=starttls body="below is backupfile"  from="zbx@ayexample.com" file=full-backup.backup