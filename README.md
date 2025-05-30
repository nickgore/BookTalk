
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

To be done...

## 🏗️ Workflow

```
GitBook URL → Content Scraper → Text Chunker → Embedding Generator → Vector Database
                                                                             ↓
User Question → Vector Search → Context Retrieval → LLM API → Response with Citations
```


## 🔮 Roadmap

- [ ] **Phase 1**: Basic URL processing and chat interface
- [ ] **Phase 2**: Multi-LLM support and advanced retrieval
- [ ] **Phase 3**: OpenAI API integration


