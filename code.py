import smtplib


# Helper function to send emails

def send_email(receiver_id):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("pythontesting08@gmail.com", "pythontest123")
    message = "dummy email"
    s.sendmail("pythontesting08@gmail.com", receiver_id, message)
    s.quit()


# Class for Tracking an Application

class TrackApplication:
    def __init__(self, application_id):
        self.id = application_id
        self.office_of_accounts_approved = False
        self.hod_approved = False
        self.director_approved = False
        self.reimbursement_done = False

    def approve_office_of_accounts(self):
        if not self.id:
            return "Application ID is not valid"
        if not self.office_of_accounts_approved \
                and not self.hod_approved and \
                not self.director_approved and not self.reimbursement_done:
            self.office_of_accounts_approved = True

    def approve_hod(self):
        if not self.id:
            return "Application ID is not valid"
        if self.office_of_accounts_approved \
                and not self.hod_approved and \
                not self.director_approved and not self.reimbursement_done:
            self.hod_approved = True

    def approve_director(self):
        if not self.id:
            return "Application ID is not valid"
        if self.office_of_accounts_approved \
                and self.hod_approved and \
                not self.director_approved and not self.reimbursement_done:
            self.director_approved = True

    def approve_reimbursement(self):
        if not self.id:
            return "Application ID is not valid"
        if self.office_of_accounts_approved \
                and self.hod_approved and \
                self.director_approved and not self.reimbursement_done:
            self.reimbursement_done = True

    def get_application_status(self):
        if not self.id:
            return "Application ID is not valid"
        if not self.office_of_accounts_approved:
            return "Office of Accounts approval pending"
        if not self.hod_approved:
            return "HOD approval pending"
        if not self.director_approved:
            return "Director approval pending"
        if not self.reimbursement_done:
            return "Reimbursement pending"
        return "Application was processed successfully"

    def send_reminder(self):
        try:
            if not self.id:
                return "Application ID is not valid"
            if not self.office_of_accounts_approved:
                send_email("tanujagarwal22@gmail.com")
                return "Email sent to office of accounts"
            if not self.hod_approved:
                send_email("tanujagarwal22@gmail.com")
                return "Email sent to HOD"
            if not self.director_approved:
                send_email("tanujagarwal22@gmail.com")
                return "Email sent to Director"
            if not self.reimbursement_done:
                send_email("tanujagarwal22@gmail.com")
                return "Reminder for reimbursement sent"
            return "Reimersentment already done"    
        except Exception:
            return "Email was not sent"

