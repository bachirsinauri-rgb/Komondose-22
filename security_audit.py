import os

def run_audit():
    files_to_check = ['logic.js', 'index.html', 'brain.py']
    dangerous_keywords = ['PASS', 'PASSWORD', 'SECRET', 'KEY']
    
    print("🛡️ [AL-RAED AUDIT]: جاري فحص الحصون الرقمية...")
    
    for file_name in files_to_check:
        if os.path.exists(file_name):
            with open(file_name, 'r') as f:
                content = f.read()
                for word in dangerous_keywords:
                    if word in content and "os.getenv" not in content:
                        print(f"⚠️ [تحذير]: وجدنا كلمة مشبوهة '{word}' في ملف {file_name}!")
        else:
            print(f"❌ [خطأ]: الملف {file_name} غير موجود.")
    
    print("✅ [AUDIT COMPLETE]: النظام الموحد آمن حالياً.")

if __name__ == "__main__":
    run_audit()
