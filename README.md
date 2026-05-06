# Asteroids

A clone of the classic Asteroids arcade game, built with Python and Pygame as part of [Boot.dev](https://boot.dev).

## Controls

| Key | Action |
|-----|--------|
| `W` | Thrust forward |
| `S` | Thrust backward |
| `A` | Rotate left |
| `D` | Rotate right |
| `Space` | Shoot |

Shoot asteroids to split them into smaller pieces. Avoid getting hit — one hit ends the game.

## Setup

This project uses **`uv`**, a fast Python package manager (think `npm` but for Python).

### 1. Install `uv`

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Or on macOS with Homebrew:

```bash
brew install uv
```

### 2. Clone the repo

```bash
git clone <repo-url>
cd asteroids
```

### 3. Run the game

```bash
uv run main.py
```

That's it. `uv` automatically creates a virtual environment and installs dependencies (just Pygame) on the first run — no separate install step needed.

## How `uv` works (for the JS-curious)

If you're coming from Node, here's the mental model:

| Node/npm | Python/uv |
|----------|-----------|
| `package.json` | `pyproject.toml` |
| `package-lock.json` | `uv.lock` |
| `node_modules/` | `.venv/` |
| `npm install` | `uv sync` (or just `uv run`) |
| `node index.js` | `uv run main.py` |

`uv run` is the key command — it handles environment setup automatically before running your script.
