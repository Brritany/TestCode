import unittest
import pandas as pd

class TestCode(unittest.TestCase):

    # 學生的資料會在這裡被載入
    # 這可以在Colab筆記本中完成，然後將DataFrame傳遞到測試類
    def setUp(self):
        self.student_data = pd.read_csv('student_data.csv')  # 假設學生的數據是這樣載入的

    def test_discharge_summary(self):
        discharge_summary_count = self.student_data[self.student_data['CATEGORY'] == 'Discharge summary'].shape[0]
        self.assertTrue(discharge_summary_count > 0, "No Discharge summary found")

    def test_merged_data(self):
        # 假設 'SUBJECT_ID' 和 'HADM_ID' 都應該在學生的DataFrame中
        self.assertIn('SUBJECT_ID', self.student_data.columns)
        self.assertIn('HADM_ID', self.student_data.columns)

    def test_final_admission(self):
        # 檢查是否每個 'SUBJECT_ID' 只出現一次
        self.assertTrue(self.student_data['SUBJECT_ID'].is_unique, "Duplicates found in final admission data")

    # 其他測試...

if __name__ == '__main__':
    unittest.main()
