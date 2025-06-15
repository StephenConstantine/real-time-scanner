"""Pytest configuration and shared fixtures."""

import pytest
import tempfile
import os
import json
from datetime import datetime
from typing import Dict, Any, List

# Import models for test data
from modules.models import (
    TrendingEvent, SearchQuery, EventAnalysis, ContentItem,
    TwitterItem, YouTubeItem, OfficialItem, WebcamItem,
    NormalizedData, GeoCoordinate, MapReadyItem, YouMapPayload,
    APIResponse, SystemConfig
)


@pytest.fixture
def temp_dir():
    """Create a temporary directory for test files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield tmpdir


@pytest.fixture
def mock_config():
    """Provide a mock system configuration."""
    return SystemConfig(
        openai_api_key="test-key-123",
        max_items_per_category=3,
        preview_items_count=2,
        results_directory="test_results",
        prompts_file="test_prompts.txt"
    )


@pytest.fixture
def sample_trending_event():
    """Sample trending event for testing."""
    return TrendingEvent(
        title="Test Event",
        description="A test event for testing purposes",
        location="Test Location",
        emoji="🧪",
        index=1
    )


@pytest.fixture
def sample_search_queries():
    """Sample search queries for testing."""
    return [
        SearchQuery(
            category="twitter",
            query="test event breaking news",
            purpose="Find recent social media posts"
        ),
        SearchQuery(
            category="youtube",
            query="test event live stream",
            purpose="Find live coverage"
        )
    ]


@pytest.fixture
def sample_event_analysis(sample_search_queries):
    """Sample event analysis for testing."""
    return EventAnalysis(
        event_name="Test Event",
        summary="A comprehensive test event analysis",
        locations=["Test Location", "Secondary Location"],
        search_queries=sample_search_queries
    )


@pytest.fixture
def sample_content_items():
    """Sample content items for testing."""
    return {
        'twitter': [
            TwitterItem(
                title="Breaking: Test Event",
                content="Test content for Twitter",
                timestamp="2024-01-01T12:00:00Z",
                url="https://twitter.com/test/123",
                source="twitter",
                metadata={"id": "123"},
                username="testuser",
                likes=100,
                retweets=25
            )
        ],
        'youtube': [
            YouTubeItem(
                title="LIVE: Test Event Coverage",
                content="Live stream description",
                timestamp="2024-01-01T12:00:00Z",
                url="https://youtube.com/watch?v=test123",
                source="youtube",
                metadata={"video_id": "test123"},
                channel_name="Test News",
                views=1000,
                likes=50,
                is_live=True
            )
        ],
        'official': [
            OfficialItem(
                title="Official Statement",
                content="Official statement content",
                timestamp="2024-01-01T12:00:00Z",
                url="https://official.gov/statement",
                source="official",
                metadata={"doc_id": "off123"},
                agency="Test Agency",
                report_type="statement"
            )
        ],
        'webcam': [
            WebcamItem(
                title="Live Webcam Feed",
                content="Live webcam from test location",
                timestamp="2024-01-01T12:00:00Z",
                url="https://webcam.test/feed",
                source="webcam",
                metadata={"cam_id": "cam123"},
                is_live=True,
                viewer_count=150
            )
        ]
    }


@pytest.fixture
def sample_normalized_data(sample_content_items):
    """Sample normalized data for testing."""
    return NormalizedData(
        event_name="Test Event",
        locations=["Test Location"],
        twitter=sample_content_items['twitter'],
        youtube=sample_content_items['youtube'],
        official=sample_content_items['official'],
        webcam=sample_content_items['webcam'],
        timestamp="2024-01-01T12:00:00Z"
    )


@pytest.fixture
def sample_geo_coordinate():
    """Sample geographic coordinate for testing."""
    return GeoCoordinate(
        latitude=40.7128,
        longitude=-74.0060,
        accuracy="high"
    )


@pytest.fixture
def sample_map_ready_items(sample_geo_coordinate):
    """Sample map-ready items for testing."""
    return [
        MapReadyItem(
            label="Test Twitter Post",
            category="twitter",
            coordinates=sample_geo_coordinate,
            content="Test content",
            metadata={"source": "twitter", "verified": True}
        ),
        MapReadyItem(
            label="Test YouTube Video",
            category="youtube",
            coordinates=sample_geo_coordinate,
            content="Test video content",
            metadata={"source": "youtube", "live": True}
        )
    ]


@pytest.fixture
def sample_youmap_payload(sample_map_ready_items):
    """Sample YouMap payload for testing."""
    return YouMapPayload(
        event_name="Test Event",
        items=sample_map_ready_items,
        created_at="2024-01-01T12:00:00Z",
        total_items=len(sample_map_ready_items)
    )


@pytest.fixture
def mock_prompts_file(temp_dir):
    """Create a mock prompts file for testing."""
    prompts_content = '''---
### test_prompt
This is a test prompt for unit testing.
It can have multiple lines.

---
### another_prompt
Another test prompt.
'''
    
    prompts_dir = os.path.join(temp_dir, 'prompts')
    os.makedirs(prompts_dir, exist_ok=True)
    
    prompts_file = os.path.join(prompts_dir, 'prompts.txt')
    with open(prompts_file, 'w') as f:
        f.write(prompts_content)
    
    return prompts_file


@pytest.fixture
def mock_results_dir(temp_dir):
    """Create a mock results directory for testing."""
    results_dir = os.path.join(temp_dir, 'results')
    os.makedirs(results_dir, exist_ok=True)
    return results_dir


@pytest.fixture
def sample_api_response():
    """Sample API response for testing."""
    return APIResponse(
        success=True,
        data={"test": "data"},
        message="Test successful",
        timestamp="2024-01-01T12:00:00Z"
    )

