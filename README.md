# 🛡️ PyShield Obfuscator - Advanced Python Code Protection

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Version](https://img.shields.io/badge/Version-1.0.0-orange)

**Advanced multi-layer obfuscation tool for Python code protection**

## 🌟 Features

### 🎯 **3 Powerful Protection Layers**

#### **Layer 1 - Content Renaming**
- Rename functions, variables, and classes
- Random patterns like `O0O0O0O`, `I1I1I1I1`
- Comprehensive code structure protection

**before:**
```python
def main(x):
    print(x)
main("5")
```

**after:**
```python
def I1lI1lI1lI1lI1lI1lI1lI1l(O0O0O0O0O0O0O0O0O0O0O0O0):
    print(O0O0O0O0O0O0O0O0O0O0O0O0)
I1lI1lI1lI1lI1lI1lI1lI1l('5')
```

#### **Layer 2 - Junk Code Injection**
- Add non-functional code to complicate analysis
- Make reverse engineering more difficult

#### **Layer 3 - Advanced Encryption**
- Uses `marshal`, `zlib`, `lzma`, `base64`
- Multiple internal encryption layers
- Extra protection against decryption attempts

## 🚀 Quick Start

### ⚡ **Instant Installation**

```bash
git clone https://github.com/abdouch-dev/pyshield-obfuscator.git

cd pyshield-obfuscator

pip install -r requirements.txt
```
### 🎮 **Usage Method**
```bash
python main.py

# then drag and drop your python file
```

### 📁 **Project Structure**
```bash
Pyshield-Obfuscator/
├── main.py              # Main interface
├── src/                 # 📦 Source code
│   ├── layer1.py        # Layer 1 - Renaming Algorithm
│   ├── layer2.py        # Layer 2 - Junk code
│   └── layer3.py        # Layer 3 - Advanced encryption
├── output/              # 📂 Encrypted files
├── requirements.txt     # 📋 Requirements
└── README.md           
```

## 🔧 **Requirements**
```bash
astor>=0.8.1
lzma>=0.1.0         
```

## **🛡️ Protection Features**
- ✅ Multi-layer protection
- ✅ Code structure hiding
- ✅ Reverse engineering resistance
- ✅ Automatic backup
- ✅ Simple user interface

## **⚠️ Important Notes**
- 🚨 For educational and ethical use only!
- 🔒 Obfuscated code becomes hard to read and analyze
- ⚡ Works with Python 3.8 and above

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**⭐ Don't forget to star the repository if you like it!**
