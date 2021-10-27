# dao_twitter

# install
`sudo apt update && sudo apt upgrade -y`

`apt install python3-pip`

`pip install -r requirements.txt`

`python3 connection.py`



# create systemd
``` bash 

cat<<-EOF > /etc/systemd/system/twitter.service
[Unit]
Description=twitter daemon
After=network-online.target

[Service]
Type=simple
Restart=always
RestartSec=1
User=root
WorkingDirectory=/root/dao_twitter
ExecStart=python3 connection.py
SyslogIdentifier=twitter
StartLimitInterval=0
LimitNOFILE=65536
LimitNPROC=65536

[Install]
WantedBy=multi-user.target
EOF

```


`sudo systemctl daemon-reload`
`sudo chmod 755 /etc/systemd/system/twitter.service`
`sudo systemctl enable twitter.service`
`sudo service twitter start `
`sudo service twitter status`

`tail -f /var/log/syslog`
