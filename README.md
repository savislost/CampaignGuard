# CampaignGuard 🛡️
> Autonomous Campaign & Link Infrastructure Agent with Human-in-the-Loop Safety Gates.

CampaignGuard prevents broken marketing links, dead destination pages (404s), and unauthorized production overwrites by combining sandboxed URL validation with an explicit human approval gate powered by TrueForge.

---

## ⚡ Core Features
- **Sandbox URL Health Checks:** Validates target URLs for HTTP 200 OK and response reachability.
- **Sanitized Short Link Generation:** Creates slug-safe promotional short URLs.
- **Live Production Writes:** Updates public GitHub Gist endpoints via authenticated REST APIs.
- **Human-in-the-Loop Safety Gate:** The agent pauses and requires human confirmation before executing irreversible production state changes.
- **Qodo-Verified Code Quality:** Built with unit tests and iterative code quality reviews.

---

## 🏗️ Architecture Flow

User Prompt -> Gemini Flash -> TrueForge Sandbox (link_manager.py) -> Safety Gate (Human Approval) -> Live Production Gist Update

---

## 🚀 Getting Started

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
