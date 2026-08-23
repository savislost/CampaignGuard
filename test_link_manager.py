import unittest
from link_manager import verify_link_health, create_short_link, update_github_gist

class TestLinkManager(unittest.TestCase):
    def test_create_short_link_slug_sanitization(self):
        res = create_short_link("https://example.com", "summer_deal!@#2026")
        self.assertEqual(res["slug"], "summer_deal2026")
        self.assertEqual(res["short_url"], "https://safe.lnk/summer_deal2026")

    def test_update_github_gist_invalid_credentials(self):
        """Ensures structured error feedback when credentials fail."""
        res = update_github_gist("invalid_id", "invalid_token", "https://safe.lnk/test")
        self.assertFalse(res["success"])
        self.assertIn("status_code", res)

if __name__ == "__main__":
    unittest.main()
