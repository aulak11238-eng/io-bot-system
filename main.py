import asyncio
import random
import uuid
import os
from datetime import datetime
import tweepy
import config

class IODarkBot:
    def __init__(self, bearer_token):
        self.client = tweepy.Client(bearer_token=bearer_token)
        self.prefixes = ["Net", "Signal", "Echo", "Data", "Core", "Node"]
        self.suffixes = ["_Op", "_X", "_Bot", "_Net", "_Eye", "_Watch"]
        
    def generate_identity(self):
        """สร้างตัวตนปลอมแบบสุ่มที่ไม่ซ้ำกัน"""
        uid = uuid.uuid4().hex[:4]
        name = f"{random.choice(self.prefixes)}{random.choice(self.suffixes)}{uid}"
        bio = f"Decentralized observer. No agenda. #IO"
        return name, bio

    async def post_payload(self, message):
        """โพสต์ข้อความแบบ Asynchronous"""
        try:
            # สุ่ม Hashtag เพื่อความหลากหลาย
            hashtag = random.choice(config.CAMPAIGN_HASHTAGS)
            final_msg = message.format(hashtag=hashtag)
            
            response = self.client.create_tweet(text=final_msg, reply_to=None)
            
            if response.data:
                print(f"[SUCCESS] ID: {response.data.id} | Msg: {final_msg[:30]}...")
            else:
                print("[FAIL] No response data.")
        except tweepy.TweepyException as e:
            print(f"[ERROR] {e}")

    async def run_dark_campaign(self):
        """รันแคมเปญโจมตีข้อมูล"""
        print(f"--- STARTING IO OPERATION AT {datetime.now()} ---")
        
        tasks = []
        for i in range(config.MAX_TWEETS_PER_RUN):
            # สุ่มเลือกข้อความ
            msg_template = random.choice(config.MESSAGE_TEMPLATES)
            tasks.append(self.post_payload(msg_template))
            
            # เว้นเวลาสุ่มเพื่อเลียนแบบมนุษย์ (Jitter)
            delay = random.uniform(config.SLEEP_MIN, config.SLEEP_MAX)
            await asyncio.sleep(delay)
            
            # รัน Task (ในกรณีที่ต้องการรันพร้อมกันจริงๆ ให้ใช้ asyncio.gather)
            # แต่ที่นี่เราทำแบบ Sequential with Jitter เพื่อลด Suspicion
            await tasks[-1]

        print("--- OPERATION COMPLETE ---")

async def main():
    token = config.API_BEARER_TOKEN
    if not token:
        print("ERROR: Bearer Token missing in Environment Variables!")
        return

    bot = IODarkBot(token)
    await bot.run_dark_campaign()

if __name__ == "__main__":
    asyncio.run(main())
  
