import os
from ldap3 import Server, Connection, ALL, ALL_ATTRIBUTES
from ldap3.core.exceptions import LDAPException

class Ldap:
    """LDAP class helper
    """
    def __init__(self):
        """Data initialization
        """
        self.ldap_host = os.getenv('LDAP_HOST')
        self.ldap_port = int(os.getenv('LDAP_PORT'))
        self.ldap_manager = os.getenv('LDAP_MANAGER')
        self.ldap_manager_password = os.getenv('LDAP_MANAGER_PASSWORD')
        self.dc = os.getenv('LDAP_DC').split('.')
        self.ldap_server = Server(
            self.ldap_host, port=self.ldap_port, get_info='ALL')

    def connect(self, params):
        """create bind to server
        
        Arguments:
            params {dict} -- username and password
        
        Returns:
            dict -- status of bind
        """
        try:
            dn = "cn={},{}dc={},dc={}".format(
                params['username'], '' if params['username'] == self.ldap_manager else 'ou=People,', self.dc[0], self.dc[1])
            conn = Connection(
                self.ldap_server, dn, password=params['password'], auto_bind=False, raise_exceptions=True)
            conn.bind()

            if conn:
                print(1, conn.last_error)
                print(conn.result)
                search_base = 'cn=Neo,ou=Group,dc={},dc={}'.format(
                    self.dc[0], self.dc[1])
                search_filter = '(&(objectClass=groupOfNames)(member={}))'.format(
                    dn)
                conn.search(search_base, search_filter,
                            attributes=ALL_ATTRIBUTES)
                print(conn.response)
                response = conn.response
                if len(response) == 0:
                    return {
                        'error_code': 49,
                        'error_message': 'User is not exist on Neo group'
                    }
                return {}
        except LDAPException as err:
            return {
                'error_code': err.result,
                'error_message': err.message
            }

    # def search(self, search_base, search_filter):
    #     """filter ldap object
        
    #     Arguments:
    #         search_base {[type]} -- [description]
    #         search_filter {[type]} -- [description]
        
    #     Returns:
    #         [type] -- [description]
    #     """
    #     try:
    #         dn = 'cn={},dc={},dc={}'.format(
    #             self.ldap_manager, self.dc[0], self.dc[1])
    #         conn = Connection(
    #             self.ldap_server, dn, password=self.ldap_manager_password, auto_bind=False, raise_exceptions=True)
    #         conn.bind()

    #         if conn:
    #             conn.search(search_base, search_filter,
    #                         attributes=ALL_ATTRIBUTES)
    #             return conn.response

    #     except LDAPException as err:
    #         return {
    #             'error_code': err.result,
    #             'error_message': err.message
    #         }

    # def users(self, query, params):
    #     """ldap user manager
        
    #     Arguments:
    #         query {[type]} -- [description]
    #         params {[type]} -- [description]
        
    #     Returns:
    #         [type] -- [description]
    #     """
    #     try:
    #         dn = 'cn={},dc={},dc={}'.format(
    #             self.ldap_manager, self.dc[0], self.dc[1])
    #         conn = Connection(
    #             self.ldap_server, dn, password=self.ldap_manager_password, auto_bind=False, raise_exceptions=True)
    #         conn.bind()
    #         if conn:
    #             new_dn = 'cn={},ou=People,dc={},dc={}'.format(
    #                 params['cn'], self.dc[0], self.dc[1])
    #             if query == 'create':
    #                 # not implemented yet
    #                 pass
    #             elif query == 'delete':
    #                 # not implemented yet
    #                 pass
    #             elif query == 'update_password':
    #                 # not implemented yet
    #                 pass

    #     except LDAPException as err:
    #         return {
    #             'error_code': err.result,
    #             'error_message': err.message
    #         }
