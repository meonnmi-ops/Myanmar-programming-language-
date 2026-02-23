
```python
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="myanmar-code",
    version="2.0.0",
    author="Aung MoeOo (MWD) & DEEPSEEK STANDARD CODER STANDARD V3",
    author_email="mimoe7897@gmail.com",
    description="မြန်မာဘာသာစကားဖြင့် ရေးသားနိုင်သော ပရိုဂရမ်းမင်းဘာသာစကား (Keywords ၁၂၇ လုံး)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mimoe7897-collab/myanmar-code",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Interpreters",
    ],
    python_requires=">=3.6",
)
```

---

📌 အကျဉ်းချုပ်

ဖိုင် အမည် နေရာ
ဖိုင် ၁ README.md root folder
ဖိုင် ၂ __init__.py myanmar_code/__init__.py
ဖိုင် ၃ setup.py root folder
