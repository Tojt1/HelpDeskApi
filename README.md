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

| Technologia  | Zastosowanie             |  
|--------------|--------------------------|
| 🐍 Python    | Główny język projektu    |
| ⚡️Fastapi    | Framework do FAST API    |
| 🐘PostgreSQL | Baza danych              | 
| 🔌psycopg2   | komunikacja z PostgreSQL |
| 🔑 JWT       | Autoryzcaja użytkowników |
| 🔒 bcrypt    | hashowanie haseł         | 
| 🐳 Docker    | konteneracja aplikacji   |
| 🧪pytest     | testowanie aplikacji     |

--- 

## 🏗 Architektura projektu 

Projekt został podzielony na kilka warstw,
aby oddzielić odpowiedzialność poszczególnych elementów

 - repository -> komunikacja z bazą danych
 - router -> endpointy API
 - schemas -> modele i walidacja danych
 - service -> logika 

---

## 📡 Endpointy
| Metoda | endpoint | Opis|
|--------|---|---|
| GET    | `/` | Get all users |  
| POST   | `/add-user`| add new user |  
| POST   | `/login`| login to account|  
| GET    | `/me` | get users information|  
| POST   | `/tickets`| create ticket|  
| GET    | `/tickets`| get tickets|  
| GET    | `/tickets/{ticket_id}`| get ticket|  
| PATCH  | `/tickets/{ticket_id}/assign`| assign agent to ticket|  
| POST   | `/tickets/{ticket_id}/comments`| add comment for ticket|  
| GET    | `/tickets/{ticket_id}/comments` | get comments for ticket|  
| GET    | `/tickets/{ticket_id}/comments/{comment_id}`| get comment|  
| DELETE | `/tickets/{ticket_id}/comments/{comment_od}`| delet comment|  
| PATCH  | `/tickets/{ticket_id}/comments/{comment_id}`| change comment_content|

---

## 🚀 Uruchomienie proejktu
Pobierz wymagane rzeczy 
 1. ``pip install -r requirements.txt``
2.  wupewnij się ze mansz: 
- Docker
- Docker Compose 
- Python

3. 🐳 Docker  
**Projekt mozna uruchomic za pomoca Dockera**  
``Docker compose up --build``


4. Po uruchomieniu API powinno być dostępne pod:  
``http://localhost:8000``

---

## 🧪Testy
testy projektu zstały stworzone za pomocą **PYTEST** 

aby uruchomić:
``pytest``


## 📚Czego nauczył mnie ten projekt?
 - Tworzenie Rest API przy użyciu FASTAPI
 - implementowanie autoryzacji za pomocą JWT
 - zabezpieczanie haseł za pomocą bcrypt
 - tworzenue testów przy użyciu pytest
 - Dockera
 - Podstawy pracy z React
 - Implementacji CRUD

---
## 🧑‍💻 Status projektu
Projekt jest ciągle rozwijany, służy on jako projekt edukacyjny.
