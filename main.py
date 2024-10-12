# main.py

from demographic_data_analyzer import demographic_data_analyzer

def main():
    # Get the results
    result = demographic_data_analyzer()

    # Print results to verify
    for key, value in result.items():
        print(f"{key}: {value}")

# Import and run tests from test_module.py
if __name__ == "__main__":
    main()
    import test_module
    test_module.run_tests()
