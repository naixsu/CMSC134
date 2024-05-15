# Machine Problem 3

# Objectives

Provided a sample web application made using Flask, a web framework written in Python. Which uses sqlite3 as its database. 

In the sample web application, users are to authenticate themselves using their login credential. After authentication, they are able to post messages and view the messages they posted   

We are to:

- Identify the security flaws found in this web application
- Fix the security flaws found in this web application

# Security Flaws

## SQL injections

SQL injections makes use of input fields present in this web application to perform an attack. The said input fields acts as an interface to the server’s database. It is possible to make entries that would make the server perform commands, not as it was intended.

### Bypass authentication

- [http://127.0.0.1:5000/login](http://127.0.0.1:5000/login)

The attacker would be able to authenticate themselves as Alice. Alice’s credentials being the first entry on the `users` table in the database.

To perform the attack, open the login page [http://127.0.0.1:5000/login](http://127.0.0.1:5000/login).  Input `' OR 1=1 --` on any of the text field in the page. After, the web application should authenticate the attacker as Alice, redirecting them to Alice home page on [http://127.0.0.1:5000/home](http://127.0.0.1:5000/home).

[SQL injection attack to bypass authentication](mp3_writeup/Screencast_from_2024-05-08_20-36-50.mp4)

SQL injection attack to bypass authentication

![https://cdn.7tv.app/emote/60b2876f4f32610f15bfc5dc/4x.webp](https://cdn.7tv.app/emote/60b2876f4f32610f15bfc5dc/4x.webp)

### Post as a different user

- [http://127.0.0.1:5000/home](http://127.0.0.1:5000/home)

The structure of the database in regards with the post have three columns. The following are `posts.id`, `posts.message`, and `posts.user`. As the web application processes the posts through a database query, it is possible to manipulate the post entry to modify the `posts.user`. This allows for anyone to post a message to other users' home page; they can also employ other attacks such as XSS. In the demonstration, the post would be show up on user 2's home page. It is possible to add post to existing or future users.

[SQL injection attack to post as a different user](mp3_writeup/Screencast_from_2024-05-11_20-58-11.webm)

SQL injection attack to post as a different user

```text
post for 2', 2); --
```

> ‘; DROP TABLE USERS
> 

## Cross-Site Request Forgery(CSRF)

Cross-Site Request Forgery makes use of the fact the use have already authenticated to the web application. Where the attacker attempts to trick the victim in sending the request. Performing the request while as an authenticated user, which the victim is potentially unaware of.

### Posting as the authenticated user

- [http://127.0.0.1:5000/posts](http://127.0.0.1:5000/posts)

The attacker would be able to submit post entries through the posts POST method. For the attack to be successful, the victim should have authenticate themselves before hand. When the victim clicks a button either through a malicious webpage/email, it sends the POST method to the server. Essentially, posting a message as the victim (their authenticated account). 

[CSRF attack through a malicious website.](mp3_writeup/Screencast_from_2024-05-08_20-42-52.mp4)

CSRF attack through a malicious website.

[CSRF attack through a malicious email.](mp3_writeup/Screencast_from_2024-05-08_20-47-55.mp4)

CSRF attack through a malicious email.

In both instanced, the user/victim is redirected to the homepage of the web application. As this is the response of the server after the posts POST method.

![https://cdn.7tv.app/emote/60af769d2c36aae19e32ec9d/4x.webp](https://cdn.7tv.app/emote/60af769d2c36aae19e32ec9d/4x.webp)

> link trauma
> 

## **Cross-Site Scripting** (XSS)

Cross-Site Scripting makes use dynamic entries of this web application, which aren’t validated. Allowing an attacker to execute browser commands on a victim’s browser. 

### Attaching scripts on post entries

- [http://127.0.0.1:5000/home](http://127.0.0.1:5000/home)

The attacker would be able to add malicious content in the web application through the post entries.

To perform an attack, authenticate as a user in the web application. Open the home page [http://127.0.0.1:5000/home](http://127.0.0.1:5000/home). A text field allows for the entry of posts, an attacker can attach HTML scripts to the page. After posting, the said script would execute as soon the user opens their home page. 

[XSS attack showing web application vulnerability.](mp3_writeup/Screencast_from_2024-05-08_20-55-37.mp4)

XSS attack showing web application vulnerability.

```jsx
<script>alert("XSS attack!");</script>
```

[This attack adds a form in the web application as message. When the victim opens the home page, the said form would be submitted automatically. Infinitely until the user/victim closes the window. ](mp3_writeup/Screencast_from_2024-05-08_21-12-11.mp4)

This attack adds a form in the web application as message. When the victim opens the home page, the said form would be submitted automatically. Infinitely until the user/victim closes the window. 

```html
<!DOCTYPE html>
<html>
<body>
    <form action="http://127.0.0.1:5000/posts" method="POST">

        <input type="hidden" name="message" value="Pop"/>
        
    </form>
    <script>
		    document.forms[0].message.value = '<form action="http://127.0.0.1:5000/posts" method="POST"><input type="hidden" name="message" value="Pop"/></form><body onload="document.forms[1].submit()"></body>'
        document.forms[0].submit();
    </script>
</body>
</html>
```

![https://cdn.7tv.app/emote/63783e67a04774e6c0963a85/4x.webp](https://cdn.7tv.app/emote/63783e67a04774e6c0963a85/4x.webp)

> glueless
> 

## Session Hijacking Attack

Session Hijacking happens when an attacked is able to obtain a valid session id from their victim. Either through insecure cookie transmission, malware infected computers, or XSS attacks. The attacker would be able to retrieve the victim’s session id to the web application. The session id allows the victim to perform any request as the user. 

### Demonstration of Session Hijacking

In this demonstration, the victim is using the Firefox Browser in Ubuntu computer. While the attacker is using the Chrome Browser in an Android phone.

For demonstration purposes, the session id from the Firefox Browser (victim) is copied to Chrome Browser (attacker). But in real life scenarios for example, an attacker may use malware to obtain the victim’s cookies, XSS attacks or sniffed in an insecure channel.

[Demonstration of Session Hijacking](mp3_writeup/Screencast_from_2024-05-10_21-41-50.mp4)

![https://cdn.7tv.app/emote/61a78600e9684edbbc37c61c/4x.webp](https://cdn.7tv.app/emote/61a78600e9684edbbc37c61c/4x.webp)

> cookies
> 

# Fixes to Security Flaws

## SQL Injection

To address the flaw of the code, we parameterized the queries instead of directly concatenating user input into the SQL query. By doing so, the input is being treated as data rather than executable code, thereby preventing attackers from injecting malicious SQL code into the query. 

```python
# Old code
res = cur.execute(
		"SELECT id from users WHERE username = '"
    + request.form["username"]
    + "' AND password = '"
    + request.form["password"] + "'"
)
```

```python
# New code
res = cur.execute(
    "SELECT id from users WHERE username = ? AND password = ?", 
    (request.form["username"], request.form["password"])
)
```

## Cross-Site Request Forgery(CSRF)

To address the CSRF problem, the `flask_wtf.csrf` library was utilized so that CSRF tokens could be used. 

```python
app.config["SECRET_KEY"] = secrets.token_hex()
csrf = CSRFProtect(app)
```

What the above code essentially does is generate a secret key and assign it to Flask’s SECRET_KEY. Afterwards, every template included in the webpage must have the code below added in its <form> part and it pretty much does the CSRF protection for you. What’s happening in the background is that even if the attack caused the Post method to run, the server still checks the validity of it through the CSRF token generated. 

```python
<input type="hidden" name="csrf_token" value="{{ csrf_token() }}" />
```

The flask_wtf package was not included in the `requirements.txt`. Install the package in the web application server. 

```bash
pip install flask_wtf
```

## **Cross-Site Scripting** (XSS)

Similar to how we addressed the problem of SQL Injection, we parameterized the queries.  The only difference this time is that the `message` is passed through an `escape()` function from the `markupsafe` library, which essentially just replaces the characters `&`, `<`, `>`, `'`, and `"` in the string with HTML-safe sequences.

More info [https://markupsafe.palletsprojects.com/en/2.1.x/escaping/#markupsafe.escape](https://markupsafe.palletsprojects.com/en/2.1.x/escaping/#markupsafe.escape). 

```python
# Old code
cur.execute(
		"INSERT INTO posts (message, user) VALUES ('"
    + request.form["message"] + "', " + str(user[0]) + ");"
)
```

```python
# New code
cur.execute(
    "INSERT INTO posts (message, user) VALUES (?, ?);",
    escape(request.form["message"], user[0])
)
```

## Session Hijacking Attack

`session_token` is one of the cookies that facilitates the identification and authentication of users

#riot

![https://cdn.7tv.app/emote/61dbb508600369a98b38de67/4x.webp](https://cdn.7tv.app/emote/61dbb508600369a98b38de67/4x.webp)

Addressing the Session Hijacking Attack, two changes were made to the web application.

First, when setting the cookies for the session id. Two tags are set to true, `secure` and `httponly`. The secure tag ensures that the cookie for the session id is only sent through HTTPS or a secure channel. The httponly tag ensures that the cookie would not be access through server side scripts or a XSS attack. These two tags ensure the attacker would not be able to obtain this cookie throughout its transmission or a malicious website.

```python
# Old code
response.set_cookie("session_token", token)
```

```python

# New code
response.set_cookie("session_token", token, secure=True, httponly=True)
```

Second, identifying the user with their IP address. It is possible for an attacker to obtain the cookie or session id of their victim through malware. Thus, having the IP address to identify which device the user is on alongside the session id, ensures the authenticity of the connection, The database `app.db` was modified to accommodate to this change, adding the user’s IP address on their session id. Other database queries that involves the `sessions` table were also modified.

Adding entry to sessions table, for establishing authenticity with their session id (token) and IP address:
```sql
ALTER TABLE sessions
ADD COLUMN ipaddress [TEXT];
```

Adding entry to sessions table, for establishing authenticity with their session id (token) and IP address:
```python
cur.execute("INSERT INTO sessions (user, token, ipaddress) VALUES ("
                        + str(user[0]) + ", '" 
                        + token + "', '" 
                        + str(request.remote_addr)  + "');")
```

Checking authenticity with session id (token) and IP address:
```python
if request.cookies.get("session_token"):
    res = cur.execute("SELECT users.id, username FROM users INNER JOIN sessions ON "
                          + "users.id = sessions.user WHERE sessions.token = '"
                          + request.cookies.get("session_token") 
                          + "' AND sessions.ipaddress = '" + str(request.remote_addr) + "';")
    user = res.fetchone()
```
