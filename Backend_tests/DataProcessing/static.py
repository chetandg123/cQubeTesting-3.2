import time
import unittest

from reuse_func import GetData

# class DistrictMaster(unittest.TestCase):
#
#     def setUp(self):
#         self.processor_name="static_data_transformer"
#         self.folder_name="district_master"
#         self.cQube_data_storage = "cQube_data_storage"
#         self.cal = GetData()
#         self.storage_type = self.cal.get_storage_type()
#         self.cal.start_nifi_processor("cQube_data_storage")
#         self.cal.start_nifi_processor(self.processor_name)
#         self.filepath = self.cal.get_filepath(self.folder_name)
#
#     def test_district_master(self):
#         if self.storage_type == "s3":
#             result = self.cal.copy_file_to_s3(self.filepath, self.folder_name)
#             time.sleep(10)
#             if result.returncode == 0:
#                 print(self.folder_name.capitalize()+" file is successfully uploaded to s3")
#                 while 1 :
#                     if self.cal.get_queued_count(self.processor_name) == 0 and self.cal.get_queued_count(self.cQube_data_storage) == 0 and len(self.cal.get_processor_group_error_msg(self.processor_name)) == 0:
#                         print(self.folder_name.capitalize()+" file is successfully processed")
#                         self.assertTrue(0 == 0,self.folder_name.capitalize()+" file is successfully processed")
#                         break
#                     elif len(self.cal.get_processor_group_error_msg(self.processor_name)) != 0:
#                         self.assertEqual(0,len(self.cal.get_processor_group_error_msg(self.processor_name)),self.cal.get_processor_group_error_msg(self.processor_name)[0])
#                         break
#                     elif self.cal.get_queued_count(self.processor_name) != 0 and self.cal.get_queued_count(self.cQube_data_storage) != 0:
#                         time.sleep(2)
#             else:
#                 print(self.folder_name.capitalize()+" file is not uploaded to s3")
#         else:
#             dir_created_result, file_copied_result = self.cal.copy_file_to_local(self.filepath, self.folder_name)
#             time.sleep(5)
#             if dir_created_result.returncode == 0 or dir_created_result.returncode == 1:
#                 print(self.folder_name.capitalize() + " folder is successfully created in emission directory")
#                 if file_copied_result.returncode == 0:
#                     print(self.folder_name.capitalize() + " file is successfully copied in emission directory of "+self.folder_name)
#                     while 1:
#                         if self.cal.get_queued_count(self.processor_name) == 0 and self.cal.get_queued_count(self.cQube_data_storage) == 0 and len(self.cal.get_processor_group_error_msg(self.processor_name)) == 0:
#                             print(self.folder_name.capitalize() + " file is successfully processed")
#                             self.assertTrue(0 == 0, self.folder_name.capitalize() + " file is successfully processed")
#                             break
#                         elif len(self.cal.get_processor_group_error_msg(self.processor_name)) != 0:
#                             self.assertEqual(0, len(self.cal.get_processor_group_error_msg(self.processor_name)),
#                                              self.cal.get_processor_group_error_msg(self.processor_name)[0])
#                             break
#                         elif self.cal.get_queued_count(self.processor_name) != 0 and self.cal.get_queued_count(self.cQube_data_storage) != 0:
#                             time.sleep(2)
#                 else:
#                     print(self.folder_name.capitalize() + " file is not copied in emission directory of " + self.folder_name)
#
#             else:
#                 print(self.folder_name.capitalize() + " folder is not created in emission directory")
#
#
#     def tearDown(self):
#         self.cal.stop_nifi_processor(self.processor_name)

# class BlockMaster(unittest.TestCase):
#
#     def setUp(self):
#         self.processor_name="static_data_transformer"
#         self.folder_name="block_master"
#         self.cQube_data_storage = "cQube_data_storage"
#         self.cal = GetData()
#         self.storage_type = self.cal.get_storage_type()
#         self.cal.start_nifi_processor("cQube_data_storage")
#         self.cal.start_nifi_processor(self.processor_name)
#         self.filepath = self.cal.get_filepath(self.folder_name)
#
#     def test_block_master(self):
#         if self.storage_type == "s3":
#             result = self.cal.copy_file_to_s3(self.filepath, self.folder_name)
#             time.sleep(10)
#             if result.returncode == 0:
#                 print(self.folder_name.capitalize()+" file is successfully uploaded to s3")
#                 while 1 :
#                     if self.cal.get_queued_count(self.processor_name) == 0 and self.cal.get_queued_count(self.cQube_data_storage) == 0 and len(self.cal.get_processor_group_error_msg(self.processor_name)) == 0:
#                         print(self.folder_name.capitalize()+" file is successfully processed")
#                         self.assertTrue(0 == 0,self.folder_name.capitalize()+" file is successfully processed")
#                         break
#                     elif len(self.cal.get_processor_group_error_msg(self.processor_name)) != 0:
#                         self.assertEqual(0,len(self.cal.get_processor_group_error_msg(self.processor_name)),self.cal.get_processor_group_error_msg(self.processor_name)[0])
#                         break
#                     elif self.cal.get_queued_count(self.processor_name) != 0 and self.cal.get_queued_count(self.cQube_data_storage) != 0:
#                         time.sleep(2)
#             else:
#                 print(self.folder_name.capitalize()+" file is not uploaded to s3")
#         else:
#             dir_created_result, file_copied_result = self.cal.copy_file_to_local(self.filepath, self.folder_name)
#             time.sleep(5)
#             if dir_created_result.returncode == 0 or dir_created_result.returncode == 1:
#                 print(self.folder_name.capitalize() + " folder is successfully created in emission directory")
#                 if file_copied_result.returncode == 0:
#                     print(self.folder_name.capitalize() + " file is successfully copied in emission directory of "+self.folder_name)
#                     while 1:
#                         if self.cal.get_queued_count(self.processor_name) == 0 and self.cal.get_queued_count(self.cQube_data_storage) == 0 and len(self.cal.get_processor_group_error_msg(self.processor_name)) == 0:
#                             print(self.folder_name.capitalize() + " file is successfully processed")
#                             self.assertTrue(0 == 0, self.folder_name.capitalize() + " file is successfully processed")
#                             break
#                         elif len(self.cal.get_processor_group_error_msg(self.processor_name)) != 0:
#                             self.assertEqual(0, len(self.cal.get_processor_group_error_msg(self.processor_name)),
#                                              self.cal.get_processor_group_error_msg(self.processor_name)[0])
#                             break
#                         elif self.cal.get_queued_count(self.processor_name) != 0 and self.cal.get_queued_count(self.cQube_data_storage) != 0:
#                             time.sleep(2)
#                 else:
#                     print(self.folder_name.capitalize() + " file is not copied in emission directory of " + self.folder_name)
#
#             else:
#                 print(self.folder_name.capitalize() + " folder is not created in emission directory")
#
#
#     def tearDown(self):
#         self.cal.stop_nifi_processor(self.processor_name)
#
# class ClusterMaster(unittest.TestCase):
#
#     def setUp(self):
#         self.processor_name="static_data_transformer"
#         self.folder_name="cluster_master"
#         self.cQube_data_storage = "cQube_data_storage"
#         self.cal = GetData()
#         self.storage_type = self.cal.get_storage_type()
#         self.cal.start_nifi_processor("cQube_data_storage")
#         self.cal.start_nifi_processor(self.processor_name)
#         self.filepath = self.cal.get_filepath(self.folder_name)
#
#     def test_cluster_master(self):
#         if self.storage_type == "s3":
#             result = self.cal.copy_file_to_s3(self.filepath, self.folder_name)
#             time.sleep(10)
#             if result.returncode == 0:
#                 print(self.folder_name.capitalize()+" file is successfully uploaded to s3")
#                 while 1 :
#                     if self.cal.get_queued_count(self.processor_name) == 0 and self.cal.get_queued_count(self.cQube_data_storage) == 0 and len(self.cal.get_processor_group_error_msg(self.processor_name)) == 0:
#                         print(self.folder_name.capitalize()+" file is successfully processed")
#                         self.assertTrue(0 == 0,self.folder_name.capitalize()+" file is successfully processed")
#                         break
#                     elif len(self.cal.get_processor_group_error_msg(self.processor_name)) != 0:
#                         self.assertEqual(0,len(self.cal.get_processor_group_error_msg(self.processor_name)),self.cal.get_processor_group_error_msg(self.processor_name)[0])
#                         break
#                     elif self.cal.get_queued_count(self.processor_name) != 0 and self.cal.get_queued_count(self.cQube_data_storage) != 0:
#                         time.sleep(2)
#             else:
#                 print(self.folder_name.capitalize()+" file is not uploaded to s3")
#         else:
#             dir_created_result, file_copied_result = self.cal.copy_file_to_local(self.filepath, self.folder_name)
#             time.sleep(5)
#             if dir_created_result.returncode == 0 or dir_created_result.returncode == 1:
#                 print(self.folder_name.capitalize() + " folder is successfully created in emission directory")
#                 if file_copied_result.returncode == 0:
#                     print(self.folder_name.capitalize() + " file is successfully copied in emission directory of "+self.folder_name)
#                     while 1:
#                         if self.cal.get_queued_count(self.processor_name) == 0 and self.cal.get_queued_count(self.cQube_data_storage) == 0 and len(self.cal.get_processor_group_error_msg(self.processor_name)) == 0:
#                             print(self.folder_name.capitalize() + " file is successfully processed")
#                             self.assertTrue(0 == 0, self.folder_name.capitalize() + " file is successfully processed")
#                             break
#                         elif len(self.cal.get_processor_group_error_msg(self.processor_name)) != 0:
#                             self.assertEqual(0, len(self.cal.get_processor_group_error_msg(self.processor_name)),
#                                              self.cal.get_processor_group_error_msg(self.processor_name)[0])
#                             break
#                         elif self.cal.get_queued_count(self.processor_name) != 0 and self.cal.get_queued_count(self.cQube_data_storage) != 0:
#                             time.sleep(2)
#                 else:
#                     print(self.folder_name.capitalize() + " file is not copied in emission directory of " + self.folder_name)
#
#             else:
#                 print(self.folder_name.capitalize() + " folder is not created in emission directory")
#
#
#     def tearDown(self):
#         self.cal.stop_nifi_processor(self.processor_name)
#
# class SchoolMaster(unittest.TestCase):
#
#     def setUp(self):
#         self.processor_name="static_data_transformer"
#         self.folder_name="school_master"
#         self.cQube_data_storage = "cQube_data_storage"
#         self.cal = GetData()
#         self.storage_type = self.cal.get_storage_type()
#         self.cal.start_nifi_processor("cQube_data_storage")
#         self.cal.start_nifi_processor(self.processor_name)
#         self.filepath = self.cal.get_filepath(self.folder_name)
#
#     def test_school_master(self):
#         if self.storage_type == "s3":
#             result = self.cal.copy_file_to_s3(self.filepath, self.folder_name)
#             time.sleep(10)
#             if result.returncode == 0:
#                 print(self.folder_name.capitalize()+" file is successfully uploaded to s3")
#                 while 1 :
#                     if self.cal.get_queued_count(self.processor_name) == 0 and self.cal.get_queued_count(self.cQube_data_storage) == 0 and len(self.cal.get_processor_group_error_msg(self.processor_name)) == 0:
#                         print(self.folder_name.capitalize()+" file is successfully processed")
#                         self.assertTrue(0 == 0,self.folder_name.capitalize()+" file is successfully processed")
#                         break
#                     elif len(self.cal.get_processor_group_error_msg(self.processor_name)) != 0:
#                         self.assertEqual(0,len(self.cal.get_processor_group_error_msg(self.processor_name)),self.cal.get_processor_group_error_msg(self.processor_name)[0])
#                         break
#                     elif self.cal.get_queued_count(self.processor_name) != 0 and self.cal.get_queued_count(self.cQube_data_storage) != 0:
#                         time.sleep(2)
#             else:
#                 print(self.folder_name.capitalize()+" file is not uploaded to s3")
#         else:
#             dir_created_result, file_copied_result = self.cal.copy_file_to_local(self.filepath, self.folder_name)
#             time.sleep(5)
#             if dir_created_result.returncode == 0 or dir_created_result.returncode == 1:
#                 print(self.folder_name.capitalize() + " folder is successfully created in emission directory")
#                 if file_copied_result.returncode == 0:
#                     print(self.folder_name.capitalize() + " file is successfully copied in emission directory of "+self.folder_name)
#                     while 1:
#                         if self.cal.get_queued_count(self.processor_name) == 0 and self.cal.get_queued_count(self.cQube_data_storage) == 0 and len(self.cal.get_processor_group_error_msg(self.processor_name)) == 0:
#                             print(self.folder_name.capitalize() + " file is successfully processed")
#                             self.assertTrue(0 == 0, self.folder_name.capitalize() + " file is successfully processed")
#                             break
#                         elif len(self.cal.get_processor_group_error_msg(self.processor_name)) != 0:
#                             self.assertEqual(0, len(self.cal.get_processor_group_error_msg(self.processor_name)),
#                                              self.cal.get_processor_group_error_msg(self.processor_name)[0])
#                             break
#                         elif self.cal.get_queued_count(self.processor_name) != 0 and self.cal.get_queued_count(self.cQube_data_storage) != 0:
#                             time.sleep(2)
#                 else:
#                     print(self.folder_name.capitalize() + " file is not copied in emission directory of " + self.folder_name)
#
#             else:
#                 print(self.folder_name.capitalize() + " folder is not created in emission directory")
#
#
#     def tearDown(self):
#         self.cal.stop_nifi_processor(self.processor_name)
#
class SchoolManagement(unittest.TestCase):

    def setUp(self):
        self.processor_name="static_data_transformer"
        self.folder_name="school_management"
        self.cQube_data_storage = "cQube_data_storage"
        self.cal = GetData()
        self.storage_type = self.cal.get_storage_type()
        self.cal.start_nifi_processor("cQube_data_storage")
        self.cal.start_nifi_processor(self.processor_name)
        self.filepath = self.cal.get_filepath(self.folder_name)

    def test_school_management(self):
        if self.storage_type == "s3":
            result = self.cal.copy_file_to_s3(self.filepath, self.folder_name)
            time.sleep(10)
            if result.returncode == 0:
                print(self.folder_name.capitalize()+" file is successfully uploaded to s3")
                while 1 :
                    if self.cal.get_queued_count(self.processor_name) == 0 and self.cal.get_queued_count(self.cQube_data_storage) == 0 and len(self.cal.get_processor_group_error_msg(self.processor_name)) == 0:
                        print(self.folder_name.capitalize()+" file is successfully processed")
                        self.assertTrue(0 == 0,self.folder_name.capitalize()+" file is successfully processed")
                        break
                    elif len(self.cal.get_processor_group_error_msg(self.processor_name)) != 0:
                        self.assertEqual(0,len(self.cal.get_processor_group_error_msg(self.processor_name)),self.cal.get_processor_group_error_msg(self.processor_name)[0])
                        break
                    elif self.cal.get_queued_count(self.processor_name) != 0 and self.cal.get_queued_count(self.cQube_data_storage) != 0:
                        time.sleep(2)
            else:
                print(self.folder_name.capitalize()+" file is not uploaded to s3")
        else:
            dir_created_result, file_copied_result = self.cal.copy_file_to_local(self.filepath, self.folder_name)
            time.sleep(5)
            if dir_created_result.returncode == 0 or dir_created_result.returncode == 1:
                print(self.folder_name.capitalize() + " folder is successfully created in emission directory")
                if file_copied_result.returncode == 0:
                    print(self.folder_name.capitalize() + " file is successfully copied in emission directory of "+self.folder_name)
                    while 1:
                        if self.cal.get_queued_count(self.processor_name) == 0 and self.cal.get_queued_count(self.cQube_data_storage) == 0 and len(self.cal.get_processor_group_error_msg(self.processor_name)) == 0:
                            print(self.folder_name.capitalize() + " file is successfully processed")
                            self.assertTrue(0 == 0, self.folder_name.capitalize() + " file is successfully processed")
                            break
                        elif len(self.cal.get_processor_group_error_msg(self.processor_name)) != 0:
                            self.assertEqual(0, len(self.cal.get_processor_group_error_msg(self.processor_name)),
                                             self.cal.get_processor_group_error_msg(self.processor_name)[0])
                            break
                        elif self.cal.get_queued_count(self.processor_name) != 0 and self.cal.get_queued_count(self.cQube_data_storage) != 0:
                            time.sleep(2)
                else:
                    print(self.folder_name.capitalize() + " file is not copied in emission directory of " + self.folder_name)

            else:
                print(self.folder_name.capitalize() + " folder is not created in emission directory")


    def tearDown(self):
        self.cal.stop_nifi_processor(self.processor_name)


if __name__ == '__main__':
    unittest.main()
