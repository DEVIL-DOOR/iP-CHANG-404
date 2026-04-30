# 🚀 iP-CHANG-404 - Ultimate Tor IP Rotator

**iP-CHANG-404** হলো একটি অ্যাডভান্সড পাইথন স্ক্রিপ্ট যা স্বয়ংক্রিয়ভাবে আপনার আইপি (IP Address) পরিবর্তন করতে পারে। এটি **Tor Network** ব্যবহার করে আপনাকে ইন্টারনেটে সম্পূর্ণ অ্যানোনিমাস রাখতে এবং ট্র্যাকিং এড়াতে সাহায্য করে।

---

## ✨ Features

* **⚡ Automatic IP Rotation:** নির্দিষ্ট সময় পর পর অটোমেটিক আইপি পরিবর্তন।
* **🌍 Specific Country Nodes:** চাইলে নির্দিষ্ট দেশের (যেমন: us, gb, de) আইপি ব্যবহার করার সুবিধা।
* **🕒 Custom Time Interval:** কত সেকেন্ড পর পর আইপি বদলাবে তা ইউজার নিজেই সেট করতে পারে।
* **🕵️ User-Agent Spoofing:** প্রতিবার রিকোয়েস্টের সাথে র্যান্ডম ইউজার-এজেন্ট ব্যবহার করে পরিচয় লুকিয়ে রাখে।
* **📊 Session Statistics:** মোট কতবার রোটেশন হয়েছে এবং কতক্ষণ ধরে সার্ভিসটি চলছে তা লাইভ দেখায়।
* **🛡️ Kill Switch:** স্ক্রিপ্ট বন্ধ করার সাথে সাথে টর সার্ভিস কিল করে দেয় যাতে আইপি লিক না হয়।

---

## 🛠️ Requirements & Installation

এই টুলটি চালানোর জন্য আপনার সিস্টেমে পাইথন এবং টর (Tor) ইন্সটল থাকতে হবে।

### 1. Update & Install Dependencies (Termux/Linux)
```bash

pkg update && pkg upgrade -y
pkg install python tor -y
pip install requests stem colorama
git clone https://github.com/DEVIL-DOOR/iP-CHANG-404
cd iP-CHANG-404
pkill tor
python IP-404.py
