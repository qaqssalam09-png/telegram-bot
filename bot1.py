import requests
import time
import random
from datetime import datetime

# ============================================
# 14 BOT TOKENİ
# ============================================

BOTS = [
    '8315663092:AAGOSoyhk9Bq-RqcuA4bjtw7LyfSFRh87GY',
    '8299455812:AAEvXvgq3vqRaJZ1s8_1TDH1ICRmh8ShAIM',
    '8298275936:AAFQDibFr1XMuTGyCNllKxFEwJm5LTcHa24',
    '8672903755:AAGltT1TH1uRgS8zTrcmeJN65_YnksH2cIU',
    '8617751410:AAH2Q2xygCG4qhomRBFjkd1wp_dlmmVUpMc',
    '8424525126:AAG_q7WXo3CaELcgUz55OxCBsdl6roPxMGY',
    '8711337681:AAFp4E-kvutw85LHYX_odYGslvKmMaDabUU',
    '8734706618:AAFRFrxObAFmxjl_2Zh7PGjuwgWef6Hn2QM',
    '8693891916:AAEOkJlo-7MCMwjKLDopGSPxaFjx13ooNKU',
    '8697754161:AAFgEImjA6yjmngZsWG2wsvZkuWS44sl64k',
    '8721459890:AAG2dhSn6L9sGgIYUf7ti7wo2AJ_MvC01KA',
    '8718987911:AAHD_3GYg6EpP6PEBNvGWV_goY8rgqnRj3o',
    '8798837330:AAENNhYOj7UvTDQZdEVFBKCCFRw-jwhGRTY',
    '8604773669:AAFUC0OrbIeakeJ7HbdOb_KKRDGvKxR-fbU'
]

# ============================================
# 1 QRUP ID
# ============================================

CHAT_ID = '-1003092491361'

# ============================================
# MESAJ
# ============================================

MESSAGE = "Salam"

# ============================================
# BOT SİSTEMİ
# ============================================

print("=" * 50)
print("🤖 14 BOT - 1 QRUP")
print("=" * 50)
print(f"Bot sayı: {len(BOTS)}")
print(f"Qrup ID: {CHAT_ID}")
print(f"Mesaj: {MESSAGE}")
print("=" * 50)
print("Bot işə başlayır...")
print("Dayandırmaq: Ctrl+C")
print("=" * 50)

counter = 0
bot_index = 0

try:
    while True:
        # Növbəti bot
        token = BOTS[bot_index]
        bot_index = (bot_index + 1) % len(BOTS)
        
        counter += 1
        
        try:
            url = f"https://api.telegram.org/bot{token}/sendMessage"
            data = {"chat_id": CHAT_ID, "text": f"{MESSAGE} #{counter}"}
            
            response = requests.post(url, json=data, timeout=10)
            
            if response.status_code == 200:
                print(f"[{datetime.now().strftime('%H:%M:%S')}] ✅ Bot {bot_index+1} - Mesaj #{counter}")
            else:
                print(f"[{datetime.now().strftime('%H:%M:%S')}] ❌ Bot {bot_index+1} - Xəta: {response.status_code}")
                
        except Exception as e:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] ⚠️ Bot {bot_index+1} - Bağlantı xətası")
        
        # 5 saniyə gözlə (hər bot növbə ilə)
        time.sleep(5)
        
except KeyboardInterrupt:
    print(f"\n🛑 Bot dayandırıldı. Cəmi {counter} mesaj")
