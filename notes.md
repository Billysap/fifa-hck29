Notes for Environment Setup

1. Prerequisite : make sure you have installed Miniconda or Anaconda.

2. `h8_env.yml` file
    - The file can be downloaded from: https://drive.google.com/file/d/1_jXaxlZDRkawfzSzMs83VbuG-j5iOt0I/view?usp=sharing
    - This file contains a list of Python libraries required for the Hacktiv8 Full-Time Data Science Bootcamp.
    - The Python version used is Python 3.9.

3. Installation guide
    - Open Command Prompt (Windows) or Terminal (macOS/Linux).
    - Navigate to the directory where the `h8_env.yml` file is located.
    - Run the following command to create the environment:
        ```bash
        conda env create -f h8_env.yml
        ```
    - Wait for the installation to complete.
    - Once finished, a new Python environment named `h8_env` will be created.

4. To see a list of all Python environments on your machine, run:
    ```bash
    conda env list
    ```

5. To activate the newly created `h8_env`, type:
    ```bash
    conda activate h8_env
    ```

6. Important : always make sure to use the `h8_env` environment when working on Hacktiv8 assignments or exercises.