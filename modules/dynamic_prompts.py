#!/usr/bin/env python3
"""
🎯 Dynamic Prompt Management System

✨ This module creates context-aware, dynamic prompts instead of hardcoded ones.
🧠 AI assistants can generate contextual prompts based on:
   - Current event details
   - User preferences
   - Real-time conditions
   - Historical performance data

🎨 Features:
   - 📝 Template-based prompt generation
   - 🔄 Context injection
   - 📊 Performance tracking
   - 🎛️ User customization
"""

import json
import datetime
from typing import Dict, Any, List, Optional
from pathlib import Path
from dataclasses import dataclass, field


@dataclass
class PromptContext:
    """🎯 Context data for dynamic prompt generation"""
    event_name: str
    event_type: str  # 🏛️ political, 🌍 environmental, 🎭 cultural, etc.
    locations: List[str] = field(default_factory=list)
    urgency_level: str = "medium"  # 🔥 high, ⚖️ medium, 🌱 low
    time_sensitivity: bool = True
    user_preferences: Dict[str, Any] = field(default_factory=dict)
    previous_results: Dict[str, Any] = field(default_factory=dict)


class DynamicPromptGenerator:
    """
    🎨 Dynamic Prompt Generator
    
    Creates contextual, adaptive prompts instead of static templates.
    Each prompt is tailored to the specific situation and requirements.
    """
    
    def __init__(self, templates_dir: str = "prompts"):
        self.templates_dir = Path(templates_dir)
        self.performance_log = self.templates_dir / "prompt_performance.json"
        self.user_preferences = self.templates_dir / "user_preferences.json"
        
        # 📊 Load performance data and preferences
        self.performance_data = self._load_performance_data()
        self.preferences = self._load_user_preferences()
    
    def generate_trending_events_prompt(self, context: PromptContext) -> str:
        """
        🌟 Generate dynamic prompt for trending events discovery
        
        Args:
            context: Current context and requirements
            
        Returns:
            Contextual prompt optimized for the current situation
        """
        urgency_emoji = {
            "high": "🔥",
            "medium": "⚖️", 
            "low": "🌱"
        }[context.urgency_level]
        
        # 🎯 Customize based on event type preference
        event_focus = self._get_event_focus(context.event_type)
        
        # 🌍 Location-specific instructions
        location_instruction = self._get_location_instruction(context.locations)
        
        prompt = f"""
{urgency_emoji} **TRENDING EVENTS DISCOVERY - {context.urgency_level.upper()} PRIORITY**

You're an expert AI news scout with real-time awareness. Your mission:

🎯 **PRIMARY OBJECTIVE**: Identify 7 trending events happening RIGHT NOW
{event_focus}
{location_instruction}

📋 **OUTPUT FORMAT** (for each event):
- 🏷️ **Event Title**: [Clear, specific title]
- 📝 **Description**: [One impactful sentence]
- 📍 **Location**: [Primary location/region]
- 🎨 **Visual**: [Relevant emoji for instant recognition]
- ⏰ **Time Context**: [How recent/urgent]

🎯 **QUALITY CRITERIA**:
✅ Events must be happening within the last 24 hours
✅ Prioritize events with real-time developments
✅ Focus on events with visual/social media coverage
✅ Include diverse geographic representation

🚀 **EXECUTION**: Present as numbered list, most urgent first!
"""
        
        # 📊 Log prompt generation for performance tracking
        self._log_prompt_usage("trending_events", {
            "event_name": context.event_name,
            "event_type": context.event_type,
            "urgency_level": context.urgency_level
        })
        
        return prompt.strip()
    
    def generate_event_analysis_prompt(self, context: PromptContext) -> str:
        """
        🧠 Generate dynamic event analysis prompt
        
        Creates contextual analysis instructions based on event characteristics
        """
        event_emoji = self._get_event_emoji(context.event_type)
        
        # 🎛️ Customize analysis depth based on urgency
        analysis_depth = self._get_analysis_depth(context.urgency_level)
        
        # 🔍 Source prioritization based on event type
        source_priorities = self._get_source_priorities(context.event_type)
        
        prompt = f"""
{event_emoji} **EVENT ANALYSIS & SEARCH STRATEGY**

🎯 **TARGET EVENT**: {context.event_name}
📊 **Analysis Level**: {analysis_depth}

### 📌 CONTEXTUAL SUMMARY
Provide a focused 2-3 sentence analysis covering:
- 🎯 **Core Issue**: What's the fundamental situation?
- 🌍 **Geographic Impact**: Where and why it matters
- ⏰ **Current Status**: What's happening right now

### 📍 IMPACT ZONES
Identify key locations experiencing direct effects from this event.

### 🔍 INTELLIGENT SEARCH STRATEGY
{source_priorities}

For each category, provide:
- **🎯 Optimized Query**: Exact search terms for maximum relevance
- **💡 Strategic Value**: Why this source matters for this specific event
- **⚡ Real-time Focus**: How to capture live developments

### 🚀 EXECUTION PRIORITY
Start with the most time-sensitive category for immediate intelligence gathering.
"""
        
        self._log_prompt_usage("event_analysis", {
            "event_name": context.event_name,
            "event_type": context.event_type,
            "urgency_level": context.urgency_level
        })
        return prompt.strip()
    
    def generate_content_retrieval_prompt(self, platform: str, query: str, context: PromptContext) -> str:
        """
        📥 Generate dynamic content retrieval prompt
        
        Args:
            platform: Target platform (twitter, youtube, official, webcam)
            query: Search query
            context: Event context
        """
        platform_config = {
            "twitter": {
                "emoji": "🐦",
                "focus": "real-time updates, eyewitness accounts, official statements",
                "metrics": "engagement rates, verification status, recency"
            },
            "youtube": {
                "emoji": "📺", 
                "focus": "live streams, recent uploads, authoritative channels",
                "metrics": "view counts, upload recency, channel credibility"
            },
            "official": {
                "emoji": "🏛️",
                "focus": "government statements, agency reports, verified sources",
                "metrics": "source authority, document recency, official verification"
            },
            "webcam": {
                "emoji": "📹",
                "focus": "live feeds, real-time visuals, geographic coverage",
                "metrics": "stream quality, viewer count, location accuracy"
            }
        }
        
        config = platform_config.get(platform, platform_config["twitter"])
        
        # 🎯 Urgency-based result count
        result_count = {
            "high": "5-7",
            "medium": "3-5", 
            "low": "2-3"
        }[context.urgency_level]
        
        prompt = f"""
{config['emoji']} **{platform.upper()} INTELLIGENCE GATHERING**

🎯 **SEARCH QUERY**: "{query}"
📊 **TARGET RESULTS**: {result_count} highest-quality items
⏰ **URGENCY LEVEL**: {context.urgency_level}

### 🔍 SEARCH FOCUS
{config['focus']}

### 📊 QUALITY METRICS
Prioritize based on: {config['metrics']}

### 📋 REQUIRED DATA POINTS
For each item, extract:
- 👤 **Source**: Username/channel name + verification status
- 📝 **Content**: Full text/title + key summary
- ⏰ **Timestamp**: Exact posting/upload time
- 📊 **Engagement**: Likes, shares, views (as available)
- 🔗 **Direct Link**: Full URL for verification
- 🎯 **Relevance Score**: How well it matches our event (1-10)

### 🚀 EXECUTION PROTOCOL
1. 🔍 Execute search with provided query
2. 📊 Rank results by relevance and quality metrics
3. 📋 Present top results in structured format
4. ⏳ Await approval before deeper analysis

🎯 **SUCCESS CRITERIA**: Results must provide actionable intelligence about "{context.event_name}"
"""
        
        self._log_prompt_usage(f"{platform}_retrieval", {
            "query": query,
            "event_name": context.event_name,
            "event_type": context.event_type,
            "urgency_level": context.urgency_level
        })
        return prompt.strip()
    
    def _get_event_focus(self, event_type: str) -> str:
        """🎯 Get event-type specific focus instructions"""
        focus_map = {
            "political": "🏛️ **Focus**: Political developments, policy changes, electoral events",
            "environmental": "🌍 **Focus**: Environmental incidents, climate events, natural disasters",
            "social": "👥 **Focus**: Social movements, community events, cultural developments",
            "economic": "💰 **Focus**: Market movements, economic policy, business developments",
            "technology": "💻 **Focus**: Tech launches, cyber events, innovation announcements",
            "security": "🛡️ **Focus**: Security incidents, safety events, emergency responses"
        }
        return focus_map.get(event_type, "🎯 **Focus**: All significant real-time developments")
    
    def _get_location_instruction(self, locations: List[str]) -> str:
        """🌍 Generate location-specific instructions"""
        if not locations:
            return "🌍 **Geographic Scope**: Global events with significant impact"
        
        location_str = ", ".join(locations)
        return f"📍 **Priority Regions**: Focus on events in or affecting {location_str}"
    
    def _get_event_emoji(self, event_type: str) -> str:
        """🎨 Get appropriate emoji for event type"""
        emoji_map = {
            "political": "🏛️",
            "environmental": "🌍", 
            "social": "👥",
            "economic": "💰",
            "technology": "💻",
            "security": "🛡️"
        }
        return emoji_map.get(event_type, "🎯")
    
    def _get_analysis_depth(self, urgency: str) -> str:
        """📊 Determine analysis depth based on urgency"""
        depth_map = {
            "high": "🔥 **RAPID RESPONSE** - Immediate actionable intelligence",
            "medium": "⚖️ **COMPREHENSIVE** - Balanced analysis with multiple perspectives",
            "low": "🌱 **THOROUGH** - Deep dive with historical context"
        }
        return depth_map[urgency]
    
    def _get_source_priorities(self, event_type: str) -> str:
        """🔍 Get source priorities based on event type"""
        priority_map = {
            "political": """
**🏛️ Official Government Sources** (Highest Priority)
**🐦 Political Twitter/Social** (Real-time reactions)
**📺 News Live Streams** (Breaking coverage)
**📹 Live Event Feeds** (Direct visuals)
""",
            "environmental": """
**🌍 Environmental Agencies** (Official data)
**📹 Live Webcams/Satellite** (Real-time visuals)
**🐦 Eyewitness Social Media** (Ground reports)
**📺 Scientific/News Sources** (Expert analysis)
"""
        }
        
        return priority_map.get(event_type, """
**🐦 Social Media Updates** (Real-time pulse)
**📺 Video Coverage** (Visual documentation)
**🏛️ Official Statements** (Authoritative sources)
**📹 Live Visual Feeds** (Direct observation)
""")
    
    def _load_performance_data(self) -> Dict:
        """📊 Load prompt performance metrics"""
        try:
            if self.performance_log.exists():
                return json.loads(self.performance_log.read_text())
        except Exception:
            pass
        return {}
    
    def _load_user_preferences(self) -> Dict:
        """🎛️ Load user customization preferences"""
        try:
            if self.user_preferences.exists():
                return json.loads(self.user_preferences.read_text())
        except Exception:
            pass
        return {
            "preferred_sources": ["twitter", "youtube", "official"],
            "urgency_bias": "medium",
            "location_focus": [],
            "event_type_priority": ["political", "environmental", "social"]
        }
    
    def _log_prompt_usage(self, prompt_type: str, context: Dict) -> None:
        """📊 Log prompt usage for performance analysis"""
        timestamp = datetime.datetime.now().isoformat()
        
        if prompt_type not in self.performance_data:
            self.performance_data[prompt_type] = []
        
        self.performance_data[prompt_type].append({
            "timestamp": timestamp,
            "context": context,
            "success": None  # To be updated later with results
        })
        
        # 💾 Save performance data
        try:
            self.performance_log.parent.mkdir(exist_ok=True)
            self.performance_log.write_text(json.dumps(self.performance_data, indent=2))
        except Exception as e:
            print(f"⚠️ Warning: Could not save performance data: {e}")


# 🎯 Example usage and testing
if __name__ == "__main__":
    # 🧪 Test the dynamic prompt system
    generator = DynamicPromptGenerator()
    
    # 🎯 Create test context
    test_context = PromptContext(
        event_name="Climate Summit Protests in Glasgow",
        event_type="environmental",
        locations=["Glasgow", "Scotland"],
        urgency_level="high",
        time_sensitivity=True
    )
    
    # 🌟 Generate trending events prompt
    trending_prompt = generator.generate_trending_events_prompt(test_context)
    print("🌟 TRENDING EVENTS PROMPT:")
    print(trending_prompt)
    print("\n" + "="*50 + "\n")
    
    # 🧠 Generate analysis prompt
    analysis_prompt = generator.generate_event_analysis_prompt(test_context)
    print("🧠 EVENT ANALYSIS PROMPT:")
    print(analysis_prompt)
    print("\n" + "="*50 + "\n")
    
    # 🐦 Generate Twitter retrieval prompt
    twitter_prompt = generator.generate_content_retrieval_prompt(
        "twitter", 
        "Glasgow climate summit protests live updates",
        test_context
    )
    print("🐦 TWITTER RETRIEVAL PROMPT:")
    print(twitter_prompt)

