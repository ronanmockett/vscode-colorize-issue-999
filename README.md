# Vscode Colorize - Issue 999

Issue: https://github.com/KamiKillertO/vscode-colorize/issues/999

When navigating to files using "Go to definition" there is a noticeable delay both in syntax highlighting and navigating to the file.

During the syntax highlighting stage all keyboard input is suspended for around 0.5-1s then the computer catches up.

When using the "Go to definition" action. You will observe up to 2s before the file opens in your IDE.

Minimal extensions for reproduction
[Python (Pylance, Python Debugger)](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
[Colorize](https://marketplace.visualstudio.com/items?itemName=kamikillerto.vscode-colorize)
