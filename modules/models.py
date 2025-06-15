"""Data models for the Real-Time Event Exploration System.

This module defines the data structures used throughout the system
for type safety and consistency.
"""

from dataclasses import dataclass
from typing import List, Dict, Any, Optional
from datetime import datetime


@dataclass
class TrendingEvent:
    """Represents a trending event from Module 0."""
    title: str
    description: str
    location: str
    emoji: str
    index: int


@dataclass
class SearchQuery:
    """Represents a search query for specific content retrieval."""
    category: str
    query: str
    purpose: str


@dataclass
class EventAnalysis:
    """Represents the analysis output from Module 1."""
    event_name: str
    summary: str
    locations: List[str]
    search_queries: List[SearchQuery]


@dataclass
class ContentItem:
    """Base class for content items from various sources."""
    title: str
    content: str
    timestamp: str
    url: str
    source: str
    metadata: Dict[str, Any]


@dataclass
class TwitterItem(ContentItem):
    """Represents a Twitter post."""
    username: str
    likes: int
    retweets: int


@dataclass
class YouTubeItem(ContentItem):
    """Represents a YouTube video."""
    channel_name: str
    views: int
    likes: int
    is_live: bool


@dataclass
class OfficialItem(ContentItem):
    """Represents an official report or statement."""
    agency: str
    report_type: str


@dataclass
class WebcamItem(ContentItem):
    """Represents a live webcam or stream."""
    is_live: bool
    viewer_count: Optional[int]


@dataclass
class NormalizedData:
    """Represents normalized data from Module 3."""
    event_name: str
    locations: List[str]
    twitter: List[TwitterItem]
    youtube: List[YouTubeItem]
    official: List[OfficialItem]
    webcam: List[WebcamItem]
    timestamp: str


@dataclass
class GeoCoordinate:
    """Represents a geographic coordinate."""
    latitude: float
    longitude: float
    accuracy: Optional[str] = None


@dataclass
class MapReadyItem:
    """Represents a data item ready for map integration."""
    label: str
    category: str
    coordinates: Optional[GeoCoordinate]
    content: str
    metadata: Dict[str, Any]


@dataclass
class YouMapPayload:
    """Final payload ready for YouMap integration."""
    event_name: str
    items: List[MapReadyItem]
    created_at: str
    total_items: int


# Response wrapper for API endpoints
@dataclass
class APIResponse:
    """Standard API response wrapper."""
    success: bool
    data: Any
    message: str
    timestamp: str


# Configuration model
@dataclass
class SystemConfig:
    """System configuration settings."""
    openai_api_key: Optional[str] = None
    max_items_per_category: int = 5
    preview_items_count: int = 3
    results_directory: str = "results"
    prompts_file: str = "prompts/prompts.txt"

