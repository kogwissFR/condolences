# Quick Deployment Checklist

Use this checklist to deploy the Kogni Memorial website step-by-step.

## ✅ Pre-Deployment

- [ ] Read INSTRUCTIONS.md completely
- [ ] Have GitHub account ready
- [ ] Have Google account ready (Uni Freiburg or personal)
- [ ] Install Jekyll locally for testing: `gem install jekyll bundler`

## ✅ Step 1: GitHub Setup

- [ ] Create new GitHub repository: `kogni-memorial` (public)
- [ ] Clone this repository to the new repo
- [ ] Update `_config.yml` with your GitHub username
- [ ] Commit and push to GitHub

## ✅ Step 2: Google Forms

- [ ] Create Google Form at https://forms.google.com
- [ ] Add all required fields (see INSTRUCTIONS.md Phase 3)
- [ ] Link form to Google Sheets
- [ ] Copy Form ID from URL
- [ ] Update `submit.html` with Form ID
- [ ] Test form submission

## ✅ Step 3: Google Sheets

- [ ] Open linked spreadsheet from form
- [ ] Add columns H-K (Status, Notes, By, Date)
- [ ] Add data validation to Status column (Pending/Approve/Reject)
- [ ] Add conditional formatting (yellow/green/red)
- [ ] Share with all department members (Editor access)
- [ ] Copy Sheet ID from URL
- [ ] Test: Submit test form → Verify appears in Sheets

## ✅ Step 4: Google Service Account

- [ ] Go to https://console.cloud.google.com/
- [ ] Create new project: "Kogni Memorial Automation"
- [ ] Enable Google Sheets API
- [ ] Create service account: "github-actions-sheets"
- [ ] Grant Editor role
- [ ] Create JSON key → Download
- [ ] Share Google Sheets with service account email (Editor access)
- [ ] Save JSON key securely

## ✅ Step 5: GitHub Secrets

- [ ] Go to repo → Settings → Secrets and variables → Actions
- [ ] Add secret: `GOOGLE_SHEETS_CREDENTIALS` = entire JSON content
- [ ] Add secret: `GOOGLE_SHEET_ID` = Sheet ID from Step 3
- [ ] Verify secrets are saved

## ✅ Step 6: University Branding

- [ ] Download Uni Freiburg logo from official site
- [ ] Save as `assets/images/uni-freiburg-logo.png`
- [ ] Optional: Extract exact brand colors from https://uni-freiburg.de/cognition/
- [ ] Optional: Update CSS variables in `assets/css/main.css`
- [ ] Commit and push

## ✅ Step 7: Test Locally

- [ ] Run `jekyll serve` in project directory
- [ ] Visit http://localhost:4000
- [ ] Test navigation (all pages load)
- [ ] Test responsive design (mobile view)
- [ ] Check for broken images/links
- [ ] Verify sample stories display correctly

## ✅ Step 8: Enable GitHub Pages

- [ ] Go to repo → Settings → Pages
- [ ] Source: "Deploy from a branch"
- [ ] Branch: `main` / `/(root)`
- [ ] Click Save
- [ ] Wait 2-3 minutes
- [ ] Visit: https://YOUR_USERNAME.github.io/kogni-memorial/
- [ ] Verify site loads correctly

## ✅ Step 9: Test Automation

- [ ] Submit test story via Google Form
- [ ] Check Google Sheets → Should appear with Status "Pending"
- [ ] Change Status to "Approve"
- [ ] Go to repo → Actions
- [ ] Click "Sync Stories from Google Sheets"
- [ ] Click "Run workflow" → "Run workflow"
- [ ] Wait ~2 minutes
- [ ] Check `_data/stories.yml` was updated
- [ ] Visit website → Verify test story appears
- [ ] Success! 🎉

## ✅ Step 10: Production Setup

- [ ] Remove test stories from Sheets (or set Status to "Reject")
- [ ] Update `submit.html` with real Google Form link
- [ ] Update `_config.yml` with final URL (if using custom domain)
- [ ] Create email notification rules in Google Sheets
- [ ] Share MODERATOR_GUIDE.md with department
- [ ] Share Google Sheets link with all moderators
- [ ] Test end-to-end: Submit real story → Approve → Verify appears
- [ ] Monitor for 24 hours to ensure daily sync works

## ✅ Step 11: Documentation

- [ ] Update PROJECT_README.md with:
  - [ ] Live site URL
  - [ ] Google Sheets link
  - [ ] Google Form link
  - [ ] Technical contact info
- [ ] Update MODERATOR_GUIDE.md with:
  - [ ] Google Sheets link
  - [ ] Support contact info
- [ ] Commit final documentation

## ✅ Step 12: Announcement

- [ ] Announce to department (email/meeting)
- [ ] Provide moderator access to Google Sheets
- [ ] Distribute MODERATOR_GUIDE.md
- [ ] Announce to alumni (email/social media)
- [ ] Monitor submissions in first week

## 🎯 Post-Launch Monitoring

**Week 1:**
- [ ] Daily check of Google Sheets for spam/issues
- [ ] Monitor GitHub Actions logs (should run daily at 9 AM UTC)
- [ ] Respond to moderator questions
- [ ] Fix any technical issues

**Week 2-4:**
- [ ] Weekly check of submissions
- [ ] Verify daily sync is working
- [ ] Collect feedback from moderators and users

**Month 2+:**
- [ ] Monthly check of system health
- [ ] Update documentation as needed
- [ ] Plan any feature enhancements

## 📞 Emergency Contacts

**If something breaks:**

1. **GitHub Actions not running:**
   - Check Actions tab for errors
   - Verify secrets are still set
   - Check service account access

2. **Form submissions not appearing:**
   - Check Google Form is linked to Sheets
   - Verify Sheets is shared with service account
   - Test manual form submission

3. **Site not updating:**
   - Check GitHub Pages status (Settings → Pages)
   - Verify last commit triggered rebuild
   - Check for build errors in Actions tab

4. **Get help:**
   - Check INSTRUCTIONS.md for detailed troubleshooting
   - Contact: [YOUR TECHNICAL CONTACT]
   - Email: kogni@psychologie.uni-freiburg.de

## ✨ Success Criteria

You're done when:

✅ Website is live and accessible  
✅ Form submissions reach Google Sheets  
✅ Moderators can approve/reject stories  
✅ Approved stories automatically appear on website  
✅ Daily sync runs without errors  
✅ All department members have moderation access  
✅ Documentation is complete and shared  

---

**Estimated Total Time:** 4-6 hours (spread over 1-2 days)

**Congratulations on launching the Kogni Memorial Website!** 🎊
