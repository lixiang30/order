
# class UrlManager(object):
#     @staticmethod
#     def buildUrl(path):
#         return path
#
#     @staticmethod
#     def buildStaticUrl(path):
#         path = path + "?ver=" + "xx年xx月xx日"
#         return path


# -*- coding: utf-8 -*-

class UrlManager(object):
    def __init__(self):
        pass

    @staticmethod
    def buildUrl( path ):
        return path

    @staticmethod
    def buildStaticUrl(path):
        ver = "%s"%( 22222222 )
        path =  "/static" + path + "?ver=" + ver
        return UrlManager.buildUrl( path )