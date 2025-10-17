# Kognitionswissenschaft Freiburg - Memorial Website

Memorial website for the Cognitive Science study program at University of Freiburg, ending in 2029. This project preserves memories and success stories from alumni.

## 🌐 Live Site

**[https://YOUR_USERNAME.github.io/kogni-memorial/](https://YOUR_USERNAME.github.io/kogni-memorial/)**

*(Replace YOUR_USERNAME with your actual GitHub username)*

---

## 📋 Table of Contents

- [For Department Members (Non-Technical)](#-for-department-members-non-technical)
- [For Developers](#-for-developers)
- [Project Architecture](#-project-architecture)
- [Deployment Guide](#-deployment-guide)
- [Documentation](#-documentation)
- [Support](#-support)

---

## 👥 For Department Members (Non-Technical)

### How to Moderate Submissions

**See [MODERATOR_GUIDE.md](MODERATOR_GUIDE.md) for complete instructions.**

**Quick Overview:**
1. **Access Google Sheets:** [LINK TO GOOGLE SHEETS]
2. **Review new submissions** (rows with yellow background = Pending)
3. **To approve:** Change "Status" column to "Approve"
4. **To reject:** Change "Status" column to "Reject"
5. **Automatic sync:** Stories appear on website within 24 hours (daily at 9 AM UTC)

### Manual Sync (Immediate Publication)

If you need a story published immediately:

1. Go to [GitHub Actions](../../actions/workflows/sync-stories.yml)
2. Click "Run workflow" → "Run workflow"
3. Wait 1-2 minutes
4. Check website for updated stories

**Note:** Requires GitHub account with repository access.

---

## 🛠 For Developers

### Local Development

```bash
# Prerequisites
# - Ruby 2.7+ with Jekyll
# - Git

# Install Jekyll
gem install bundler jekyll

# Clone repository
git clone https://github.com/YOUR_USERNAME/kogni-memorial.git
cd kogni-memorial

# Serve locally
jekyll serve

# Visit http://localhost:4000
```

### Testing Changes

```bash
# Validate stories data
python3 scripts/validate_data.py

# Test sync script locally (requires credentials)
export GOOGLE_CREDENTIALS='...'
export SHEET_ID='...'
python3 scripts/sync_stories.py
```

### Making Changes

1. **Edit content:** Modify HTML files in root or `_includes/`, `_layouts/`
2. **Edit styles:** Modify `assets/css/main.css`
3. **Test locally:** Run `jekyll serve`
4. **Commit and push:** Changes auto-deploy via GitHub Pages

---

## 🏗 Project Architecture

```
┌─────────────────────────────────────────┐
│  GitHub Pages (Jekyll)                  │
│  • Static site generation               │
│  • Displays approved stories            │
│  • https://username.github.io/repo      │
└─────────────────────────────────────────┘
              ↓ (external link)
┌─────────────────────────────────────────┐
│  Google Form (Submission)               │
│  • Collects story submissions           │
│  • Opens in new tab/window              │
│  • form.google.com/YOUR_FORM_ID         │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│  Google Sheets (Database)               │
│  • Stores all submissions               │
│  • Status: Pending/Approve/Reject       │
│  • Collaborative moderation             │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│  GitHub Actions (Automation)            │
│  • Runs daily at 9 AM UTC               │
│  • Reads approved stories from Sheets   │
│  • Generates _data/stories.yml          │
│  • Commits → Triggers rebuild           │
└─────────────────────────────────────────┘
```

### Technology Stack

- **Frontend:** Jekyll (static site generator)
- **Hosting:** GitHub Pages (free, reliable)
- **Form:** Google Forms (external redirect)
- **Database:** Google Sheets (collaborative)
- **Automation:** GitHub Actions (daily sync)
- **Styling:** Custom CSS (Uni Freiburg branding)

---

## 🚀 Deployment Guide

### Prerequisites

- GitHub account
- Google account (Workspace or personal)
- Basic command line knowledge

### Step 1: Setup GitHub Repository

```bash
# Create new repository on GitHub.com
# Name: kogni-memorial
# Visibility: Public (required for GitHub Pages free tier)

# Clone this repository
cd ~/Documents/Projekte/Condolences
git init
git remote add origin https://github.com/YOUR_USERNAME/kogni-memorial.git
git branch -M main
```

### Step 2: Update Configuration

1. **Edit `_config.yml`:**
   ```yaml
   baseurl: "" # or "/kogni-memorial" if using subdomain
   url: "https://YOUR_USERNAME.github.io"
   ```

2. **Edit `submit.html`:**
   - Replace `YOUR_FORM_ID` with actual Google Form ID (see Step 3)

### Step 3: Create Google Form

1. Go to https://forms.google.com
2. Create new form: "Kognitionswissenschaft Freiburg - Erinnerungen einreichen"
3. Add fields (see INSTRUCTIONS.md Phase 3 for details):
   - Name (required)
   - E-Mail (optional)
   - Abschlussjahr (optional, number 1990-2029)
   - Titel (required, min 5 chars)
   - Geschichte (required, min 50 chars)
   - Art der Einreichung (multiple choice)
4. Link to Google Sheets: Responses → Create Spreadsheet
5. **Copy Form ID** from URL: `https://forms.google.com/d/FORM_ID/edit`

### Step 4: Configure Google Sheets

1. Open linked spreadsheet
2. Add columns H-K: Status, Moderation Notes, Moderated By, Moderation Date
3. Add data validation to column H: Pending, Approve, Reject
4. Share with all department members (Editor access)
5. **Copy Sheet ID** from URL: `https://docs.google.com/spreadsheets/d/SHEET_ID/edit`

### Step 5: Create Google Service Account

1. Go to https://console.cloud.google.com/
2. Create project: "Kogni Memorial Automation"
3. Enable **Google Sheets API**
4. Create Service Account:
   - Name: "github-actions-sheets"
   - Role: Editor
5. Create JSON key → Download
6. **Share Google Sheets with service account email** (Editor access)

### Step 6: Add GitHub Secrets

1. Go to repository → Settings → Secrets and variables → Actions
2. Add secrets:
   - `GOOGLE_SHEETS_CREDENTIALS`: Paste entire JSON from Step 5
   - `GOOGLE_SHEET_ID`: Paste Sheet ID from Step 4

### Step 7: Add University Logo

1. Download Uni Freiburg logo from official site
2. Save as `assets/images/uni-freiburg-logo.png`
3. Recommended size: 200x60px or similar

### Step 8: Deploy

```bash
# Commit all files
git add .
git commit -m "Initial commit: Kogni Memorial Website"
git push -u origin main
```

### Step 9: Enable GitHub Pages

1. Go to repository → Settings → Pages
2. Source: **Deploy from a branch**
3. Branch: **main** / **/(root)**
4. Click **Save**
5. Wait 2-3 minutes for deployment
6. Visit: `https://YOUR_USERNAME.github.io/kogni-memorial/`

### Step 10: Test Everything

- [ ] Website loads correctly
- [ ] Navigation works
- [ ] Submit page shows (with placeholder form link)
- [ ] Update `submit.html` with real Google Form URL
- [ ] Test form submission → Check Google Sheets
- [ ] Approve a test story in Sheets
- [ ] Manually trigger GitHub Actions workflow
- [ ] Verify story appears on website

---

## 📁 Project Structure

```
kogni-memorial/
├── _config.yml              # Jekyll configuration
├── _layouts/
│   └── default.html         # Base layout template
├── _includes/
│   ├── header.html          # Site header with navigation
│   └── footer.html          # Site footer with links
├── _data/
│   └── stories.yml          # Auto-generated story data
├── assets/
│   ├── css/
│   │   └── main.css         # Main stylesheet
│   └── images/
│       └── uni-freiburg-logo.png
├── scripts/
│   ├── sync_stories.py      # Google Sheets sync script
│   ├── validate_data.py     # Data validation script
│   └── requirements.txt     # Python dependencies
├── .github/
│   └── workflows/
│       └── sync-stories.yml # GitHub Actions workflow
├── index.html               # Homepage
├── submit.html              # Submission page
├── about.html               # About page
├── privacy.html             # Privacy policy
├── MODERATOR_GUIDE.md       # Guide for moderators
├── README.md                # This file
├── DATA.md                  # Data structure documentation
├── REQUIREMENTS.md          # Project requirements
└── INSTRUCTIONS.md          # Implementation instructions
```

### Key Files to Edit

| File | Purpose | When to Edit |
|------|---------|--------------|
| `_config.yml` | Site configuration | Change URL, title, settings |
| `submit.html` | Submission page | Update Google Form link |
| `assets/css/main.css` | Styling | Adjust colors, fonts, layout |
| `_data/stories.yml` | Story data | Auto-generated (don't edit manually) |
| `_includes/header.html` | Navigation | Add/remove menu items |
| `_includes/footer.html` | Footer | Update contact info, links |

---

## 📚 Documentation

- **[INSTRUCTIONS.md](INSTRUCTIONS.md)** - Complete implementation guide (9 phases)
- **[MODERATOR_GUIDE.md](MODERATOR_GUIDE.md)** - How to moderate submissions (for non-technical users)
- **[REQUIREMENTS.md](REQUIREMENTS.md)** - Functional and non-functional requirements
- **[DATA.md](DATA.md)** - Data structures and flows
- **[README.md](README.md)** - This file (project overview)

---

## 🔧 Maintenance

### Regular Tasks

- **Weekly:** Review pending submissions in Google Sheets
- **Monthly:** Check GitHub Actions logs for errors
- **Quarterly:** Review and update privacy policy if needed
- **Annually:** Renew Google Service Account credentials (if needed)

### Common Issues

**Issue: Stories not appearing after approval**
- Check GitHub Actions logs for errors
- Verify service account has Sheets access
- Manually trigger workflow to test

**Issue: Form submissions not in Sheets**
- Verify form is linked to correct spreadsheet
- Check form responses tab

**Issue: GitHub Actions failing**
- Check secrets are correctly set (GOOGLE_SHEETS_CREDENTIALS, GOOGLE_SHEET_ID)
- Verify service account JSON is valid
- Check Python script logs

**Issue: Site not updating**
- GitHub Pages rebuild takes 1-2 minutes
- Hard refresh browser (Cmd+Shift+R / Ctrl+Shift+F5)
- Check repository Actions tab for build status

### Updating Content

**To change homepage text:**
1. Edit `index.html`
2. Commit and push
3. Wait for GitHub Pages rebuild (1-2 minutes)

**To update navigation:**
1. Edit `_includes/header.html`
2. Update `<nav>` section
3. Commit and push

**To change styling:**
1. Edit `assets/css/main.css`
2. Use browser DevTools to test changes
3. Commit and push

---

## 🎨 Customization

### Colors (Uni Freiburg Branding)

Edit `assets/css/main.css` `:root` section:

```css
:root {
  --primary-color: #004a99;     /* Uni Freiburg Blue */
  --primary-dark: #003d7a;
  --secondary-color: #6c757d;
  /* ... */
}
```

**TODO:** Extract exact colors from https://uni-freiburg.de/cognition/

### Typography

Default font stack:
```css
--font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, ...;
```

To use custom fonts, add to `_layouts/default.html`:
```html
<link href="https://fonts.googleapis.com/css2?family=YOUR_FONT" rel="stylesheet">
```

---

## 🔒 Security & Privacy

- **HTTPS:** Enforced by GitHub Pages
- **No tracking:** No Google Analytics or third-party cookies
- **GDPR compliant:** Privacy policy included
- **Email privacy:** Email addresses never displayed publicly
- **Data retention:** Defined in DATA.md and privacy policy

---

## 📞 Support

### For Moderators
- **Questions about moderation:** See MODERATOR_GUIDE.md
- **Content questions:** kogni@psychologie.uni-freiburg.de

### For Technical Issues
- **GitHub/Deployment:** [YOUR TECHNICAL CONTACT]
- **Google Sheets/Forms:** [YOUR TECHNICAL CONTACT]
- **General support:** kogni@psychologie.uni-freiburg.de

### Reporting Issues

Open an issue on GitHub: [https://github.com/YOUR_USERNAME/kogni-memorial/issues](https://github.com/YOUR_USERNAME/kogni-memorial/issues)

---

## 🙏 Credits

**Developed using the Promptotyping Method**

- **University:** Universität Freiburg
- **Department:** Abteilung Kognitionswissenschaft
- **Year:** 2025
- **Purpose:** Preserve memories of the Cognitive Science program (ending 2029)

---

## 📄 License

This project is developed for the University of Freiburg. All content (stories) remains the property of the respective authors.

Website code and structure: Available for educational and archival purposes.

---

**Last Updated:** October 2025  
**Project Status:** Active Development  
**Target Go-Live:** [YOUR TARGET DATE]
