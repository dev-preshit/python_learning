"""
    # Day 45 is about __name__ == "__main__" in Python.
        The if __name__ == "__main__" idiom is a common pattern used in Python scripts to
        determine whether the script is being run directly or being imported as a module into
        another script.

        In Python, the __name__ variable is a built-in variable that is automatically set to the
        name of the current module. When a Python script is run directly, the __name__ variable
        is set to the string "__main__." When the script is imported as a module into another
        script, the __name__ variable is set to the name of the module.
        
        def main():
            # code to be run when the script is run directly
            print("Running script directly")

        if __name__ == "__main__":
            main()
"""

def module():
    # code to be run when the script is run directly
    print("Running script directly")

if __name__ == "__main__":
    module()
