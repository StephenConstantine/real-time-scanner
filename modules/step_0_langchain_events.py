#!/usr/bin/env python3
"""
🌟 PURPOSE:
Discovers REAL trending events using LangChain's web search capabilities and AI analysis.

🔗 DEPENDENCIES:
- langchain (AI orchestration framework)
- langchain-community (web search tools)
- langchain-openai (OpenAI integration)
- datetime, json (data handling)
- models.py (TrendingEvent data structures)
- os, sys (system integration)

📑 STRUCTURE:
L35  🎯 RealTimeEventsDiscoverer     — main orchestrator class
L55  🔍 _setup_langchain_tools()     — configure search and AI tools
L75  🎨 _create_ui_messages()        — interface text generation
L95  🔍 _search_breaking_news()      — real-time news search
L125 🧠 _analyze_with_ai()           — AI analysis of real events
L155 🚀 discover_real_events()       — core discovery method
L195 📦 _process_search_results()    — search result processing
L225 📊 _create_event_objects()      — data structure creation
L250 🎭 _display_results()           — result presentation
L280 💾 _save_results()              — data persistence
L310 🔍 example_usage()              — executable demonstration
"""

import os
import sys
import json
from datetime import datetime
from typing import List, Dict, Any, Optional
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

sys.path.append(str(Path(__file__).parent.parent))

# LangChain imports for real-time data
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from langchain.agents import Tool

from modules.models import TrendingEvent


class RealTimeEventsDiscoverer:
    """
    🎯 Discovers REAL trending events using LangChain web search + AI analysis
    
    ### 📘 FOR DUMMIES:
    # This class uses LangChain to actually search the internet for real news,
    # then uses AI to analyze what it finds and format it nicely.
    # It's like having a research assistant that can read the web for you.
    ###
    
    🔍 KEYWORDS: real-time search, web scraping, AI analysis, current events
    """
    
    def __init__(self, api_key: Optional[str] = None):
        # Set up OpenAI API
        self.api_key = api_key or os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError("🚨 OpenAI API key required. Set OPENAI_API_KEY environment variable.")
        
        ### 📘 FOR DUMMIES:
        # Set up all the tools we need:
        # 1. AI for thinking and analysis
        # 2. Web search for finding real information
        # 3. Results folder for saving what we find
        ###
        self._setup_langchain_tools()
        
        # Set up results directory
        self.results_dir = Path("results")
        self.results_dir.mkdir(exist_ok=True)
    
    def _setup_langchain_tools(self) -> None:
        """🔍 Configure LangChain tools for real-time search and AI analysis"""
        ### 📘 FOR DUMMIES:
        # This sets up our "toolbox":
        # - A search engine (DuckDuckGo) to find real news
        # - An AI brain (OpenAI) to understand what we found
        ###
        
        # Initialize OpenAI Chat model
        self.llm = ChatOpenAI(
            openai_api_key=self.api_key,
            model_name="gpt-4",
            temperature=0.3  # Low temperature for more consistent results
        )
        
        # Initialize web search tool
        self.search_tool = DuckDuckGoSearchRun()
        
        # Create search queries for different types of breaking news
        self.search_queries = [
            "breaking news today",
            "trending events now",
            "latest world news",
            "current events 2024",
            "major news headlines today"
        ]
    
    def _create_ui_messages(self) -> Dict[str, str]:
        """🎨 Create user interface text elements"""
        return {
            "welcome": (
                "\n🌟 " + "="*60 + "\n"
                "     REAL-TIME EVENT DISCOVERY (LANGCHAIN POWERED)\n"
                "" + "="*60 + "\n\n"
                "🌍 Searching the web for actual trending events...\n"
            ),
            "searching": (
                "🔍 Web search in progress...\n"
                "   • Querying news sources\n"
                "   • Finding breaking stories\n"
                "   • Analyzing real-time data\n"
            ),
            "analyzing": (
                "🧠 AI analysis of findings...\n"
                "   • Processing search results\n"
                "   • Identifying key events\n"
                "   • Ranking by significance\n"
            ),
            "complete": "✨ Analysis complete. Here are today's REAL trending events:\n",
            "footer": (
                "\n" + "="*60 + "\n"
                "📞 Sources: Live web search results\n"
                "💡 Select an event number for detailed analysis\n"
                "" + "="*60 + "\n"
            )
        }
    
    def _search_breaking_news(self) -> List[str]:
        """🔍 Search the web for real breaking news and trending events"""
        ### 📘 FOR DUMMIES:
        # This function actually goes out to the internet and searches
        # for real news that's happening right now. It's like using
        # Google to find the latest headlines.
        ###
        
        all_results = []
        
        for query in self.search_queries:
            try:
                # Perform web search
                results = self.search_tool.run(query)
                all_results.append(f"Query: {query}\nResults: {results}\n---\n")
                
                ### 📘 FOR DUMMIES:
                # Each search gives us a bunch of text about current news.
                # We collect all of these results to analyze together.
                ###
                
            except Exception as e:
                print(f"⚠️ Search failed for '{query}': {str(e)}")
                continue
        
        return all_results
    
    def _analyze_with_ai(self, search_results: List[str]) -> str:
        """🧠 Use AI to analyze real search results and extract trending events"""
        ### 📘 FOR DUMMIES:
        # This takes all the messy search results and asks our AI to
        # read through them and pick out the most important events
        # happening right now.
        ###
        
        # Combine all search results
        combined_results = "\n".join(search_results)
        
        # Create analysis prompt
        analysis_prompt = f"""
You are an expert news analyst. Below are real-time search results from the web about current trending events.

Analyze these search results and extract the 7 most significant trending events happening RIGHT NOW.

SEARCH RESULTS:
{combined_results}

IMPORTANT: Extract REAL events from these search results. Do not make up events.

Respond with EXACTLY this JSON format:
{{
  "events": [
    {{
      "title": "Real event title from search results",
      "description": "Brief description based on search results",
      "location": "Location mentioned in search results",
      "emoji": "Relevant emoji",
      "source": "Indicate this came from web search"
    }}
  ]
}}

Requirements:
- Exactly 7 events
- Only use information found in the search results
- Focus on most recent/significant events
- Include diverse geographic coverage
- JSON format only, no markdown

Respond with JSON only:"""
        
        try:
            # Get AI analysis
            messages = [
                SystemMessage(content="You are an expert news analyst with access to real-time information."),
                HumanMessage(content=analysis_prompt)
            ]
            
            response = self.llm(messages)
            return response.content
            
        except Exception as e:
            print(f"🚨 AI analysis failed: {str(e)}")
            return ""
    
    def discover_real_events(self, max_events: int = 7) -> List[TrendingEvent]:
        """
        🚀 Execute the complete real-time event discovery process
        
        ### 📘 FOR DUMMIES:
        # This is the main function that:
        # 1. Searches the web for real news
        # 2. Has AI analyze what it found
        # 3. Turns the results into neat event objects
        # 4. Shows them beautifully to the user
        ###
        
        🔍 KEYWORDS: real-time discovery, web search, AI analysis
        """
        ui = self._create_ui_messages()
        print(ui["welcome"])
        
        # Step 1: Search the web for real news
        print(ui["searching"])
        search_results = self._search_breaking_news()
        
        if not search_results:
            print("🚨 No search results found. Check internet connection.")
            return []
        
        # Step 2: Analyze results with AI
        print(ui["analyzing"])
        ai_analysis = self._analyze_with_ai(search_results)
        
        if not ai_analysis:
            print("🚨 AI analysis failed.")
            return []
        
        # Step 3: Process results into structured events
        events = self._process_search_results(ai_analysis)
        
        # Step 4: Display and save results
        self._display_results(events)
        self._save_results(events, search_results)
        
        return events
    
    def _process_search_results(self, ai_response: str) -> List[TrendingEvent]:
        """📦 Parse AI analysis into structured TrendingEvent objects"""
        ### 📘 FOR DUMMIES:
        # The AI gives us back text, but we need to turn that into
        # organized TrendingEvent objects that our program can work with.
        ###
        
        try:
            # Clean up the response
            cleaned = ai_response.strip()
            
            # Extract JSON from response
            if "```json" in cleaned:
                start = cleaned.find("```json") + 7
                end = cleaned.find("```", start)
                if end != -1:
                    cleaned = cleaned[start:end].strip()
            elif "{" in cleaned and "}" in cleaned:
                start = cleaned.find("{")
                end = cleaned.rfind("}") + 1
                cleaned = cleaned[start:end].strip()
            
            # Parse JSON
            data = json.loads(cleaned)
            
            if "events" not in data:
                raise ValueError("Missing 'events' key in AI response")
            
            # Create event objects
            events = self._create_event_objects(data["events"])
            return events
            
        except json.JSONDecodeError as e:
            print(f"🚨 JSON parsing error: {str(e)}")
            print(f"🔍 AI response preview: {ai_response[:500]}...")
            return []
        except Exception as e:
            print(f"🚨 Processing error: {str(e)}")
            return []
    
    def _create_event_objects(self, events_data: List[Dict]) -> List[TrendingEvent]:
        """📊 Create TrendingEvent objects from AI analysis"""
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
        """🎭 Present real events in formatted output"""
        ui = self._create_ui_messages()
        print(ui["complete"])
        
        if not events:
            print("🤔 No events extracted from search results.")
            return
        
        for event in events:
            print(f"""
┌──────────────────────────────────────────────────┐
│ {event.emoji} {event.index}. {event.title:<40} │
├──────────────────────────────────────────────────┤
│ 📍 Location: {event.location:<32} │
│ 📝 Summary:  {event.description:<32} │
│ 🌍 Source:   Real web search results        │
└──────────────────────────────────────────────────┘""")
        
        print(ui["footer"])
    
    def _save_results(self, events: List[TrendingEvent], search_results: List[str]) -> None:
        """💾 Save real event discovery results with search metadata"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"real_trending_events_{timestamp}.json"
        filepath = self.results_dir / filename
        
        result_data = {
            "metadata": {
                "timestamp": datetime.now().isoformat(),
                "source": "LangChain web search + AI analysis",
                "search_queries": self.search_queries,
                "total_events": len(events),
                "is_real_data": True
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
            ],
            "raw_search_results": search_results  # Save raw data for debugging
        }
        
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(result_data, f, indent=2, ensure_ascii=False)
            print(f"💾 Real event data saved: {filepath}")
        except Exception as e:
            print(f"⚠️ Save failed: {str(e)}")


# ----- Example Usage -----

def example_usage():
    """
    🔍 Demonstrate REAL trending events discovery using LangChain
    
    ### 📘 FOR DUMMIES:
    # This function shows how to use our real event finder.
    # Unlike the fake examples, this actually searches the internet!
    ###
    
    🔍 KEYWORDS: real events, web search, demonstration
    """
    print("🚀 LangChain Real-Time Events Discovery - Example\n")
    
    try:
        discoverer = RealTimeEventsDiscoverer()
        
        events = discoverer.discover_real_events(max_events=7)
        
        print(f"\n📊 Summary:")
        print(f"   • Found {len(events)} REAL events")
        print(f"   • Source: Live web search")
        print(f"   • Saved to results directory")
        print(f"   • Ready for Step 1 analysis")
        
        return events
        
    except Exception as e:
        print(f"🚨 Example failed: {str(e)}")
        return []


if __name__ == "__main__":
    example_usage()

