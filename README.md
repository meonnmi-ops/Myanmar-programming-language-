# Myanmar Programming Language (Myanmar Code) v2.1.0

မြန်မာဘာသာစကားဖြင့် ရေးသားနိုင်သော ပရိုဂရမ်းမင်းဘာသာစကား (Myanmar Programming Language)

## ✨ ထူးခြားချက်များ (Features)

- **Keywords စုစုပေါင်း ၂၁၃ လုံး** (Python + JavaScript + C++ + Java)
- **String Protection** - စာသားထဲမှာရှိသော keyword များကို မပြောင်းလဲပါ
- **Myanmar Digit Conversion** - ၀-၉ → 0-9 အလိုက်လိုက်ပြောင်းနိုင်ပါသည်
- **Declaration Keyword Removal** - var/const/let (ကိန်း/အတည်/နေရာ) ကို အလိုက်ဖျက်ပေးသည်
- **Full Python Execution** - Myanmar code → Python → exec() အခြေခံ အလုပ်လုပ်ပါသည်
- **translate() method** - Debug အတွက် Python code ကို ကြည့်နိုင်ပါသည်
- **12/12 Tests Pass** - အောင်မြင်မှု 100%

## 📦 တပ်ဆင်နည်း (Installation)

```bash
pip install myanmar-code
```

## 🚀 အသုံးပြုနည်း (Usage)

### Basic Print
```python
from myanmar_code import MyanmarCodeEngine

engine = MyanmarCodeEngine()

# Basic print
engine.execute('ပုံနှိပ်("မင်္ဂလာပါ")')
# Output: မင်္ဂလာပါ
```

### Variables & If/Else
```python
engine.execute('''
အတည် အရမ်း = ၁၀
အကယ်၍ အရမ်း > ၅:
    ပုံနှိပ်("ကြီးပါ")
မဟုတ်ပါက:
    ပုံနှိပ်("သေးပါ")
''')
# Output: ကြီးပါ
```

### Functions
```python
engine.execute('''
အဓိပ္ပာယ် မင်္ဂလာပါ_ပုံနှိပ်():
    ပုံနှိပ်("Myanmar Programming Language")
    ပြန်ပေး "အောင်မြင်ပါသည်"

မင်္ဂလာပါ_ပုံနှိပ်()
''')
```

### Classes
```python
engine.execute('''
အတန်း ကား:
    အဓိပ္ပာယ် __init__(ဒီ, အမည်):
        ဒီ.အမည် = အမည်

    အဓိပ္ပာယ် ဖော်ပြ():
        ပုံနှိပ်("ယနေ့နေ့ " + ဒီ.အမည် + " ကားပါသည်")

b = ကား("သွင်း")
b.ဖော်ပြ()
''')
```

### For Loop & Lists
```python
engine.execute('''
အတည် နာမည်စာရင်း = ["မင်္ဂလာ", "အောင်မင်း", "ချိုခင်း"]
အတွက် နာမည် in နာမည်စာရင်း:
    ပုံနှိပ်(နာမည်)
''')
```

### Try/Except Error Handling
```python
engine.execute('''
ကြိုးစား:
    ရလဒ် = ၁၀ မြှောက်ပါ ၀
    ပုံနှိပ်(ရလဒ်)
ဖမ်းမိ အမှား:
    ပုံနှိပ်("အမှားဖြစ်ပါသည်: " + အမှား)
နောက်ဆုံး:
    ပုံနှိပ်("ဆက်လုပ်ပါသည်")
''')
```

### Translate (Debug)
```python
# See translated Python code without executing
code = engine.translate('အတည် x = ၁၀\nပုံနှိပ်(x)')
print(code)
# Output: x = 10\nprint(x)
```

## 🔑 Keyword Categories

| Category | Count | Examples |
|----------|-------|---------|
| Core Python | 35+ | ပုံနှိပ်(print), အကယ်၍(if), အတွက်(for) |
| JavaScript | 14+ | လုပ်ဆောင်ချက်(function), ဒီ(this), အသစ်(new) |
| C++/Java | 30+ | လူသိ(public), ဘိုက်(byte), အက္ခရာ(char) |
| Operators | 16+ | ပေါင်း(+), နှုတ်(-), မြှောက်(*), စား(/) |
| Built-ins | 25+ | အရှည်(len), ပတ်လမ်း(range), ပုံစံ(type) |
| **Total** | **213** | |

## 📂 File Structure

```
Myanmar-programming-language-/
├── myanmar_code/
│   └── __init__.py          # Engine v2.1.0 (213 keywords, string protection)
├── examples/
│   ├── hello.mmr             # Basic examples
│   └── calculator.mmr        # Calculator example
├── web-ide/
│   └── index.html            # Web IDE
├── Keywords.json              # All 213 keywords data
├── setup.py                   # pip package config
├── README.md                  # This file
└── License                    # MIT License
```

## 🧪 Tests

All 12 tests pass:
- ✅ Basic print
- ✅ String protection (keywords inside strings NOT translated)
- ✅ Variables with Myanmar names
- ✅ If/else statements
- ✅ For loops with range()
- ✅ Function definition and calls
- ✅ Try/except error handling
- ✅ Class with __init__
- ✅ List operations
- ✅ While loops
- ✅ Arithmetic calculations
- ✅ Boolean values

## 👑 ဖန်တီးသူ (Authors)

Aung MoeOo (MWD) & MYANOS Team

## 📄 လိုင်စင် (License)

MIT License - အချိန်းအစားအသုံးပြုနိုင်ပါသည်

## 🔗 Links

- **GitHub**: https://github.com/meonnmi-ops/Myanmar-programming-language-
- **Web IDE**: https://meonnmi-ops.github.io/myanmar-code/web-ide
- **MYANOS IDE**: https://github.com/meonnmi-ops/myanoide

© ২၀၂၆ မြန်မာကုဒ碁 (Myanmar Code)
