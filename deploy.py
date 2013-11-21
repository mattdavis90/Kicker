class Deploy:
  def __init__(self, base):
    self._moduleName = "deploy"
    self._base = base

  def _deployHost(self, host):
    print "Deploying to", host
    self._base.runSSHCommand(host, ['puppet', 'agent', '--no-daemonize', '-v', '-o'])

  def getMethodName(self):
    return self._moduleName

  def run(self, argv):
    retVal = False
    argc = len(argv)

    if argc > 0:
      method = argv[0]

      if method == 'file' and argc > 1:
        hosts = self._base.readHosts(argv[1])

        for host in hosts:
          self._deployHost(host)

        retVal = True
      elif method == 'hosts' and argc > 1:
        for host in argv[1:]:
          self._deployHost(host)

        retVal = True

    return retVal

  def printHelp(self, appname):
    print "\t" + appname, self._moduleName + " file <filename>"
    print "\t" + appname, self._moduleName + " hosts <hostname> [<hostname> ...]"
