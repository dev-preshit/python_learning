"""
    #Day 43 is about Virtual Environment in Python...
        A virtual environment is a tool used to isolate specific 
        Python environments on a single machine, allowing you to work
        on multiple projects with different dependencies and packages 
        without conflicts. This can be especially useful when
        working on projects that have conflicting package versions 
        or packages that are not compatible with each other.
        To create a virtual environment in Python, you can use the venv 
        module that comes with Python. Here's an example of
        how to create a virtual environment and activate it.
"""
"""
    # Create a virtual environment
        python -m venv myenv(env_name)

    # Activate the virtual environment (Linux/mac0S)
        source myenv/bin/activate

    # Activate the virtual environment (Windows)
        myenv/Scripts/activate.bat (ps1 if working in powershell)

    # Deactivate the virtual environment
        deactivate

    # Output the list of installed packages and their versions to a file
        pip freeze > requirements. txt
    This will create a requirements .txt file that will have data 
    of packages with there version

    # Install the packages listed in the requirements. txt file
        pip install -r requirements .txt
"""