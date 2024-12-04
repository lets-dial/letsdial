Here's the updated `README.md` with the added link to *LetsDial*:

---

# LetsDial - Telecom Solutions API

Welcome to the official repository for *LetsDial*, a comprehensive Python library that provides businesses with a suite of telecom services. The LetsDial API integrates virtual numbers, bulk SMS messaging, VOIP solutions, and cloud contact center services—all designed to optimize business communications and customer interactions.

Visit our website: [LetsDial](https://www.letsdial.com/)

## Overview

*LetsDial* offers modern telecom tools tailored for businesses to enhance customer engagement and streamline communications. With cutting-edge technology, our platform makes it easier for companies to manage their telecom needs and scale efficiently.

This repository houses a Python package that simplifies integration with LetsDial's API, allowing users to easily implement services like virtual numbers, SMS campaigns, and voice solutions in their applications.

## Features

- **Virtual Numbers**: Get dedicated local or international phone numbers for your business operations.
- **VOIP Services**: Integrate reliable and cost-effective voice communication into your application.
- **Cloud Contact Center**: Build and manage a cloud-based call center with advanced features for support teams.

## Installation

To install the LetsDial Python package, follow these simple steps:

### 1. Clone the repository:

```bash
git clone https://github.com/LetsDial/letsdial-python.git
```

### 2. Navigate into the project directory:

```bash
cd letsdial-python
```

### 3. Install dependencies:

```bash
pip install -r requirements.txt
```

### 4. Install the package for local development:

```bash
pip install -e .
```

This will install the package in "editable" mode, allowing you to modify the code as needed while testing your changes.

## Usage Example

Once you've installed the package, you can begin interacting with LetsDial's services in your Python application.

Here’s an example of how to send a simple greeting message using the library:

### Example Code:

```python
# Import the LetsDial package
from letsdial import communication

# Initialize the service (replace with your actual credentials)
service = communication.LetsDialService(api_key='your_api_key')

# Send a greeting message
response = service.send_sms(
    to='+1234567890',  # Recipient phone number
    message='Hello, from LetsDial!'
)

print("Message sent successfully!" if response['status'] == 'success' else "Failed to send message")
```

This example demonstrates how to send an SMS using the LetsDial service. Replace `your_api_key` with your actual API key and the phone number with the recipient's phone number.

## Documentation

- **Virtual Numbers**: To request a virtual number, use the `get_virtual_number` function.
- **VOIP Calls**: The `make_voip_call` function facilitates VOIP calls for businesses.
- **Cloud Contact Center**: Use the `create_contact_center` function to create and manage cloud-based call centers.

For detailed documentation, check the [Wiki](https://github.com/LetsDial/letsdial-python/wiki) or refer to the API reference section.

## Contributing

We appreciate your interest in contributing to *LetsDial*. To help improve this project, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch for your feature or bug fix.
3. Commit your changes with descriptive messages.
4. Submit a pull request with a clear description of what you have changed.

### Code Style

- Follow PEP8 for Python coding standards.
- Write unit tests for new features.
- Ensure all tests pass before submitting your pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Support

If you have any questions, need help, or encountered any issues, feel free to reach out:

- Open an issue on GitHub.
- Contact us via email at [support@letsdial.com](mailto:support@letsdial.com).

## Contact

For general inquiries or business collaborations, visit our website at [LetsDial](https://www.letsdial.com/).

---

This version includes the link to *LetsDial*'s website at the appropriate locations. Let me know if you need any more changes!
