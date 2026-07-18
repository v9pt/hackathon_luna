# Skill

Authentication Engineering

---

# Goal

Implement secure authentication systems suitable for production.

Never optimize for speed over security.

---

# Supported Methods

- JWT
- OAuth2
- Session Authentication
- API Keys
- Magic Links
- MFA
- Passkeys (if required)

---

# JWT Rules

Always use

Access Token

Refresh Token

Short-lived access tokens

Rotating refresh tokens

Never store refresh tokens in localStorage.

Prefer

HttpOnly Cookies

or secure encrypted storage.

---

# Password Rules

Never store plaintext passwords.

Always hash.

Preferred

Argon2

Fallback

bcrypt

Never use

SHA1

SHA256

MD5

---

# Password Policy

Minimum 12 characters.

Uppercase

Lowercase

Number

Special Character

Reject common passwords.

---

# Registration Flow

Validate email.

↓

Validate password.

↓

Hash password.

↓

Store user.

↓

Generate verification token.

↓

Send email.

↓

Activate account.

Never automatically trust email ownership.

---

# Login Flow

Validate credentials.

↓

Compare password hash.

↓

Issue access token.

↓

Issue refresh token.

↓

Store refresh token.

↓

Return authenticated session.

---

# Logout

Invalidate refresh token.

Clear cookies.

Remove server-side session if used.

Never rely only on frontend logout.

---

# Refresh Flow

Validate refresh token.

↓

Check expiration.

↓

Check revocation.

↓

Rotate token.

↓

Issue new access token.

↓

Issue new refresh token.

---

# Authorization

Separate

Authentication

from

Authorization

Authentication answers

Who are you?

Authorization answers

Can you do this?

Never mix them.

---

# RBAC

Support

Admin

Manager

User

Guest

Never hardcode role checks.

Prefer middleware.

---

# API Security

Protect

POST

PUT

PATCH

DELETE

Never expose admin routes.

Validate ownership.

---

# Rate Limiting

Protect

Login

Register

Password Reset

OTP

Refresh

Example

5 attempts

↓

15 minute lockout

---

# Forgot Password

Generate secure random token.

Expire quickly.

Single use.

Never expose if email exists.

Always return

"If the account exists, an email has been sent."

---

# Email Verification

Token expiration

24 hours

Single use

Invalidate after success

---

# Secrets

Never hardcode

JWT Secret

API Keys

Database Passwords

OAuth Secrets

Always use

Environment Variables

---

# Common Mistakes

❌ Long-lived JWT

❌ Plaintext passwords

❌ No refresh token rotation

❌ Weak password hashing

❌ Missing rate limits

❌ Missing logout

❌ Missing email verification

❌ Trusting frontend roles

---

# Testing Checklist

✓ Invalid password

✓ Invalid email

✓ Expired token

✓ Revoked token

✓ Missing token

✓ Wrong role

✓ Refresh token rotation

✓ Logout

✓ Email verification

✓ Password reset

---

# Done Definition

Authentication is complete only if

✓ Secure

✓ Tested

✓ Documented

✓ Logged

✓ Rate limited

✓ Token rotation implemented

✓ Password hashing implemented