
class UrlManager(object):
    @staticmethod
    def buildUrl(path):
        return path

    @staticmethod
    def buildStaticUrl(path):
        path = path + "?ver=" + "xx年xx月xx日"
        return path
