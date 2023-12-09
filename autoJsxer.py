## this py script run a terminal command to convert jsxbin to jsx
## ./jsxer sampelaJsxbin.jsxbin

import os
import subprocess

## get all jsxbin files in the current directory
def getJsxbinFiles():
    jsxbinFiles = []
    for file in os.listdir(os.getcwd()):
        if file.endswith(".jsxbin"):
            jsxbinFiles.append(file)
    return jsxbinFiles

## create terminal command to convert jsxbin to jsx
def createTerminalCommand(jsxbinFile):
    return "./jsxer " + jsxbinFile

## run terminal command
def runTerminalCommand(terminalCommand):
    subprocess.call(terminalCommand, shell=True)

## main function
def main():
    jsxbinFiles = getJsxbinFiles()
    for jsxbinFile in jsxbinFiles:
        terminalCommand = createTerminalCommand(jsxbinFile)
        runTerminalCommand(terminalCommand)

## run main function
if __name__ == "__main__":
    main()

