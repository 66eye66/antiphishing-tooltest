import unittest
from server_agent.agent import PhishingAgent

class TestPhishingAgent(unittest.TestCase):
    def test_spoofing_detection(self):
        agent = PhishingAgent()
        email = b"From: attacker@phishing.com\nSubject: Urgent!\n\nClick here: http://trusted.com"
        self.assertIn("Potential phishing: Domain spoofing detected", agent.scan_email(email))

    def test_suspicious_link(self):
        agent = PhishingAgent()
        email = b"From: trusted@trusted.com\nSubject: Urgent!\n\nClick here: http://phishing.com"
        self.assertIn("Potential phishing: Suspicious link detected", agent.scan_email(email))

    def test_anomaly_detection(self):
        agent = PhishingAgent()
        email = b"From: trusted@trusted.com\nSubject: Urgent!\n\nThis is a very suspicious email."
        self.assertIn("Potential phishing: Anomaly detected", agent.scan_email(email))

if __name__ == '__main__':
    unittest.main()