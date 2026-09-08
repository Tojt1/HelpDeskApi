import resend
import config

resend.api_key = config.RESEND_API_KEY

def sendWelocme_email(user_email):
    params = {
        "from": "onboarding@resend.dev",
        "to": [user_email],
        "subject": "Witaj!",
        "html": """
        <h1>Witaj w naszej aplikacji </h1>
        <p>Dziękujemy, że skorzystałeś z naszej aplikacji.</p>
        <p> Mamy nadziję, że miło będzie ci się z niej korzystało</p>
        <h2>HelpDesk API</h2>
        """
    }

    resend.Emails.send(params)


def sendDelete_email(user_email):
    params = {
        "from": "onboarding@resend.dev",
        "to": [user_email],
        "subject": "Przykro nam że już nas opuszczasz",
        "html": """
            <h1>Przykro nam, że już nas opuszczas</h1>
            <p>Siema</p>
        """
    }

    resend.Emails.send(params)
