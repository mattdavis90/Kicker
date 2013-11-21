class Kick:
  def __init__(self, base):
    self._moduleName = "kick"
    self._base = base

  def _setHostToPXE(self, host):
    print "Changing Cobbler to kick", host

    self._base.runCommand(['cobbler', 'system', 'edit', '--name', host, '--netboot-enabled=Y'])

  def _syncCobbler(self):
    print "Syncing Cobbler"

    self._base.runCommand(['cobbler', 'sync'])

  def _rebootHost(self, host):
    print "Rebooting", host

    self._base.runSSHCommand(host, ['reboot'])

  def _kickHosts(self, hosts):
    for host in hosts:
      self._setHostToPXE(host)

    self._syncCobbler()

    for host in hosts:
      self._rebootHost(host)

  def getMethodName(self):
    return self._moduleName

  def run(self, argv):
    retVal = False
    argc = len(argv)

    if argc > 0:
      method = argv[0]

      if method == 'file' and argc > 1:
        hosts = self._base.readHosts(argv[1])

        self._kickHosts(hosts)

        retVal = True
      elif method == 'hosts' and argc > 1:
        self._kickHosts(argv[1:])

        retVal = True

    return retVal

  def printHelp(self, appname):
    print "\t" + appname, self._moduleName + " file <filename>"
    print "\t" + appname, self._moduleName + " hosts <hostname> [<hostname> ...]"
