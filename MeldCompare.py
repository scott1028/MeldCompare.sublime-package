import sublime
import sublime_plugin
import os
import webbrowser
import subprocess

fileA = fileB = None


def settings():
    return sublime.load_settings('MeldCompare.sublime-settings')


def is_windows():
    return os.name == 'nt'


def get_location():
    return settings().get('meld_compare_path')


def plugin_loaded() -> None:
    # If we are on windows - set a custom path
    if is_windows():
        if os.path.exists("%s\meld\meld.exe" % os.environ['ProgramFiles(x86)']):
            settings().set("meld_compare_path", '"%s\meld\meld.exe"' % os.environ['ProgramFiles(x86)'])
            sublime.save_settings("MeldCompare.sublime-settings")
        elif os.path.exists("%s\meld\meld.exe" % os.environ['ProgramFiles']):
            settings().set("meld_compare_path", "%s\meld\meld.exe" % os.environ['ProgramFiles'])
            sublime.save_settings("MeldCompare.sublime-settings")
        elif os.path.exists(settings().get('meld_compare_path')):
            return
        else:
            sublime.error_message('Could not find Meld Compare. Please set the path to your tool in MeldCompare.sublime-settings.')


def recordActiveFile(f):
    global fileA
    global fileB
    fileB = fileA
    fileA = f


def runMacMeldCompare():
    if fileA is not None and fileB is not None:
        print(
            "MeldCompare comparing: LEFT [" + fileA + "] | RIGHT [" + fileB + "]")
        subprocess.Popen([str(get_location()), str(fileA), str(fileB)])
        print("Should be open...")
    else:
        print(
            "You must have activated TWO files to compare.\nPlease select two tabs to compare and try again")
        sublime.error_message(
            "You must have activated TWO files to compare.\nPlease select two tabs to compare and try again")


def runWinMeldCompare():
    if fileA is not None and fileB is not None:
        cmd_line = '%s "%s" "%s"' % (get_location(), fileA, fileB)
        print(
            "MeldCompare comparing: LEFT [" + fileA + "] | RIGHT [" + fileB + "]")
        subprocess.Popen(cmd_line)
    else:
        print(
            "You must have activated TWO files to compare.\nPlease select two tabs to compare and try again")
        sublime.error_message(
            "You must have activated TWO files to compare.\nPlease select two tabs to compare and try again")


class MeldCompareCommand(sublime_plugin.ApplicationCommand):

    def run(self):
        # For Windows
        if is_windows():
            if os.path.exists(get_location()):
                runWinMeldCompare()
                return
            else:
                sublime.error_message('Could not find Meld Compare. Please set the path to your tool in MeldCompare.sublime-settings.')
                return

        # For OSX
        if os.path.exists(get_location()):
            runMacMeldCompare()

        else:
            commandLinePrompt = sublime.ok_cancel_dialog('Could not find bcompare.\nPlease install the command line tools.', 'Do it now!')
            if commandLinePrompt:
                new = 2  # open in a new tab, if possible
                url = "http://www.scootersoftware.com/support.php?zz=kb_OSXInstallCLT"
                webbrowser.open(url, new=new)
                bCompareInstalled = sublime.ok_cancel_dialog('Once you have installed the command line tools, click the ok button to continue')
                if bCompareInstalled:
                    if os.path.exists("/usr/bin/meld"):
                        runMacMeldCompare()

                    else:
                        sublime.error_message('Still could not find bcompare. \nPlease make sure it exists at:\n/usr/local/bin/bcompare\nand try again')

                else:
                    sublime.error_message('Please try again after you have command line tools installed.')
            else:
                sublime.error_message('Please try again after you have command line tools installed.')


class MeldCompareFileListener(sublime_plugin.EventListener):
    def on_activated(self, view):
        if view.file_name() is not None and view.file_name() != fileA:
            recordActiveFile(view.file_name())
