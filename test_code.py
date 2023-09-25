import unittest
import pandas as pd

class TestCode(unittest.TestCase):

    def setUp(self):
        self.student_data = pd.read_csv('final_admission.csv')

    def test_discharge_summary(self):
        discharge_summary_count = self.student_data[self.student_data['CATEGORY'] == 'Discharge summary'].shape[0]
        self.assertTrue(discharge_summary_count > 0, "No Discharge summary found")

    def test_merged_data(self):
        # 假設 'SUBJECT_ID' 和 'HADM_ID' 都在DataFrame中
        self.assertIn('SUBJECT_ID', self.student_data.columns)
        self.assertIn('HADM_ID', self.student_data.columns)

    def test_final_admission(self):
        # 檢查是否每個 'SUBJECT_ID' 只出現一次
        self.assertTrue(self.student_data['SUBJECT_ID'].is_unique, "Duplicates found in final admission data")

    def test_exclude_newborn(self):
        # 檢查是否有未排除的新生兒
        newborn_count = self.student_data[self.student_data['ADMISSION_TYPE'] == 'NEWBORN'].shape[0]
        self.assertEqual(newborn_count, 0, "Newborn records found")

    def test_exclude_dih(self):
        # 檢查是否有未排除的院內死亡
        dih_count = self.student_data[self.student_data['DIH'] == 1].shape[0]
        self.assertEqual(dih_count, 0, "Deaths in hospital found")

    def test_final_count(self):
        # 檢查最終檔案筆數
        final_count = self.student_data.shape[0]
        self.assertEqual(final_count, 32174, f"Expected 32174 but got {final_count}")

if __name__ == '__main__':
    unittest.main()
