# 🎫 HelpDesk API

#### REST API do obsługi zgłoszeń (ticketów) w systemie HelpDesk.
**Użytkownik może stworzyć zgłoszenie, nadać mu tytuł oraz opisać na czym polega jego proble,
natomiast administrator jest w stanie przypisać się do tego problemu,
a następnie kontaktować się z uytkownikiem aby go rozwiązać.
Na koniec administrator może zmienić ticket na zakończony po rozwiązaniu problemu.** 

---
##  ✨ Funkcjonalność
 - 👤 Logowanie i rejestracja użytkowników
 - 🔒Logowanie i autoryzacja za pomocą JWT
 - ✉️Tworzenie ticketów
 - 🛡️Role użytkwników
 - 🧑‍💼Przypisywanie agenta do ticketu
 - 💬Dodawanie komentarzy
 - 🔁Zmiana statussu ticketów
 - 🐳 Docker
 - 🧪Testy

---
## 🛠️ Technologie

| Technologia | Zastosowanie          |  
| ----------- |-----------------------|
|🐍 Python    | Główny język projektu |
|⚡️Fastapi    | Framework do FAST API |
| 🐘PostgreSQL| Baza danych           | 



**Projekt zosał podzielony na warstwy**  
repository.py  
router.py  
schemas.py  
service.py  



## Endpointy
| GET | `/` | Get all users |  
|POST| `/add-user`| add new user |  
|POST| `/login`| login to account|  
| GET | `/me` | get users information|  
|POST| `/tickets`| create ticket|  
| GET | `/tickets`| get tickets|  
| GET | `/tickets/{ticket_id}`| get ticket|  
|PATCH| `/tickets/{ticket_id}/assign`| assign agent to ticket|  
|POST| `/tickets/{ticket_id}/comments`| add comment for ticket|  
| GET | `/tickets/{ticket_id}/comments` | get comments for ticket|  
| GET | `/tickets/{ticket_id}/comments/{comment_id}`| get comment|  
|DELETE| `/tickets/{ticket_id}/comments/{comment_od}`| delet comment|  
|PATCH| `/tickets/{ticket_id}/comments/{comment_id}`| change comment_content|


## 📖 Czego nauczył mnie ten projekt?
 - Fastapi
 - Krud
 - docker
 - react

