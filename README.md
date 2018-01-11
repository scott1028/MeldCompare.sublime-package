Description
===========
The Sublime Text MeldCompare plugin is a modified version of the excellent [WinMerge/FileMerge](https://github.com/SublimeText/WinMerge) plugin.

[BeyondCompare](http://www.scootersoftware.com/) is a nice GUI file difference engine that is cross platform, with support for both Windows and OSX. This package adds support to Sublime Text 2 and 3 for allowing you to diff the last two active views, even if they are in different Sublime windows.

Package Installation
====================
Install using [Package Control](https://packagecontrol.io/installation) by searching for "BeyondCompare".

Alternativly, bring up a command line in the Packages/ folder of your Sublime user folder, and execute the following:
> git clone git://github.com/npadley/BeyondCompare.git

When you launch Sublime Text, it will pick up the contents of this package so that you can consume the goodness that it provides.

Instructions for Use
====================

As you move around and work, the plugin remembers the to most recent active files or tabs. When activated, it loads those two files into BeyondCompare for you.

After making any merge changes in the application, save and close your files. You should then receive a message to reload the files in the editor.

Use the keyboard shortcut [Ctrl-Opt-D] to launch BeyondCompare.

Use the menu item under Tools or the menu item under the right-click context menu.

Installation Instructions for OS X
==================================

In order to get started, it's important to make sure that you have command line tools installed.

To do that, start BeyondCompare, then go to Beyond Compare in the menu bar and click the Install Command Line Tools item. After that, you should be able to use this plugin.

If the above instructions do not work, please read the [latest documentation] (http://www.scootersoftware.com/support.php?zz=kb_OSXInstallCLT)

Installation Instructions for Windows and Linux
===============================================

All that is required is for you to have a working copy of the program installed. You can find those instructions at: http://www.scootersoftware.com/download.php
