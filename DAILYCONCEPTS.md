# Daily Concepts Used

## Day 1: System Structure & Setup

### Architecture
Organizing files and folders in such a way that there is proper readability and structure. A robust architecture separates concerns (e.g., separating data ingestion, processing, and output) and ensures the repository remains navigable as complexity grows.

### Virtual Environment
An isolated Python environment designed to avoid conflicts with global Python installations and to manage dependency versions on a per-project basis.
* **Command:** `python -m venv venv`
* **Best Practice:** Always activate the virtual environment before installing packages to ensure project encapsulation.

### Requirements Management
The tracking of dependencies and allowing proper manageability. Utilizing tools to generate a `requirements.txt` or `pyproject.toml` ensures that the exact versions of libraries are documented, allowing seamless deployment and collaboration.

### Git
A Version Control System (VCS) allowing teams to track codebase changes, revert to previous history states, and collaborate concurrently through branching and merging.

### Modular Design
Breaking down functionality into smaller, logically separated modules to ensure code reusability and easier problem handling. This avoids monolithic scripts and makes unit testing straightforward.

### Notebook Workflow
Utilizing an experimentation environment (like Jupyter Notebooks) instead of directly writing untested logic into production modules. It allows developers to verify whether each unit of code works as expected through iterative, visual feedback.

---

## Day 2: Code Quality & Error Handling

### Defensive Programming
Writing code that inherently expects things to go wrong. Robust software anticipates user errors and edge cases.
* **Scenario:** Users may provide an incorrect file type (e.g., `a.csv` instead of `b.csv`), or malformed data. Real systems must handle bad inputs via validation checks rather than allowing the program to crash on corrupted data.

### Exception Handling
Handling runtime errors safely to maintain control flow. Without this, an application may crash abruptly. Exception handling catches these anomalies, allowing the application to report useful error messages or execute fallback procedures.
* **Implementation Example:**
    ```python
    try:
        # Code that might raise an exception
        process_data()
    except FileNotFoundError:
        # Graceful error reporting
        print("Required file was not found. Please check the directory.")
    except Exception as e:
        # Catch-all for unexpected issues
        print(f"An unexpected error occurred: {e}")
    ```

### Metadata
Data that provides information about other data.
* **Examples:** Number of rows, columns, data types, null counts, and memory usage.
* **Usage:** Exploratory Data Analysis (EDA) and Machine Learning decisions heavily depend on metadata. In advanced architectures, it is used by automated modules such as a Cleaning Agent, EDA Agent, and Feature Agent to make dynamic processing decisions.

### Logging Levels
A standardized way to track system behavior and execution flow, crucial for debugging production environments (e.g., deployed AI models). Common logging levels from least to most severe are:
1.  **DEBUG:** Detailed information for diagnosing problems.
2.  **INFO:** Confirmation that the program is working as expected.
3.  **WARNING:** An indication of an unexpected event, though the software continues to function.
4.  **ERROR:** A serious problem preventing a specific function from executing.
5.  **CRITICAL:** A fatal error indicating the program may crash or halt.

### Single Responsibility Principle (SRP)
The principle stating that **One function = One responsibility**. Each function, class, or module should have only one reason to change, making the codebase highly maintainable, readable, and easier to unit-test.
