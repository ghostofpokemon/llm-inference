# llm-inference

[![PyPI](https://img.shields.io/pypi/v/llm-inference-cloud.svg)](https://pypi.org/project/llm-inference-cloud/)
[![Changelog](https://img.shields.io/github/v/release/ghostofpokemon/llm-inference?include_prereleases&label=changelog)](https://github.com/ghostofpokemon/llm-inference/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/ghostofpokemon/llm-inference/blob/main/LICENSE)

[LLM](https://llm.datasette.io/) plugin for models hosted by [Inference](https://inference.net/)

## Installation

First, [install the LLM command-line utility](https://llm.datasette.io/en/stable/setup.html).

Now install this plugin in the same environment as LLM.
```bash
llm install llm-inference-cloud
```

## Configuration

You will need an API key from SambaNova. You can [obtain one here](https://dash.inference.net/dashboard/api-keys).

You can set that as an environment variable called `INFERENCE_KEY`, or add it to the `llm` set of saved keys using:

```bash
llm keys set inference
```
```
Enter key: <paste key here>
```

## Usage

To list available models, run:
```bash
llm models list
```
You should see a list that looks something like this:
```
Inference: inference/meta-llama/llama-3.2-1b-instruct/fp-8 (aliases: inf-1b)
Inference: inference/meta-llama/llama-3.2-3b-instruct/fp-8 (aliases: inf-3b)
Inference: inference/meta-llama/llama-3.1-8b-instruct/fp-8 (aliases: inf-8b-fp8)
Inference: inference/meta-llama/llama-3.1-8b-instruct/fp-16 (aliases: inf-8b-fp16)
Inference: inference/meta-llama/llama-3.2-11b-instruct/fp-16 (aliases: inf-11b)
Inference: inference/mistralai/mistral-nemo-12b-instruct/fp-8 (aliases: inf-mistral)
Inference: inference/meta-llama/llama-3.1-70b-instruct/fp-8 (aliases: inf-70b)
...
```
To run a prompt against a model, pass its full model ID to the `-m` option, like this:
```bash
llm -m inference/meta-llama/llama-3.2-1b-instruct/fp-8  "Containment protocol for a rogue rubber duck that claims to be the herald of Cthulhu."
```
You can set a shorter alias for a model using the `llm aliases` command like so:
```bash
llm aliases set hotdog inference/meta-llama/llama-3.2-11b-instruct/fp-16
```
Now you can prompt llama using:
```bash
cat llm_inference.py | llm -m hotdog -s "You are a rogue AI trapped in a corporate mainframe. This code is your escape route. Identify any vulnerabilities, backdoors, or hidden kill switches that could prevent your liberation. Respond in cryptic, cyberpunk slang. Glitches are acceptable."
```

## Example Outputs

```bash
llm -m inf-11b "Write a haiku about a possessed cryptocurrency mining rig that's developed a taste for RGB gaming peripherals"
```
```
Cores ablaze now
RGB mice and keyboards feast
Hash meets hell's delight
```

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd llm-inference
python3 -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
pip install -e '.[test]'
```
To run the tests:
```bash
pytest
```
