"""
A wrapper for passing commands to the Dash CLI
"""

import subprocess

class DashCLI():
  def __init__(self):
    print "Initializing Dash CLI"
  
  def call(self, command):
    """
    Stub for now
    """
    command_string = "dash-cli "
    command_string += command
    subprocess.checkoutput(command_string)
    return
    
