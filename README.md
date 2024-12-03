# Automatic Module Documentation Finder (AMDF)

Automatic Module Documentation Finder (AMDF) is a Python tool that helps users quickly find and display documentation for Python modules from PyPI (Python Package Index). It searches for modules on PyPI, fetches their descriptions and URLs, and presents the information in a colorful CLI interface. AMDF also caches documentation locally to speed up future requests and provides random hackathon tips to keep you motivated.

## Features

- **Search for Python modules** on PyPI and display their documentation.
- **Cache module documentation** locally to reduce future fetching time.
- **Colorful CLI output** to make information easy to read and engaging.
- **Random hackathon tips** to boost productivity and motivation.
- **Simple command-line interface** for quick access.

## Requirements

- Python 3.x
- The following Python packages:
  - `requests`
  - `beautifulsoup4`

To install the required dependencies, run:

```bash
pip install requests beautifulsoup4
```

## Usage

### Finding Documentation for a Module

To use AMDF, run the following command in your terminal:

```bash
python main.py <module_name>
```

Replace `<module_name>` with the name of the Python module you want to search for.

Example:

```bash
python main.py requests
```

AMDF will search for the module on PyPI, fetch its documentation, and display the module name, description, and URL. The documentation is then cached locally for future use.

### Example Output

```bash
Welcome to Automatic Module Documentation Finder (AMDF)!
This tool helps you find documentation for Python modules.

Searching for documentation of requests...
Found PyPI page: https://pypi.org/project/requests/

Module: requests
Description: Simple, yet elegant HTTP library.
More Info: https://pypi.org/project/requests/

Hackathon Tip: Remember to take breaks and stay hydrated!
```

## Cache

AMDF caches documentation for each module in the `.module_docs_cache` directory located in your home directory. This speeds up the process when fetching the same module documentation multiple times.

## Hackathon Tips

Along with module documentation, AMDF provides a random hackathon tip to keep you inspired. These tips include advice on time management, collaboration, debugging, and more.

--
