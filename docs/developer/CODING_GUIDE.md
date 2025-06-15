# 🚩 The Amnesiac Coder Guide
Instant clarity for humans and AI—friendly, practical, and readable.

## 🎯 Why This Guide Exists
This guide ensures instant understanding of your code, even if you're encountering it for the first time—no prior knowledge or context needed. It explicitly helps readers (especially AI or non-coders) quickly grasp:

- What each piece of code does.
- Why it's important or was built this way.
- Where exactly key logic and important functions are located.

📘 "The Art of Readable Code":
"Code should be clear enough to understand at a glance."

## 📝 How to Structure Your Files (Clearly)
Start every code file with these 3 clear sections:

### 🌟 PURPOSE
Clearly state, in a single sentence, exactly what this file accomplishes.

📙 "A Philosophy of Software Design": "Explicitly document the intent to reduce cognitive load."

### 🔗 DEPENDENCIES
Explicitly list external modules, APIs, or files this code needs to do its job.

📗 "Living Documentation": "Clearly document dependencies and interfaces right alongside the code."

### 📑 STRUCTURE (Emoji-Enhanced TOC with Line Numbers)
Clearly outline each important function or logic block with intuitive emojis and exact line numbers.

Automatically maintained by AI to ensure accuracy.

🎨 "Beautiful Code": "Structure your code visually and intuitively, aiding rapid understanding."

**Practical Example:**

```python
"""
🌟 PURPOSE:
Fetch news articles, analyze sentiment, produce summaries, and store results.

🔗 DEPENDENCIES:
- sentiment_analyzer.py (sentiment scoring)

📑 CONTENTS:
L12 📥 fetch_html(url)          — retrieve webpage HTML
L30 🧹 parse_article(html)      — extract main article text
L55 🧠 analyze_sentiment(text)  — determine sentiment
L75 📄 summarize_text(text)     — create concise summary
L95 📂 save_json(data)          — save structured data
L115 🚀 example_usage()         — runnable demonstration
"""
```

## 🧑‍💻 Clear, Human-Friendly Function Comments
Clearly and briefly explain every major function in simple language. Each comment should:

- State exactly what the function does.
- If the reasoning isn't obvious, add a second brief comment explicitly explaining why the function exists.

Example:

```python
# Fetch HTML from a webpage, retrying automatically if needed.
# (Retries reduce issues with temporary network outages.)
def fetch_html(url):
    pass
```

📘 "The Art of Readable Code":
"Explain why, not just what—give clarity where confusion could happen."

## 📘 🐣 Friendly Contextual Notes ("Dummies" and "ELI5")
Choose exactly one of these friendly notes only when extra clarity is needed:

**📘 "For Dummies" Sidebar:** Clearly explain subtle decisions or logic details.

```python
response = requests.get(url, timeout=10)

### 📘 FOR DUMMIES:
# 10 seconds is long enough for most responses,
# short enough not to cause delays.
###
```

**🐣 "ELI5" Explanation:** Playful, intuitive metaphor for tricky logic.

```python
for attempt in range(3):
    response = requests.get(url)
    if response.ok:
        return response.text
    # 🐣 ELI5: If the website doesn't answer first time, politely ask again.
```

Never use both in the same location—contextually choose just one.

📙 "A Philosophy of Software Design":
"Explicitly document decisions, but never redundantly—clarity comes from simplicity."

## 🔍 Keyword Tags (AI & Human Searchability)
Clearly tag critical functions with concise, searchable keywords. It helps you and your AI immediately find key logic.

Example:

```python
# 🔍 KEYWORDS: HTML fetching, retries
def fetch_html(url):
    pass
```

📗 "Living Documentation":
"Keep your documentation explicitly searchable for easy navigation."

## 🎨 Visual & Structural Clarity (Simple, Intuitive Formatting)
Clearly use visual separators or intuitive structures to group related code. Simple, consistent visual patterns make understanding immediate:

Example:

```python
# ----- Fetching and Parsing -----
def fetch_html(url):
    pass

def parse_article(html):
    pass

# ----- Sentiment and Summarization -----
def analyze_sentiment(text):
    pass
```

🎨 "Beautiful Code":
"Code structure should immediately guide the reader visually, making patterns obvious."

## ✅ General Coding Best Practices (From the Experts)

**📘 Boswell & Foucher:**
- Use simple, intention-revealing function and variable names.
- Write comments clearly explaining the reasoning behind tricky logic.
- Make important logic easy to find visually.

**📗 Cyrille Martraire:**
- Keep documentation alive and always accurate—auto-update whenever possible.
- Embed runnable examples (executable documentation) to clearly verify behavior.

**📙 John Ousterhout:**
- Explicitly document interfaces and dependencies upfront.
- Avoid redundancy—clarity and simplicity reduce cognitive load.

**🎨 Beautiful Code (Oram & Wilson):**
- Use intuitive visual structures and occasional metaphors to make code logic immediately clear and memorable.

## 🚫 What to Avoid (To Keep Things Fun & Clear)
❌ Don't duplicate explanations in multiple places.

❌ Avoid overly verbose or redundant comments—concise and clear is best.

❌ Don't mix "For Dummies" and ELI5 explanations together; contextually choose one.

## 🤖 Maintenance (Easy and Automatic)
Let your AI automatically keep line numbers in your emoji-enhanced TOC accurate. Relax, it's handled.

📗 "Living Documentation":
"Automate your documentation—make updates painless and reliable."

## 🎯 Final Thought
Your code should always feel like a clear, friendly story—instantly understood, fun to explore, and easy to maintain. Whether you're an AI, coder, or curious non-coder, this guide ensures every code encounter feels welcoming and instantly clear.

📘 "The Art of Readable Code":
"Writing code is simple. Reading code—that's the real art form."

