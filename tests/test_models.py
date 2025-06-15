"""Tests for data models."""

import pytest
from datetime import datetime
from modules.models import (
    TrendingEvent, SearchQuery, EventAnalysis, ContentItem,
    TwitterItem, YouTubeItem, OfficialItem, WebcamItem,
    NormalizedData, GeoCoordinate, MapReadyItem, YouMapPayload,
    APIResponse, SystemConfig
)


class TestTrendingEvent:
    """Test TrendingEvent model."""
    
    def test_creation(self, sample_trending_event):
        """Test TrendingEvent creation."""
        assert sample_trending_event.title == "Test Event"
        assert sample_trending_event.location == "Test Location"
        assert sample_trending_event.index == 1
        assert isinstance(sample_trending_event.emoji, str)
    
    def test_required_fields(self):
        """Test that all required fields are present."""
        event = TrendingEvent(
            title="Test",
            description="Desc",
            location="Loc",
            emoji="🌍",
            index=1
        )
        assert event.title == "Test"
        assert event.description == "Desc"
        assert event.location == "Loc"
        assert event.emoji == "🌍"
        assert event.index == 1


class TestSearchQuery:
    """Test SearchQuery model."""
    
    def test_creation(self):
        """Test SearchQuery creation."""
        query = SearchQuery(
            category="twitter",
            query="breaking news",
            purpose="Find recent posts"
        )
        assert query.category == "twitter"
        assert query.query == "breaking news"
        assert query.purpose == "Find recent posts"


class TestEventAnalysis:
    """Test EventAnalysis model."""
    
    def test_creation(self, sample_event_analysis):
        """Test EventAnalysis creation."""
        assert sample_event_analysis.event_name == "Test Event"
        assert len(sample_event_analysis.locations) == 2
        assert len(sample_event_analysis.search_queries) == 2
        assert isinstance(sample_event_analysis.search_queries[0], SearchQuery)


class TestContentItems:
    """Test content item models."""
    
    def test_twitter_item(self, sample_content_items):
        """Test TwitterItem model."""
        twitter_item = sample_content_items['twitter'][0]
        assert isinstance(twitter_item, TwitterItem)
        assert twitter_item.username == "testuser"
        assert twitter_item.likes == 100
        assert twitter_item.retweets == 25
        assert twitter_item.source == "twitter"
    
    def test_youtube_item(self, sample_content_items):
        """Test YouTubeItem model."""
        youtube_item = sample_content_items['youtube'][0]
        assert isinstance(youtube_item, YouTubeItem)
        assert youtube_item.channel_name == "Test News"
        assert youtube_item.views == 1000
        assert youtube_item.is_live is True
    
    def test_official_item(self, sample_content_items):
        """Test OfficialItem model."""
        official_item = sample_content_items['official'][0]
        assert isinstance(official_item, OfficialItem)
        assert official_item.agency == "Test Agency"
        assert official_item.report_type == "statement"
    
    def test_webcam_item(self, sample_content_items):
        """Test WebcamItem model."""
        webcam_item = sample_content_items['webcam'][0]
        assert isinstance(webcam_item, WebcamItem)
        assert webcam_item.is_live is True
        assert webcam_item.viewer_count == 150


class TestNormalizedData:
    """Test NormalizedData model."""
    
    def test_creation(self, sample_normalized_data):
        """Test NormalizedData creation."""
        assert sample_normalized_data.event_name == "Test Event"
        assert len(sample_normalized_data.locations) == 1
        assert len(sample_normalized_data.twitter) == 1
        assert len(sample_normalized_data.youtube) == 1
        assert len(sample_normalized_data.official) == 1
        assert len(sample_normalized_data.webcam) == 1
        assert sample_normalized_data.timestamp == "2024-01-01T12:00:00Z"


class TestGeoCoordinate:
    """Test GeoCoordinate model."""
    
    def test_creation(self, sample_geo_coordinate):
        """Test GeoCoordinate creation."""
        assert sample_geo_coordinate.latitude == 40.7128
        assert sample_geo_coordinate.longitude == -74.0060
        assert sample_geo_coordinate.accuracy == "high"
    
    def test_optional_accuracy(self):
        """Test GeoCoordinate with no accuracy."""
        coord = GeoCoordinate(latitude=0.0, longitude=0.0)
        assert coord.accuracy is None


class TestMapReadyItem:
    """Test MapReadyItem model."""
    
    def test_creation(self, sample_map_ready_items):
        """Test MapReadyItem creation."""
        item = sample_map_ready_items[0]
        assert item.label == "Test Twitter Post"
        assert item.category == "twitter"
        assert item.coordinates is not None
        assert isinstance(item.coordinates, GeoCoordinate)
        assert "source" in item.metadata


class TestYouMapPayload:
    """Test YouMapPayload model."""
    
    def test_creation(self, sample_youmap_payload):
        """Test YouMapPayload creation."""
        assert sample_youmap_payload.event_name == "Test Event"
        assert len(sample_youmap_payload.items) == 2
        assert sample_youmap_payload.total_items == 2
        assert sample_youmap_payload.created_at == "2024-01-01T12:00:00Z"


class TestAPIResponse:
    """Test APIResponse model."""
    
    def test_success_response(self, sample_api_response):
        """Test successful API response."""
        assert sample_api_response.success is True
        assert sample_api_response.data == {"test": "data"}
        assert sample_api_response.message == "Test successful"
    
    def test_error_response(self):
        """Test error API response."""
        error_response = APIResponse(
            success=False,
            data=None,
            message="Error occurred",
            timestamp="2024-01-01T12:00:00Z"
        )
        assert error_response.success is False
        assert error_response.data is None
        assert "Error" in error_response.message


class TestSystemConfig:
    """Test SystemConfig model."""
    
    def test_creation(self, mock_config):
        """Test SystemConfig creation."""
        assert mock_config.openai_api_key == "test-key-123"
        assert mock_config.max_items_per_category == 3
        assert mock_config.preview_items_count == 2
        assert mock_config.results_directory == "test_results"
    
    def test_defaults(self):
        """Test SystemConfig with default values."""
        config = SystemConfig()
        assert config.openai_api_key is None
        assert config.max_items_per_category == 5
        assert config.preview_items_count == 3
        assert config.results_directory == "results"
        assert config.prompts_file == "prompts/prompts.txt"

