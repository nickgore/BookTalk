
**!!! Note**: This project is currently in active development. Features and documentation may change as the project evolves.

# BookTalk RAG Chat

A smart documentation assistant that transforms any **GitBook** documentation into an interactive **AI-powered chat** interface. Built with low-code tool **Retool**.

## 🚀 Features (WIP...)

- **Multi-Source Documentation**: Ingest GitBook documentation from any public URL.
- **Intelligent Chat Interface**: Ask questions in natural language and get contextual answers
- **Multi-LLM Support**: Choose between chat API
- **Vector Search**: Semantic similarity search for more accurate information retrieval


## 🛠️ Tech Stack

- **Frontend**: Retool (Self-hosted)
- **Database**: PostgreSQL with pgvector extension
- **AI/ML**: Bert Embeddings, Multiple LLM APIs
- **Infrastructure**: Docker Compose
- **Vector Storage**: pgvector for semantic search


## 🚀 Quick Start

### Prerequisites

- **Docker** and **Docker Compose** installed

### 1. Clone and launch:
```bash
git clone git@github.com:nickgore/BookTalk.git
cd BookTalk
cp .env.example .env
# !!! Edit .env with your valid retool license key

# Launch all services
docker-compose up -d
```


> **Note**: Get a free Retool license at [retool.com](https://retool.com) for self-hosted deployment


### 2. Initial Retool Setup

1. **Open Retool in your browser:**
   ```
   http://localhost:3000/auth/signup
   ```

2. **Create admin account:**
   - Fill in your email address
   - Create a secure password
   - Complete the setup wizard

3. **You'll be redirected to the Retool dashboard**

### 3. Import the BookTalk App
- Click **"Create"** → **"From JSON/ZIP"**
- Upload the file: `./retool/apps/BookTalk.json`


## 🏗️ Workflow

```
GitBook URL → Content Scraper → Text Chunker → Embedding Generator → Vector Database
                                                                             ↓
User Question → Vector Search → Context Retrieval → LLM API → Response with Citations
```


## 🔮 Roadmap

- [x] **Phase 1**: Basic URL processing and chat interface
- [x] **Phase 2**: OpenAI API integration
- [ ] **Phase 3**: GitBook parser with API interface (python, langchain)
- [ ] **Phase 4**: Vector search
- [ ] **Phase 5**: Multi-LLM support and advanced retrieval



## Monitoring with Portainer
Access Portainer at http://localhost:9000 to monitor your containers in real-time. You can view resource usage, logs, and restart services if needed.
