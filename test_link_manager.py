import unittest
from link_manager import verify_link_health, create_short_link, update_social_bio

class TestLinkManager(unittest.TestCase):
    def test_create_short_link_slug_sanitization(self):
        """Ensures unsafe special characters are removed from URL slugs."""
        res = create_short_link("https://example.com", "summer_deal!@#2026")
        self.assertEqual(res["slug"], "summer_deal2026")
        self.assertEqual(res["short_url"], "https://safe.lnk/summer_deal2026")

    def test_mock_bio_update_payload(self):
        """Verifies social bio payload formatting."""
        res = update_social_bio("instagram", "official_brand", "https://safe.lnk/summer_deal2026")
        self.assertTrue(res["success"])
        self.assertEqual(res["platform"], "instagram")
        self.assertEqual(res["profile_id"], "official_brand")

if __name__ == "__main__":
    unittest.main()
