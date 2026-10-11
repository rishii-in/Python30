print("="*50)
print("     AI Personal Assistant   ")
print("="*50)
print()
print(" Hello! I am your AI Personal Assistant. How can I help you today?")
print()
print("Available Commands:")
print("-"*50)
print("Hello, Hi, How are you, Who are you, Help, Study, Python, Practice, Motivation, Tired, Joke, Fun fact, Music, Weather, Movie, Career, Project, Cricket, Security, Food, Tfi, Thank you, Bye, Exit")
print(""*50)
commands = {
    "hello": "Hello! 👋 How can I help you?",
    "hi": "Hi! 😊 Nice to meet you.",
    "how are you": "I'm doing great! 🤖 Thanks for asking.",
    "who are you": "I am your AI Personal Assistant 🤖.",
    
    "help": "Try: hello, study, python, motivation, joke, music, weather, career, exit.",
    
    "study": "📚 Focus on one topic and practice it with code.",
    "python": "🐍 Python is great for AI, ML, automation, and data science.",
    "practice": "💻 Don't just read code. Write and run it yourself!",
    
    "motivation": "🔥 Keep going! Consistency is more important than perfection.",
    "tired": "😌 Take a short break and come back refreshed.",
    
    "joke": "😂 Why do programmers prefer dark mode? Because light attracts bugs!",
    "fun fact": "💡 Python was named after Monty Python.",
    
    "music": "🎵 Music mode activated! Whats your favorite song",
    "weather": "🌤️ Weather information is updated ",
    "movie": "🎬 Movie mode activated! Whats your favorite movie",
    "career": "💼 Build skills through projects, practice, and interview preparation.",
    "project": "🚀 Build projects that solve real-world problems.",
    "cricket": "🏏 Cricket is mostly about hitman,king,thala",
    "security": "🔐 Never share your passwords or OTPs with anyone.",
    "food": "🍽️ What are you craving today? Something spicy, sweet, or healthy?",
    "tfi": "📰 Tfi means prabhas,allu arjun,Nani,ntr,mahesh babu,pspk,ramcharan,etc....",
    "thank you": "You're welcome! 😊",
    "bye": "Goodbye! 👋 Keep learning!",
    "exit": "Assistant shutting down... 👋"
 
}
while True:
    user=input("\nPlease enter a command:")
    user=user.lower().strip()
    if user in commands:
        print("\n🤖 Assistant:",commands[user])
    else:
        print("\n🤖 Assistant: Sorry, I didn't understand that command. Please try again or type 'help' for a list of commands.")
    if user == "exit":
        print("\n🤖 Assistant: Goodbye! Have a great day! 👋")
        break