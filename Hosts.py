import requests


class Hosts:
    def __init__(self, filepath):
        self.comment = '# WEBSITE BLOCKER'

        self.filepath = filepath
        try:
            self.f = open(filepath, 'r+')  # r+
            self.fileContents = self.f.read()
        except IOError:
            self.f = open(filepath, 'w')
            self.fileContents = ''
        if self.fileContents.find(self.comment) == -1:
            self.writeIndex = len(self.fileContents)
            self.hosts = []
        else:
            self.writeIndex = self.fileContents.find(self.comment) + len(self.comment)
            hostsString = self.fileContents[self.writeIndex:].strip()

            self.hosts = []
            if hostsString:
                for line in hostsString.split('\n'):
                    isEnabled = True

                    if line[0] == '#':
                        isEnabled = False
                        line = line[1:]

                    self.hosts.append([*line.split(' '), isEnabled])

        self.f.seek(self.writeIndex)

    def getHosts(self):
        return list(map(lambda e: e[1], self.hosts))

    def addHost(self, domain):
        try:
            requests.get('http://' + domain)
            if ['127.0.0.1', domain, True] not in self.hosts:
                self.hosts.append(['127.0.0.1', domain, True])
                return True
        except:
            return False

    def isHostEnabled(self, domain):
        for i in range(len(self.hosts)):
            if self.hosts[i][1] == domain:
                return self.hosts[i][2]

    def disableHost(self, domain):
        for i in range(len(self.hosts)):
            if self.hosts[i][1] == domain:
                self.hosts[i][2] = False

    def enableHost(self, domain):
        for i in range(len(self.hosts)):
            if self.hosts[i][1] == domain:
                self.hosts[i][2] = True

    def deleteHost(self, domain):
        self.hosts = list(filter(lambda i: i[1] != domain, self.hosts))

    def deleteAllHosts(self):
        self.hosts = []

    def write(self):
        hosts = ''
        if self.fileContents.find(self.comment) == -1:
            hosts = '\n' + self.comment + '\n'
        if self.hosts:
            for redirect, domain, isEnabled in self.hosts:
                if not isEnabled:
                    hosts += '#'
                hosts += redirect + ' ' + domain + '\n'
        self.f.write('\n' + hosts)
        self.f.truncate()
        self.f.seek(self.writeIndex)
