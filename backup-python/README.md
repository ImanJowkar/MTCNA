# Backup from mikrotik routeros with python 

I discovered a [GitHub repository](https://github.com/d4vidcn/routeros_ssh_connector) containing a Python library designed for connecting to MikroTik devices. This library enables us to perform various actions, such as creating backup from mikrotik.
so I write a simple python code to backup from mikrotik and send this backup to your email address whicd you specifiy in the .env file.

I have created a cronjob for executing this script .

# usage 
```
# create .env file like .env.example

# install requirement.txt
pip3 install -r requirement.txt

# finally run the main.py file

python main.py

```


## you can create a cronjob

```
crontab -e

# add 


*/2 * * * * /root/venv/bin/python /root/app/main.py 

# run At every 2nd minute


```