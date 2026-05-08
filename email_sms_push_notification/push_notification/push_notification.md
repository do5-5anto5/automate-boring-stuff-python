# Push Notifications with ntfy.sh

[ntfy.sh](https://ntfy.sh) is a free, HTTP-based pub-sub notification service that allows you to send and receive short messages via simple web requests.

## Key Features
* **Free & Open:** No registration or sign-up required.
* **Cross-Platform:** Available for Android, iOS, and Web browsers.
* **Simple Integration:** Uses standard HTTP requests (can be used with the Python `requests` library).

## How it Works: Topics
The service operates on a **Topic** system, which functions like a public chat room:
* **Public Access:** Anyone can publish to or subscribe from any topic if they know the name.
* **Privacy:** To keep notifications private, use a "Secret Topic" (a long string of random letters and numbers) that acts as a password.
* **Case Sensitivity:** Topic names distinguish between uppercase and lowercase letters.

## Security Best Practices
> [!WARNING]
> Even when using secret topics, **never** send sensitive information (passwords, credit card numbers, etc.) through ntfy, as it is a public-facing service.

## Getting Started
1. **Install the App:** Download the `ntfy` app on your phone or use [ntfy.sh/app](https://ntfy.sh/app).
2. **Subscribe:** Add your unique topic name in the app to start listening for messages.
3. **Send Notifications:** Use an HTTP POST/PUT request to send a message to `https://ntfy.sh/your_topic`.