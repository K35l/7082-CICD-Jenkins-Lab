import subprocess
import sys
import unittest


class TestApp(unittest.TestCase):
    def test_app_runs_successfully(self):
        result = subprocess.run(
            [sys.executable, "app.py"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, msg=f"Error output: {result.stderr}")
        self.assertTrue(len(result.stdout.strip()) > 0, "Expected output from app.py")


if __name__ == "__main__":
    unittest.main()