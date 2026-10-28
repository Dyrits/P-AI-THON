# P-AI-THON

## About The Project

An AI coding agent in Python, from Boot.dev (per the project name in pyproject.toml): it sends a prompt to the Google Gemini API (google-genai) and can call local tools, such as reading file information and a calculator, to answer coding questions.

### Built With

- Python 3.12+
- Google Gemini API (google-genai)
- uv (project and dependency management)

## Getting Started

### Prerequisites

- uv (or Python 3.12+ with pip)
- A Gemini API key

### Installation

```sh
uv sync
```

Copy `.env.example` to `.env` and fill in the values.

### Running

```sh
uv run main.py "<your prompt here>"
```

## License

No license file is present in this repository.

## Contact

Dyrits - https://github.com/Dyrits
