# 🚀 **Real-Time Event Exploration System: Developer Handoff Document**

**Goal:**
Build a modular, AI-driven system that conversationally guides users through discovering, analyzing, retrieving, and organizing real-time event information.

---

## 🤖 **FOR AI ASSISTANTS: CONTEXT & CONTINUITY SYSTEM**

> **⚡ CRITICAL**: If you're an AI assistant working on this project, read these files FIRST:

### 📋 **1. Session Context Files**
- **`AI_SESSION_LOG.md`** - Complete session history, actions taken, and project context
- **`CODEBASE_MAP.md`** - Detailed architecture map with implementation status
- **Recent Git commits** - Use `git log --oneline -10` to see latest changes

### 🎯 **2. Dynamic Prompt System** 
**IMPORTANT**: This project now uses **dynamic, context-aware prompts** instead of hardcoded templates.

- **📁 `modules/dynamic_prompts.py`** - Context-aware prompt generation system
- **🔧 Usage**: `DynamicPromptGenerator` creates prompts based on event type, urgency, and context
- **⚠️ Note**: Static prompts in `prompts/prompts.txt` are now legacy - use dynamic system

### 🛠️ **3. AI Session Management**
- **📱 `ai_session_update.py`** - CLI utility to log your actions
- **Usage**: `python ai_session_update.py --action "description" --files "file1,file2"`
- **📊 Updates**: Automatically updates session logs with git status and changes

### 🎨 **4. Code Style Guidelines**
- **Emojis for visual scanning**: 🔍 🚀 ⚠️ 💡 🔧 📊 🎯
- **Self-documenting code**: Clear variable names and comprehensive docstrings
- **Status indicators**: ✅ implemented, ❓ needs review, 🔄 in progress

---

## 📌 **1. Overview (High-Level Description)**

* Clearly explain the system's overall purpose.
* Summarize conversational interaction flow.
* Highlight modular design and dynamic prompting principles.

---

## 📂 **2. Directory & File Structure**

```
real time scanner/
├── 🤖 AI_SESSION_LOG.md           # 📋 Session tracking & context
├── 🗺️ CODEBASE_MAP.md            # 📊 Architecture documentation  
├── 🔧 ai_session_update.py        # 🛠️ AI session management utility
│
├── modules/                       # 🏗️ Core processing pipeline
│   ├── 🎯 dynamic_prompts.py      # ✅ Context-aware prompt generation
│   ├── step_0_trending_events.py  # ❓ Event detection (needs implementation)
│   ├── step_1_event_analysis.py   # ❓ Analysis engine (needs implementation)
│   ├── step_2_content_retrieval.py # ❓ Content fetcher (needs implementation)
│   ├── step_3_data_normalization.py # ❓ Data cleaner (needs implementation)
│   ├── step_4_final_integration.py # ❓ Final integration (needs implementation)
│   ├── models.py                   # ❓ Data models (needs implementation)
│   ├── utils.py                    # ❓ Helper functions (needs implementation)
│   └── __init__.py                 # ✅ Package initializer
│
├── prompts/                       # 💭 AI prompt management
│   ├── prompts.txt                 # 📄 Legacy static prompts (superseded)
│   └── __init__.py                 # ✅ Package initializer
│
├── results/                       # 📊 Output storage
│   └── __init__.py                 # ✅ Package initializer
│
├── requirements.txt               # 📋 Dependencies
├── .env.template                  # 🔐 Environment config template
└── README.md                      # 📖 This documentation
```

**Status Legend**: ✅ Implemented | ❓ Needs Implementation | 🔄 In Progress

---

## 🧩 **3. Module Descriptions & Responsibilities**

Clearly define each module's input, output, and main task:

### **3.1 Trending Events (`step_0_trending_events.py`)**

* **Input:** None (initial launch).
* **Output:** List of trending events (title, description, location, emoji).
* **Task:** Retrieve real-time trending events from an AI/API.

### **3.2 Event Analysis & Search Setup (`step_1_event_analysis.py`)**

* **Input:** User-selected event (from module 0).
* **Output:** Event summary, affected locations, exact search queries (Twitter, YouTube, Official sources).
* **Task:** AI dynamically generates overview and queries for subsequent searches.

### **3.3 Content Retrieval (`step_2_content_retrieval.py`)**

* **Input:** Search queries dynamically generated in Step 1.
* **Output:** Previews & detailed data from Twitter, YouTube, Official sources.
* **Task:** Execute searches, provide previews first, await user confirmation, then retrieve detailed data.

### **3.4 Data Normalization (`step_3_data_normalization.py`)**

* **Input:** Raw data from previous content retrieval.
* **Output:** Cleaned, structured, standardized JSON data.
* **Task:** Normalize metadata, timestamps, engagement metrics, clearly organize data for final step.

### **3.5 Final Integration & Mapping (`step_4_final_integration.py`)**

* **Input:** Normalized data from previous step.
* **Output:** Map-ready structured JSON data (coordinates, labels, categories).
* **Task:** Assign geo-coordinates, labels clearly for easy integration into YouMap.

---

## 📄 **4. Prompts Document Specification (`prompts/prompts.txt`)**

Single, clearly organized Markdown file holding all AI prompts, separated clearly with section headers:

```
### Trending Events Discovery Prompt
(prompt text)

---

### Event Analysis & Search Setup Prompt
(prompt text)

---

### Twitter Retrieval Prompt
(prompt text)

---

### YouTube Retrieval Prompt
(prompt text)

---

### Official Reports Retrieval Prompt
(prompt text)

---

### Final Integration Prompt
(prompt text)
```

* Clearly specify placeholders (`[Dynamic Search Phrase]`) dynamically filled from previous AI outputs.

---

## 🔄 **5. Dynamic Prompt Logic (Critical Instruction)**

* Never hardcode prompts within modules.
* Dynamically inject context from previous AI outputs at each step.
* Clearly instruct AI to rely strictly on previously generated dynamic content.

**Example instruction in modules:**

```python
prompt = load_prompt('Twitter Retrieval Prompt').replace('[Dynamic Search Phrase]', previous_step_query)
```

---

## 🗃 **6. Output File Naming & Saving Standards**

* Automatically save each step's output in the `results/` directory.
* Clearly structured filenames:
  `[step_name]_[event_name]_[timestamp].json`
  Example: `twitter_preview_power_outage_SF_20250615_1220.json`

---

## ✅ **7. User Interaction Flow & Checkpoints**

Clearly structured conversational checkpoints at each retrieval step:

1. Display brief preview.
2. Prompt user clearly: "Fetch detailed results? (Yes/No): \_\_"
3. Only proceed after explicit user confirmation.

---

## 🛠 **8. Technical Stack & Recommendations**

* Python as primary language.
* OpenAI API (GPT models) recommended for AI-powered tasks.
* JSON clearly structured outputs for data portability.
* Optionally, cloud integration (AWS, Google Cloud) for scaling.

---

## 🚨 **9. Sprint's Essential Reminders for Development**

* Keep modules clearly independent and focused.
* Maintain clear, dynamic contextual chaining between modules.
* Explicitly document prompt placeholders clearly for dynamic replacements.
* Ensure conversational and simple user interactions.

---

## 🎯 **10. Next Steps (Clear Immediate Actions)**

1. Set up repository and file structure exactly as specified.
2. Populate prompt document (`prompts.txt`) clearly.
3. Build foundational modules sequentially:

   * Step 0 (Trending Events retrieval)
   * Step 1 (Event Analysis & dynamic query generation)
   * Steps 2–4 (Content retrieval, normalization, integration)
4. Test conversational interaction flow iteratively.

---

This is exactly the clear, practical, complete developer handoff document you need—ready for immediate coding action.

**Let's sprint to build! 🚀**

---

# 📝 **PROMPT EXAMPLES FOR EACH MODULE** (like psudo-code you can use to understand the way the system works with the AI)

## 🔎 **Module 0: Trending Events Discovery**

```
You're an AI-powered news scout. Quickly identify 7 trending real-time events happening now. For each event, clearly provide:

- Event Title
- Brief one-line description  
- Primary Location
- Relevant Emoji for instant recognition

Format it as a numbered list. Only include real-world events happening right now. GO!
```

---

## 🎯 **Module 1: Event Analysis 8 Search Planning**
*Assuming user selected "LA Protest 2025"*

```
You're an expert analyst AI. The selected event is: **LA Protest 2025**

### 📌 SUMMARY:
Provide a concise 2–3 sentence overview describing:
- Why and where the protest is happening
- What's currently unfolding

### 📍 LOCATIONS:
List all key LA neighborhoods impacted by the protest today.

### 🗂 INFORMATION CATEGORIES 8 SEARCH PLAN:
Choose exactly 4 relevant real-time content categories to comprehensively cover this event.

Structure exactly like this:

**Twitter Updates**
- Optimized Search Query: "[provide exact query]"
- Why It's Useful: Social media updates from eyewitnesses, organizers, and official voices.

**YouTube Live 8 Clips**
- Optimized Search Query: "[provide exact query]"
- Why It's Useful: Real-time visual coverage providing situational awareness.

**Official Reports**
- Optimized Search Query: "[provide exact query using official domains like whitehouse.gov, cityofla.org, ca.gov, lapdonline.org]"
- Why It's Useful: Verified statements from government or authoritative official sources.

**Live Webcams (Live YouTube or Google video feeds)**
- Optimized Search Query: "[provide exact query searching live webcams or currently live video streams]"
- Why It's Useful: Real-time visuals of protest areas directly from live webcams or streams.

Finally, clearly produce an expert-level subtask prompt for **Twitter Updates** using this template:

> You're an expert AI [Category] investigator.  
> Use this exact query: "[QUERY]"  
> Retrieve top preview items and await confirmation before deep dive.
```

---

## 🌐 **Module 2A: Twitter Expert Subtask Prompt**

```
You're an expert AI Twitter investigator.

Search Twitter immediately using this exact query:
"[DYNAMIC TWITTER QUERY FROM MODULE 1]"

Fetch the top 3–5 most relevant tweets, prioritizing verified sources, protest organizers, and influential accounts. Include clearly:

- Author username
- Exact tweet content
- Tweet timestamp
- Likes 8 retweets count
- Direct URL

First, briefly preview these results. Await approval before retrieving full results.
```

---

## 📹 **Module 2B: YouTube Expert Subtask Prompt**

```
You're an expert AI YouTube investigator.

Immediately search YouTube using this exact query:
"[DYNAMIC YOUTUBE QUERY FROM MODULE 1]"

Find the top 2–3 authoritative recent videos or live streams related to "LA Protest 2025". Clearly provide each item's:

- Channel name
- Video title
- One-sentence summary
- Upload or live timestamp
- View and like counts
- Direct URL

Preview these results first. Await approval before deeper retrieval.
```

---

## 🏛 **Module 2C: Official Reports Expert Subtask Prompt**

```
You're an expert AI investigator for official sources.

Immediately perform a web search using this exact query:
"[DYNAMIC OFFICIAL REPORTS QUERY FROM MODULE 1]"

Specifically target authoritative sources from official websites such as whitehouse.gov, cityofla.org, ca.gov, lapdonline.org, or UN.org.

Clearly return the top 2–3 official statements or reports, including:

- Agency or official source name
- Report title
- One-line summary
- Exact publication timestamp
- Direct URL

Preview results before retrieving further details.
```

---

## 🎥 **Module 2D: Live Webcams Expert Subtask Prompt**

```
You're an expert AI investigator for live webcams and live video streams.

Use this exact query now:
"[DYNAMIC LIVE WEBCAM QUERY FROM MODULE 1]"

Specifically search YouTube Live or Google Videos for webcams or live streaming video actively broadcasting "LA Protest 2025".

Clearly provide the top 2 real-time feeds including:

- Stream title
- Current live status (confirm actively live: yes/no)
- Viewer count
- Direct URL

Briefly preview these results. Await confirmation before retrieving additional details.
```

---

## 🗂 **Module 3: Data Normalization 8 Organization**

```
You've now gathered data on **LA Protest 2025**.

Normalize and structure data exactly like this:

- Convert all timestamps to ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ)
- Standardize engagement metrics (likes, views, retweets) clearly and consistently
- Group all entries clearly by category: Twitter, YouTube, Official, Webcam
- Summaries clearly limited to 25 words or fewer

Produce final structured JSON exactly like:

````json
{
  "event_name": "LA Protest 2025",
  "locations": ["Downtown LA", "City Hall", "Federal Building"],
  "twitter": [...],
  "youtube": [...],
  "official": [...],
  "webcam": [...]
}
```

---

## 📍 **Module 4: Final Integration for YouMap**

```
🚀 Finalizing Data for YouMap Integration

Perform exactly these tasks clearly and concisely:

1. Assign precise geo-coordinates to each item (when available)
2. Create simple, user-friendly labels (50 chars max) for each data point
3. Clearly ensure all categories match the YouMap data schema
4. Produce a fully structured final JSON payload, clearly formatted and ready for ingestion into YouMap.

Confirm completion explicitly by stating:
**"YouMap payload ready."**
```

---

*These prompt examples demonstrate the exact conversational flow and dynamic context chaining that powers the Real-Time Event Exploration System.*

