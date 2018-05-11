void app_init_logging(char* output_file_name_override, void* user_data, void (*o_cb)(void* user_data, FfiResult* result));
void app_output_log_path(char* output_file_name, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, char* log_path));
void app_pub_sign_key(App* app, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, SignPubKeyHandle handle));
void sign_generate_key_pair(App* app, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, SignPubKeyHandle pk_h, SignSecKeyHandle sk_h));
void sign_pub_key_new(App* app, SignPublicKey* data, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, SignPubKeyHandle handle));
void sign_pub_key_get(App* app, SignPubKeyHandle handle, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, SignPublicKey* pub_sign_key));
void sign_pub_key_free(App* app, SignPubKeyHandle handle, void* user_data, void (*o_cb)(void* user_data, FfiResult* result));
void sign_sec_key_new(App* app, SignSecretKey* data, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, SignSecKeyHandle handle));
void sign_sec_key_get(App* app, SignSecKeyHandle handle, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, SignSecretKey* pub_sign_key));
void sign_sec_key_free(App* app, SignSecKeyHandle handle, void* user_data, void (*o_cb)(void* user_data, FfiResult* result));
void app_pub_enc_key(App* app, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, EncryptPubKeyHandle pk_h));
void enc_generate_key_pair(App* app, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, EncryptPubKeyHandle pk_h, EncryptSecKeyHandle sk_h));
void enc_pub_key_new(App* app, AsymPublicKey* data, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, EncryptPubKeyHandle pk_h));
void enc_pub_key_get(App* app, EncryptPubKeyHandle handle, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, AsymPublicKey* pub_enc_key));
void enc_pub_key_free(App* app, EncryptPubKeyHandle handle, void* user_data, void (*o_cb)(void* user_data, FfiResult* result));
void enc_secret_key_new(App* app, AsymSecretKey* data, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, EncryptSecKeyHandle sk_h));
void enc_secret_key_get(App* app, EncryptSecKeyHandle handle, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, AsymSecretKey* sec_enc_key));
void enc_secret_key_free(App* app, EncryptSecKeyHandle handle, void* user_data, void (*o_cb)(void* user_data, FfiResult* result));
void sign(App* app, uint8_t* data, uintptr_t data_len, SignSecKeyHandle sign_sk_h, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, uint8_t* signed_data, uintptr_t signed_data_len));
void verify(App* app, uint8_t* signed_data, uintptr_t signed_data_len, SignPubKeyHandle sign_pk_h, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, uint8_t* verified_data, uintptr_t verified_data_len));
void encrypt(App* app, uint8_t* data, uintptr_t data_len, EncryptPubKeyHandle pk_h, EncryptSecKeyHandle sk_h, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, uint8_t* ciphertext, uintptr_t ciphertext_len));
void decrypt(App* app, uint8_t* data, uintptr_t data_len, EncryptPubKeyHandle pk_h, EncryptSecKeyHandle sk_h, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, uint8_t* plaintext, uintptr_t plaintext_len));
void encrypt_sealed_box(App* app, uint8_t* data, uintptr_t data_len, EncryptPubKeyHandle pk_h, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, uint8_t* ciphertext, uintptr_t ciphertext_len));
void decrypt_sealed_box(App* app, uint8_t* data, uintptr_t data_len, EncryptPubKeyHandle pk_h, EncryptSecKeyHandle sk_h, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, uint8_t* plaintext, uintptr_t plaintext_len));
void sha3_hash(uint8_t* data, uintptr_t data_len, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, uint8_t* hash, uintptr_t hash_len));
void generate_nonce(void* user_data, void (*o_cb)(void* user_data, FfiResult* result, AsymNonce* nonce));
void idata_new_self_encryptor(App* app, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, SEWriterHandle se_h));
void idata_write_to_self_encryptor(App* app, SEWriterHandle se_h, uint8_t* data, uintptr_t data_len, void* user_data, void (*o_cb)(void* user_data, FfiResult* result));
void idata_close_self_encryptor(App* app, SEWriterHandle se_h, CipherOptHandle cipher_opt_h, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, XorNameArray* name));
void idata_fetch_self_encryptor(App* app, XorNameArray* name, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, SEReaderHandle se_h));
void idata_serialised_size(App* app, XorNameArray* name, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, uint64_t serialised_size));
void idata_size(App* app, SEReaderHandle se_h, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, uint64_t size));
void idata_read_from_self_encryptor(App* app, SEReaderHandle se_h, uint64_t from_pos, uint64_t len, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, uint8_t* data, uintptr_t data_len));
void idata_self_encryptor_writer_free(App* app, SEWriterHandle handle, void* user_data, void (*o_cb)(void* user_data, FfiResult* result));
void idata_self_encryptor_reader_free(App* app, SEReaderHandle handle, void* user_data, void (*o_cb)(void* user_data, FfiResult* result));
void cipher_opt_new_plaintext(App* app, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, CipherOptHandle handle));
void cipher_opt_new_symmetric(App* app, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, CipherOptHandle handle));
void cipher_opt_new_asymmetric(App* app, EncryptPubKeyHandle peer_encrypt_key_h, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, CipherOptHandle handle));
void cipher_opt_free(App* app, CipherOptHandle handle, void* user_data, void (*o_cb)(void* user_data, FfiResult* result));
void mdata_entry_actions_new(App* app, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, MDataEntryActionsHandle entry_actions_h));
void mdata_entry_actions_insert(App* app, MDataEntryActionsHandle actions_h, uint8_t* key, uintptr_t key_len, uint8_t* value, uintptr_t value_len, void* user_data, void (*o_cb)(void* user_data, FfiResult* result));
void mdata_entry_actions_update(App* app, MDataEntryActionsHandle actions_h, uint8_t* key, uintptr_t key_len, uint8_t* value, uintptr_t value_len, uint64_t entry_version, void* user_data, void (*o_cb)(void* user_data, FfiResult* result));
void mdata_entry_actions_delete(App* app, MDataEntryActionsHandle actions_h, uint8_t* key, uintptr_t key_len, uint64_t entry_version, void* user_data, void (*o_cb)(void* user_data, FfiResult* result));
void mdata_entry_actions_free(App* app, MDataEntryActionsHandle actions_h, void* user_data, void (*o_cb)(void* user_data, FfiResult* result));
void test_create_app(char* app_id, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, App* app));
void test_create_app_with_access(AuthReq* auth_req, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, App* o_app));
void test_simulate_network_disconnect(App* app, void* user_data, void (*o_cb)(void* user_data, FfiResult* result));
void mdata_permissions_new(App* app, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, MDataPermissionsHandle perm_h));
void mdata_permissions_len(App* app, MDataPermissionsHandle permissions_h, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, uintptr_t size));
void mdata_permissions_get(App* app, MDataPermissionsHandle permissions_h, SignPubKeyHandle user_h, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, PermissionSet* perm_set));
void mdata_list_permission_sets(App* app, MDataPermissionsHandle permissions_h, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, UserPermissionSet* user_perm_sets, uintptr_t user_perm_sets_len));
void mdata_permissions_insert(App* app, MDataPermissionsHandle permissions_h, SignPubKeyHandle user_h, PermissionSet* permission_set, void* user_data, void (*o_cb)(void* user_data, FfiResult* result));
void mdata_permissions_free(App* app, MDataPermissionsHandle permissions_h, void* user_data, void (*o_cb)(void* user_data, FfiResult* result));
void mdata_info_new_private(XorNameArray* name, uint64_t type_tag, SymSecretKey* secret_key, SymNonce* nonce, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, MDataInfo* mdata_info));
void mdata_info_random_public(uint64_t type_tag, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, MDataInfo* mdata_info));
void mdata_info_random_private(uint64_t type_tag, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, MDataInfo* mdata_info));
void mdata_info_encrypt_entry_key(MDataInfo* info, uint8_t* input, uintptr_t input_len, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, uint8_t* enc_entry_key, uintptr_t enc_entry_key_len));
void mdata_info_encrypt_entry_value(MDataInfo* info, uint8_t* input, uintptr_t input_len, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, uint8_t* enc_entry_value, uintptr_t enc_entry_value_len));
void mdata_info_decrypt(MDataInfo* info, uint8_t* input, uintptr_t input_len, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, uint8_t* mdata_info_decrypt, uintptr_t mdata_info_decrypt_len));
void mdata_info_serialise(MDataInfo* info, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, uint8_t* encoded, uintptr_t encoded_len));
void mdata_info_deserialise(uint8_t* encoded_ptr, uintptr_t encoded_len, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, MDataInfo* mdata_info));
void mdata_encode_metadata(MetadataResponse* metadata, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, uint8_t* encoded, uintptr_t encoded_len));
void encode_auth_req(AuthReq* req, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, uint32_t req_id, char* encoded));
void encode_containers_req(ContainersReq* req, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, uint32_t req_id, char* encoded));
void encode_unregistered_req(uint8_t* extra_data, uintptr_t extra_data_len, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, uint32_t req_id, char* encoded));
void encode_share_mdata_req(ShareMDataReq* req, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, uint32_t req_id, char* encoded));
void decode_ipc_msg(char* msg, void* user_data, void (*o_auth)(void* user_data, uint32_t req_id, AuthGranted* auth_granted), void (*o_unregistered)(void* user_data, uint32_t req_id, uint8_t* serialised_cfg, uintptr_t serialised_cfg_len), void (*o_containers)(void* user_data, uint32_t req_id), void (*o_share_mdata)(void* user_data, uint32_t req_id), void (*o_revoked)(void* user_data), void (*o_err)(void* user_data, FfiResult* result, uint32_t req_id));
void mdata_entries_new(App* app, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, MDataEntriesHandle entries_h));
void mdata_entries_insert(App* app, MDataEntriesHandle entries_h, uint8_t* key, uintptr_t key_len, uint8_t* value, uintptr_t value_len, void* user_data, void (*o_cb)(void* user_data, FfiResult* result));
void mdata_entries_len(App* app, MDataEntriesHandle entries_h, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, uintptr_t len));
void mdata_entries_get(App* app, MDataEntriesHandle entries_h, uint8_t* key, uintptr_t key_len, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, uint8_t* content, uintptr_t content_len, uint64_t version));
void mdata_list_entries(App* app, MDataEntriesHandle entries_h, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, MDataEntry* entries, uintptr_t entries_len));
void mdata_entries_free(App* app, MDataEntriesHandle entries_h, void* user_data, void (*o_cb)(void* user_data, FfiResult* result));
void app_unregistered(uint8_t* bootstrap_config, uintptr_t bootstrap_config_len, void* user_data, void (*o_disconnect_notifier_cb)(void* user_data), void (*o_cb)(void* user_data, FfiResult* result, App* app));
void app_registered(char* app_id, AuthGranted* auth_granted, void* user_data, void (*o_disconnect_notifier_cb)(void* user_data), void (*o_cb)(void* user_data, FfiResult* result, App* app));
void app_reconnect(App* app, void* user_data, void (*o_cb)(void* user_data, FfiResult* result));
void app_account_info(App* app, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, AccountInfo* account_info));
void app_exe_file_stem(void* user_data, void (*o_cb)(void* user_data, FfiResult* result, char* filename));
void app_set_additional_search_path(char* new_path, void* user_data, void (*o_cb)(void* user_data, FfiResult* result));
void app_free(App* app);
void app_reset_object_cache(App* app, void* user_data, void (*o_cb)(void* user_data, FfiResult* result));
void app_container_name(char* app_id, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, char* container_name));
void mdata_put(App* app, MDataInfo* info, MDataPermissionsHandle permissions_h, MDataEntriesHandle entries_h, void* user_data, void (*o_cb)(void* user_data, FfiResult* result));
void mdata_get_version(App* app, MDataInfo* info, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, uint64_t version));
void mdata_serialised_size(App* app, MDataInfo* info, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, uint64_t serialised_size));
void mdata_get_value(App* app, MDataInfo* info, uint8_t* key, uintptr_t key_len, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, uint8_t* content, uintptr_t content_len, uint64_t version));
void mdata_entries(App* app, MDataInfo* info, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, MDataEntriesHandle entries_h));
void mdata_list_keys(App* app, MDataInfo* info, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, MDataKey* keys, uintptr_t keys_len));
void mdata_list_values(App* app, MDataInfo* info, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, MDataValue* values, uintptr_t values_len));
void mdata_mutate_entries(App* app, MDataInfo* info, MDataEntryActionsHandle actions_h, void* user_data, void (*o_cb)(void* user_data, FfiResult* result));
void mdata_list_permissions(App* app, MDataInfo* info, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, MDataPermissionsHandle perm_h));
void mdata_list_user_permissions(App* app, MDataInfo* info, SignPubKeyHandle user_h, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, PermissionSet* perm_set));
void mdata_set_user_permissions(App* app, MDataInfo* info, SignPubKeyHandle user_h, PermissionSet* permission_set, uint64_t version, void* user_data, void (*o_cb)(void* user_data, FfiResult* result));
void mdata_del_user_permissions(App* app, MDataInfo* info, SignPubKeyHandle user_h, uint64_t version, void* user_data, void (*o_cb)(void* user_data, FfiResult* result));
void dir_fetch_file(App* app, MDataInfo* parent_info, char* file_name, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, File* file, uint64_t version));
void dir_insert_file(App* app, MDataInfo* parent_info, char* file_name, File* file, void* user_data, void (*o_cb)(void* user_data, FfiResult* result));
void dir_update_file(App* app, MDataInfo* parent_info, char* file_name, File* file, uint64_t version, void* user_data, void (*o_cb)(void* user_data, FfiResult* result));
void dir_delete_file(App* app, MDataInfo* parent_info, char* file_name, uint64_t version, void* user_data, void (*o_cb)(void* user_data, FfiResult* result));
void file_open(App* app, MDataInfo* parent_info, File* file, uint64_t open_mode, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, FileContextHandle file_h));
void file_size(App* app, FileContextHandle file_h, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, uint64_t size));
void file_read(App* app, FileContextHandle file_h, uint64_t position, uint64_t len, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, uint8_t* data, uintptr_t data_len));
void file_write(App* app, FileContextHandle file_h, uint8_t* data, uintptr_t data_len, void* user_data, void (*o_cb)(void* user_data, FfiResult* result));
void file_close(App* app, FileContextHandle file_h, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, File* file));
void access_container_refresh_access_info(App* app, void* user_data, void (*o_cb)(void* user_data, FfiResult* result));
void access_container_fetch(App* app, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, ContainerPermissions* container_perms, uintptr_t container_perms_len));
void access_container_get_container_mdata_info(App* app, char* name, void* user_data, void (*o_cb)(void* user_data, FfiResult* result, MDataInfo* mdata_info));
