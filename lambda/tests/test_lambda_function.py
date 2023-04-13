# Built-in imports
import os, sys
import unittest
from unittest.mock import patch, MagicMock

# External imports
from moto import mock_sts

# Add path to find lambda_dns directory for own imports
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

# Own imports
import src.lambda_function as _lambda


class TestLambdaFunction(unittest.TestCase):
    """
    TestCase for unit testing the inner Lambda Function functionalities.
    """

    # The "mock_sts" decorator allows to "mock/fake" the sts API calls for tests
    @mock_sts()
    def test_get_current_aws_account(self):
        """
        Test the expected STS API calls for obtaining the AWS account.
        """
        account = _lambda.get_current_aws_account()
        self.assertEqual(account, "123456789012")

    # Mock account to test the lambda_handler response structure
    def test_lambda_handler(self):
        """
        Test that validates the expected dictionary response structure only,
        without relying on the STS API call (being completely mocked)
        """
        example_response = {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": {
                "account": MagicMock,
                "datetime": "2023_04_12-18_59_52Z",
                "message": "Hello from Santi",
            }
        }

        with patch("src.lambda_function.get_current_aws_account") as mocked_get_current_aws_account:
            response = _lambda.lambda_handler(None, None)
            self.assertEqual(
                response["statusCode"],
                example_response["statusCode"]
            )
            self.assertEqual(
                response["body"]["message"],
                example_response["body"]["message"]
            )
            self.assertIsInstance(
                response["body"]["account"],
                MagicMock,
                "Error in mocking the <get_current_aws_account()> function, use \
                MagicMock for this test case"
            )


if __name__ == "__main__":
    unittest.main()
