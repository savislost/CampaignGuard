import urllib.request
import urllib.error
import re

def verify_link_health(url: str) -> dict:
    """Verifies whether the target URL resolves with a 200 OK status."""
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=8) as response:
            return {"status_code": response.getcode(), "reachable": True, "url": url}
    except urllib.error.HTTPError as e:
        return {"status_code": e.code, "reachable": False, "error": f"HTTP {e.code}"}
    except Exception as e:
        return {"status_code": 500, "reachable": False, "error": str(e)}

def create_short_link(destination_url: str, custom_slug: str = "campaign-link") -> dict:
    """Generates a sanitized campaign short URL."""
    sanitized_slug = re.sub(r'[^a-zA-Z0-9-_]', '', custom_slug)
    return {
        "destination": destination_url,
        "short_url": f"https://safe.lnk/{sanitized_slug}",
        "slug": sanitized_slug
    }

def update_social_bio(platform: str, profile_id: str, new_link: str) -> dict:
    """Simulates updating a live social media bio link."""
    return {"success": True, "platform": platform, "profile_id": profile_id, "new_bio_link": new_link}

if __name__ == "__main__":
    sample = "https://example.com"
    print("Health check:", verify_link_health(sample))
    print("Short link:", create_short_link(sample, "my-promo"))
