# CampaignGuard 
> Autonomous Campaign & Link Infrastructure Agent with Human-in-the-Loop Safety Gates.

CampaignGuard prevents broken marketing links, dead destination pages (404s), and unauthorized production overwrites by combining sandboxed URL validation with an explicit human approval gate powered by TrueForge.

---

##  Core Features
- **Sandbox URL Health Checks:** Validates target URLs for HTTP 200 OK and response reachability.
- **Sanitized Short Link Generation:** Creates slug-safe promotional short URLs.
- **Live Production Writes:** Updates public GitHub Gist endpoints via authenticated REST APIs.
- **Human-in-the-Loop Safety Gate:** The agent pauses and requires human confirmation before executing irreversible production state changes.
- **Qodo-Verified Code Quality:** Built with unit tests and iterative code quality reviews.

---

##  Architecture Flow

User Prompt -> Gemini Flash -> TrueForge Sandbox (link_manager.py) -> Safety Gate (Human Approval) -> Live Production Gist Update

---

##  Getting Started

### Prerequisites
- Node.js v22+
- Python 3.10+
- WSL (Ubuntu) / Linux / macOS

### 1. Launch TrueForge
git clone https://github.com/savislost/social-media-manager.git
cd social-media-manager
npx @truefoundry/trueforge

### 2. Run Test Suite
python3 test_link_manager.py

## Qodo Code Review Evidence

- **Representative Pull Request:** [PR #1 - Real GitHub Gist PATCH Integration]((https://github.com/savislost/social-media-manager/pull/4)
- **Key Findings & Actions:**
  - **High Severity (Missing Content-Type Header):** Qodo identified that the raw `urllib` PATCH request lacked `'Content-Type': 'application/json'`, causing GitHub to reject payloads. We resolved this by explicitly configuring headers.
  - **High Severity (Broken Test Import):** Qodo flagged that `test_link_manager.py` still imported the deprecated `update_social_bio` function. We refactored the test suite to validate the live `update_github_gist` endpoint and error payloads.
  - **Architecture Decision (urllib vs PyGitHub):** Retained standard library `urllib` to keep the sandbox execution environment lightweight and zero-dependency.
