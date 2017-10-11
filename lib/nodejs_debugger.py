import os

import sublime
import sublime_plugin

from .nodejs_base import NodeTextCommand
from .nodejs_debug import debug

class NodejsDebugger(object):
    """
    Mixin class with debugging features
    """

    def show_output(self, result):
        s = sublime.load_settings("Nodejs.sublime-settings")
        if s.get('output_to_new_tab'):
            self.scratch(result, title="Node Output",
                         syntax="Packages/Text/Plain text.tmLanguage")
        else:
            self.panel(result)
    
    def show_command_panel(self, initial_text=None):
        if not initial_text:
            initial_text = ""
        caption = "command (type h for help)"
        self.get_window().show_input_panel(caption, initial_text, self.on_done,
                self.on_change, self.on_cancel)

    def on_done(self, input):
        self.previous_command = input
        self._thread.proc.stdin.write(input)
        self.debugger_output = self._thread.proc.stdout.read() 
        #self._thread.proc.communicate(input=input, timeout=90) 
        self.show_output(self.debugger_output)
        self.show_command_panel(self.previous_command)

    def on_change(self, input):
        debug('NodejsDebugger - on_change - user input', input)

    def on_cancel(self):
        debug('NodejsDebugger - on_change - user input', '')

    def proccess_command(self):
        self.show_command_panel()
