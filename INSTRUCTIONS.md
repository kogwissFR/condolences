# Implementation Instructions - Cognitive Science Memorial Website
**Version:** 1.0.0 | **Date:** 17. Oktober 2025 | **Phase:** INSTRUCTIONS

## ARCHITECTURE OVERVIEW

```
GitHub Pages (Jekyll) ←→ Google Form → Google Sheets → GitHub Actions → Rebuild
     │                         │              │                │
     │                         │              │                └─ Automated daily sync
     │                         │              └─ Collaborative moderation
     │                         └─ Submission collection
     └─ Public story display
```

**Technology Stack:**
- **Frontend:** Jekyll (static site generator)
- **Hosting:** GitHub Pages
- **Submission Form:** Google Forms (external redirect)
- **Database:** Google Sheets
- **Automation:** GitHub Actions
- **Styling:** Custom CSS matching Uni Freiburg branding

---

## PHASE 1: REPOSITORY SETUP

### Step 1.1: Initialize GitHub Repository

```bash
# Create new repository on GitHub
# Name: kogni-memorial (or your preferred name)
# Public repository (for GitHub Pages)

# Clone locally
cd ~/Documents/Projekte/Condolences
git init
git remote add origin https://github.com/YOUR_USERNAME/kogni-memorial.git
```

### Step 1.2: Create Jekyll Project Structure

```bash
# Create directory structure
mkdir -p _layouts _includes _data assets/css assets/js assets/images
touch _config.yml index.html submit.html about.html
```

### Step 1.3: Create _config.yml

```yaml
# _config.yml
title: "Kognitionswissenschaft Freiburg - Erinnerungen"
description: "Erinnerungen und Erfolgsgeschichten ehemaliger Studierender"
baseurl: "" # Leave empty if using custom domain, or "/repo-name" for GitHub Pages
url: "https://YOUR_USERNAME.github.io" # Your GitHub Pages URL

# Build settings
markdown: kramdown
theme: minima # Can be removed after custom styling

# Collections (optional for future expansion)
collections:
  stories:
    output: false

# Exclude from build
exclude:
  - README.md
  - DATA.md
  - REQUIREMENTS.md
  - INSTRUCTIONS.md
  - knowledge/
  - .DS_Store

# Defaults
defaults:
  - scope:
      path: ""
    values:
      layout: "default"
```

---

## PHASE 2: JEKYLL SITE IMPLEMENTATION

### Step 2.1: Create Base Layout

**File: `_layouts/default.html`**

```html
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{ page.title }} | {{ site.title }}</title>
  <meta name="description" content="{{ site.description }}">
  <link rel="stylesheet" href="{{ '/assets/css/main.css' | relative_url }}">
</head>
<body>
  {% include header.html %}
  
  <main class="container">
    {{ content }}
  </main>
  
  {% include footer.html %}
</body>
</html>
```

### Step 2.2: Create Header Component

**File: `_includes/header.html`**

```html
<header class="site-header">
  <div class="header-container">
    <div class="logo">
      <!-- University Freiburg Siegelement (cloverleaf) -->
      <!-- TODO: Download official logo from uni-freiburg.de and place in assets/images/ -->
      <img src="{{ '/assets/images/uni-freiburg-logo.svg' | relative_url }}" 
           alt="Universität Freiburg Logo" 
           class="uni-logo">
      <div class="site-title">
        <h1>Kognitionswissenschaft</h1>
        <p class="subtitle">Erinnerungen & Erfolgsgeschichten</p>
      </div>
    </div>
    
    <nav class="main-nav">
      <ul>
        <li><a href="{{ '/' | relative_url }}" {% if page.url == '/' %}class="active"{% endif %}>Startseite</a></li>
        <li><a href="{{ '/submit.html' | relative_url }}" {% if page.url == '/submit.html' %}class="active"{% endif %}>Geschichte einreichen</a></li>
        <li><a href="{{ '/about.html' | relative_url }}" {% if page.url == '/about.html' %}class="active"{% endif %}>Über dieses Projekt</a></li>
      </ul>
    </nav>
  </div>
</header>
```

### Step 2.3: Create Footer Component

**File: `_includes/footer.html`**

```html
<footer class="site-footer">
  <div class="footer-container">
    <div class="footer-section">
      <h3>Kontakt</h3>
      <p>Abteilung Kognitionswissenschaft<br>
         Hebelstraße 10, 79104 Freiburg</p>
    </div>
    
    <div class="footer-section">
      <h3>Links</h3>
      <ul>
        <li><a href="https://uni-freiburg.de/cognition/" target="_blank" rel="noopener">Offizielle Homepage</a></li>
        <li><a href="https://uni-freiburg.de/" target="_blank" rel="noopener">Universität Freiburg</a></li>
      </ul>
    </div>
    
    <div class="footer-section">
      <h3>Rechtliches</h3>
      <ul>
        <li><a href="{{ '/privacy.html' | relative_url }}">Datenschutz</a></li>
        <li><a href="https://uni-freiburg.de/cognition/Impressum" target="_blank">Impressum</a></li>
        <li><a href="https://uni-freiburg.de/barrierefreiheit/" target="_blank">Barrierefreiheit</a></li>
      </ul>
    </div>
  </div>
  
  <div class="footer-bottom">
    <p>&copy; {{ 'now' | date: "%Y" }} Universität Freiburg | Kognitionswissenschaft endet 2029</p>
  </div>
</footer>
```

### Step 2.4: Create Homepage

**File: `index.html`**

```html
---
layout: default
title: Startseite
---

<section class="hero">
  <h1>Erinnerungen an die Kognitionswissenschaft</h1>
  <p class="lead">
    Der Studiengang Kognitionswissenschaft wird in den kommenden Jahren abgewickelt 
    und endet 2029. Auf dieser Seite sammeln wir Erinnerungen und Erfolgsgeschichten 
    ehemaliger Studierender.
  </p>
  <a href="{{ '/submit.html' | relative_url }}" class="btn btn-primary">
    Ihre Geschichte einreichen
  </a>
</section>

<section class="stories">
  <h2>Geschichten unserer Alumni</h2>
  
  {% if site.data.stories %}
    {% assign sorted_stories = site.data.stories | sort: 'publication_date' | reverse %}
    
    <div class="stories-grid">
      {% for story in sorted_stories limit:20 %}
      <article class="story-card">
        <h3>{{ story.title }}</h3>
        <div class="story-meta">
          <span class="author">{{ story.author_name }}</span>
          {% if story.graduation_year %}
          <span class="year">Abschluss {{ story.graduation_year }}</span>
          {% endif %}
          <span class="date">{{ story.publication_date | date: "%d.%m.%Y" }}</span>
        </div>
        <div class="story-content">
          {{ story.content | newline_to_br }}
        </div>
        <span class="story-type">{{ story.story_type }}</span>
      </article>
      {% endfor %}
    </div>
    
    {% if site.data.stories.size > 20 %}
    <div class="pagination-info">
      <p>Zeige {{ sorted_stories | size | at_most: 20 }} von {{ site.data.stories.size }} Geschichten</p>
      <!-- TODO: Implement pagination if needed -->
    </div>
    {% endif %}
    
  {% else %}
    <div class="no-stories">
      <p>Noch keine Geschichten eingereicht. Seien Sie der Erste!</p>
      <a href="{{ '/submit.html' | relative_url }}" class="btn btn-secondary">
        Erste Geschichte einreichen
      </a>
    </div>
  {% endif %}
</section>
```

### Step 2.5: Create Submission Page

**File: `submit.html`**

```html
---
layout: default
title: Geschichte einreichen
---

<section class="submit-page">
  <h1>Ihre Geschichte einreichen</h1>
  
  <div class="intro">
    <p>
      Vielen Dank für Ihr Interesse, Ihre Erinnerungen oder Erfolgsgeschichten zu teilen!
    </p>
    <p>
      Bitte füllen Sie das folgende Formular aus. Ihre Einreichung wird von unserem Team 
      geprüft und in Kürze auf dieser Seite veröffentlicht.
    </p>
  </div>
  
  <div class="form-info">
    <h2>Was können Sie einreichen?</h2>
    <ul>
      <li><strong>Erinnerungen:</strong> Besondere Momente, prägende Erlebnisse, lustige Anekdoten aus dem Studium</li>
      <li><strong>Erfolgsgeschichten:</strong> Wie hat das Kogni-Studium Ihre Karriere beeinflusst? Wo sind Sie heute?</li>
    </ul>
    
    <h3>Hinweise:</h3>
    <ul>
      <li>Mindestlänge: 50 Zeichen (ca. 1-2 Sätze)</li>
      <li>Maximallänge: 5000 Zeichen (ca. 1-2 Seiten)</li>
      <li>Name und E-Mail sind optional, aber hilfreich für Rückfragen</li>
      <li>Ihr Beitrag wird manuell geprüft, bevor er veröffentlicht wird</li>
    </ul>
  </div>
  
  <div class="cta-box">
    <a href="https://forms.google.com/YOUR_FORM_ID" 
       target="_blank" 
       rel="noopener noreferrer"
       class="btn btn-primary btn-large">
      Zum Einreichungsformular →
    </a>
    <p class="form-note">
      Das Formular öffnet sich in einem neuen Tab. 
      Nach dem Absenden können Sie zu dieser Seite zurückkehren.
    </p>
  </div>
  
  <div class="privacy-note">
    <h3>Datenschutz</h3>
    <p>
      Ihre Daten werden gemäß der <a href="{{ '/privacy.html' | relative_url }}">Datenschutzerklärung</a> 
      verarbeitet. Ihre E-Mail-Adresse wird niemals öffentlich angezeigt.
    </p>
  </div>
</section>
```

### Step 2.6: Create About Page

**File: `about.html`**

```html
---
layout: default
title: Über dieses Projekt
---

<section class="about-page">
  <h1>Über dieses Projekt</h1>
  
  <div class="content">
    <h2>Warum diese Seite?</h2>
    <p>
      Der Studiengang Kognitionswissenschaft an der Universität Freiburg wird in den 
      kommenden Jahren abgewickelt und endet im Jahr 2029. Diese Seite dient als digitales 
      Denkmal und Archiv für die Erinnerungen, Erfolge und Geschichten aller, die diesen 
      besonderen Studiengang durchlaufen haben.
    </p>
    
    <h2>Was ist Kognitionswissenschaft?</h2>
    <p>
      Kognitionswissenschaft (KW) hat zum Ziel, die geistigen Leistungen des Menschen, 
      die ihnen zugrundeliegenden Vorgänge und Voraussetzungen zu untersuchen. Das Studium 
      kombiniert Ansätze aus Psychologie, Informatik, Linguistik, Philosophie und 
      Neurowissenschaften.
    </p>
    
    <h2>Mitmachen</h2>
    <p>
      Haben Sie Kognitionswissenschaft in Freiburg studiert? Teilen Sie Ihre Erinnerungen 
      und Erfolgsgeschichten! Jeder Beitrag hilft dabei, die Geschichte dieses einzigartigen 
      Studiengangs zu bewahren.
    </p>
    <a href="{{ '/submit.html' | relative_url }}" class="btn btn-primary">
      Geschichte einreichen
    </a>
    
    <h2>Kontakt</h2>
    <p>
      Bei Fragen oder Anregungen wenden Sie sich bitte an:<br>
      <a href="mailto:kogni@psychologie.uni-freiburg.de">kogni@psychologie.uni-freiburg.de</a>
    </p>
    
    <h2>Timeline</h2>
    <ul class="timeline">
      <li><strong>2025-2028:</strong> Aktive Sammlung von Geschichten</li>
      <li><strong>2029:</strong> Letzter Abschlussjahrgang</li>
      <li><strong>2029+:</strong> Archivierung und langfristige Bewahrung</li>
    </ul>
  </div>
</section>
```

### Step 2.7: Create Styling

**File: `assets/css/main.css`**

```css
/* Base styles matching Uni Freiburg aesthetic */
:root {
  /* TODO: Extract exact colors from uni-freiburg.de/cognition/ */
  --primary-color: #004a99; /* Uni Freiburg Blue (approximate) */
  --secondary-color: #6c757d;
  --text-color: #333;
  --bg-color: #fff;
  --border-color: #ddd;
  --success-color: #28a745;
  --link-color: #004a99;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  font-size: 16px;
  line-height: 1.6;
  color: var(--text-color);
  background-color: var(--bg-color);
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

/* Header */
.site-header {
  background-color: var(--bg-color);
  border-bottom: 2px solid var(--primary-color);
  padding: 20px 0;
}

.header-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
}

.logo {
  display: flex;
  align-items: center;
  gap: 15px;
}

.uni-logo {
  height: 60px;
  width: auto;
}

.site-title h1 {
  font-size: 1.5rem;
  color: var(--primary-color);
  margin-bottom: 0;
}

.site-title .subtitle {
  font-size: 0.9rem;
  color: var(--secondary-color);
}

.main-nav ul {
  list-style: none;
  display: flex;
  gap: 20px;
}

.main-nav a {
  text-decoration: none;
  color: var(--text-color);
  padding: 5px 10px;
  border-radius: 4px;
  transition: background-color 0.2s;
}

.main-nav a:hover,
.main-nav a.active {
  background-color: var(--primary-color);
  color: white;
}

/* Hero Section */
.hero {
  text-align: center;
  padding: 60px 20px;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
  margin-bottom: 40px;
}

.hero h1 {
  font-size: 2.5rem;
  color: var(--primary-color);
  margin-bottom: 20px;
}

.hero .lead {
  font-size: 1.2rem;
  max-width: 800px;
  margin: 0 auto 30px;
  line-height: 1.8;
}

/* Buttons */
.btn {
  display: inline-block;
  padding: 12px 30px;
  text-decoration: none;
  border-radius: 5px;
  font-weight: 600;
  transition: all 0.3s;
  cursor: pointer;
  border: none;
  font-size: 1rem;
}

.btn-primary {
  background-color: var(--primary-color);
  color: white;
}

.btn-primary:hover {
  background-color: #003d7a;
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0,0,0,0.2);
}

.btn-secondary {
  background-color: var(--secondary-color);
  color: white;
}

.btn-large {
  font-size: 1.2rem;
  padding: 16px 40px;
}

/* Stories Section */
.stories {
  padding: 40px 20px;
}

.stories h2 {
  text-align: center;
  font-size: 2rem;
  color: var(--primary-color);
  margin-bottom: 40px;
}

.stories-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 30px;
  margin-bottom: 40px;
}

.story-card {
  background: white;
  border: 1px solid var(--border-color);
  border-radius: 8px;
  padding: 25px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  transition: box-shadow 0.3s;
}

.story-card:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

.story-card h3 {
  color: var(--primary-color);
  margin-bottom: 15px;
  font-size: 1.3rem;
}

.story-meta {
  display: flex;
  gap: 15px;
  flex-wrap: wrap;
  font-size: 0.9rem;
  color: var(--secondary-color);
  margin-bottom: 15px;
  padding-bottom: 15px;
  border-bottom: 1px solid var(--border-color);
}

.story-meta span {
  display: inline-block;
}

.story-content {
  margin-bottom: 15px;
  line-height: 1.7;
  white-space: pre-line;
}

.story-type {
  display: inline-block;
  font-size: 0.85rem;
  padding: 4px 12px;
  background-color: #f0f0f0;
  border-radius: 12px;
  color: var(--secondary-color);
}

.no-stories {
  text-align: center;
  padding: 60px 20px;
}

.no-stories p {
  font-size: 1.2rem;
  margin-bottom: 20px;
  color: var(--secondary-color);
}

/* Submit Page */
.submit-page {
  padding: 40px 20px;
  max-width: 800px;
  margin: 0 auto;
}

.submit-page h1 {
  color: var(--primary-color);
  margin-bottom: 30px;
}

.intro {
  background-color: #f8f9fa;
  padding: 20px;
  border-radius: 8px;
  margin-bottom: 30px;
}

.form-info {
  margin-bottom: 40px;
}

.form-info h2,
.form-info h3 {
  color: var(--primary-color);
  margin-top: 20px;
  margin-bottom: 15px;
}

.form-info ul {
  margin-left: 20px;
  line-height: 1.8;
}

.cta-box {
  text-align: center;
  padding: 40px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 12px;
  margin-bottom: 30px;
}

.cta-box .btn {
  font-size: 1.3rem;
  padding: 18px 50px;
}

.form-note {
  color: white;
  margin-top: 15px;
  font-size: 0.9rem;
}

.privacy-note {
  background-color: #f8f9fa;
  padding: 20px;
  border-left: 4px solid var(--primary-color);
  border-radius: 4px;
}

/* About Page */
.about-page {
  padding: 40px 20px;
  max-width: 900px;
  margin: 0 auto;
}

.about-page h1 {
  color: var(--primary-color);
  margin-bottom: 30px;
}

.about-page h2 {
  color: var(--primary-color);
  margin-top: 30px;
  margin-bottom: 15px;
}

.about-page .content {
  line-height: 1.8;
}

.timeline {
  list-style: none;
  margin-left: 0;
  padding-left: 20px;
  border-left: 3px solid var(--primary-color);
}

.timeline li {
  padding: 10px 0 10px 20px;
  position: relative;
}

.timeline li::before {
  content: '';
  position: absolute;
  left: -8px;
  top: 18px;
  width: 12px;
  height: 12px;
  background-color: var(--primary-color);
  border-radius: 50%;
}

/* Footer */
.site-footer {
  background-color: #f8f9fa;
  border-top: 2px solid var(--primary-color);
  margin-top: 60px;
  padding: 40px 20px 20px;
}

.footer-container {
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 30px;
  margin-bottom: 30px;
}

.footer-section h3 {
  color: var(--primary-color);
  margin-bottom: 15px;
  font-size: 1.1rem;
}

.footer-section ul {
  list-style: none;
}

.footer-section ul li {
  margin-bottom: 8px;
}

.footer-section a {
  color: var(--text-color);
  text-decoration: none;
}

.footer-section a:hover {
  color: var(--primary-color);
  text-decoration: underline;
}

.footer-bottom {
  text-align: center;
  padding-top: 20px;
  border-top: 1px solid var(--border-color);
  color: var(--secondary-color);
  font-size: 0.9rem;
}

/* Responsive */
@media (max-width: 768px) {
  .header-container {
    flex-direction: column;
    gap: 20px;
  }
  
  .main-nav ul {
    flex-direction: column;
    gap: 10px;
    text-align: center;
  }
  
  .hero h1 {
    font-size: 1.8rem;
  }
  
  .stories-grid {
    grid-template-columns: 1fr;
  }
  
  .footer-container {
    grid-template-columns: 1fr;
  }
}
```

---

## PHASE 3: GOOGLE FORMS SETUP

### Step 3.1: Create Google Form

1. Go to https://forms.google.com
2. Click "+" to create new form
3. **Form Title:** "Kognitionswissenschaft Freiburg - Erinnerungen einreichen"
4. **Form Description:**
   ```
   Teilen Sie Ihre Erinnerungen und Erfolgsgeschichten aus dem Kogni-Studium. 
   Ihre Einreichung wird geprüft und auf der Memorial-Website veröffentlicht.
   ```

### Step 3.2: Add Form Fields

**Field 1: Name (Short answer)**
- Question: "Ihr Name (oder Pseudonym)"
- Help text: "Wie soll Ihr Name angezeigt werden? Sie können auch 'Anonym' eingeben."
- Required: Yes

**Field 2: E-Mail (Short answer)**
- Question: "E-Mail-Adresse (optional)"
- Help text: "Für Rückfragen. Wird nicht öffentlich angezeigt."
- Validation: Text → Email
- Required: No

**Field 3: Graduation Year (Short answer)**
- Question: "Abschlussjahr (optional)"
- Help text: "In welchem Jahr haben Sie Ihr Kogni-Studium abgeschlossen?"
- Validation: Number → Between 1990 and 2029
- Required: No

**Field 4: Title (Short answer)**
- Question: "Titel Ihrer Geschichte"
- Help text: "Eine kurze Überschrift (5-200 Zeichen)"
- Required: Yes
- Validation: Length → Minimum 5 characters

**Field 5: Story Content (Paragraph)**
- Question: "Ihre Geschichte"
- Help text: "Teilen Sie Ihre Erinnerung oder Erfolgsgeschichte (50-5000 Zeichen)"
- Required: Yes
- Validation: Length → Minimum 50 characters

**Field 6: Story Type (Multiple choice)**
- Question: "Art der Einreichung"
- Options:
  - Erinnerung (Anekdote, besonderer Moment)
  - Erfolgsgeschichte (Karriere, Werdegang)
  - Beides
- Required: No

### Step 3.3: Configure Form Settings

1. Click Settings (gear icon)
2. **General:**
   - Uncheck "Limit to 1 response"
   - Check "Collect email addresses" → No (we have optional field)
3. **Presentation:**
   - Confirmation message:
     ```
     Vielen Dank für Ihre Einreichung!
     
     Ihre Geschichte wird von unserem Team geprüft und in Kürze 
     auf der Website veröffentlicht.
     
     Zurück zur Website: [LINK TO YOUR GITHUB PAGES SITE]
     ```
   - Check "Show link to submit another response"
4. **Quizzes:** Leave disabled

### Step 3.4: Link Form to Google Sheets

1. In form editor, click "Responses" tab
2. Click Google Sheets icon (green)
3. Create new spreadsheet: "Kogni Memorial Submissions"
4. Sheet will auto-populate with responses

---

## PHASE 4: GOOGLE SHEETS MODERATION SETUP

### Step 4.1: Configure Spreadsheet

1. Open the linked Google Sheets
2. **Column Headers** (auto-created by form):
   - A: Timestamp
   - B: Ihr Name (oder Pseudonym)
   - C: E-Mail-Adresse (optional)
   - D: Abschlussjahr (optional)
   - E: Titel Ihrer Geschichte
   - F: Ihre Geschichte
   - G: Art der Einreichung

3. **Add Manual Columns:**
   - H: Status (for moderation)
   - I: Moderation Notes
   - J: Moderated By
   - K: Moderation Date

### Step 4.2: Add Data Validation for Status Column

1. Select column H (Status), starting from H2
2. Data → Data validation
3. Criteria: List of items
4. Items: `Pending, Approve, Reject`
5. Show dropdown in cell: Yes
6. On invalid data: Reject input
7. Save

### Step 4.3: Set Default Status Formula

1. In cell H2, enter formula:
   ```
   =IF(A2<>"", IF(H2="", "Pending", H2), "")
   ```
2. Copy formula down column H
3. This auto-sets "Pending" for new submissions

### Step 4.4: Add Conditional Formatting

1. Select data range (A2:K1000)
2. Format → Conditional formatting
3. **Rule 1 (Approved):**
   - Format cells if: Custom formula is `=$H2="Approve"`
   - Formatting: Light green background
4. **Rule 2 (Rejected):**
   - Format cells if: Custom formula is `=$H2="Reject"`
   - Formatting: Light red background
5. **Rule 3 (Pending):**
   - Format cells if: Custom formula is `=$H2="Pending"`
   - Formatting: Light yellow background

### Step 4.5: Share with Department

1. Click "Share" button
2. Add department members' emails
3. Permission: Editor (can modify)
4. Send invitation

### Step 4.6: Set Up Email Notifications

1. Tools → Notification rules
2. "Notify me when: A user submits a form"
3. "Notify me with: Email - daily digest" (or immediate for faster response)
4. Save

---

## PHASE 5: DATA EXPORT STRUCTURE

### Step 5.1: Create stories.yml Template

**File: `_data/stories.yml`**

```yaml
# This file is auto-generated by GitHub Actions
# Do not edit manually - changes will be overwritten

- id: "001"
  author_name: "Maria Schmidt"
  graduation_year: 2018
  title: "Von der Kogni zur KI-Forschung"
  content: |
    Mein Studium der Kognitionswissenschaft hat mir die Türen zur KI-Forschung geöffnet. 
    Die interdisziplinäre Ausbildung war perfekt für meine spätere Karriere...
  story_type: "Erfolgsgeschichte"
  publication_date: "2025-10-16"
  submission_date: "2025-10-15"

# More stories will be added here automatically
```

---

## PHASE 6: GITHUB ACTIONS AUTOMATION

### Step 6.1: Create Google Service Account

1. Go to https://console.cloud.google.com/
2. Create new project: "Kogni Memorial Automation"
3. Enable Google Sheets API
4. Create Service Account:
   - Name: "github-actions-sheets"
   - Role: "Editor"
5. Create JSON key, download it
6. **IMPORTANT:** Add service account email to Google Sheets (Share with Editor access)

### Step 6.2: Add Secrets to GitHub

1. Go to GitHub repository → Settings → Secrets and variables → Actions
2. Click "New repository secret"
3. Name: `GOOGLE_SHEETS_CREDENTIALS`
4. Value: Paste entire JSON content from service account key
5. Add another secret:
   - Name: `GOOGLE_SHEET_ID`
   - Value: The Sheet ID from URL (https://docs.google.com/spreadsheets/d/SHEET_ID/edit)

### Step 6.3: Create GitHub Actions Workflow

**File: `.github/workflows/sync-stories.yml`**

```yaml
name: Sync Stories from Google Sheets

on:
  schedule:
    # Run daily at 9 AM UTC (10 AM CET, 11 AM CEST)
    - cron: '0 9 * * *'
  workflow_dispatch: # Allow manual trigger

jobs:
  sync:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      
      - name: Install dependencies
        run: |
          pip install gspread oauth2client PyYAML
      
      - name: Sync stories from Google Sheets
        env:
          GOOGLE_CREDENTIALS: ${{ secrets.GOOGLE_SHEETS_CREDENTIALS }}
          SHEET_ID: ${{ secrets.GOOGLE_SHEET_ID }}
        run: python scripts/sync_stories.py
      
      - name: Commit and push if changed
        run: |
          git config --global user.name 'GitHub Actions Bot'
          git config --global user.email 'actions@github.com'
          git add _data/stories.yml
          git diff --quiet && git diff --staged --quiet || (git commit -m "Auto-sync: Update stories from Google Sheets [$(date +'%Y-%m-%d %H:%M')]" && git push)
```

### Step 6.4: Create Sync Script

**File: `scripts/sync_stories.py`**

```python
#!/usr/bin/env python3
"""
Sync approved stories from Google Sheets to Jekyll data file.
Runs via GitHub Actions on schedule.
"""

import os
import json
import yaml
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def main():
    # Load credentials from environment
    creds_json = os.environ.get('GOOGLE_CREDENTIALS')
    sheet_id = os.environ.get('SHEET_ID')
    
    if not creds_json or not sheet_id:
        print("ERROR: Missing required environment variables")
        return
    
    # Authenticate with Google Sheets
    creds_dict = json.loads(creds_json)
    scope = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(creds)
    
    # Open spreadsheet
    sheet = client.open_by_key(sheet_id).sheet1
    
    # Get all records
    records = sheet.get_all_records()
    
    # Filter approved stories
    approved_stories = []
    story_id = 1
    
    for record in records:
        status = record.get('Status', '').strip()
        
        if status == 'Approve':
            # Extract and clean data
            story = {
                'id': f"{story_id:03d}",
                'author_name': record.get('Ihr Name (oder Pseudonym)', 'Anonym').strip(),
                'title': record.get('Titel Ihrer Geschichte', '').strip(),
                'content': record.get('Ihre Geschichte', '').strip(),
                'story_type': record.get('Art der Einreichung', '').strip() or 'Nicht angegeben',
                'submission_date': parse_date(record.get('Timestamp', '')),
                'publication_date': parse_date(record.get('Moderation Date', '')) or datetime.now().strftime('%Y-%m-%d'),
            }
            
            # Add optional fields
            grad_year = record.get('Abschlussjahr (optional)', '')
            if grad_year and str(grad_year).isdigit():
                story['graduation_year'] = int(grad_year)
            
            # Validate required fields
            if story['title'] and story['content'] and len(story['content']) >= 50:
                approved_stories.append(story)
                story_id += 1
    
    # Sort by publication date (newest first)
    approved_stories.sort(key=lambda x: x['publication_date'], reverse=True)
    
    # Write to YAML file
    output_path = '_data/stories.yml'
    os.makedirs('_data', exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# This file is auto-generated by GitHub Actions\n")
        f.write("# Do not edit manually - changes will be overwritten\n")
        f.write(f"# Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}\n\n")
        yaml.dump(approved_stories, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
    
    print(f"✓ Synced {len(approved_stories)} approved stories to {output_path}")

def parse_date(date_str):
    """Parse various date formats from Google Sheets."""
    if not date_str:
        return None
    
    # Try common formats
    formats = [
        '%Y-%m-%d',
        '%d/%m/%Y',
        '%m/%d/%Y %H:%M:%S',
        '%d.%m.%Y',
    ]
    
    for fmt in formats:
        try:
            return datetime.strptime(str(date_str), fmt).strftime('%Y-%m-%d')
        except ValueError:
            continue
    
    # If parsing fails, return current date
    return datetime.now().strftime('%Y-%m-%d')

if __name__ == '__main__':
    main()
```

### Step 6.5: Create scripts directory

```bash
mkdir -p scripts
chmod +x scripts/sync_stories.py
```

---

## PHASE 7: GITHUB PAGES DEPLOYMENT

### Step 7.1: Create GitHub Pages Configuration

Add to `_config.yml`:

```yaml
# GitHub Pages settings
plugins:
  - jekyll-feed
  - jekyll-seo-tag

# GitHub Pages will use these automatically
```

### Step 7.2: Create .gitignore

**File: `.gitignore`**

```
_site/
.sass-cache/
.jekyll-cache/
.jekyll-metadata
.DS_Store
*.swp
*.swo
*~
Gemfile.lock
node_modules/
```

### Step 7.3: Commit and Push

```bash
git add .
git commit -m "Initial commit: Jekyll site with Google Forms integration"
git branch -M main
git push -u origin main
```

### Step 7.4: Enable GitHub Pages

1. Go to repository → Settings → Pages
2. Source: Deploy from a branch
3. Branch: `main` / `/(root)`
4. Click Save
5. Wait 1-2 minutes for deployment
6. Site will be available at: `https://YOUR_USERNAME.github.io/kogni-memorial/`

---

## PHASE 8: TESTING & VALIDATION

### Step 8.1: Test Workflow Checklist

- [ ] **Form Submission Test**
  1. Go to Google Form URL
  2. Submit test story
  3. Verify appears in Google Sheets with "Pending" status
  4. Verify email notification received (if configured)

- [ ] **Moderation Test**
  1. Open Google Sheets
  2. Change test story status to "Approve"
  3. Add moderation notes and date
  4. Verify row turns green (conditional formatting)

- [ ] **Automation Test**
  1. Go to GitHub Actions tab
  2. Manually trigger "Sync Stories" workflow
  3. Wait for completion (~1 minute)
  4. Check if `_data/stories.yml` updated
  5. Check if site rebuilt automatically
  6. Visit site, verify story appears

- [ ] **Display Test**
  1. Visit homepage
  2. Verify story displays correctly
  3. Check responsive design (mobile, tablet)
  4. Test navigation links
  5. Verify footer links work

- [ ] **Privacy Test**
  1. Verify email addresses not visible on public site
  2. Check that only approved stories show
  3. Confirm rejection doesn't publish

### Step 8.2: Performance Testing

```bash
# Run Lighthouse audit
npx lighthouse https://YOUR_USERNAME.github.io/kogni-memorial/ --view

# Expected scores:
# Performance: ≥85
# Accessibility: ≥90
# Best Practices: ≥90
# SEO: ≥90
```

### Step 8.3: Accessibility Testing

- [ ] Keyboard navigation (Tab through all interactive elements)
- [ ] Screen reader test (NVDA/JAWS)
- [ ] Color contrast check (WAVE browser extension)
- [ ] Alt text for images
- [ ] Semantic HTML structure

---

## PHASE 9: DOCUMENTATION & HANDOFF

### Step 9.1: Create README for Repository

**File: `README.md` (replace existing)**

```markdown
# Kognitionswissenschaft Freiburg - Memorial Website

Memorial website for the Cognitive Science study program at University of Freiburg, ending in 2029.

## Live Site

[https://YOUR_USERNAME.github.io/kogni-memorial/](https://YOUR_USERNAME.github.io/kogni-memorial/)

## For Department Members: How to Moderate Submissions

1. **Access Google Sheets:** [LINK TO GOOGLE SHEETS]
2. **Review new submissions** (rows with yellow background = Pending)
3. **To approve:** Change "Status" column to "Approve"
4. **To reject:** Change "Status" column to "Reject"
5. **Add notes:** Use "Moderation Notes" column for internal comments
6. **Automatic sync:** Stories appear on website within 24 hours (daily at 9 AM)

### Manual Sync (Immediate Publication)

1. Go to [GitHub Actions](../../actions)
2. Click "Sync Stories from Google Sheets"
3. Click "Run workflow" → "Run workflow"
4. Wait 1-2 minutes for completion
5. Check website for updated stories

## For Developers: Technical Setup

### Local Development

```bash
# Install Jekyll
gem install bundler jekyll

# Clone repository
git clone https://github.com/YOUR_USERNAME/kogni-memorial.git
cd kogni-memorial

# Serve locally
jekyll serve

# Visit http://localhost:4000
```

### Architecture

- **Frontend:** Jekyll (static site generator)
- **Hosting:** GitHub Pages
- **Form:** Google Forms (external redirect)
- **Database:** Google Sheets
- **Automation:** GitHub Actions (daily sync)

### Key Files

- `_data/stories.yml` - Story data (auto-generated, do not edit manually)
- `scripts/sync_stories.py` - Sync script from Google Sheets
- `.github/workflows/sync-stories.yml` - GitHub Actions workflow
- `assets/css/main.css` - Styling
- `_layouts/default.html` - Base layout
- `index.html` - Homepage
- `submit.html` - Submission info page

### Updating Styles

1. Edit `assets/css/main.css`
2. Test locally with `jekyll serve`
3. Commit and push
4. GitHub Pages auto-rebuilds (1-2 minutes)

## Project Documentation

- `README.md` - Context and goals (original savepoint)
- `DATA.md` - Data structures and flows
- `REQUIREMENTS.md` - Functional and non-functional requirements
- `INSTRUCTIONS.md` - Complete implementation guide

## Support

For technical issues, contact: [YOUR CONTACT]

For content questions, contact: kogni@psychologie.uni-freiburg.de
```

### Step 9.2: Create Quick Start Guide for Non-Technical Users

**File: `MODERATOR_GUIDE.md`**

```markdown
# Moderator Guide: Geschichten prüfen und veröffentlichen

## Schritt-für-Schritt Anleitung

### 1. Neue Einreichung erhalten

Sie erhalten eine E-Mail-Benachrichtigung, wenn jemand eine Geschichte eingereicht hat.

### 2. Google Sheets öffnen

Öffnen Sie das Spreadsheet: [LINK EINFÜGEN]

### 3. Geschichte prüfen

Neue Einreichungen sind **gelb** markiert und haben Status "Pending".

**Prüfen Sie:**
- ✓ Ist der Inhalt angemessen?
- ✓ Bezieht sich die Geschichte auf Kognitionswissenschaft?
- ✓ Ist die Länge ausreichend (mindestens 50 Zeichen)?
- ✓ Enthält der Text beleidigende oder unangemessene Inhalte?

### 4. Entscheidung treffen

**Zum Genehmigen:**
1. Klicken Sie auf die Zelle in der Spalte "Status"
2. Wählen Sie "Approve" aus dem Dropdown-Menü
3. Die Zeile wird **grün**
4. Optional: Notiz in Spalte "Moderation Notes" hinzufügen

**Zum Ablehnen:**
1. Klicken Sie auf die Zelle in der Spalte "Status"
2. Wählen Sie "Reject" aus dem Dropdown-Menü
3. Die Zeile wird **rot**
4. Optional: Grund in Spalte "Moderation Notes" angeben

### 5. Automatische Veröffentlichung

- Genehmigte Geschichten erscheinen **automatisch täglich um 9 Uhr** auf der Website
- Sie müssen nichts weiter tun!

### 6. Sofortige Veröffentlichung (optional)

Wenn Sie möchten, dass eine Geschichte sofort erscheint:

1. Gehen Sie zu: https://github.com/YOUR_USERNAME/kogni-memorial/actions
2. Klicken Sie auf "Sync Stories from Google Sheets"
3. Klicken Sie auf "Run workflow" (grüner Button)
4. Bestätigen Sie mit "Run workflow"
5. Nach 1-2 Minuten ist die Geschichte online

## Häufige Fragen

**F: Kann ich eine Entscheidung rückgängig machen?**  
A: Ja, ändern Sie einfach den Status zurück. Beim nächsten Sync wird die Geschichte entfernt/hinzugefügt.

**F: Was passiert mit abgelehnten Geschichten?**  
A: Sie werden niemals öffentlich angezeigt, bleiben aber im Spreadsheet sichtbar.

**F: Können mehrere Personen gleichzeitig moderieren?**  
A: Ja, Google Sheets unterstützt gleichzeitiges Bearbeiten.

**F: Wie lange dauert es, bis Änderungen sichtbar sind?**  
A: Automatisch: bis zu 24 Stunden. Manuell: 1-2 Minuten.

## Kontakt bei Problemen

Technische Probleme: [CONTACT]  
Inhaltliche Fragen: kogni@psychologie.uni-freiburg.de
```

---

## DATA VORTEX PREVENTION ⚠️

### Critical Checkpoints for Data Transformations

**Checkpoint 1: Google Forms → Google Sheets**
- ✓ Verify all form fields map correctly to columns
- ✓ Test with special characters (ä, ö, ü, ß)
- ✓ Test with line breaks in content
- ✓ Verify timestamp format

**Checkpoint 2: Google Sheets → Python Script**
- ✓ Encoding: UTF-8 throughout
- ✓ Handle empty/null values gracefully
- ✓ Validate data types (year as integer)
- ✓ Sanitize for YAML special characters (`:`, `-`, `|`)

**Checkpoint 3: Python → YAML File**
- ✓ Use `allow_unicode=True` in yaml.dump
- ✓ Preserve line breaks with `|` literal block
- ✓ Escape special characters
- ✓ Test with 0 stories (empty file)

**Checkpoint 4: YAML → Jekyll**
- ✓ Verify Jekyll can parse stories.yml
- ✓ Test with missing optional fields
- ✓ Handle null values in templates (`{% if %}`)
- ✓ Proper date formatting

**Checkpoint 5: Jekyll → HTML**
- ✓ XSS prevention (Jekyll auto-escapes)
- ✓ Preserve paragraph breaks (`newline_to_br`)
- ✓ Test with very long content (5000 chars)
- ✓ Test with minimal content (50 chars)

### Validation Script

**File: `scripts/validate_data.py`**

```python
#!/usr/bin/env python3
"""
Validate stories.yml data integrity.
Run before committing changes.
"""

import yaml
import sys
from datetime import datetime

def validate_stories():
    errors = []
    
    try:
        with open('_data/stories.yml', 'r', encoding='utf-8') as f:
            stories = yaml.safe_load(f)
    except FileNotFoundError:
        print("✓ No stories.yml yet (acceptable for new project)")
        return True
    except yaml.YAMLError as e:
        print(f"✗ YAML parsing error: {e}")
        return False
    
    if not stories:
        print("✓ Empty stories list (acceptable)")
        return True
    
    for i, story in enumerate(stories, 1):
        # Required fields
        required = ['id', 'author_name', 'title', 'content', 'publication_date']
        for field in required:
            if field not in story or not story[field]:
                errors.append(f"Story {i}: Missing required field '{field}'")
        
        # Content length validation
        content = story.get('content', '')
        if len(content) < 50:
            errors.append(f"Story {i}: Content too short ({len(content)} chars, min 50)")
        if len(content) > 5000:
            errors.append(f"Story {i}: Content too long ({len(content)} chars, max 5000)")
        
        # Title length validation
        title = story.get('title', '')
        if len(title) < 5:
            errors.append(f"Story {i}: Title too short ({len(title)} chars, min 5)")
        if len(title) > 200:
            errors.append(f"Story {i}: Title too long ({len(title)} chars, max 200)")
        
        # Date format validation
        pub_date = story.get('publication_date', '')
        try:
            datetime.strptime(pub_date, '%Y-%m-%d')
        except ValueError:
            errors.append(f"Story {i}: Invalid publication_date format (expected YYYY-MM-DD)")
        
        # Graduation year validation (if present)
        grad_year = story.get('graduation_year')
        if grad_year and (not isinstance(grad_year, int) or grad_year < 1990 or grad_year > 2029):
            errors.append(f"Story {i}: Invalid graduation_year (must be 1990-2029)")
    
    if errors:
        print(f"✗ Found {len(errors)} validation errors:\n")
        for error in errors:
            print(f"  - {error}")
        return False
    else:
        print(f"✓ All {len(stories)} stories validated successfully")
        return True

if __name__ == '__main__':
    success = validate_stories()
    sys.exit(0 if success else 1)
```

---

## DEPLOYMENT CHECKLIST

### Pre-Launch

- [ ] Download Uni Freiburg logo and add to `assets/images/`
- [ ] Extract exact colors from official site and update CSS
- [ ] Replace `YOUR_USERNAME` in all files with actual GitHub username
- [ ] Replace `YOUR_FORM_ID` with actual Google Form ID
- [ ] Add Google Service Account email to Sheets with Editor access
- [ ] Add GitHub secrets (GOOGLE_SHEETS_CREDENTIALS, GOOGLE_SHEET_ID)
- [ ] Test form submission end-to-end
- [ ] Test moderation workflow
- [ ] Test GitHub Actions sync
- [ ] Create privacy policy page (`privacy.html`)
- [ ] Test on mobile devices
- [ ] Run Lighthouse audit
- [ ] Run accessibility checks

### Launch

- [ ] Push to GitHub
- [ ] Enable GitHub Pages
- [ ] Verify site is live
- [ ] Test all links from public site
- [ ] Share Google Form link on `submit.html`
- [ ] Share Google Sheets with all department members
- [ ] Send onboarding email to moderators with `MODERATOR_GUIDE.md`

### Post-Launch

- [ ] Monitor first submissions
- [ ] Verify automated sync works on schedule
- [ ] Collect feedback from first users
- [ ] Make styling adjustments as needed
- [ ] Plan announcement to alumni network

---

## MAINTENANCE & TROUBLESHOOTING

### Common Issues

**Issue: Stories not appearing after approval**
- Check GitHub Actions logs for errors
- Verify Google Service Account has Sheets access
- Manually trigger workflow to test
- Check `_data/stories.yml` was updated

**Issue: Form submissions not reaching Sheets**
- Verify form is linked to correct Sheet
- Check form responses tab
- Test with simple submission

**Issue: GitHub Actions failing**
- Check secrets are correctly set
- Verify Service Account JSON is valid
- Check Python script logs in Actions tab
- Test script locally with credentials

**Issue: Site not updating**
- GitHub Pages can take 1-2 minutes to rebuild
- Check repository "Actions" tab for build status
- Hard refresh browser (Cmd+Shift+R)

### Long-term Maintenance

**Annual Tasks:**
- Review and renew Google Service Account credentials (if needed)
- Update year in footer (`_includes/footer.html`)
- Archive old submissions (backup Google Sheets)

**2029 Transition to Static Archive:**
- Export final `stories.yml`
- Disable Google Form (close submissions)
- Remove GitHub Actions workflow (no more syncing)
- Add banner: "Submissions closed, archive preserved"
- Consider exporting to static HTML for ultimate preservation

---

## NEXT PHASE: PROTOTYPE IMPLEMENTATION

All instructions are complete. Ready to:

1. **Execute these instructions** to build the working site
2. **Test each phase** sequentially
3. **Deploy to production** after validation
4. **Train department members** on moderation workflow

---

**SAVEPOINT VALIDATION:**

✅ **Context (README.md):** Goals and constraints documented  
✅ **Data (DATA.md):** Structures and flows defined  
✅ **Requirements (REQUIREMENTS.md):** Functional/non-functional specs complete  
✅ **Instructions (INSTRUCTIONS.md):** Complete implementation guide with validation checkpoints  

**All Promptotyping phases complete. Ready for CODE generation.**

---

*This document serves as the immutable INSTRUCTIONS savepoint for the Cognitive Science Memorial Website project.*
