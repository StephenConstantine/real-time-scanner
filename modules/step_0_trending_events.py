#!/usr/bin/env python3
"""
🌟 PURPOSE:
Discovers trending real-time events through AI conversation and returns structured data.

🔗 DEPENDENCIES:
- openai (AI conversation engine)
- datetime, json (data handling)
- models.py (TrendingEvent data structures)
- dynamic_prompts.py (context-aware prompt generation)
- os, sys (system integration)

📑 STRUCTURE:
L39  🎯 TrendingEventsDiscoverer     — main orchestrator class
L68  🎨 _create_ui_messages()       — interface text generation
L95  🧠 _generate_prompt()          — prompt engineering
L132 🚀 discover_events()           — core discovery method
L194 📦 _process_response()         — response parsing
L224 📊 _create_event_objects()     — data structure creation
L250 🎭 _display_results()          — result presentation
L275 💾 _save_results()             — data persistence
L315 🔍 example_usage()             — executable demonstration
"""

import os
import sys
import json
import openai
from datetime import datetime
from typing import List, Dict, Any, Optional
from pathlib import Path
from dotenv import load_dotenv
from langchain_community.utilities import GoogleSerperAPIWrapper

# Load environment variables
load_dotenv()

sys.path.append(str(Path(__file__).parent.parent))

from modules.models import TrendingEvent
from modules.dynamic_prompts import DynamicPromptGenerator, PromptContext


class TrendingEventsDiscoverer:
    """
    🎯 Discovers trending events using AI conversation
    
    🔍 KEYWORDS: event discovery, AI conversation, data processing
    """
    
    def __init__(self, api_key: Optional[str] = None):
        # Get API keys from environment variables
        self.openai_api_key = api_key or os.getenv('OPENAI_API_KEY')
        self.serper_api_key = os.getenv('SERPER_API_KEY')
        
        if not self.serper_api_key:
            raise ValueError("🚨 Serper API key required. Set SERPER_API_KEY environment variable.")
        if not self.openai_api_key:
            raise ValueError("🚨 OpenAI API key required. Set OPENAI_API_KEY environment variable.")
        
        ### 📘 FOR DUMMIES:
        # We set up TWO connections:
        # 1. Serper - gets REAL web data from Google
        # 2. OpenAI - analyzes that real data intelligently
        ###
        openai.api_key = self.openai_api_key
        self.search = GoogleSerperAPIWrapper()
        
        # Initialize the prompt generator (creates smart questions for the AI)
        self.prompt_generator = DynamicPromptGenerator()
        
        ### 📘 FOR DUMMIES:
        # This creates a folder called "results" where we'll save our findings.
        # If the folder already exists, that's fine - we won't overwrite anything.
        ###
        self.results_dir = Path("results")
        self.results_dir.mkdir(exist_ok=True)
    
    def _create_ui_messages(self) -> Dict[str, str]:
        """🎨 Create user interface text elements"""
        ### 📘 FOR DUMMIES:
        # This function creates all the pretty text that users see on their screen.
        # Think of it like writing the script for what our program will "say" to users.
        ###
        return {
            "welcome": (
                "\n🌟 " + "="*60 + "\n"
                "     REAL-TIME EVENT DISCOVERY\n"
                "" + "="*60 + "\n\n"
                "🔥 Discovering current trending events...\n"
            ),
            "processing": (
                "🧠 Analyzing information streams...\n"
                "   • Scanning news sources\n"
                "   • Identifying patterns\n"
                "   • Ranking by significance\n"
            ),
            "complete": "✨ Discovery complete. Here are today's significant events:\n",
            "footer": (
                "\n" + "="*60 + "\n"
                "💡 Select an event number for detailed analysis\n"
                "" + "="*60 + "\n"
            )
        }
    
    def _fetch_real_news(self, query: str = "breaking news today") -> List[Dict]:
        """📰 Fetch real news data from Serper API"""
        ### 📘 FOR DUMMIES:
        # This gets REAL news articles from Google News instead of asking AI to make up events.
        # It's like reading actual newspapers instead of writing fiction.
        ###
        try:
            import http.client
            
            conn = http.client.HTTPSConnection('google.serper.dev')
            payload = json.dumps({
                'q': query,
                'num': 10  # Get 10 real news articles
            })
            headers = {
                'X-API-KEY': self.serper_api_key,
                'Content-Type': 'application/json'
            }
            
            conn.request('POST', '/news', payload, headers)
            res = conn.getresponse()
            data = res.read()
            result = json.loads(data.decode('utf-8'))
            
            if 'news' in result:
                return result['news']
            else:
                print(f"⚠️ No news found in API response. Keys: {list(result.keys())}")
                return []
                
        except Exception as e:
            print(f"🚨 Failed to fetch real news: {str(e)}")
            return []
    
    def _generate_analysis_prompt(self, real_news: List[Dict], context: PromptContext) -> str:
        """🧠 Generate AI prompt to analyze real news data"""
        ### 📘 FOR DUMMIES:
        # Instead of asking AI to make up events, we give it REAL news articles
        # and ask it to pick the 7 most significant ones and format them nicely.
        ###
        
        # Format real news for AI analysis
        news_text = "\n".join([
            f"• {article.get('title', 'No title')} - {article.get('source', 'Unknown')} ({article.get('date', 'No date')})\n"
            f"  {article.get('snippet', 'No description')}"
            for article in real_news[:10]  # Limit to 10 articles
        ])
        
        prompt = f"""
🎯 **REAL-TIME EVENT ANALYSIS TASK**

You are analyzing REAL breaking news articles from Google News. Your job is to:
1. Select the 7 MOST SIGNIFICANT events from the real news below
2. Format them according to our requirements
3. Add appropriate locations and emojis

📰 **REAL NEWS DATA (Current Breaking News):**
{news_text}

**OUTPUT REQUIREMENTS**:
Respond with EXACTLY this JSON format (no additional text, no explanations):

{{
  "events": [
    {{
      "title": "Clear, concise event title",
      "description": "Brief but informative description", 
      "location": "Primary location affected",
      "emoji": "Relevant emoji",
      "time_context": "When this happened (from article date)"
    }}
  ]
}}

✅ Requirements:
- Use ONLY the real news provided above
- Select exactly 7 most significant events
- Order by significance/impact
- Extract or infer locations from the articles
- Choose appropriate emojis for each event type
- JSON format only, no markdown
- Use clear, engaging titles

🚀 RESPOND WITH JSON ONLY - NO OTHER TEXT."""
        
        return prompt
    
    def discover_events(self, urgency_level: str = "medium", event_focus: str = "global") -> List[TrendingEvent]:
        """
        🚀 Execute the complete event discovery process
        
        🔍 KEYWORDS: orchestration, AI conversation, data processing
        """
        ### 📘 FOR DUMMIES:
        # This is the main function that does everything:
        # 1. Shows welcome message
        # 2. Talks to the AI
        # 3. Gets back a list of events
        # 4. Shows them nicely to the user
        # 5. Saves them to a file
        ###
        ui = self._create_ui_messages()
        print(ui["welcome"])
        
        context = PromptContext(
            event_name="trending_discovery",
            event_type=event_focus,
            urgency_level=urgency_level,
            time_sensitivity=True
        )
        
        print(ui["processing"])
        print("   • Fetching real news from Google...")
        
        try:
            # Step 1: Get REAL news data from Serper
            real_news = self._fetch_real_news("breaking news today")
            
            if not real_news:
                print("⚠️ No real news found, check API connection")
                return []
            
            print(f"   • Found {len(real_news)} real news articles")
            print("   • Analyzing with AI intelligence...")
            
            # Step 2: Use AI to analyze the REAL data
            prompt = self._generate_analysis_prompt(real_news, context)
            
            ### 📘 FOR DUMMIES:
            # Now we give the AI REAL news articles and ask it to pick the most
            # important ones and format them nicely. The AI isn't making up events,
            # it's analyzing real information like a smart research assistant.
            ###
            response = openai.chat.completions.create(
                model="gpt-4",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert intelligence analyst. Analyze real news data and extract the most significant events. Follow instructions precisely."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.2,  # Lower = more focused analysis
                max_tokens=2000,  # Maximum length of AI response
                top_p=0.8         # Controls creativity vs accuracy
            )
            
            events = self._process_response(response.choices[0].message.content)
            self._display_results(events)
            self._save_results(events, context)
            
            return events
            
        except Exception as e:
            print(f"🚨 Discovery failed: {str(e)}")
            print("💡 Check API key and connection")
            return []
    
    def _process_response(self, raw_response: str) -> List[TrendingEvent]:
        """📦 Parse AI response into structured objects"""
        ### 📘 FOR DUMMIES:
        # The AI sends back text, but we need to turn that text into
        # organized data our program can work with. This function does that conversion.
        ###
        try:
            # Clean up the response (remove any extra formatting)
            cleaned = raw_response.strip()
            
            # Look for JSON content in the response
            if "```json" in cleaned:
                # Extract JSON from markdown code blocks
                start = cleaned.find("```json") + 7
                end = cleaned.find("```", start)
                if end != -1:
                    cleaned = cleaned[start:end].strip()
            elif "```" in cleaned:
                # Extract JSON from generic code blocks
                start = cleaned.find("```") + 3
                end = cleaned.find("```", start)
                if end != -1:
                    cleaned = cleaned[start:end].strip()
            elif "{" in cleaned and "}" in cleaned:
                # Extract JSON directly if no code blocks
                start = cleaned.find("{")
                end = cleaned.rfind("}") + 1
                cleaned = cleaned[start:end].strip()
            
            # Convert text to structured data
            data = json.loads(cleaned)
            
            if "events" not in data:
                raise ValueError("Missing 'events' key in response")
            
            events = self._create_event_objects(data["events"])
            return events
            
        except json.JSONDecodeError as e:
            print(f"🚨 JSON parsing error: {str(e)}")
            print(f"🔍 Raw response preview: {raw_response[:500]}...")
            return []
        except Exception as e:
            print(f"🚨 Processing error: {str(e)}")
            return []
    
    def _create_event_objects(self, events_data: List[Dict]) -> List[TrendingEvent]:
        """📊 Create TrendingEvent objects from raw data"""
        ### 📘 FOR DUMMIES:
        # This takes the raw event information and packages it into
        # neat, organized "TrendingEvent" objects that our program
        # knows how to work with properly.
        ###
        events = []
        
        for i, event_data in enumerate(events_data, 1):
            try:
                event = TrendingEvent(
                    title=event_data.get("title", "Unknown Event"),
                    description=event_data.get("description", "No description"),
                    location=event_data.get("location", "Unknown Location"),
                    emoji=event_data.get("emoji", "📍"),
                    index=i
                )
                events.append(event)
                
            except Exception as e:
                print(f"⚠️ Skipping malformed event {i}: {str(e)}")
                continue
        
        return events
    
    def _display_results(self, events: List[TrendingEvent]) -> None:
        """🎭 Present events in formatted output"""
        ### 📘 FOR DUMMIES:
        # This makes the events look pretty on the screen with nice
        # borders and formatting. Think of it like creating a 
        # beautiful poster from plain information.
        ###
        ui = self._create_ui_messages()
        print(ui["complete"])
        
        if not events:
            print("🤔 No events found. Check API response.")
            return
        
        for event in events:
            print(f"""
┌──────────────────────────────────────────────────┐
│ {event.emoji} {event.index}. {event.title:<40} │
├──────────────────────────────────────────────────┤
│ 📍 Location: {event.location:<32} │
│ 📝 Summary:  {event.description:<32} │
└──────────────────────────────────────────────────┘""")
        
        print(ui["footer"])
    
    def _save_results(self, events: List[TrendingEvent], context: PromptContext) -> None:
        """💾 Save results to JSON file"""
        ### 📘 FOR DUMMIES:
        # This saves all our discovered events to a file on the computer
        # so we can look at them later or use them in other parts of our program.
        # It's like keeping a digital notebook of what we found.
        ###
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"trending_events_{timestamp}.json"
        filepath = self.results_dir / filename
        
        result_data = {
            "metadata": {
                "timestamp": datetime.now().isoformat(),
                "urgency_level": context.urgency_level,
                "event_type": context.event_type,
                "total_events": len(events)
            },
            "events": [
                {
                    "index": event.index,
                    "title": event.title,
                    "description": event.description,
                    "location": event.location,
                    "emoji": event.emoji
                }
                for event in events
            ]
        }
        
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(result_data, f, indent=2, ensure_ascii=False)
            print(f"💾 Results saved: {filepath}")
        except Exception as e:
            print(f"⚠️ Save failed: {str(e)}")


# ----- Example Usage -----

def example_usage():
    """
    🔍 Demonstrate trending events discovery
    
    🔍 KEYWORDS: example, demonstration, testing
    """
    ### 📘 FOR DUMMIES:
    # This function shows how to use our event discoverer.
    # It's like a demo or tutorial that anyone can run to see how it works.
    ###
    print("🚀 Trending Events Discovery - Example\n")
    
    try:
        discoverer = TrendingEventsDiscoverer()
        
        events = discoverer.discover_events(
            urgency_level="high",
            event_focus="global"
        )
        
        print(f"\n📊 Summary:")
        print(f"   • Found {len(events)} events")
        print(f"   • Saved to results directory")
        print(f"   • Ready for next step")
        
        return events
        
    except Exception as e:
        print(f"🚨 Example failed: {str(e)}")
        return []


if __name__ == "__main__":
    example_usage()

