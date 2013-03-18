from yum.plugins import PluginYumExit, TYPE_CORE, TYPE_INTERACTIVE
try:
    import json
except ImportError:
    import simplejson as json

requires_api_version = '2.5'

plugin_type = (TYPE_INTERACTIVE,)

def config_hook(conduit):
    parser = conduit.getOptParser()
    parser.add_option('', '--json', dest='json', action='store_true',
           default=False, help="show pending package changes as JSON")

def postresolve_hook(conduit):
    opts, commands = conduit.getCmdLine()

    if opts.json:
        packages = {}

        for transaction in conduit.getTsInfo():
            if transaction.name not in packages:
                packages[transaction.name] = {}

            version = { "version": transaction.version, "release": transaction.release,
                    "epoch": transaction.epoch, "arch": transaction.arch, "state": transaction.ts_state }

            if transaction.ts_state:
                packages[transaction.name]["pending"] = version
            else:
                packages[transaction.name]["current"] = version

        print( json.dumps(packages) )
        raise PluginYumExit('')
