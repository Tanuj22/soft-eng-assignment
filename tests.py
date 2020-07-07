import unittest
from code import TrackApplication


class Stub:
    def application_id():
        return 2

    def invalid_id():
        return None



class TrackApplicationTest(unittest.TestCase):

    def setUp(self):
        self.application = TrackApplication(Stub.application_id())
        self.invalid_application = TrackApplication(Stub.invalid_id())

    def test_valid_creation(self):
        self.assertEqual(self.application.id, Stub.application_id())
        self.assertEqual(self.application.office_of_accounts_approved, False)
        self.assertEqual(self.application.hod_approved, False)
        self.assertEqual(self.application.director_approved, False)
        self.assertEqual(self.application.reimbursement_done, False)

    def test_approval_from_office_of_accounts(self):
        self.application.approve_office_of_accounts()
        self.assertEqual(self.application.office_of_accounts_approved, True)
        self.assertEqual(self.application.hod_approved, False)
        self.assertEqual(self.application.director_approved, False)
        self.assertEqual(self.application.reimbursement_done, False)

    def test_approval_from_hod(self):
        self.application.approve_office_of_accounts()
        self.application.approve_hod()
        self.assertEqual(self.application.office_of_accounts_approved, True)
        self.assertEqual(self.application.hod_approved, True)
        self.assertEqual(self.application.director_approved, False)
        self.assertEqual(self.application.reimbursement_done, False)

    def test_approval_from_director(self):
        self.application.approve_office_of_accounts()
        self.application.approve_hod()
        self.application.approve_director()
        self.assertEqual(self.application.office_of_accounts_approved, True)
        self.assertEqual(self.application.hod_approved, True)
        self.assertEqual(self.application.director_approved, True)
        self.assertEqual(self.application.reimbursement_done, False)
        

    def test_reimbursement_done(self):
        self.application.approve_office_of_accounts()
        self.application.approve_hod()
        self.application.approve_director()
        self.application.approve_reimbursement()
        self.assertEqual(self.application.office_of_accounts_approved, True)
        self.assertEqual(self.application.hod_approved, True)
        self.assertEqual(self.application.director_approved, True)
        self.assertEqual(self.application.reimbursement_done, True)
    
    def test_approval_when_id_invalid(self):
        return_val = self.invalid_application.approve_office_of_accounts()
        self.assertEqual(return_val, "Application ID is not valid")
        return_val = self.invalid_application.approve_hod()
        self.assertEqual(return_val, "Application ID is not valid")
        return_val = self.invalid_application.approve_director()
        self.assertEqual(return_val, "Application ID is not valid")
        return_val = self.invalid_application.approve_reimbursement()
        self.assertEqual(return_val, "Application ID is not valid")

    def test_hod_cannot_approve_before_office_of_accounts(self):
        self.application.approve_hod()
        self.assertEqual(self.application.hod_approved, False)

    def test_director_cannot_approve_before_hod(self):
        self.application.approve_director()
        self.assertEqual(self.application.director_approved, False)

    def test_reimbursement_not_possible_before_directors_approval(self):
        self.application.approve_reimbursement()
        self.assertEqual(self.application.reimbursement_done, False)

    def test_application_status_after_submission(self):
        application_status = self.application.get_application_status()
        self.assertEqual(application_status, "Office of Accounts approval pending")

    def test_application_status_after_office_of_accounts_approval(self):
        self.application.approve_office_of_accounts()
        application_status = self.application.get_application_status()
        self.assertEqual(application_status, "HOD approval pending")

    def test_application_status_after_hod_approval(self):
        self.application.approve_office_of_accounts()
        self.application.approve_hod()
        application_status = self.application.get_application_status()
        self.assertEqual(application_status, "Director approval pending")

    def test_application_status_director_approval(self):
        self.application.approve_office_of_accounts()
        self.application.approve_hod()
        self.application.approve_director()
        application_status = self.application.get_application_status()
        self.assertEqual(application_status, "Reimbursement pending")


    def test_application_status_after_reimbursement(self):
        self.application.approve_office_of_accounts()
        self.application.approve_hod()
        self.application.approve_director()
        self.application.approve_reimbursement()
        application_status = self.application.get_application_status()
        self.assertEqual(application_status, "Application was processed successfully")


    def test_application_status_when_id_invalid(self):
        application_status = self.invalid_application.get_application_status()
        self.assertEqual(application_status, "Application ID is not valid")

    def test_reminder_alert_to_office_of_accounts(self):
        return_val = self.application.send_reminder()
        self.assertEqual(return_val, "Email sent to office of accounts")

    def test_reminder_alert_to_hod(self):
        self.application.approve_office_of_accounts()
        return_val = self.application.send_reminder()                    
        self.assertEqual(return_val, "Email sent to HOD")

    def test_reminder_alert_to_director(self):
        self.application.approve_office_of_accounts()
        self.application.approve_hod()
        return_val = self.application.send_reminder()
        self.assertEqual(return_val, "Email sent to Director")


    def test_reminder_alert_for_reimbursement(self):
        self.application.approve_office_of_accounts()
        self.application.approve_hod()
        self.application.approve_director()
        return_val = self.application.send_reminder()
        self.assertEqual(return_val, "Reminder for reimbursement sent")

    def test_reminder_when_reimbersement_done(self):
        self.application.approve_office_of_accounts()
        self.application.approve_hod()
        self.application.approve_director()
        self.application.approve_reimbursement()
        return_val = self.application.send_reminder()
        self.assertEqual(return_val, "Reimersentment already done")

    def test_reminder_when_id_invalid(self):
        return_val = self.invalid_application.send_reminder()
        self.assertEqual(return_val, "Application ID is not valid")

        
if __name__ == '__main__':
    unittest.main()
