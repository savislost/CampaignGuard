import urllib.request
import urllib.error
import json
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

def create_short_link(destination_url: str, custom_slug: str = "campaign") -> dict:
    """Generates a sanitized campaign short URL."""
    sanitized_slug = re.sub(r'[^a-zA-Z0-9-_]', '', custom_slug)
    return {
        "destination": destination_url,
        "short_url": f"https://safe.lnk/{sanitized_slug}",
        "slug": sanitized_slug
    }

def update_github_gist(gist_id: str, github_token: str, new_link: str) -> dict:
    """IRREVERSIBLE ACTION: Updates a live public GitHub Gist with the new campaign link."""
    api_url = f"https://api.github.com/gists/{gist_id}"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {github_token}",
        "Content-Type": "application/json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "CampaignGuard-Agent"
    }
    data = {
        "description": "Active Campaign Link",
        "files": {
            "campaign_link.txt": {"content": f"Live Campaign URL: {new_link}"}
        }
    }
    
    req = urllib.request.Request(api_url, data=json.dumps(data).encode('utf-8'), headers=headers, method='PATCH')
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            status = response.getcode()
            return {
                "success": status == 200,
                "status_code": status,
                "gist_id": gist_id,
                "message": "Live Gist overwritten successfully."
            }
    except urllib.error.HTTPError as e:
        error_body = e.read().decode('utf-8', errors='ignore')
        return {
            "success": False,
            "status_code": e.code,
            "error_type": "HTTPError",
            "details": error_body
        }
    except Exception as e:
        return {
            "success": False,
            "status_code": 500,
            "error_type": "UnexpectedException",
            "details": str(e)
        }

if __name__ == "__main__":
    print("Agent Tools Loaded.")
