
# Getting Started

## Clone the repository

```bash
git clone https://github.com/JonathanMiz/first-rag-tutorial.git
```

## Create a virtual environment

```bash
python3 -m venv .venv
```

## Activate virtual environment

```bash
source .venv/bin/activate
```

## Install dependencies

```bash
pip3 install -r requirements.txt
```

## Add OpenAI API key

Create a file called `.env` in the root directory and add the following line:

```
OPENAI_API_KEY=your-api-key
```

## Build the database

```bash
python3 build_vector_db.py
```

## Query the database

```bash
python3 main.py
```

## Watch the full step-by-step tutorial

[![Watch the tutorial](https://img.youtube.com/vi/dNIQgDVDt1k/maxresdefault.jpg)](https://youtu.be/dNIQgDVDt1k)