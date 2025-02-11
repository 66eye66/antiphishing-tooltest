# Anti-Phishing Tool

## Installation
1. Clone the repository.
2. Install dependencies: `pip install django`.
3. Run migrations: `python manage.py migrate`.
4. Run the Django admin panel: `python manage.py runserver`.

## Usage
- Access the admin dashboard at `http://localhost:8000/admin_dashboard`.
- Configure phishing detection rules, whitelist, and blacklist.

## Testing
Run tests with: `python -m unittest tests/test_agent.py`.

## GDPR/CCPA Compliance
Data anonymization is enabled by default. Update `settings.py` to disable if not required.