
## yum-transaction-json

Show pending YUM upgrades and installs as a JSON data structure.

### Installation

First install the required dependencies

    yum install python-simplejson

Then copy the plugin and its config to the correct locations

    cp transaction-json.py /usr/lib/yum-plugins/

    cp transaction-json.conf /etc/yum/pluginconf.d/transaction-json.conf

Once installed (and a configfile with enabled is added) run with

     $ yum -q update --json


    {
        "NetworkManager": {
            "pending": {
                "arch": "x86_64",
                "epoch": "1",
                "release": "29.el7_2",
                "state": "u",
                "version": "1.0.6"
            }
        },
        "NetworkManager-libnm": {
            "pending": {
                "arch": "x86_64",
                "epoch": "1",
                "release": "29.el7_2",
                "state": "u",
                "version": "1.0.6"
            }
        }
    }

### Packaging

If you want to build your own `yum-transaction-json` package then the
[yum-transaction-json fpm-cookery recipe](https://github.com/deanwilson/unixdaemon-fpm-cookery-recipes/tree/master/recipes/yum-transaction-json) is a quick way to get started.

#### Author
[Dean Wilson](http://www.unixdaemon.net)
