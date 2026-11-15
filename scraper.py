import requests
from bs4 import BeautifulSoup

url = "https://dvsteam.vn/id-apple-shadowrocket"

try:
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # البحث عن الإيميل وكلمة المرور من الموقع الأصلي
        email = "غير متوفر حالياً"
        password = "غير متوفر حالياً"
        
        # محاولة استخراج الحسابات من عناصر الصفحة
        code_blocks = soup.find_all(['code', 'span', 'p', 'div'])
        for block in code_blocks:
            text = block.get_text().strip()
            if '@' in text and '.' in text and len(text) < 50 and ' ' not in text:
                email = text
                break
                
        # (اختياري) محاولة البحث عن الباسورد بقرب الإيميل أو النصوص المتاحة
        for block in code_blocks:
            text = block.get_text().strip()
            if len(text) >= 6 and len(text) <= 20 and '@' not in text and any(c.isupper() for c in text) and any(c.isdigit() for c in text):
                password = text
                break

        # تصميم الصفحة الاحترافي الذي سيتم تحديثه تلقائياً
        html_content = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kurd0oAccounts</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col justify-between p-4 font-sans">
    
    <!-- Header / Branding -->
    <header class="text-center pt-8 pb-4">
        <div class="inline-block p-3 bg-gradient-to-tr from-amber-500/20 to-blue-500/20 rounded-2xl mb-3 border border-slate-800 shadow-inner">
            <i class="fa-solid fa-shield-halved text-3xl text-amber-400"></i>
        </div>
        <h1 class="text-3xl font-extrabold tracking-wide bg-gradient-to-r from-amber-400 to-yellow-200 bg-clip-text text-transparent">Kurd0oAccounts</h1>
        <a href="https://t.me/Kurd0o1" target="_blank" class="inline-flex items-center gap-2 mt-2 px-4 py-1.5 bg-blue-500/10 border border-blue-500/20 text-blue-400 text-sm font-medium rounded-full hover:bg-blue-500/20 transition-all">
            <i class="fa-brands fa-telegram text-base"></i> @Kurd0o1
        </a>
    </header>

    <!-- Main Content (Account Card) -->
    <main class="max-w-md mx-auto my-auto w-full">
        <div class="bg-slate-900/80 backdrop-blur-md border border-slate-800/80 rounded-2xl p-5 shadow-xl relative overflow-hidden">
            <div class="absolute top-0 right-0 left-0 h-1 bg-gradient-to-r from-amber-500 to-blue-500"></div>
            
            <div class="flex items-center justify-between mb-4">
                <span class="text-xs font-semibold px-2.5 py-1 bg-amber-500/10 text-amber-400 rounded-lg border border-amber-500/20">حساب Apple ID نشط</span>
                <span class="text-xs text-slate-400"><i class="fa-regular fa-clock ml-1"></i>تحديث تلقائي</span>
            </div>

            <!-- Email Field -->
            <div class="mb-3">
                <label class="block text-xs text-slate-400 mb-1 font-medium">البريد الإلكتروني</label>
                <div class="flex items-center justify-between bg-slate-950 border border-slate-800 rounded-xl p-3">
                    <span dir="ltr" id="account-email" class="text-blue-400 font-mono text-sm select-all tracking-wider">{email}</span>
                    <button onclick="copyText('account-email', this)" class="text-xs bg-slate-800 hover:bg-slate-700 text-slate-300 px-3 py-1.5 rounded-lg transition-colors flex items-center gap-1">
                        <i class="fa-regular fa-copy"></i> نسخ
                    </button>
                </div>
            </div>

            <!-- Password Field -->
            <div>
                <label class="block text-xs text-slate-400 mb-1 font-medium">كلمة المرور</label>
                <div class="flex items-center justify-between bg-slate-950 border border-slate-800 rounded-xl p-3">
                    <span dir="ltr" id="account-pass" class="text-emerald-400 font-mono text-sm select-all tracking-wider">{password}</span>
                    <button onclick="copyText('account-pass', this)" class="text-xs bg-slate-800 hover:bg-slate-700 text-slate-300 px-3 py-1.5 rounded-lg transition-colors flex items-center gap-1">
                        <i class="fa-regular fa-copy"></i> نسخ
                    </button>
                </div>
            </div>
        </div>
    </main>

    <!-- Footer -->
    <footer class="text-center text-xs text-slate-500 pb-4">
        جميع الحقوق محفوظة &copy; Kurd0oAccounts
    </footer>

    <!-- Copy Script -->
    <script>
        function copyText(elementId, btn) {{
            const text = document.getElementById(elementId).innerText;
            navigator.clipboard.writeText(text).then(() => {{
                const originalHTML = btn.innerHTML;
                btn.innerHTML = '<i class="fa-solid fa-check text-emerald-400"></i> تم النسخ';
                btn.classList.add('bg-emerald-500/20', 'text-emerald-300');
                setTimeout(() => {{
                    btn.innerHTML = originalHTML;
                    btn.classList.remove('bg-emerald-500/20', 'text-emerald-300');
                }}, 1500);
            }});
        }}
    </script>
</body>
</html>
"""
        
        # حفظ النتائج مباشرة في ملف index.html الرئيسي للموقع
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html_content)
            
        print("تم جلب وتحديث الموقع بنجاح!")

except Exception as e:
    print(f"حدث خطأ: {e}")
