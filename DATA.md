# Data Structures - Cognitive Science Memorial Website
**Version:** 1.0.0 | **Date:** 17. Oktober 2025 | **Phase:** DATA

## CORE DATA ENTITIES

### 1. SUBMISSION (Einreichung)
Represents a memory or success story submitted by an alumnus/visitor.

```
Submission {
  id: UUID (unique identifier)
  status: ENUM [pending, approved, rejected]
  submission_date: DateTime (ISO 8601)
  publication_date: DateTime | null (set when approved)
  
  // Content fields
  author_name: String (required, 2-100 chars)
  author_email: String (optional, for contact/notifications)
  graduation_year: Integer | null (optional, e.g., 2015)
  title: String (required, 5-200 chars, headline for story)
  content: Text (required, 50-5000 chars, the actual memory/story)
  story_type: ENUM [memory, success_story, both] (optional categorization)
  
  // Metadata
  ip_address: String (spam prevention, GDPR consideration)
  user_agent: String (browser info)
  moderation_notes: Text | null (admin internal notes)
  moderated_by: String | null (admin username)
  moderation_date: DateTime | null
}
```

**Validation Rules:**
- `author_name`: Required, trim whitespace, no HTML
- `title`: Required, max 200 chars, sanitize for XSS
- `content`: Required, min 50 chars (ensure substance), max 5000 chars, preserve paragraphs
- `graduation_year`: Optional, range 1990-2029 (program existence period)
- `author_email`: Optional, valid email format if provided

**Example Record (Approved):**
```json
{
  "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "status": "approved",
  "submission_date": "2025-10-15T14:23:00Z",
  "publication_date": "2025-10-16T09:00:00Z",
  "author_name": "Maria Schmidt",
  "author_email": "maria.schmidt@example.com",
  "graduation_year": 2018,
  "title": "Von der Kogni zur KI-Forschung",
  "content": "Mein Studium der Kognitionswissenschaft hat mir die Türen zur KI-Forschung geöffnet. Die interdisziplinäre Ausbildung war perfekt für meine spätere Karriere...",
  "story_type": "success_story",
  "moderation_notes": "Approved - inspiring story",
  "moderated_by": "admin1",
  "moderation_date": "2025-10-16T08:55:00Z"
}
```

**Example Record (Pending):**
```json
{
  "id": "b2c3d4e5-f6g7-8901-bcde-fg2345678901",
  "status": "pending",
  "submission_date": "2025-10-17T10:15:00Z",
  "publication_date": null,
  "author_name": "Anonym",
  "author_email": null,
  "graduation_year": null,
  "title": "Unvergessliche Seminaratmosphäre",
  "content": "Die kleinen Seminare und die enge Betreuung durch die Dozenten haben das Kogni-Studium so besonders gemacht...",
  "story_type": "memory",
  "moderation_notes": null,
  "moderated_by": null,
  "moderation_date": null
}
```

### 2. ADMIN USER (Administrator)
Manages content moderation (simplified authentication for MVP).

```
AdminUser {
  id: UUID
  username: String (unique, required)
  password_hash: String (bcrypt/argon2)
  email: String
  created_date: DateTime
  last_login: DateTime | null
  is_active: Boolean (for deactivation)
}
```

**Note:** Basic auth sufficient for MVP. Consider university SSO integration for official deployment.

### 3. CONFIGURATION (Website-Einstellungen)
Global settings for the memorial website.

```
Configuration {
  site_title: String (default: "Kognitionswissenschaft - Erinnerungen & Erfolge")
  welcome_message: Text (displayed on homepage)
  submission_open: Boolean (enable/disable new submissions)
  items_per_page: Integer (pagination, default: 20)
  program_end_year: Integer (default: 2029)
  display_mode: ENUM [chronological, random, curated] (ordering of approved stories)
  show_graduation_year: Boolean (privacy option)
}
```

## DATA FLOW

### Submission Flow
```
1. User visits website
   ↓
2. Fills submission form (name, title, content, optional: email, grad year)
   ↓
3. Submits → Validation (client + server-side)
   ↓
4. If valid → Create Submission record with status="pending"
   ↓
5. Confirmation page shown to user
   ↓
6. Admin reviews in moderation panel
   ↓
7. Admin approves → status="approved", publication_date=now
   OR
   Admin rejects → status="rejected", internal notes
   ↓
8. Approved submissions appear on public page
```

### Display Flow
```
1. Public page loads
   ↓
2. Query: SELECT * FROM submissions WHERE status='approved' ORDER BY publication_date DESC
   ↓
3. Render submissions (title, author, optional grad year, content, date)
   ↓
4. Pagination if needed
```

## DATA STORAGE

### MVP Options
1. **SQLite** - Simple, file-based, sufficient for moderate traffic
2. **PostgreSQL** - Recommended for university hosting, scalable
3. **JSON files** - Quick prototype only, not recommended for production

### Recommended: SQLite for MVP, PostgreSQL for production

## DATA VOLUMES (Estimated)

- **Expected submissions:** 50-500 over 4 years
- **Approved rate:** ~80% (after moderation)
- **Display content:** 40-400 stories
- **Average story size:** 500-1000 chars = ~1KB per story
- **Total storage:** < 1MB for text content (negligible)

## DATA PRIVACY (GDPR)

### Personal Data Collected
- Name (required) - potentially pseudonymous ("Anonym" allowed)
- Email (optional) - for notifications only
- Graduation year (optional)
- IP address (technical, spam prevention)

### Privacy Measures
1. Email is optional and never displayed publicly
2. IP addresses stored temporarily (30 days), then anonymized
3. Users can request deletion (contact admin email)
4. No tracking cookies beyond essential functionality
5. Privacy policy required on website

### Data Retention
- Approved submissions: Permanent archival (purpose of site)
- Rejected submissions: 90 days, then deleted
- Pending submissions: 180 days, then auto-rejected

## DATA VALIDATION & SECURITY

### Input Sanitization
- HTML stripping (text-only content)
- XSS prevention (escape all user input)
- SQL injection prevention (parameterized queries)
- Email validation (RFC 5322 compliance)
- Rate limiting (max 3 submissions per IP per day)

### Spam Prevention
- Basic honeypot field (hidden from humans)
- Submission time tracking (reject if < 5 seconds)
- IP-based rate limiting
- Manual moderation as ultimate filter

## INCOMPLETE DATA WARNING ⚠️

**Current uncertainties affecting data model:**
1. **Categorization scheme** - Need decision on how to organize stories (chronological, thematic, etc.)
2. **Search functionality** - Not yet specified, might require full-text search fields
3. **Multilingual support** - German primary, but international alumni might submit in English
4. **Media attachments** - Currently text-only, but future photos would require File entity

**These gaps are acceptable for MVP but should be addressed before production.**

## NEXT PHASE
→ **EXPLORATION** - Create analysis scripts to validate data structures with test content
→ **REQUIREMENTS.md** - Define functional and non-functional requirements based on this data model

---
*This document serves as the immutable DATA savepoint for the Cognitive Science Memorial Website project.*
