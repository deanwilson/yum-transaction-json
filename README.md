Show pending YUM upgrades and installs as a JSON data structure.

To install

  yum install python-simplejson

  cp transaction-json.py /usr/lib/yum-plugins/

  echo -e "[main]\nenabled = 1" > /etc/yum/pluginconf.d/transaction-json.conf

Once installed (and a configfile with enabled is added) run with

   yum -q update --json
