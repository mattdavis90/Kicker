import os
import subprocess

class Base:
  def __init__(self, hostsDir):
    self._hostsDir = hostsDir

  def _getUsername(self):
    return 'puppetagent'

  def _getFile(self, filename, trunc):
    filename = self._hostsDir + filename

    try:
      if trunc:
        fHandle = open(filename, 'w+')
      else:
        fHandle = open(filename, 'r+')
    except IOError:
      fHandle = open(filename, 'w+')

    return fHandle

  def readHosts(self, filename):
    retVal = []

    fHandle = self._getFile(filename, False)

    for line in fHandle:
      line = line.strip()

      if line:
        retVal.append(line)

    fHandle.close()

    return retVal

  def writeHosts(self, filename, hosts):
    fHandle = self._getFile(filename, True)

    for host in hosts:
      fHandle.write(host + '\n')

    fHandle.close()

  def addHost(self, filename, host):
    hosts = self.readHosts(filename)

    hosts.append(host)

    self.writeHosts(filename, hosts)

  def remHost(self, filename, host):
    hosts = self.readHosts(filename)

    if host in hosts: hosts.remove(host)

    self.writeHosts(filename, hosts)
