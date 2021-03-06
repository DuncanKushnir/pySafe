########################################################################################################################
#
# pySafe - Authenticator Interface
#
# This is really just a stub  ... files like this should be able to import the interface and just go, but code structure
# really needs some thought
#
#
#
########################################################################################################################

# This brings all the c interfaces into this module ..  at this point still clean code
import safenet.interface as interface
import safenet.safeUtils as safeUtils
import queue

import safenet.mutableData as mutableData
import safenet.immutableData as immutableData
import safenet.authenticator as authenticator

#NULL=interface.NULL
appQueue = queue.Queue()

# From here on in is just a very basic 'working' example
# todo we need heavy thought on how to structure the various classes.
class app:
    def __init__(self,
                 name='SAFE_Connection',
                 version='0.0.0',
                 vendor='rid+dask',
                 addr='http://localhost',
                 alternate_crust_config=None):
        self.name = name
        self.version = version
        self.vendor = vendor
        self.url = addr
        self.lib_auth = interface.lib_auth
        self.lib_app = interface.lib_app
        self.authenticator = authenticator.authenticator(self.lib_auth, self.lib_app)
        self.mutableData = mutableData.mutableData(self.lib_auth, self.lib_app)
        self.immutableData = immutableData.immutableData(self.lib_auth, self.lib_app)

        #Try and add this here...
        #if alternate_crust_config is None:
        #    interface.add_local_crust_config()


    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _test_create_app(self, app_id, user_data, o_cb=None):
        """
            bytes, [any], [function], [custom ffi lib]
            char* app_id, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result, App* app)
        """
        @ffi.callback("void(void* ,FfiResult* ,App*)")
        def _test_create_app_o_cb(user_data ,result ,app):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result ,app)
    
    
        self.lib.safe_app.test_create_app(app_id, user_data, _test_create_app_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _test_create_app_with_access(self, auth_req, user_data, o_cb=None):
        """
            AuthReq*, [any], [function], [custom ffi lib]
            AuthReq* auth_req, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result, App* o_app)
        """
        @ffi.callback("void(void* ,FfiResult* ,App*)")
        def _test_create_app_with_access_o_cb(user_data ,result ,o_app):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result ,o_app)
    
    
        self.lib.safe_app.test_create_app_with_access(auth_req, user_data, _test_create_app_with_access_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _test_simulate_network_disconnect(self, app, user_data, o_cb=None):
        """
            App*, [any], [function], [custom ffi lib]
            App* app, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result)
        """
        @ffi.callback("void(void* ,FfiResult*)")
        def _test_simulate_network_disconnect_o_cb(user_data ,result):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result)
    
    
        self.lib.safe_app.test_simulate_network_disconnect(app, user_data, _test_simulate_network_disconnect_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _app_init_logging(self, output_file_name_override, user_data, o_cb=None):
        """
            bytes, [any], [function], [custom ffi lib]
            char* output_file_name_override, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result)
        """
        @ffi.callback("void(void* ,FfiResult*)")
        def _app_init_logging_o_cb(user_data ,result):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result)
    
    
        self.lib.safe_app.app_init_logging(output_file_name_override, user_data, _app_init_logging_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _app_output_log_path(self, output_file_name, user_data, o_cb=None):
        """
            bytes, [any], [function], [custom ffi lib]
            char* output_file_name, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result, char* log_path)
        """
        @ffi.callback("void(void* ,FfiResult* ,char*)")
        def _app_output_log_path_o_cb(user_data ,result ,log_path):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result ,log_path)
    
    
        self.lib.safe_app.app_output_log_path(output_file_name, user_data, _app_output_log_path_o_cb)
    
        


    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _app_unregistered(self, bootstrap_config, bootstrap_config_len, user_data, o_disconnect_notifier_cb=None, o_cb=None):
        """
            uint8_t*, uintptr_t, [any], [function], [function], [custom ffi lib]
            uint8_t* bootstrap_config, uintptr_t bootstrap_config_len, void* user_data
    
            > callback functions:
            (*o_disconnect_notifier_cb)(void* user_data)
            (*o_cb)(void* user_data, FfiResult* result, App* app)
        """
        @ffi.callback("void(void*)")
        def _app_unregistered_o_disconnect_notifier_cb(user_data):
            appQueue.put('gotResult')
            if o_disconnect_notifier_cb:
                o_disconnect_notifier_cb(user_data)
    
    
        @ffi.callback("void(void* ,FfiResult* ,App*)")
        def _app_unregistered_o_cb(user_data ,result ,app):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result ,app)
    
    
        self.lib.safe_app.app_unregistered(bootstrap_config, bootstrap_config_len, user_data, _app_unregistered_o_disconnect_notifier_cb, _app_unregistered_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _app_registered(self, app_id, auth_granted, user_data, o_disconnect_notifier_cb=None, o_cb=None):
        """
            bytes, AuthGranted*, [any], [function], [function], [custom ffi lib]
            char* app_id, AuthGranted* auth_granted, void* user_data
    
            > callback functions:
            (*o_disconnect_notifier_cb)(void* user_data)
            (*o_cb)(void* user_data, FfiResult* result, App* app)
        """
        @ffi.callback("void(void*)")
        def _app_registered_o_disconnect_notifier_cb(user_data):
            appQueue.put('gotResult')
            if o_disconnect_notifier_cb:
                o_disconnect_notifier_cb(user_data)
    
    
        @ffi.callback("void(void* ,FfiResult* ,App*)")
        def _app_registered_o_cb(user_data ,result ,app):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result ,app)
    
    
        self.lib.safe_app.app_registered(app_id, auth_granted, user_data, _app_registered_o_disconnect_notifier_cb, _app_registered_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _app_reconnect(self, app, user_data, o_cb=None):
        """
            App*, [any], [function], [custom ffi lib]
            App* app, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result)
        """
        @ffi.callback("void(void* ,FfiResult*)")
        def _app_reconnect_o_cb(user_data ,result):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result)
    
    
        self.lib.safe_app.app_reconnect(app, user_data, _app_reconnect_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _app_account_info(self, app, user_data, o_cb=None):
        """
            App*, [any], [function], [custom ffi lib]
            App* app, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result, AccountInfo* account_info)
        """
        @ffi.callback("void(void* ,FfiResult* ,AccountInfo*)")
        def _app_account_info_o_cb(user_data ,result ,account_info):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result ,account_info)
    
    
        self.lib.safe_app.app_account_info(app, user_data, _app_account_info_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _app_exe_file_stem(self, user_data, o_cb=None):
        """
            [any], [function], [custom ffi lib]
            void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result, char* filename)
        """
        @ffi.callback("void(void* ,FfiResult* ,char*)")
        def _app_exe_file_stem_o_cb(user_data ,result ,filename):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result ,filename)
    
    
        self.lib.safe_app.app_exe_file_stem(user_data, _app_exe_file_stem_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _app_set_additional_search_path(self, new_path, user_data, o_cb=None):
        """
            bytes, [any], [function], [custom ffi lib]
            char* new_path, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result)
        """
        @ffi.callback("void(void* ,FfiResult*)")
        def _app_set_additional_search_path_o_cb(user_data ,result):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result)
    
    
        self.lib.safe_app.app_set_additional_search_path(new_path, user_data, _app_set_additional_search_path_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _app_free(self, app):
        """
            App*, [custom ffi lib]
            App* app
    
            > callback functions:
        """
        self.lib.safe_app.app_free(app)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _app_reset_object_cache(self, app, user_data, o_cb=None):
        """
            App*, [any], [function], [custom ffi lib]
            App* app, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result)
        """
        @ffi.callback("void(void* ,FfiResult*)")
        def _app_reset_object_cache_o_cb(user_data ,result):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result)
    
    
        self.lib.safe_app.app_reset_object_cache(app, user_data, _app_reset_object_cache_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _app_container_name(self, app_id, user_data, o_cb=None):
        """
            bytes, [any], [function], [custom ffi lib]
            char* app_id, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result, char* container_name)
        """
        @ffi.callback("void(void* ,FfiResult* ,char*)")
        def _app_container_name_o_cb(user_data ,result ,container_name):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result ,container_name)
    
    
        self.lib.safe_app.app_container_name(app_id, user_data, _app_container_name_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _encode_auth_req(self, req, user_data, o_cb=None):
        """
            AuthReq*, [any], [function], [custom ffi lib]
            AuthReq* req, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result, uint32_t req_id, char* encoded)
        """
        @ffi.callback("void(void* ,FfiResult* ,uint32_t ,char*)")
        def _encode_auth_req_o_cb(user_data ,result ,req_id ,encoded):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result ,req_id ,encoded)
    
    
        self.lib.safe_app.encode_auth_req(req, user_data, _encode_auth_req_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _encode_containers_req(self, req, user_data, o_cb=None):
        """
            ContainersReq*, [any], [function], [custom ffi lib]
            ContainersReq* req, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result, uint32_t req_id, char* encoded)
        """
        @ffi.callback("void(void* ,FfiResult* ,uint32_t ,char*)")
        def _encode_containers_req_o_cb(user_data ,result ,req_id ,encoded):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result ,req_id ,encoded)
    
    
        self.lib.safe_app.encode_containers_req(req, user_data, _encode_containers_req_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _encode_unregistered_req(self, extra_data, extra_data_len, user_data, o_cb=None):
        """
            uint8_t*, uintptr_t, [any], [function], [custom ffi lib]
            uint8_t* extra_data, uintptr_t extra_data_len, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result, uint32_t req_id, char* encoded)
        """
        @ffi.callback("void(void* ,FfiResult* ,uint32_t ,char*)")
        def _encode_unregistered_req_o_cb(user_data ,result ,req_id ,encoded):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result ,req_id ,encoded)
    
    
        self.lib.safe_app.encode_unregistered_req(extra_data, extra_data_len, user_data, _encode_unregistered_req_o_cb)
    
 
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _decode_ipc_msg(self, msg, user_data, o_auth=None, o_unregistered=None, o_containers=None, o_share_mdata=None, o_revoked=None, o_err=None):
        """
            bytes, [any], [function], [function], [function], [function], [function], [function], [custom ffi lib]
            char* msg, void* user_data
    
            > callback functions:
            (*o_auth)(void* user_data, uint32_t req_id, AuthGranted* auth_granted)
            (*o_unregistered)(void* user_data, uint32_t req_id, uint8_t* serialised_cfg, uintptr_t serialised_cfg_len)
            (*o_containers)(void* user_data, uint32_t req_id)
            (*o_share_mdata)(void* user_data, uint32_t req_id)
            (*o_revoked)(void* user_data)
            (*o_err)(void* user_data, FfiResult* result, uint32_t req_id)
        """
        @ffi.callback("void(void* ,uint32_t ,AuthGranted*)")
        def _decode_ipc_msg_o_auth(user_data ,req_id ,auth_granted):
            appQueue.put('gotResult')
            if o_auth:
                o_auth(user_data ,req_id ,auth_granted)
    
    
        @ffi.callback("void(void* ,uint32_t ,uint8_t* ,uintptr_t)")
        def _decode_ipc_msg_o_unregistered(user_data ,req_id ,serialised_cfg ,serialised_cfg_len):
            appQueue.put('gotResult')
            if o_unregistered:
                o_unregistered(user_data ,req_id ,serialised_cfg ,serialised_cfg_len)
    
    
        @ffi.callback("void(void* ,uint32_t)")
        def _decode_ipc_msg_o_containers(user_data ,req_id):
            appQueue.put('gotResult')
            if o_containers:
                o_containers(user_data ,req_id)
    
    
        @ffi.callback("void(void* ,uint32_t)")
        def _decode_ipc_msg_o_share_mdata(user_data ,req_id):
            appQueue.put('gotResult')
            if o_share_mdata:
                o_share_mdata(user_data ,req_id)
    
    
        @ffi.callback("void(void*)")
        def _decode_ipc_msg_o_revoked(user_data):
            appQueue.put('gotResult')
            if o_revoked:
                o_revoked(user_data)
    
    
        @ffi.callback("void(void* ,FfiResult* ,uint32_t)")
        def _decode_ipc_msg_o_err(user_data ,result ,req_id):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_err:
                o_err(user_data ,result ,req_id)
    
    
        self.lib.safe_app.decode_ipc_msg(msg, user_data, _decode_ipc_msg_o_auth, _decode_ipc_msg_o_unregistered, _decode_ipc_msg_o_containers, _decode_ipc_msg_o_share_mdata, _decode_ipc_msg_o_revoked, _decode_ipc_msg_o_err)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _access_container_refresh_access_info(self, app, user_data, o_cb=None):
        """
            App*, [any], [function], [custom ffi lib]
            App* app, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result)
        """
        @ffi.callback("void(void* ,FfiResult*)")
        def _access_container_refresh_access_info_o_cb(user_data ,result):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result)
    
    
        self.lib.safe_app.access_container_refresh_access_info(app, user_data, _access_container_refresh_access_info_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _access_container_fetch(self, app, user_data, o_cb=None):
        """
            App*, [any], [function], [custom ffi lib]
            App* app, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result, ContainerPermissions* container_perms, uintptr_t container_perms_len)
        """
        @ffi.callback("void(void* ,FfiResult* ,ContainerPermissions* ,uintptr_t)")
        def _access_container_fetch_o_cb(user_data ,result ,container_perms ,container_perms_len):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result ,container_perms ,container_perms_len)
    
    
        self.lib.safe_app.access_container_fetch(app, user_data, _access_container_fetch_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _access_container_get_container_mdata_info(self, app, name, user_data, o_cb=None):
        """
            App*, bytes, [any], [function], [custom ffi lib]
            App* app, char* name, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result, MDataInfo* mdata_info)
        """
        @ffi.callback("void(void* ,FfiResult* ,MDataInfo*)")
        def _access_container_get_container_mdata_info_o_cb(user_data ,result ,mdata_info):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result ,mdata_info)
    
    
        self.lib.safe_app.access_container_get_container_mdata_info(app, name, user_data, _access_container_get_container_mdata_info_o_cb)
    



    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _dir_fetch_file(self, app, parent_info, file_name, user_data, o_cb=None):
        """
            App*, MDataInfo*, bytes, [any], [function], [custom ffi lib]
            App* app, MDataInfo* parent_info, char* file_name, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result, File* file, uint64_t version)
        """
        @ffi.callback("void(void* ,FfiResult* ,File* ,uint64_t)")
        def _dir_fetch_file_o_cb(user_data ,result ,file ,version):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result ,file ,version)
    
    
        self.lib.safe_app.dir_fetch_file(app, parent_info, file_name, user_data, _dir_fetch_file_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _dir_insert_file(self, app, parent_info, file_name, file, user_data, o_cb=None):
        """
            App*, MDataInfo*, bytes, File*, [any], [function], [custom ffi lib]
            App* app, MDataInfo* parent_info, char* file_name, File* file, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result)
        """
        @ffi.callback("void(void* ,FfiResult*)")
        def _dir_insert_file_o_cb(user_data ,result):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result)
    
    
        self.lib.safe_app.dir_insert_file(app, parent_info, file_name, file, user_data, _dir_insert_file_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _dir_update_file(self, app, parent_info, file_name, file, version, user_data, o_cb=None):
        """
            App*, MDataInfo*, bytes, File*, uint64_t, [any], [function], [custom ffi lib]
            App* app, MDataInfo* parent_info, char* file_name, File* file, uint64_t version, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result, uint64_t new_version)
        """
        @ffi.callback("void(void* ,FfiResult* ,uint64_t)")
        def _dir_update_file_o_cb(user_data ,result ,new_version):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result ,new_version)
    
    
        self.lib.safe_app.dir_update_file(app, parent_info, file_name, file, version, user_data, _dir_update_file_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _dir_delete_file(self, app, parent_info, file_name, version, user_data, o_cb=None):
        """
            App*, MDataInfo*, bytes, uint64_t, [any], [function], [custom ffi lib]
            App* app, MDataInfo* parent_info, char* file_name, uint64_t version, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result, uint64_t new_version)
        """
        @ffi.callback("void(void* ,FfiResult* ,uint64_t)")
        def _dir_delete_file_o_cb(user_data ,result ,new_version):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result ,new_version)
    
    
        self.lib.safe_app.dir_delete_file(app, parent_info, file_name, version, user_data, _dir_delete_file_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _file_open(self, app, parent_info, file, open_mode, user_data, o_cb=None):
        """
            App*, MDataInfo*, File*, uint64_t, [any], [function], [custom ffi lib]
            App* app, MDataInfo* parent_info, File* file, uint64_t open_mode, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result, FileContextHandle file_h)
        """
        @ffi.callback("void(void* ,FfiResult* ,FileContextHandle)")
        def _file_open_o_cb(user_data ,result ,file_h):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result ,file_h)
    
    
        self.lib.safe_app.file_open(app, parent_info, file, open_mode, user_data, _file_open_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _file_size(self, app, file_h, user_data, o_cb=None):
        """
            App*, FileContextHandle, [any], [function], [custom ffi lib]
            App* app, FileContextHandle file_h, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result, uint64_t size)
        """
        @ffi.callback("void(void* ,FfiResult* ,uint64_t)")
        def _file_size_o_cb(user_data ,result ,size):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result ,size)
    
    
        self.lib.safe_app.file_size(app, file_h, user_data, _file_size_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _file_read(self, app, file_h, position, len, user_data, o_cb=None):
        """
            App*, FileContextHandle, uint64_t, uint64_t, [any], [function], [custom ffi lib]
            App* app, FileContextHandle file_h, uint64_t position, uint64_t len, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result, uint8_t* data, uintptr_t data_len)
        """
        @ffi.callback("void(void* ,FfiResult* ,uint8_t* ,uintptr_t)")
        def _file_read_o_cb(user_data ,result ,data ,data_len):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result ,data ,data_len)
    
    
        self.lib.safe_app.file_read(app, file_h, position, len, user_data, _file_read_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _file_write(self, app, file_h, data, data_len, user_data, o_cb=None):
        """
            App*, FileContextHandle, uint8_t*, uintptr_t, [any], [function], [custom ffi lib]
            App* app, FileContextHandle file_h, uint8_t* data, uintptr_t data_len, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result)
        """
        @ffi.callback("void(void* ,FfiResult*)")
        def _file_write_o_cb(user_data ,result):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result)
    
    
        self.lib.safe_app.file_write(app, file_h, data, data_len, user_data, _file_write_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _file_close(self, app, file_h, user_data, o_cb=None):
        """
            App*, FileContextHandle, [any], [function], [custom ffi lib]
            App* app, FileContextHandle file_h, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result, File* file)
        """
        @ffi.callback("void(void* ,FfiResult* ,File*)")
        def _file_close_o_cb(user_data ,result ,file):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result ,file)
    
    
        self.lib.safe_app.file_close(app, file_h, user_data, _file_close_o_cb)
    


    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _app_pub_sign_key(self, app, user_data, o_cb=None):
        """
            App*, [any], [function], [custom ffi lib]
            App* app, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result, SignPubKeyHandle handle)
        """
        @ffi.callback("void(void* ,FfiResult* ,SignPubKeyHandle)")
        def _app_pub_sign_key_o_cb(user_data ,result ,handle):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result ,handle)
    
    
        self.lib.safe_app.app_pub_sign_key(app, user_data, _app_pub_sign_key_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _sign_generate_key_pair(self, app, user_data, o_cb=None):
        """
            App*, [any], [function], [custom ffi lib]
            App* app, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result, SignPubKeyHandle public_key_h, SignSecKeyHandle secret_key_h)
        """
        @ffi.callback("void(void* ,FfiResult* ,SignPubKeyHandle ,SignSecKeyHandle)")
        def _sign_generate_key_pair_o_cb(user_data ,result ,public_key_h ,secret_key_h):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result ,public_key_h ,secret_key_h)
    
    
        self.lib.safe_app.sign_generate_key_pair(app, user_data, _sign_generate_key_pair_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _sign_pub_key_new(self, app, data, user_data, o_cb=None):
        """
            App*, SignPublicKey*, [any], [function], [custom ffi lib]
            App* app, SignPublicKey* data, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result, SignPubKeyHandle handle)
        """
        @ffi.callback("void(void* ,FfiResult* ,SignPubKeyHandle)")
        def _sign_pub_key_new_o_cb(user_data ,result ,handle):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result ,handle)
    
    
        self.lib.safe_app.sign_pub_key_new(app, data, user_data, _sign_pub_key_new_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _sign_pub_key_get(self, app, handle, user_data, o_cb=None):
        """
            App*, SignPubKeyHandle, [any], [function], [custom ffi lib]
            App* app, SignPubKeyHandle handle, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result, SignPublicKey* pub_sign_key)
        """
        @ffi.callback("void(void* ,FfiResult* ,SignPublicKey*)")
        def _sign_pub_key_get_o_cb(user_data ,result ,pub_sign_key):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result ,pub_sign_key)
    
    
        self.lib.safe_app.sign_pub_key_get(app, handle, user_data, _sign_pub_key_get_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _sign_pub_key_free(self, app, handle, user_data, o_cb=None):
        """
            App*, SignPubKeyHandle, [any], [function], [custom ffi lib]
            App* app, SignPubKeyHandle handle, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result)
        """
        @ffi.callback("void(void* ,FfiResult*)")
        def _sign_pub_key_free_o_cb(user_data ,result):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result)
    
    
        self.lib.safe_app.sign_pub_key_free(app, handle, user_data, _sign_pub_key_free_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _sign_sec_key_new(self, app, data, user_data, o_cb=None):
        """
            App*, SignSecretKey*, [any], [function], [custom ffi lib]
            App* app, SignSecretKey* data, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result, SignSecKeyHandle handle)
        """
        @ffi.callback("void(void* ,FfiResult* ,SignSecKeyHandle)")
        def _sign_sec_key_new_o_cb(user_data ,result ,handle):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result ,handle)
    
    
        self.lib.safe_app.sign_sec_key_new(app, data, user_data, _sign_sec_key_new_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _sign_sec_key_get(self, app, handle, user_data, o_cb=None):
        """
            App*, SignSecKeyHandle, [any], [function], [custom ffi lib]
            App* app, SignSecKeyHandle handle, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result, SignSecretKey* pub_sign_key)
        """
        @ffi.callback("void(void* ,FfiResult* ,SignSecretKey*)")
        def _sign_sec_key_get_o_cb(user_data ,result ,pub_sign_key):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result ,pub_sign_key)
    
    
        self.lib.safe_app.sign_sec_key_get(app, handle, user_data, _sign_sec_key_get_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _sign_sec_key_free(self, app, handle, user_data, o_cb=None):
        """
            App*, SignSecKeyHandle, [any], [function], [custom ffi lib]
            App* app, SignSecKeyHandle handle, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result)
        """
        @ffi.callback("void(void* ,FfiResult*)")
        def _sign_sec_key_free_o_cb(user_data ,result):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result)
    
    
        self.lib.safe_app.sign_sec_key_free(app, handle, user_data, _sign_sec_key_free_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _app_pub_enc_key(self, app, user_data, o_cb=None):
        """
            App*, [any], [function], [custom ffi lib]
            App* app, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result, EncryptPubKeyHandle public_key_h)
        """
        @ffi.callback("void(void* ,FfiResult* ,EncryptPubKeyHandle)")
        def _app_pub_enc_key_o_cb(user_data ,result ,public_key_h):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result ,public_key_h)
    
    
        self.lib.safe_app.app_pub_enc_key(app, user_data, _app_pub_enc_key_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _enc_generate_key_pair(self, app, user_data, o_cb=None):
        """
            App*, [any], [function], [custom ffi lib]
            App* app, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result, EncryptPubKeyHandle public_key_h, EncryptSecKeyHandle secret_key_h)
        """
        @ffi.callback("void(void* ,FfiResult* ,EncryptPubKeyHandle ,EncryptSecKeyHandle)")
        def _enc_generate_key_pair_o_cb(user_data ,result ,public_key_h ,secret_key_h):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result ,public_key_h ,secret_key_h)
    
    
        self.lib.safe_app.enc_generate_key_pair(app, user_data, _enc_generate_key_pair_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _enc_pub_key_new(self, app, data, user_data, o_cb=None):
        """
            App*, AsymPublicKey*, [any], [function], [custom ffi lib]
            App* app, AsymPublicKey* data, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result, EncryptPubKeyHandle public_key_h)
        """
        @ffi.callback("void(void* ,FfiResult* ,EncryptPubKeyHandle)")
        def _enc_pub_key_new_o_cb(user_data ,result ,public_key_h):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result ,public_key_h)
    
    
        self.lib.safe_app.enc_pub_key_new(app, data, user_data, _enc_pub_key_new_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _enc_pub_key_get(self, app, handle, user_data, o_cb=None):
        """
            App*, EncryptPubKeyHandle, [any], [function], [custom ffi lib]
            App* app, EncryptPubKeyHandle handle, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result, AsymPublicKey* pub_enc_key)
        """
        @ffi.callback("void(void* ,FfiResult* ,AsymPublicKey*)")
        def _enc_pub_key_get_o_cb(user_data ,result ,pub_enc_key):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result ,pub_enc_key)
    
    
        self.lib.safe_app.enc_pub_key_get(app, handle, user_data, _enc_pub_key_get_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _enc_pub_key_free(self, app, handle, user_data, o_cb=None):
        """
            App*, EncryptPubKeyHandle, [any], [function], [custom ffi lib]
            App* app, EncryptPubKeyHandle handle, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result)
        """
        @ffi.callback("void(void* ,FfiResult*)")
        def _enc_pub_key_free_o_cb(user_data ,result):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result)
    
    
        self.lib.safe_app.enc_pub_key_free(app, handle, user_data, _enc_pub_key_free_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _enc_secret_key_new(self, app, data, user_data, o_cb=None):
        """
            App*, AsymSecretKey*, [any], [function], [custom ffi lib]
            App* app, AsymSecretKey* data, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result, EncryptSecKeyHandle sk_h)
        """
        @ffi.callback("void(void* ,FfiResult* ,EncryptSecKeyHandle)")
        def _enc_secret_key_new_o_cb(user_data ,result ,sk_h):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result ,sk_h)
    
    
        self.lib.safe_app.enc_secret_key_new(app, data, user_data, _enc_secret_key_new_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _enc_secret_key_get(self, app, handle, user_data, o_cb=None):
        """
            App*, EncryptSecKeyHandle, [any], [function], [custom ffi lib]
            App* app, EncryptSecKeyHandle handle, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result, AsymSecretKey* sec_enc_key)
        """
        @ffi.callback("void(void* ,FfiResult* ,AsymSecretKey*)")
        def _enc_secret_key_get_o_cb(user_data ,result ,sec_enc_key):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result ,sec_enc_key)
    
    
        self.lib.safe_app.enc_secret_key_get(app, handle, user_data, _enc_secret_key_get_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _enc_secret_key_free(self, app, handle, user_data, o_cb=None):
        """
            App*, EncryptSecKeyHandle, [any], [function], [custom ffi lib]
            App* app, EncryptSecKeyHandle handle, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result)
        """
        @ffi.callback("void(void* ,FfiResult*)")
        def _enc_secret_key_free_o_cb(user_data ,result):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result)
    
    
        self.lib.safe_app.enc_secret_key_free(app, handle, user_data, _enc_secret_key_free_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _sign(self, app, data, data_len, sign_sk_h, user_data, o_cb=None):
        """
            App*, uint8_t*, uintptr_t, SignSecKeyHandle, [any], [function], [custom ffi lib]
            App* app, uint8_t* data, uintptr_t data_len, SignSecKeyHandle sign_sk_h, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result, uint8_t* signed_data, uintptr_t signed_data_len)
        """
        @ffi.callback("void(void* ,FfiResult* ,uint8_t* ,uintptr_t)")
        def _sign_o_cb(user_data ,result ,signed_data ,signed_data_len):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result ,signed_data ,signed_data_len)
    
    
        self.lib.safe_app.sign(app, data, data_len, sign_sk_h, user_data, _sign_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _verify(self, app, signed_data, signed_data_len, sign_pk_h, user_data, o_cb=None):
        """
            App*, uint8_t*, uintptr_t, SignPubKeyHandle, [any], [function], [custom ffi lib]
            App* app, uint8_t* signed_data, uintptr_t signed_data_len, SignPubKeyHandle sign_pk_h, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result, uint8_t* verified_data, uintptr_t verified_data_len)
        """
        @ffi.callback("void(void* ,FfiResult* ,uint8_t* ,uintptr_t)")
        def _verify_o_cb(user_data ,result ,verified_data ,verified_data_len):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result ,verified_data ,verified_data_len)
    
    
        self.lib.safe_app.verify(app, signed_data, signed_data_len, sign_pk_h, user_data, _verify_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _encrypt(self, app, data, data_len, public_key_h, secret_key_h, user_data, o_cb=None):
        """
            App*, uint8_t*, uintptr_t, EncryptPubKeyHandle, EncryptSecKeyHandle, [any], [function], [custom ffi lib]
            App* app, uint8_t* data, uintptr_t data_len, EncryptPubKeyHandle public_key_h, EncryptSecKeyHandle secret_key_h, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result, uint8_t* ciphertext, uintptr_t ciphertext_len)
        """
        @ffi.callback("void(void* ,FfiResult* ,uint8_t* ,uintptr_t)")
        def _encrypt_o_cb(user_data ,result ,ciphertext ,ciphertext_len):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result ,ciphertext ,ciphertext_len)
    
    
        self.lib.safe_app.encrypt(app, data, data_len, public_key_h, secret_key_h, user_data, _encrypt_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _decrypt(self, app, data, data_len, public_key_h, secret_key_h, user_data, o_cb=None):
        """
            App*, uint8_t*, uintptr_t, EncryptPubKeyHandle, EncryptSecKeyHandle, [any], [function], [custom ffi lib]
            App* app, uint8_t* data, uintptr_t data_len, EncryptPubKeyHandle public_key_h, EncryptSecKeyHandle secret_key_h, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result, uint8_t* plaintext, uintptr_t plaintext_len)
        """
        @ffi.callback("void(void* ,FfiResult* ,uint8_t* ,uintptr_t)")
        def _decrypt_o_cb(user_data ,result ,plaintext ,plaintext_len):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result ,plaintext ,plaintext_len)
    
    
        self.lib.safe_app.decrypt(app, data, data_len, public_key_h, secret_key_h, user_data, _decrypt_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _encrypt_sealed_box(self, app, data, data_len, public_key_h, user_data, o_cb=None):
        """
            App*, uint8_t*, uintptr_t, EncryptPubKeyHandle, [any], [function], [custom ffi lib]
            App* app, uint8_t* data, uintptr_t data_len, EncryptPubKeyHandle public_key_h, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result, uint8_t* ciphertext, uintptr_t ciphertext_len)
        """
        @ffi.callback("void(void* ,FfiResult* ,uint8_t* ,uintptr_t)")
        def _encrypt_sealed_box_o_cb(user_data ,result ,ciphertext ,ciphertext_len):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result ,ciphertext ,ciphertext_len)
    
    
        self.lib.safe_app.encrypt_sealed_box(app, data, data_len, public_key_h, user_data, _encrypt_sealed_box_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _decrypt_sealed_box(self, app, data, data_len, public_key_h, secret_key_h, user_data, o_cb=None):
        """
            App*, uint8_t*, uintptr_t, EncryptPubKeyHandle, EncryptSecKeyHandle, [any], [function], [custom ffi lib]
            App* app, uint8_t* data, uintptr_t data_len, EncryptPubKeyHandle public_key_h, EncryptSecKeyHandle secret_key_h, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result, uint8_t* plaintext, uintptr_t plaintext_len)
        """
        @ffi.callback("void(void* ,FfiResult* ,uint8_t* ,uintptr_t)")
        def _decrypt_sealed_box_o_cb(user_data ,result ,plaintext ,plaintext_len):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result ,plaintext ,plaintext_len)
    
    
        self.lib.safe_app.decrypt_sealed_box(app, data, data_len, public_key_h, secret_key_h, user_data, _decrypt_sealed_box_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _sha3_hash(self, data, data_len, user_data, o_cb=None):
        """
            uint8_t*, uintptr_t, [any], [function], [custom ffi lib]
            uint8_t* data, uintptr_t data_len, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result, uint8_t* hash, uintptr_t hash_len)
        """
        @ffi.callback("void(void* ,FfiResult* ,uint8_t* ,uintptr_t)")
        def _sha3_hash_o_cb(user_data ,result ,hash ,hash_len):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result ,hash ,hash_len)
    
    
        self.lib.safe_app.sha3_hash(data, data_len, user_data, _sha3_hash_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _generate_nonce(self, user_data, o_cb=None):
        """
            [any], [function], [custom ffi lib]
            void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result, AsymNonce* nonce)
        """
        @ffi.callback("void(void* ,FfiResult* ,AsymNonce*)")
        def _generate_nonce_o_cb(user_data ,result ,nonce):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result ,nonce)
    
    
        self.lib.safe_app.generate_nonce(user_data, _generate_nonce_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _cipher_opt_new_plaintext(self, app, user_data, o_cb=None):
        """
            App*, [any], [function], [custom ffi lib]
            App* app, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result, CipherOptHandle handle)
        """
        @ffi.callback("void(void* ,FfiResult* ,CipherOptHandle)")
        def _cipher_opt_new_plaintext_o_cb(user_data ,result ,handle):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result ,handle)
    
    
        self.lib.safe_app.cipher_opt_new_plaintext(app, user_data, _cipher_opt_new_plaintext_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _cipher_opt_new_symmetric(self, app, user_data, o_cb=None):
        """
            App*, [any], [function], [custom ffi lib]
            App* app, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result, CipherOptHandle handle)
        """
        @ffi.callback("void(void* ,FfiResult* ,CipherOptHandle)")
        def _cipher_opt_new_symmetric_o_cb(user_data ,result ,handle):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result ,handle)
    
    
        self.lib.safe_app.cipher_opt_new_symmetric(app, user_data, _cipher_opt_new_symmetric_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _cipher_opt_new_asymmetric(self, app, peer_encrypt_key_h, user_data, o_cb=None):
        """
            App*, EncryptPubKeyHandle, [any], [function], [custom ffi lib]
            App* app, EncryptPubKeyHandle peer_encrypt_key_h, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result, CipherOptHandle handle)
        """
        @ffi.callback("void(void* ,FfiResult* ,CipherOptHandle)")
        def _cipher_opt_new_asymmetric_o_cb(user_data ,result ,handle):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result ,handle)
    
    
        self.lib.safe_app.cipher_opt_new_asymmetric(app, peer_encrypt_key_h, user_data, _cipher_opt_new_asymmetric_o_cb)
    
    
    
    @safeUtils.safeThread(timeout=5,queue=appQueue)
    def _cipher_opt_free(self, app, handle, user_data, o_cb=None):
        """
            App*, CipherOptHandle, [any], [function], [custom ffi lib]
            App* app, CipherOptHandle handle, void* user_data
    
            > callback functions:
            (*o_cb)(void* user_data, FfiResult* result)
        """
        @ffi.callback("void(void* ,FfiResult*)")
        def _cipher_opt_free_o_cb(user_data ,result):
            self.safeUtils.checkResult(result)
            appQueue.put('gotResult')
            if o_cb:
                o_cb(user_data ,result)
    
    
        self.lib.safe_app.cipher_opt_free(app, handle, user_data, _cipher_opt_free_o_cb)
    
