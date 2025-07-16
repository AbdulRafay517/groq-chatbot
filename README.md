# Groq Chatbot

A Python-based chatbot project designed for experimenting with intent recognition and conversational AI. The repository contains multiple versions (`v1.py`, `v2.py`, `v3.py`, `v4.py`) to showcase iterative improvements and different approaches to chatbot logic.

## Features

- Intent recognition using data from `intents.csv`
- Modular Python scripts for chatbot logic
- Follows PEP8 and uses type hints
- Designed for extensibility and experimentation

## File Structure

- `intents.csv`: Contains intent definitions and example utterances
- `v1.py` to `v4.py`: Different versions of the chatbot implementation

## Getting Started

1. **Clone the repository:**

   ```cmd
   git clone https://github.com/AbdulRafay517/groq-chatbot.git
   cd groq-chatbot
   ```

2. **Install dependencies:**

   - This project uses only standard Python libraries. If you add external dependencies, list them here and update setup instructions.

3. **Run a chatbot version:**

   ```cmd
   python v1.py
   ```

   Replace `v1.py` with any version you want to test.

## Development Guidelines

- Use Python 3.8+
- Follow PEP8 and format code with `black`
- Add unit tests in a `/tests` folder (mirror main app structure)
- Use `pydantic` for data validation if adding models
- Prefer modular code and clear separation of concerns

## Contributing

1. Fork the repo and create your branch.
2. Add new features in a new version file (e.g., `v5.py`) or as a module.
3. Write unit tests for new features.
4. Update this `README.md` as needed.

## License

MIT License

---
*This README is generated based on the repository structure and project conventions. Update as new features or dependencies are added.*
