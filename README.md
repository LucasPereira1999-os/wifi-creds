# 💫 About Me

Hi there! 👋  
I'm an **aspiring ethical hacker** with a strong passion for offensive security — especially **Web Exploitation** 🌐 and **Malware Development** 🐍💣.

I’m currently leveling up my skills through hands-on labs and challenges at platforms like:

- 🧠 Hack The Box  
- 🛡️ PortSwigger Web Security Academy  
- 🔍 APISEC University  

I love understanding systems by breaking them — then putting them back together. Whether it’s bypassing web filters, writing payloads, or evading modern defenses, I’m constantly learning and pushing my limits.

---

## 🧠 Interests

- Web application vulnerabilities (XSS, SSRF, IDOR, etc.)
- Malware development & EDR evasion
- Offensive tooling and scripting (Python, PowerShell)
- Red team operations & post-exploitation tactics

> _"Learn. Break. Understand. Repeat."_

---

## 🌐 Connect With Me

[![Discord](https://img.shields.io/badge/Discord-%237289DA.svg?logo=discord&logoColor=white)](https://discord.gg/@james_carter11)  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://linkedin.com/in/alwi-muzakki-62443b360)  
[![Email](https://img.shields.io/badge/Email-D14836?logo=gmail&logoColor=white)](mailto:blazeice628@gmail.com)

---

# 💻 Tech Stack

![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![PowerShell](https://img.shields.io/badge/PowerShell-5391FE?style=for-the-badge&logo=powershell&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

---

# 📊 GitHub Stats

![](https://github-readme-stats.vercel.app/api?username=LucasPereira1999-os&theme=tokyonight&hide_border=false&include_all_commits=false&count_private=false)<br/>
![](https://nirzak-streak-stats.vercel.app/?user=LucasPereira1999-os&theme=tokyonight&hide_border=false)<br/>
![](https://github-readme-stats.vercel.app/api/top-langs/?username=LucasPereira1999-os&theme=tokyonight&hide_border=false&include_all_commits=false&count_private=false&layout=compact)

---

[![](https://visitcount.itsvg.in/api?id=LucasPereira1999-os&icon=4&color=0)](https://visitcount.itsvg.in)

---

# 📡 `postexploit-wifi-creds`

### WiFi Password Extractor (Windows) — for Red Team Post-Exploitation

This script extracts all stored Wi-Fi SSIDs and their plaintext passwords (`Key Content`) from a Windows system using the built-in `netsh` utility.

🛠 **Use Cases:**
- Post-exploitation (after initial access)
- Internal reconnaissance
- Red team labs and adversary simulation
- Ethical hacking education & research

⚠️ **Legal Disclaimer:**  
This tool is intended for use **only in authorized environments** (e.g., penetration testing, labs, research).  
**Unauthorized use is strictly prohibited.** The author assumes no responsibility for misuse.

---

## 🧰 Features

- Enumerates all saved Wi-Fi profiles (SSIDs)
- Extracts associated plaintext passwords
- Saves results to a clean output file
- Fully compatible with Windows OS (via `netsh`)

---

## 📦 Requirements

- Windows 10/11
- Python 3.x
- Admin/root shell (if needed to access secured profiles)

---

## 🚀 Usage

```bash
python wifi_extractor.py
