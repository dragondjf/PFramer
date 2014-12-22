import os
from functools import partial
from util.pluginbase import PluginBase

plugin_base = PluginBase(package='RPCPlugins',
                         searchpath=[os.sep.join([os.getcwd(), 'rpcplugins', 'builtin_plugins'])])

class Application(object):

    def __init__(self, name):
        super(Application, self).__init__()
        self.name = name
        self.source = plugin_base.make_plugin_source(
            searchpath=[os.sep.join([os.getcwd(), 'rpcplugins', name, 'plugins'])],
            identifier=self.name)

        self._plugins = {}
        for plugin_name in self.source.list_plugins():
            plugin = self.source.load_plugin(plugin_name)
            self._plugins.update({plugin_name: plugin})

    @property
    def plugins(self):
        return self._plugins

rpcApp = Application('app1')
