import requests

def save_binary_response(url, output_file):
    try:
        # Make GET request
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Save the binary content to a file
            with open(output_file, 'wb') as file:
                file.write(response.content)
            print(f"Binary content saved to {output_file}")
        else:
            print(f"Error: {response.status_code} - {response.text}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
url = "https://tiles-dev.arealytics.com.au/data/buildings/16/60625/37972.json"
output_file = "output.pbf"
save_binary_response(url, output_file)
