# monitorPower
Monitor power status

# Setup
You will need to add your Gmail address and password to a file in `~/.monitorPower/config.yaml`,
which should contain:

```yaml
user-email: myusername@gmail.com
user-password: mypassword
```

In addition, you need to allow less secure apps on your gmail account. The
instructions to do so can be found [here][1].

You also need to install `psutil` by 
```bash
python3 -m pip install psutil
```

[1]: https://devanswers.co/allow-less-secure-apps-access-gmail-account/
