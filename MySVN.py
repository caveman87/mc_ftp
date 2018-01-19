import pysvn
import myLogger
import os, shutil


class McSVN:
    def __init__(self):
        self.name = "svn"
        self.mc_web_remote = 'svn://15.107.29.25/trunk/40. CUT/40.10 SRC/menuCenter_web/trunk'
        self.mc_web_local = 'D:\Data\menuCeter_web'
        self.client = pysvn.Client()
        self.logging = myLogger.MyLogger().mylogging()

    def check_out(self):
        self.logging.info("check out from {} to {} ".format(self.mc_web_remote, self.mc_web_local))
        self.client.checkout(self.mc_web_remote, self.mc_web_local)
        self.logging.info("check out finished.")

    def mc_update(self):
        self.logging.info("update menuCenter_web")
        headrev_before = self.client.info(self.mc_web_local).revision.number
        self.logging.info("Current Head Revision: " + str(headrev_before))
        self.client.update(self.mc_web_local)
        self.logging.info("updated.")
        headrev_after = self.client.info(self.mc_web_local).revision.number
        self.logging.info("updated Head Revision: " + str(headrev_after))

    def get_changes(self):
        changes = self.client.status(self.mc_web_local)
        self.logging.info('files to be added:')
        self.logging.info([f.path for f in changes if f.text_status == pysvn.wc_status_kind.added])
        self.logging.info('files to be removed:')
        self.logging.info([f.path for f in changes if f.text_status == pysvn.wc_status_kind.deleted])
        self.logging.info('files that have changed:')
        self.logging.info([f.path for f in changes if f.text_status == pysvn.wc_status_kind.modified])
        self.logging.info('files with merge conflicts:')
        self.logging.info([f.path for f in changes if f.text_status == pysvn.wc_status_kind.conflicted])
        self.logging.info('unversioned files:')
        self.logging.info([f.path for f in changes if f.text_status == pysvn.wc_status_kind.unversioned])


