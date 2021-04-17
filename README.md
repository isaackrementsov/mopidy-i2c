# mopidy-i2c
Code to display current Mopidy track info on I2C display
## How to run
To run Mopidy-I2C as a service:
```bash
mv mopidy-i2c.service /lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable mopidy-i2c
sudo systemctl start mopidy-i2c
```
