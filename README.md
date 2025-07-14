<p align="center">
  <img src="https://github.com/LucasPereira1999-os/wifi-creds/edit/main/logo%20wifi.png" width="220" alt="WiFi Scanner Logo"/>
</p>

<h1 align="center">🔐 WiFi Credential Extractor (Windows)</h1>

<p align="center">
  <em>A lightweight post-exploitation tool to extract saved SSIDs and passwords from Windows systems.</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/status-active-brightgreen.svg"/>
  <img src="https://img.shields.io/badge/platform-windows-blue"/>
  <img src="https://img.shields.io/badge/license-MIT-purple"/>
  <img src="https://img.shields.io/badge/python-3.6+-yellow.svg"/>
</p>

---

## 📌 Overview

**WiFi Credential Extractor** is a lightweight Python script that collects saved Wi-Fi SSIDs and their passwords on a Windows machine using the native `netsh` command.  
It is ideal for:

- 🔍 Red team reconnaissance  
- 🧪 Post-exploitation tasks  
- 🔐 Internal audits and password recovery

---

## ⚙️ Features

- 🔹 Extracts all saved SSIDs on the system
- 🔹 Retrieves passwords using `netsh wlan show profile <SSID> key=clear`
- 🔹 Saves results in clean, readable `.txt` files
- 🔹 No external libraries required — pure Python
- 🔹 Designed for use in authorized red team or lab environments

---

## 🛠️ Usage

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
