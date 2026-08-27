# HelpDesk API

**Jest to projekt w którym użytkownik może utworzyć ticket z problemem,
natomiast administrator może przypisać się do tego ticketu aż nie zostanie on zakońcxzony**

##  📝Funkcjonalność

- Rejestracja użytkownika
- Twordzenie tokenów JWT
- Role użytkownika
- Tworzenie ticketów
- Przypisywanie agenta
- tworzenie komentarzy
- zmiana statusu
- usuwanie komentarzy
- Filtrowanie
- Docker
- Test

## 💡Technologie

 - Python
 - FastApi
 - Postgresql
 - psycopg2
 - JWT
 - bcrypt
 - Docker
 - Pytest



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

