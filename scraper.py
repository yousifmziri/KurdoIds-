import requests
from bs4 import BeautifulSoup

url = "https://dvsteam.vn/id-apple-shadowrocket"

try:
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        email = "غير متوفر حالياً"
        password = "غير متوفر حالياً"
        
        # البحث الذكي داخل كل النصوص والرموز بصفحة dvsteam
        elements = soup.find_all(['code', 'span', 'p', 'div', 'td', 'strong'])
        
        for el in elements:
            text = el.get_text().strip()
            # البحث عن البريد الإلكتروني الصحيح
            if '@' in text and '.' in text and len(text) < 60 and ' ' not in text and '@js001.club' in text:
                email = text
                break
        
        # إذا ما لكى نطاق معين، ياخذ أي إيميل صالح
        if email == "غير متوفر حالياً":
            for el in elements:
                text = el.get_text().strip()
                if '@' in text and '.' in text and len(text) < 50 and ' ' not in text:
                    email = text
                    break

        for el in elements:
            text = el.get_text().strip()
            # البحث عن كلمة مرور مطابقة للمواصفات (أحرف وأرقام)
            if len(text) >= 6 and len(text) <= 25 and '@' not in text and any(c.isupper() for c in text) and any(c.isdigit() for c in text):
                password = text
                break

        # تصميمك الأصلي والفخم المرتبط بالتحديث التلقائي
        html_content = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kurd0oAccounts</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;800&display=swap');
        body {{ font-family: 'Tajawal', sans-serif; background-color: #0B0F19; color: #F3F4F6; }}
    </style>
</head>
<body class="min-h-screen flex flex-col justify-between items-center p-4">
    
    <div class="w-full max-w-md mx-auto flex flex-col items-center pt-8">
        <!-- Logo / Icon -->
        <div class="w-16 h-16 bg-gradient-to-tr from-amber-500 to-yellow-300 rounded-2xl flex items-center justify-center shadow-lg shadow-amber-500/20 mb-4">
            <i class="fa-solid fa-shield-halved text-2xl text-slate-950"></i>
        </div>
        
        <h1 class="text-2xl font-extrabold tracking-wide text-amber-400 mb-2">Kurd0oAccounts</h1>
        
        <!-- Telegram Channel Badge -->
        <a href="https://t.me/Kurd0o1" target="_blank" class="flex items-center gap-2 px-4 py-1.5 bg-slate-900 border border-slate-800 rounded-full text-blue-400 text-xs font-semibold shadow hover:bg-slate-800 transition">
            <span>Kurd0o1@</span>
            <i class="fa-brands fa-telegram text-blue-400"></i>
        </a>
    </div>

    <!-- Main Card -->
    <main class="w-full max-w-md mx-auto my-6">
        <div class="bg-slate-900/90 backdrop-blur border border-slate-800/80 rounded-2xl p-5 shadow-2xl relative overflow-hidden">
            <div class="absolute top-0 right-0 left-0 h-1 bg-gradient-to-r from-amber-500 via-blue-500 to-indigo-500"></div>
            
            <div class="flex items-center justify-between mb-5">
                <span class="text-xs font-medium text-slate-400 flex items-center gap-1">
                    <i class="fa-regular fa-clock text-amber-400"></i> محدث الآن
                </span>
                <span class="text-xs font-bold px-3 py-1 bg-amber-500/10 text-amber-400 rounded-lg border border-amber-500/20">حساب Apple ID جاهز</span>
            </div>

            <!-- Email Field -->
            <div class="mb-4">
                <label class="block text-xs text-slate-400 mb-1.5 font-medium">البريد الإلكتروني</label>
                <div class="flex items-center justify-between bg-slate-950 border border-slate-800 rounded-xl p-3 shadow-inner">
                    <button onclick="copyText('account-email', this)" class="text-xs bg-slate-800 hover:bg-slate-700 text-slate-200 px-3 py-1.5 rounded-lg transition flex items-center gap-1.5">
                        <i class="fa-regular fa-copy"></i> نسخ
                    </button>
                    <span dir="ltr" id="account-email" class="text-slate-200 font-mono text-sm select-all tracking-wider">{email}</span>
                </div>
            </div>

            <!-- Password Field -->
            <div>
                <label class="block text-xs text-slate-400 mb-1.5 font-medium">كلمة المرور</label>
                <div class="flex items-center justify-between bg-slate-950 border border-slate-800 rounded-xl p-3 shadow-inner">
                    <button onclick="copyText('account-pass', this)" class="text-xs bg-slate-800 hover:bg-slate-700 text-slate-200 px-3 py-1.5 rounded-lg transition flex items-center gap-1.5">
                        <i class="fa-regular fa-copy"></i> نسخ
                    </button>
                    <span dir="ltr" id="account-pass" class="text-slate-200 font-mono text-sm select-all tracking-wider">{password}</span>
                </div>
            </div>
        </div>
    </main>

    <!-- Footer -->
    <footer class="w-full text-center text-xs text-slate-500 pb-2">
        جميع الحقوق محفوظة &copy; Kurd0oAccounts
    </footer>

    <!-- Copy Script -->
    <script>
        function copyText(elementId, btn) {{
            const text = document.getElementById(elementId).innerText;
            navigator.clipboard.writeText(text).then(() => {{
                const originalHTML = btn.innerHTML;
                btn.innerHTML = '<i class="fa-solid fa-check text-emerald-400"></i> تم النسخ';
                setTimeout(() => {{
                    btn.innerHTML = originalHTML;
                }}, 1500);
            }});
        }}
    </script>
</body>
</html>
"""
        
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html_content)
            
        print("تم تحديث الكود وسحب الحساب بنجاح!")

except Exception as e:
    print(f"خطأ: {e}")
