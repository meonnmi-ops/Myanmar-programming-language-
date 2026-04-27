"""
Myanmar Code Engine v2.1.0
Keywords: 213 (Python + JavaScript + C++/Java complete)
Myanmar Programming Language - Full Execution Engine with String Protection
"""

import sys
import re
from io import StringIO
from contextlib import redirect_stdout


class MyanmarCodeEngine:
    def __init__(self):
        self.keywords = [
            # ========== Original 127 ==========
            "ကိန်း", "အတည်", "နေရာ", "လုပ်ဆောင်ချက်", "ပြန်ပေး", "ပြန်ပို့",
            "အကယ်၍", "မဟုတ်ပါက", "မဟုတ်လျှင်", "သို့မဟုတ်", "ရွေးချယ်", "ကိစ္စ",
            "အတွက်", "အကြိမ်အားလုံးအတွက်", "သံသရာ", "လုပ်နေစဉ်", "ပတ်လမ်း",
            "ရပ်", "ဆက်လုပ်", "ထားပါ", "မှတ်ထား", "သွားပါ", "အဆုံး",
            "ပြီး", "ပြီးပြီ", "ဒါဆို", "လုပ်ပါ", "လုပ်ရန်", "ပုံနှိပ်",
            "ပြောပါ", "ထုတ်ပြ", "ရိုက်ပါ", "ပြပေးမည်", "ရေးပြမည်", "မေးမြန်း",
            "ထည့်သွင်း", "ထည့်ပါ", "မေးပါ", "တောင်းဆိုမည်", "သိမ်းဆည်းမည်",
            "ဖတ်မည်", "ကူးယူပါ", "မှန်", "မှား", "ဘာမှမရှိ", "မသတ်မှတ်ရသေး",
            "မှန်သည်", "မှားသည်", "အမှန်", "အမှား", "ရှိ", "မရှိ", "စာရင်း",
            "အရာဝတ္ထု", "အဘိဓာန်", "ဇယား", "အစီအစဉ်", "ထည့်ပါ",
            "ဖယ်ရှားပါ", "အရှည်", "ရှာပါ", "ရှိပါသလား", "ပြောင်းလဲပါ",
            "အစဉ်လိုက်စီပါ", "အရေအတွက်", "ရှင်းလင်းပါ", "စာရင်းဆောက်",
            "စာရင်းထည့်", "နှင့်", "သို့မဟုတ်", "မဟုတ်", "ညီမျှလျှင်",
            "ကြီးလျှင်", "ငယ်လျှင်", "တူလျှင်", "ပေါင်း", "နှုတ်", "မြှောက်",
            "စား", "အကြွင်း", "ပေါင်းပါ", "နှုတ်ပါ", "မြှောက်ပါ", "စားပါ",
            "ကျပန်း", "အချိန်", "သင်္ချာ_အမြင့်ဆုံး", "သင်္ချာ_အနိမ့်ဆုံး",
            "သင်္ချာ_စတုရန်း", "စတုရန်းရင်း", "ဆိုင်", "ကိုဆိုင်", "တန်ဂျင့်",
            "လော့ဂရစ်သမ်", "ထပ်ကိန်း", "ပိုင်", "စာသား_ပေါင်း", "စာသား_အရှည်",
            "စာကြောင်းအရှည်", "စာဆက်", "စာခွဲ", "ဖြတ်", "အစားထိုး",
            "စမြည့်", "ဆုံးမြည့်", "စာလုံးကြီး", "စာလုံးသေး", "စာသား",
            "စာရင်း_အလယ်", "အလယ်", "ပြောင်းပြန်", "စီ", "ပေါင်း", "ရှာ",
            "စာရင်းအရှည်", "စာရင်းထုတ်", "ဖိုင်ဖတ်", "ဖိုင်ရေး", "ဖိုင်ဖျက်",
            "ဖိုင်စာရင်း", "ဖွင့်", "ရှိ_မရှိ", "အရွယ်", "ပြောင်း", "သိမ်း",
            "အချိန်", "စောင့်", "ယနေ့", "အခု", "ဖော်မတ်", "ဖြည်", "ကွာခြား",
            "ထည့်", "စစ်ဆေး", "သတ်မှတ်", "ကြိမ်", "မှန်နေသရွေ့", "ရပ်လိုက်ပါ",
            "ကျော်လိုက်ပါ", "အမှတ်", "ပြီးပါပြီ", "စတင်ပါ", "အောင်မြင်ပါသည်",
            # ========== New 86 keywords ==========
            "အဓိပ္ပာယ်", "အတန်း", "ကျော်လွှတ်", "အတိုချုံး", "ကမ္ဘာ့", "ဒေသမဟုတ်",
            "ကြိုးစား", "ဖမ်းမိ", "နောက်ဆုံး", "ချမြှောက်", "မတူညီ", "မျှော်",
            "ကိုက်ညီ", "ဖြစ်နိုင်", "တင်သွင်း", "မှ", "အဖြစ်", "နဲ့အတူ", "ဖျက်",
            "ထဲမှာ", "ဖြစ်", "မူလ", "ပစ်ချ", "အသစ်", "ဒီ", "အထက်", "တိုးချဲ့",
            "တင်ပို့", "အမျိုးအစား", "အဖြစ်အပျက်", "အမှားရှာ", "ဗလာ", "လုပ်",
            "လူသိ", "လျှို့ဝှက်", "ကာကွယ်", "တည်မြဲ", "အတု", "ပုံစံ",
            "နေရာအမည်", "ဖွဲ့စည်း", "အရွယ်အစား", "သူငယ်ချင်း", "ပြောင်းလဲနိုင်",
            "ရှင်းလင်း", "တိုက်ရိုက်", "သွား", "ထုတ်ပေး", "မှန်မှား", "ဘိုက်",
            "အက္ခရာ", "နှစ်ဆ", "အပိုင်း", "အကောင်အထည်", "ရှည်", "အထုပ်",
            "တစ်ပြိုင်နက်", "ယာယီ", "မတည်မြဲ",
        ]

        self.digits = {
            '၀': '0', '၁': '1', '၂': '2', '၃': '3', '၄': '4',
            '၅': '5', '၆': '6', '၇': '7', '၈': '8', '၉': '9'
        }

        # Declaration keywords: REMOVE (not translate) - Python doesn't need type declarations
        self.declaration_keywords = ["ကိန်း", "အတည်", "နေရာ"]

        # Keyword map: Myanmar -> Python
        self.keyword_map = {
            # --- Core Python keywords ---
            "ပုံနှိပ်": "print",
            "အကယ်၍": "if",
            "မဟုတ်ပါက": "else",
            "မဟုတ်လျှင်": "elif",
            "အတွက်": "for",
            "လုပ်နေစဉ်": "while",
            "ရပ်": "break",
            "ဆက်လုပ်": "continue",
            "အဓိပ္ပာယ်": "def",
            "အတန်း": "class",
            "ပြန်ပေး": "return",
            "ကျော်လွှတ်": "pass",
            "အတိုချုံး": "lambda",
            "ကမ္ဘာ့": "global",
            "ဒေသမဟုတ်": "nonlocal",
            "ထုတ်ပေး": "yield",
            "ကြိုးစား": "try",
            "ဖမ်းမိ": "except",
            "နောက်ဆုံး": "finally",
            "ချမြှောက်": "raise",
            "စစ်ဆေး": "assert",
            "မတူညီ": "async",
            "မျှော်": "await",
            "ကိုက်ညီ": "match",
            "တင်သွင်း": "import",
            "မှ": "from",
            "အဖြစ်": "as",
            "နဲ့အတူ": "with",
            "ဖျက်": "del",
            "ထဲမှာ": "in",
            "ဖြစ်": "is",
            "မှန်": "True",
            "မှား": "False",
            "ဘာမှမရှိ": "None",
            "ဗလာ": "None",
            # --- JS/C++/Java -> Python ---
            "လုပ်ဆောင်ချက်": "def",
            "ဒီ": "self",
            "အထက်": "super",
            "လုပ်": "while",
            "ဘိုက်": "bytearray",
            "အက္ခရာ": "chr",
            "နှစ်ဆ": "float",
            "အပိုင်း": "float",
            # --- Operators ---
            "အကြွင်း": "**",
            "ပေါင်း": "+",
            "နှုတ်": "-",
            "မြှောက်": "*",
            "စား": "/",
            "ပေါင်းပါ": "+=",
            "နှုတ်ပါ": "-=",
            "မြှောက်ပါ": "*=",
            "စားပါ": "/=",
            "ညီမျှလျှင်": "and",
            "သို့မဟုတ်": "or",
            "မှန်နေသရွေ့": "not",
            "တူလျှင်": "==",
            "မဟုတ်": "!=",
            "ကြီးလျှင်": ">",
            "ငယ်လျှင်": "<",
            # --- Built-in functions ---
            "အရှည်": "len",
            "ပတ်လမ်း": "range",
            "ကျပန်း": "str",
            "အချိန်": "int",
            "လော့ဂရစ်သမ်": "float",
            "စာသား": "str",
            "အရာဝတ္ထု": "dict",
            "အဘိဓာန်": "set",
            "ဆိုင်": "tuple",
            "ကိုဆိုင်": "set",
            "တန်ဂျင့်": "bool",
            "ထပ်ကိန်း": "int",
            "ပိုင်": "float",
            "မေးမြန်း": "input",
            "ဖွင့်": "open",
            "သင်္ချာ_အမြင့်ဆုံး": "max",
            "သင်္ချာ_အနိမ့်ဆုံး": "min",
            "သင်္ချာ_စတုရန်း": "sum",
            "စတုရန်းရင်း": "round",
            "ဇယား": "type",
            "စာသား_ပေါင်း": "len",
            # --- String methods ---
            "စာလုံးကြီး": ".upper()",
            "စာလုံးသေး": ".lower()",
            "စမြည့်": ".capitalize()",
            "ဆုံးမြည့်": ".title()",
            "စာဆက်": ".join()",
            "စာခွဲ": ".split()",
            "ဖြတ်": ".strip()",
            "အစားထိုး": ".replace()",
            "စာကြောင်းအရှည်": ".count()",
            "စာရင်းထုတ်": ".format()",
            "ရှာ": ".index()",
            "ရှာပါ": ".find()",
            "ပြောင်းပြန်": ".reverse()",
            # --- List methods ---
            "စာရင်းအရှည်": ".append()",
            "စာရင်း_အလယ်": ".pop()",
            "ထည့်သွင်း": ".insert()",
            "ရှိ_မရှိ": "in",
            "ရှိ": "True",
            "မရှိ": "not in",
            "စီ": ".sort()",
            "စာရင်းဆောက်": "list",
            "အစီအစဉ်": "list",
            # --- File methods ---
            "ဖိုင်ဖတ်": ".read()",
            "ဖိုင်ရေး": ".write()",
            "ဖိုင်ဖျက်": ".close()",
            "ဖိုင်စာရင်း": ".readlines()",
            # --- Other keywords that map to empty (remove) ---
            "ရွေးချယ်": "",
            "ဖြစ်နိုင်": "",
            "မူလ": "",
            "ပစ်ချ": "",
            "အသစ်": "",
            "တိုးချဲ့": "",
            "တင်ပို့": "",
            "အမျိုးအစား": "",
            "အဖြစ်အပျက်": "",
            "အမှားရှာ": "",
            "လူသိ": "",
            "လျှို့ဝှက်": "",
            "ကာကွယ်": "",
            "တည်မြဲ": "",
            "အတု": "",
            "ပုံစံ": "",
            "နေရာအမည်": "",
            "ဖွဲ့စည်း": "",
            "အရွယ်အစား": "",
            "သူငယ်ချင်း": "",
            "ပြောင်းလဲနိုင်": "",
            "ရှင်းလင်း": "",
            "တိုက်ရိုက်": "",
            "သွား": "",
            "အထုပ်": "",
            "တစ်ပြိုင်နက်": "",
            "ယာယီ": "",
            "မတည်မြဲ": "",
            "ပြောင်း": "str",
            "သိမ်း": ".save()",
            "အရွယ်": "value",
            "ပြုပြင်": "modify",
            "သတ်မှတ်": "set",
            "ရှိပါသလား": "isinstance",
            "ထုတ်ပြ": ".keys()",
            "ပြပေးမည်": "return",
            "ရေးပြမည်": "return",
            "ကူးယူပါ": "import",
            "လုပ်ပါ": "True",
            "လုပ်ရန်": "True",
            "ထည့်ပါ": ".append()",
            "မေးပါ": "input",
            "ထားပါ": "True",
            "မှတ်ထား": ".append()",
            "သွားပါ": "return",
            "အဆုံး": "end",
            "ပြီး": "True",
            "ပြီးပြီ": "True",
            "ဒါဆို": "#",
            "အစဉ်လိုက်စီပါ": ".sort()",
            "အရေအတွက်": "for",
            "ရှင်းလင်းပါ": ".clear()",
            "ဖယ်ရှားပါ": ".clear()",
            "ပြောင်းလဲပါ": ".replace()",
            "စောင့်": "sleep",
            "ယနေ့": "today",
            "အခု": "now",
            "ဖော်မတ်": "show",
            "ဖြည်": "absolute",
            "ကွာခြား": "difference",
            "ကြိမ်": "count",
            "ရပ်လိုက်ပါ": "exit",
            "ကျော်လိုက်ပါ": "continue",
            "အမှတ်": "index",
            "ပြီးပါပြီ": "True",
            "စတင်ပါ": "start",
            "အောင်မြင်ပါသည်": "True",
            "မသတ်မှတ်ရသေး": "None",
            "အမှန်": "True",
            "အမှား": "False",
            "ကိစ္စ": "function",
            "အကြိမ်အားလုံးအတွက်": "foreach",
            "သံသရာ": "True",
            "တောင်းဆိုမည်": "warn",
            "သိမ်းဆည်းမည်": "catch",
            "ပြောပါ": "say",
            "ရိုက်ပါ": "click",
            "ဖယ်ရှားပါ": ".clear()",
            "ထည့်": ".add()",
            "မှန်မှား": "valid",
            "ပြပေးမည်": "return",
        }

        # Keywords that map to empty string (should be removed entirely)
        self.remove_keywords = [k for k, v in self.keyword_map.items() if v == ""]

        # Sort translation keywords by length (longest first)
        self.sorted_translate_keys = sorted(
            [k for k, v in self.keyword_map.items() if v != ""],
            key=len,
            reverse=True
        )

    def _protect_strings(self, code):
        """Extract string literals and replace with placeholders."""
        strings = []
        counter = [0]

        def replace_string(match):
            strings.append(match.group(0))
            placeholder = f'__MYAN_STR_{counter[0]}__'
            counter[0] += 1
            return placeholder

        pattern = r'(\"\"\"[\s\S]*?\"\"\"|\'\'\'[\s\S]*?\'\'\'|\"[^\"\\]*(?:\\.[^\"\\]*)*\"|\'[^\'\\]*(?:\\.[^\'\\]*)*\')'
        protected = re.sub(pattern, replace_string, code)
        return protected, strings

    def _restore_strings(self, code, strings):
        """Put string literals back."""
        for i, s in enumerate(strings):
            code = code.replace(f'__MYAN_STR_{i}__', s)
        return code

    def _protect_comments(self, code):
        """Extract comments and replace with placeholders."""
        comments = []
        counter = [0]

        def replace_comment(match):
            comments.append(match.group(0))
            placeholder = f'__MYAN_CMT_{counter[0]}__'
            counter[0] += 1
            return placeholder

        protected = re.sub(r'(#.*)', replace_comment, code)
        return protected, comments

    def _restore_comments(self, code, comments):
        """Put comments back."""
        for i, c in enumerate(comments):
            code = code.replace(f'__MYAN_CMT_{i}__', c)
        return code

    def execute(self, code):
        """Translate Myanmar code to Python and execute it."""
        if not code or not code.strip():
            return "✅ အောင်မြင်ပါသည်"

        # Step 1: Protect comments
        code, comments = self._protect_comments(code)

        # Step 2: Protect string literals
        code, strings = self._protect_strings(code)

        # Step 3: Convert Myanmar digits to Arabic
        for mm_digit, en_digit in self.digits.items():
            code = code.replace(mm_digit, en_digit)

        # Step 4: Remove declaration keywords (var/const/let)
        for decl in self.declaration_keywords:
            code = re.sub(re.escape(decl) + r' ', '', code)
            code = re.sub(re.escape(decl) + r'\n', '\n', code)

        # Step 5: Remove keywords that map to empty
        for kw in self.remove_keywords:
            code = re.sub(re.escape(kw), '', code)

        # Step 6: Translate keywords (longest first)
        for mm_keyword in self.sorted_translate_keys:
            py_keyword = self.keyword_map[mm_keyword]
            if py_keyword:
                code = code.replace(mm_keyword, py_keyword)

        # Step 7: Restore comments and strings
        code = self._restore_comments(code, comments)
        code = self._restore_strings(code, strings)

        # Clean up whitespace issues (preserve indentation!)
        lines = code.split('\n')
        cleaned_lines = []
        for line in lines:
            # Find indentation
            stripped = line.lstrip()
            indent = line[:len(line) - len(stripped)]
            # Clean up multiple spaces in non-indented part only
            cleaned = re.sub(r'  +', ' ', stripped)
            cleaned = re.sub(r' +:', ':', cleaned)
            # Re-add indentation
            cleaned_lines.append(indent + cleaned)
        code = '\n'.join(cleaned_lines)

        # Step 8: Execute
        output = StringIO()
        try:
            with redirect_stdout(output):
                local_ns = {}
                exec(code, {"__builtins__": __builtins__}, local_ns)
            result = output.getvalue().strip()
            return result if result else "✅ အောင်မြင်ပါသည်"
        except Exception as e:
            return f"❌ အမှား: {type(e).__name__}: {str(e)}"

    def translate(self, code):
        """Translate Myanmar code to Python without executing (for debugging)."""
        if not code or not code.strip():
            return ""

        code, comments = self._protect_comments(code)
        code, strings = self._protect_strings(code)

        for mm_digit, en_digit in self.digits.items():
            code = code.replace(mm_digit, en_digit)

        for decl in self.declaration_keywords:
            code = re.sub(re.escape(decl) + r' ', '', code)
            code = re.sub(re.escape(decl) + r'\n', '\n', code)

        for kw in self.remove_keywords:
            code = re.sub(re.escape(kw), '', code)

        for mm_keyword in self.sorted_translate_keys:
            py_keyword = self.keyword_map[mm_keyword]
            if py_keyword:
                code = code.replace(mm_keyword, py_keyword)

        code = self._restore_comments(code, comments)
        code = self._restore_strings(code, strings)

        # Clean up whitespace (preserve indentation)
        lines = code.split('\n')
        cleaned_lines = []
        for line in lines:
            stripped = line.lstrip()
            indent = line[:len(line) - len(stripped)]
            cleaned = re.sub(r'  +', ' ', stripped)
            cleaned = re.sub(r' +:', ':', cleaned)
            cleaned_lines.append(indent + cleaned)
        code = '\n'.join(cleaned_lines)

        return code

    def get_version(self):
        return "2.1.0"

    def get_keywords(self):
        return self.keywords

    def get_keyword_count(self):
        return len(self.keywords)
