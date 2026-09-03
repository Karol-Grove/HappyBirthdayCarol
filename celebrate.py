import time
import sys

def celebrate_carol():
    print("=" * 60)
    print("🎉 HAPPY BIRTHDAY CAROL! 🎉")
    print("🐍 Senior Python Developer & Chief Bug Slayer")
    print("=" * 60)
    
    messages = [
        "⚡ Initializing birthday party sequence...",
        "🍰 Baking infinite chocolate cake...",
        "🚀 Deploying zero-bug Python backend...",
        "✨ Status: 200 OK | All tests passing! Have a wonderful day!"
    ]
    
    for msg in messages:
        print(msg)
        time.sleep(0.2)
    
    print("\n🎂 HAPPY BIRTHDAY CAROL! 🥳🎉🐍\n")

if __name__ == "__main__":
    celebrate_carol()
