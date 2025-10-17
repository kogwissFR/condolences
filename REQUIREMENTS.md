# Requirements - Cognitive Science Memorial Website
**Version:** 1.0.0 | **Date:** 17. Oktober 2025 | **Phase:** REQUIREMENTS

## FUNCTIONAL REQUIREMENTS (Core Features)

### FR-1: Public Story Display
**Priority:** CRITICAL | **Testable:** Yes

**Description:** Display approved memories and success stories on public-facing page.

**Acceptance Criteria:**
- [ ] 1.1: Display all approved submissions chronologically (newest first)
- [ ] 1.2: Show title, author name, content, publication date for each story
- [ ] 1.3: Optionally show graduation year if provided by author
- [ ] 1.4: Implement pagination (20 stories per page)
- [ ] 1.5: Responsive layout (mobile, tablet, desktop)
- [ ] 1.6: Stories are readable without horizontal scrolling
- [ ] 1.7: Page loads in < 3 seconds on standard connection

**Test Cases:**
- Load public page with 0 stories → Show "Noch keine Geschichten" message
- Load page with 25 stories → Show first 20, pagination controls visible
- Click "Nächste Seite" → Load stories 21-25
- View on mobile (375px width) → Content properly formatted

---

### FR-2: Submission Form
**Priority:** CRITICAL | **Testable:** Yes

**Description:** Allow anyone to submit memories/success stories without authentication.

**Acceptance Criteria:**
- [ ] 2.1: Form accessible from prominent "Geschichte einreichen" button
- [ ] 2.2: Required fields: Name, Title, Story content
- [ ] 2.3: Optional fields: Email, Graduation year
- [ ] 2.4: Client-side validation before submission
- [ ] 2.5: Character limits enforced (Title: 200, Content: 50-5000)
- [ ] 2.6: Submission creates record with status="pending"
- [ ] 2.7: Success confirmation shown after submission
- [ ] 2.8: Form resets after successful submission
- [ ] 2.9: Error messages clear and in German

**Validation Rules:**
- Name: 2-100 characters, trim whitespace
- Title: 5-200 characters, no HTML
- Content: 50-5000 characters, preserve line breaks
- Email: Valid RFC 5322 format if provided
- Graduation year: Integer 1990-2029 if provided

**Test Cases:**
- Submit with all required fields → Success
- Submit with title < 5 chars → Error "Titel zu kurz (mindestens 5 Zeichen)"
- Submit with content < 50 chars → Error "Geschichte zu kurz (mindestens 50 Zeichen)"
- Submit with invalid email → Error "Ungültige E-Mail-Adresse"
- Submit with XSS attempt (`<script>alert('xss')</script>`) → HTML stripped/escaped

---

### FR-3: Admin Moderation Panel
**Priority:** CRITICAL | **Testable:** Yes

**Description:** Admin interface to review, approve, or reject pending submissions.

**Acceptance Criteria:**
- [ ] 3.1: Admin login page with username/password authentication
- [ ] 3.2: List all pending submissions in moderation queue
- [ ] 3.3: Display full submission details (name, title, content, date, email, grad year)
- [ ] 3.4: "Approve" button → Sets status="approved", publication_date=now
- [ ] 3.5: "Reject" button → Sets status="rejected", optional rejection note
- [ ] 3.6: View count of pending submissions
- [ ] 3.7: Logout functionality
- [ ] 3.8: Session timeout after 60 minutes inactivity

**Security Requirements:**
- Passwords hashed with bcrypt (cost factor ≥12)
- Session tokens secure, httpOnly, sameSite
- CSRF protection on all admin actions
- Admin panel not indexed by search engines (robots.txt, meta noindex)

**Test Cases:**
- Login with valid credentials → Access moderation panel
- Login with invalid credentials → Error "Ungültige Anmeldedaten"
- Approve submission → Appears on public page immediately
- Reject submission → Removed from pending queue, not visible publicly
- Access /admin without login → Redirect to login page

---

### FR-4: Visual Style Matching
**Priority:** HIGH | **Testable:** Yes (visual QA)

**Description:** Adopt design and branding from official Kogni homepage (https://uni-freiburg.de/cognition/).

**Acceptance Criteria:**
- [ ] 4.1: Use University of Freiburg logo/Siegelement (cloverleaf)
- [ ] 4.2: Match color scheme from official site
- [ ] 4.3: Use similar typography (fonts, sizes, weights)
- [ ] 4.4: Implement consistent navigation structure
- [ ] 4.5: Footer with same links (Impressum, Datenschutz, Kontakt, etc.)
- [ ] 4.6: Responsive breakpoints match university standard
- [ ] 4.7: German language throughout (date formats: DD.MM.YYYY)

**Design Elements to Adopt:**
- University Freiburg branding guidelines
- Clean, academic aesthetic
- Accessibility (WCAG 2.1 AA compliance)
- Professional, respectful tone for memorial context

**Test Cases:**
- Side-by-side visual comparison with official homepage
- Color picker verification of primary/secondary colors
- Font inspector verification
- Logo resolution and placement check

---

### FR-5: Content Privacy & GDPR Compliance
**Priority:** CRITICAL | **Testable:** Yes (legal review)

**Description:** Ensure data handling complies with German/EU privacy laws.

**Acceptance Criteria:**
- [ ] 5.1: Privacy policy page accessible from footer
- [ ] 5.2: Email addresses never displayed publicly
- [ ] 5.3: IP addresses stored for max 30 days, then anonymized
- [ ] 5.4: Contact email for data deletion requests
- [ ] 5.5: No third-party tracking (Google Analytics, etc.) without consent
- [ ] 5.6: Optional cookie banner if cookies used beyond essential
- [ ] 5.7: Data retention policy documented (approved: permanent, rejected: 90 days)

**Privacy Policy Must Include:**
- What data is collected (name, optional email/grad year, IP)
- Why data is collected (memorial/archive purpose)
- How long data is retained
- User rights (access, deletion, correction)
- Contact information for privacy inquiries

**Test Cases:**
- Submit story → Email not visible on public page
- Request data deletion → Admin can remove submission
- Check cookies → Only essential session cookies present

---

## NON-FUNCTIONAL REQUIREMENTS

### NFR-1: Performance
**Priority:** HIGH | **Testable:** Yes

- [ ] Page load time < 3 seconds (3G connection)
- [ ] Time to interactive < 5 seconds
- [ ] Lighthouse performance score ≥ 85
- [ ] Static site generation for optimal speed (GitHub Pages)

**Test Method:** Lighthouse, WebPageTest, real-device testing

---

### NFR-2: Accessibility
**Priority:** HIGH | **Testable:** Yes

- [ ] WCAG 2.1 Level AA compliance
- [ ] Keyboard navigation fully functional
- [ ] Screen reader compatible (ARIA labels where needed)
- [ ] Color contrast ratio ≥ 4.5:1 for body text
- [ ] Semantic HTML structure
- [ ] Alt text for all images

**Test Method:** WAVE, axe DevTools, NVDA/JAWS screen reader testing

---

### NFR-3: Browser Compatibility
**Priority:** MEDIUM | **Testable:** Yes

- [ ] Chrome/Edge (last 2 versions)
- [ ] Firefox (last 2 versions)
- [ ] Safari (last 2 versions, iOS 14+)
- [ ] Graceful degradation for older browsers

**Test Method:** BrowserStack or manual testing

---

### NFR-4: Scalability
**Priority:** MEDIUM | **Testable:** Yes

- [ ] Support 500+ approved stories without performance degradation
- [ ] Database queries optimized (indexed fields)
- [ ] Pagination prevents loading entire dataset
- [ ] Static site generation handles expected volume

**Test Method:** Load testing with synthetic data (500-1000 stories)

---

### NFR-5: Maintainability
**Priority:** HIGH | **Testable:** Partially (code review)

- [ ] Clean, documented code (comments for complex logic)
- [ ] Separation of concerns (data layer, presentation layer)
- [ ] README with setup/deployment instructions
- [ ] Minimal dependencies (security/maintenance burden)
- [ ] GitHub Pages deployment workflow documented

**Test Method:** Code review, documentation review

---

### NFR-6: Security
**Priority:** CRITICAL | **Testable:** Yes

- [ ] Input sanitization (XSS prevention)
- [ ] Parameterized queries (SQL injection prevention)
- [ ] Rate limiting (3 submissions per IP per day)
- [ ] Honeypot spam prevention
- [ ] HTTPS enforced (GitHub Pages provides this)
- [ ] Admin panel password security (bcrypt hashing)
- [ ] CSRF tokens on admin actions

**Test Method:** OWASP ZAP scan, manual penetration testing

---

### NFR-7: Long-term Archival
**Priority:** HIGH | **Testable:** No (time-dependent)

- [ ] Static site generation ensures content preserved even without active backend
- [ ] Export functionality (JSON/CSV) for full data backup
- [ ] Documentation for converting to pure static archive after 2029
- [ ] Markdown export option for universal readability

**Consideration:** After 2029 when program ends, site should transition to read-only archive with minimal maintenance requirements.

---

## OPTIONAL FEATURES (Future Enhancements)

### OF-1: Search Functionality
**Priority:** LOW | **Testable:** Yes

- Full-text search across story titles and content
- Filter by graduation year range
- Filter by story type (memory vs. success)

**Defer to:** Post-MVP if user feedback indicates need

---

### OF-2: Story Tagging
**Priority:** LOW | **Testable:** Yes

- Admin adds tags during moderation (e.g., "Forschung", "Ausland", "Promotion")
- Public filtering by tags
- Tag cloud visualization

**Defer to:** Post-MVP

---

### OF-3: Statistics Dashboard
**Priority:** LOW | **Testable:** Yes

- Total submissions (pending, approved, rejected)
- Submissions over time graph
- Graduation year distribution
- Popular story types

**Defer to:** Post-MVP, admin convenience feature

---

### OF-4: Email Notifications
**Priority:** LOW | **Testable:** Yes

- Optional: Email submitter when story is approved
- Requires email infrastructure setup

**Defer to:** Post-MVP, only if university provides email service

---

## TECHNOLOGY CONSTRAINTS

### TC-1: GitHub Pages Hosting
**Implications:**
- Static site generation required (no server-side processing at runtime)
- Backend logic must run during build/deploy time
- Consider JAMstack approach: Static frontend + API for form submissions
- Options: 
  - **Option A:** Pure static with admin builds locally, commits approved stories
  - **Option B:** Static frontend + serverless backend (Netlify Functions, Vercel, etc.) for form/admin
  - **Recommended:** Hybrid - GitHub Pages for frontend, separate admin panel on university server

### TC-2: Database Selection
**Given GitHub Pages constraint:**
- **Option A:** JSON files in repo (simple, version-controlled, but requires rebuild for changes)
- **Option B:** External database (Firebase, Supabase) + API layer
- **Option C:** University-hosted database + admin panel, GitHub Pages serves static export
- **Recommended:** Option C for MVP (university DB + periodic static export)

### TC-3: Form Submission Handling
**Challenge:** GitHub Pages can't process POST requests
**Solution:** 
- Form submission points to external endpoint (university server, serverless function)
- OR use form service (Formspree, Netlify Forms) with webhook to database
- **Recommended:** Netlify Forms (free tier, GDPR-compliant) OR simple university CGI script

---

## CONSISTENCY CHECKS ✓

### Requirements vs. Context (README.md)
- ✅ Manual moderation → FR-3 defined
- ✅ Open submissions → FR-2 no authentication required
- ✅ Text-only → No file upload requirements
- ✅ Semi-official → FR-4 style matching required
- ✅ Program ends 2029 → NFR-7 archival considerations

### Requirements vs. Data (DATA.md)
- ✅ Submission entity maps to FR-2 form fields
- ✅ Admin user entity supports FR-3 authentication
- ✅ Status enum (pending/approved/rejected) aligns with workflow
- ✅ GDPR considerations in DATA.md match FR-5
- ✅ Validation rules consistent between DATA.md and FR-2

### Testability
- ✅ All critical functional requirements have concrete test cases
- ✅ Non-functional requirements specify measurement methods
- ✅ Acceptance criteria are binary (pass/fail)

### Completeness
- ✅ All core user stories covered (submit, view, moderate)
- ✅ Security requirements addressed
- ✅ Privacy/GDPR requirements specified
- ✅ Performance and accessibility defined
- ⚠️ **GitHub Pages hosting requires architectural decisions** (see TC-1, TC-2, TC-3)

---

## OPEN TECHNICAL DECISIONS ⚠️

**TD-1: Static Site Generation Approach**
Given GitHub Pages constraint, we need to decide:
- Pure static (admin commits changes) vs. Hybrid (external API + static frontend)
- Build tool (Next.js, Gatsby, Hugo, Jekyll, 11ty, or plain HTML/JS)
- **Recommendation needed before INSTRUCTIONS.md**

**TD-2: Admin Panel Location**
- Host admin on GitHub Pages (security concern for public site)
- Separate university-hosted admin subdomain
- Local-only admin tool (admin builds + deploys)
- **Recommendation needed before INSTRUCTIONS.md**

**TD-3: Form Backend Service**
- Netlify Forms (easy, GDPR-compliant, free tier)
- University CGI script (more control, requires IT dept)
- Serverless function (Vercel, Netlify Functions)
- **Recommendation needed before INSTRUCTIONS.md**

---

## NEXT PHASE

**Before proceeding to INSTRUCTIONS.md, we must resolve TD-1, TD-2, TD-3.**

**Recommended approach for decision:**
1. Assess university IT support availability (can they host admin panel?)
2. Choose static site generator based on team skills (React → Next.js, Simple → Hugo/Jekyll)
3. Select form backend that minimizes maintenance burden

**Alternative:** I can generate multiple INSTRUCTIONS.md variants for different architectural approaches, then you choose.

---
*This document serves as the immutable REQUIREMENTS savepoint for the Cognitive Science Memorial Website project.*
