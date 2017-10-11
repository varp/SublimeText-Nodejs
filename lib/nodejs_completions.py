import sublime
import sublime_plugin

from .nodejs_debug import debug, info


class NodeCompletion(sublime_plugin.EventListener):
    """
    Smart completions for Nodejs 
    """

    pass
    # def on_query_completions(self, view, prefix, locations):
    #     info('CALL from on_query_comnpletions')

    #     if (view.match_selector(locations[0], 'source.js')):

    #         debug('view', view)
    #         debug('prefix', prefix)
    #         debug('locations', locations)

    #         real_prefix = view.substr(
    #                 sublime.Region(int(locations[0]) - 2, int(locations[0]) - 1)
    #                 )

    #         debug('real_prefix', real_prefix)

    #         return (
    #                 [
    #                     ['NS', 'Nodejs'], 
    #                     ['console', 'console'],
    #                     ['console.info', 'console.info()'],
    #                     ['console.dir', 'console.dir($0)'], 
    #                     ['console.debug', 'console.debug($0)'],
    #                     ['process', 'process'],
    #                     ['process._dlopen', 'process._dlopen($0)'],
    #                     ['process.kill', 'process.kill()']
    #                 ],
    #                 sublime.INHIBIT_EXPLICIT_COMPLETIONS)