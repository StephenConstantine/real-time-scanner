# 🗺️ Codebase Architecture Map

> 🤖 **AI Context File**: Read this to understand the entire codebase structure and relationships

---

## 🎯 System Architecture Overview

```
🌍 Real-Time Scanner Pipeline
    │
    └── 🔁 Step 0: Trending Events Detection
        │
        └── 🔁 Step 1: Event Analysis
            │
            └── 🔁 Step 2: Content Retrieval
                │
                └── 🔁 Step 3: Data Normalization
                    │
                    └── 🔁 Step 4: Final Integration
                        │
                        🏁 OUTPUT
```

---

## 📁 Module Detailed Breakdown

### 🌟 `step_0_trending_events.py`
**Purpose**: Initial event detection and trending analysis  
**Input**: External APIs/feeds  
**Output**: Raw trending events data  
**Key Functions**: 
- Event detection algorithms
- Trend scoring mechanisms
- Data source integration

**📄 Current Implementation Status**: 
- ❓ Needs review - check for hardcoded vs dynamic prompts
- ❓ API integration status unknown
- ❓ Error handling needs assessment

---

### 🧠 `step_1_event_analysis.py`
**Purpose**: Deep analysis of detected events  
**Input**: Raw events from step_0  
**Output**: Analyzed event data with insights  
**Key Functions**:
- Event categorization
- Sentiment analysis
- Impact assessment

**📄 Current Implementation Status**:
- ❓ AI prompts usage needs review
- ❓ Analysis algorithms need documentation
- ❓ Performance optimization needed

---

### 📥 `step_2_content_retrieval.py`
**Purpose**: Fetch additional content related to events  
**Input**: Analyzed events from step_1  
**Output**: Enriched events with additional content  
**Key Functions**:
- Content scraping/API calls
- Data validation
- Content filtering

**📄 Current Implementation Status**:
- ❓ Rate limiting implementation unknown
- ❓ Content source diversity needs review
- ❓ Caching mechanisms missing

---

### 🔄 `step_3_data_normalization.py`
**Purpose**: Clean and standardize all collected data  
**Input**: Raw content from step_2  
**Output**: Normalized, structured data  
**Key Functions**:
- Data cleaning
- Format standardization
- Quality assurance

**📄 Current Implementation Status**:
- ❓ Data validation rules need review
- ❓ Output format standardization needed
- ❓ Error handling for malformed data

---

### 🔗 `step_4_final_integration.py`
**Purpose**: Final data integration and output generation  
**Input**: Normalized data from step_3  
**Output**: Final processed results  
**Key Functions**:
- Data aggregation
- Report generation
- Output formatting

**📄 Current Implementation Status**:
- ❓ Output format needs standardization
- ❓ Integration with external systems unknown
- ❓ Performance metrics needed

---

### 📊 `models.py`
**Purpose**: Data models and structures  
**Contains**: 
- Event data models
- Configuration classes
- Data validation schemas

**📄 Current Implementation Status**:
- ❓ Model completeness needs review
- ❓ Type hints need verification
- ❓ Validation logic needs testing

---

### 🛠️ `utils.py`
**Purpose**: Shared utility functions  
**Contains**:
- Common helper functions
- Configuration management
- Logging utilities

**📄 Current Implementation Status**:
- ❓ Function documentation needed
- ❓ Error handling review required
- ❓ Performance optimization opportunities

---

## 💭 Prompts System

### 📁 `prompts/` Directory
**Purpose**: AI prompt templates and management  
**Key Issue**: User mentioned prompts should be DYNAMIC, not hardcoded  

**🚨 Critical TODO**: 
- Review current prompt implementation
- Design dynamic prompt system
- Implement context-aware prompt generation

---

## 📊 Results & Output

### 📁 `results/` Directory
**Purpose**: Store processed outputs  
**Structure**: TBD - needs standardization  

---

## 🔧 Configuration & Environment

### 🔐 `.env.template`
**Purpose**: Environment configuration template  
**Contains**: API keys, configuration parameters  

### 📋 `requirements.txt`
**Purpose**: Python dependencies  
**Status**: ❓ Needs dependency audit and cleanup  

---

## 🔄 Data Flow Diagram

```
🌍 External Sources
    │
    ↓ 📥 Fetch
    │
🌟 Step 0: Trending Events
    │
    ↓ 📊 Raw Events
    │
🧠 Step 1: Analysis
    │
    ↓ 📊 Analyzed Events
    │
📥 Step 2: Content Retrieval
    │
    ↓ 📊 Enriched Events
    │
🔄 Step 3: Normalization
    │
    ↓ 📊 Clean Data
    │
🔗 Step 4: Integration
    │
    ↓ 📊 Final Output
    │
📊 Results Storage
```

---

## 🔍 Dependencies & Relationships

### 🔗 Module Dependencies
- All steps depend on `models.py` for data structures
- All steps use `utils.py` for common functions
- Sequential dependency: step_n depends on step_(n-1)
- `prompts/` system used by analysis steps

### 🎯 External Dependencies
- API services (need documentation)
- Database connections (status unknown)
- File system for results storage

---

## 📝 Notes for Future AI Sessions

### 🔍 Key Questions to Investigate:
1. **Dynamic Prompts**: How are prompts currently managed? Are they hardcoded?
2. **Error Handling**: What happens when steps fail?
3. **Configuration**: How is the system configured for different environments?
4. **Testing**: What test coverage exists?
5. **Performance**: Are there bottlenecks in the pipeline?

### 🚀 Recommended First Actions for New AI Sessions:
1. Read `AI_SESSION_LOG.md` for context
2. Review recent Git commits
3. Examine current prompts implementation
4. Test run the pipeline to identify issues
5. Update documentation after any changes

---

*🤖 Last Updated: 2025-06-15T18:09:46Z by Claude (Anthropic)*

