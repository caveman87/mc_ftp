import configparser


class Env(object):
    def __new__(self, cls, *args, **kwargs):
        if not hasattr(self,'instance'):
            self.instance = super(Env, self).__new__(self)
            return self.instance

    def __init__(self, cls):
        self.cp = configparser.ConfigParser()
        self.cp.read(".\config\config.ini")
        self.secs = self.cp.sections()

    def local_env(self):
        local_path = self.cp.get('local_path', 'local_dir')
        return local_path

    def host_jenkins(self):
        my_dict = {}
        my_dict['host'] = self.cp.get('jenkins', 'host_ip')
        my_dict['port'] = self.cp.getint('jenkins', 'host_port')
        my_dict['username'] = self.cp.get('jenkins', 'username')
        my_dict['password'] = self.cp.get('jenkins', 'password')
        my_dict['remote_dir'] = self.cp.get('jenkins', 'remote_dir')
        return my_dict

    def host_201(self):
        host_201 = self.cp.items('mc_201')
        my_dict = {}
        my_dict['host'] = self.cp.get('mc_201', 'host_ip')
        my_dict['port'] = self.cp.getint('mc_201', 'host_port')
        my_dict['username'] = self.cp.get('mc_201', 'username')
        my_dict['password'] = self.cp.get('mc_201', 'password')
        my_dict['remote_dir'] = self.cp.get('mc_201', 'remote_dir')
        my_dict['log_dir'] = self.cp.get('mc_201', 'log_dir')
        return my_dict

    def host_202(self):
        host_202 = self.cp.items('mc_202')
        my_dict = {}
        my_dict['host'] = self.cp.get('mc_202', 'host_ip')
        my_dict['port'] = self.cp.getint('mc_202', 'host_port')
        my_dict['username'] = self.cp.get('mc_202', 'username')
        my_dict['password'] = self.cp.get('mc_202', 'password')
        my_dict['remote_dir'] = self.cp.get('mc_202', 'remote_dir')
        my_dict['log_dir'] = self.cp.get('mc_202', 'log_dir')
        return my_dict

    def host_57(self):
        my_dict = {}
        my_dict['host'] = self.cp.get('mc_57', 'host_ip')
        my_dict['port'] = self.cp.getint('mc_57', 'host_port')
        my_dict['username'] = self.cp.get('mc_57', 'username')
        my_dict['password'] = self.cp.get('mc_57', 'password')
        my_dict['remote_dir'] = self.cp.get('mc_57', 'remote_dir')
        my_dict['log_dir'] = self.cp.get('mc_57', 'log_dir')
        return my_dict

    def host_prd_nh_12(self):
        my_dict = {}
        my_dict['host'] = self.cp.get('pro_nh_12', 'host_ip')
        my_dict['port'] = self.cp.getint('pro_nh_12', 'host_port')
        my_dict['username'] = self.cp.get('pro_nh_12', 'username')
        my_dict['password'] = self.cp.get('pro_nh_12', 'password')
        my_dict['remote_dir'] = self.cp.get('pro_nh_12', 'remote_dir')
        my_dict['log_dir'] = self.cp.get('pro_nh_12', 'log_dir')
        return my_dict

    def host_prd_nh_9(self):
        my_dict = {}
        my_dict['host'] = self.cp.get('pro_nh_9', 'host_ip')
        my_dict['port'] = self.cp.getint('pro_nh_9', 'host_port')
        my_dict['username'] = self.cp.get('pro_nh_9', 'username')
        my_dict['password'] = self.cp.get('pro_nh_9', 'password')
        my_dict['remote_dir'] = self.cp.get('pro_nh_9', 'remote_dir')
        my_dict['log_dir'] = self.cp.get('pro_nh_9', 'log_dir')
        return my_dict

    def host_prd_zr_12(self):
        my_dict = {}
        my_dict['host'] = self.cp.get('pro_zr_12', 'host_ip')
        my_dict['port'] = self.cp.getint('pro_zr_12', 'host_port')
        my_dict['username'] = self.cp.get('pro_zr_12', 'username')
        my_dict['password'] = self.cp.get('pro_zr_12', 'password')
        my_dict['remote_dir'] = self.cp.get('pro_zr_12', 'remote_dir')
        my_dict['log_dir'] = self.cp.get('pro_zr_12', 'log_dir')
        return my_dict

    def host_prd_zr_9(self):
        my_dict = {}
        my_dict['host'] = self.cp.get('pro_zr_9', 'host_ip')
        my_dict['port'] = self.cp.getint('pro_zr_9', 'host_port')
        my_dict['username'] = self.cp.get('pro_zr_9', 'username')
        my_dict['password'] = self.cp.get('pro_zr_9', 'password')
        my_dict['remote_dir'] = self.cp.get('pro_zr_9', 'remote_dir')
        my_dict['log_dir'] = self.cp.get('pro_zr_9', 'log_dir')
        return my_dict

    def svn_dxc(self):
        my_dict = {}
        my_dict['svn_path'] = self.cp.get("svn_dxc", 'svn_path')
        my_dict['username'] = self.cp.get("svn_dxc", 'username')
        my_dict['password'] = self.cp.get("svn_dxc", 'password')
        return my_dict

    def svn_yum(self):
        my_dict = {}
        my_dict['svn_path'] = self.cp.get('svn_yum', 'svn_path')
        my_dict['username'] = self.cp.get('svn_yum', 'username')
        my_dict['password'] = self.cp.get('svn_yum', 'password')
        return my_dict


