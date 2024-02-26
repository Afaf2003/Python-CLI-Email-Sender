
# Python Command Line Email Sender

This Python script provides a simple command line interface (CLI) to send emails. It allows users to specify the recipient's email address, subject, and message content directly from the terminal.

## Prerequisites

Before running the script, ensure you have Python 3 installed on your system.

## Setup

1. Clone the repository to your local machine:

```bash
git clone https://github.com/Afaf2003/My-first-Repo.git
```

2. Navigate to the project directory:

```bash
cd My-first-Repo
```


## Usage

Run the script `main.py` with the following command:

```bash
python main.py "sender@example.com" "receiver@example.com" "password_sender" "Your Subject" "Your Message Body"
```

Replace `recipient@example.com` with the recipient's email address, `"Your Subject"` with the subject of the email, and `"Your Message Body"` with the content of the email message.

You will be prompted to enter your email credentials (username and password) for authentication.

**Note:** If you're using Gmail, you may need to allow less secure apps to access your account. You can do this by going to your Google account settings and enabling "Allow less secure apps".

## Options

The script supports the following command line options:

- `--to`: The email address of the recipient.
- `--subject`: The subject of the email.
- `--message`: The content of the email message.
- `--attachment` (optional): Path to an attachment file to be included in the email.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This script was inspired by the need for a simple way to send emails via command line.
- Special thanks to the developers of the libraries used in this project.

Feel free to contribute to this project by submitting bug fixes, feature enhancements, or suggestions!
