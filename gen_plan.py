
import json, os

# ─── PLAN DATA ──────────────────────────────────────────────────────────────
PHASES = [

{"ph":0,"title":"Environment + GStack Setup","duration":"3 days",
 "goal":"Claude Code installed. GStack running. All dev accounts active. You understand what every GStack skill does before writing a line of code.",
 "days":[
  {"d":1,"name":"Day 1","title":"Install Claude Code + GStack",
   "dev":[
    {"t":"Install Claude Code (Anthropic's CLI coding agent): run npm install -g @anthropic/claude-code in terminal. Then: claude --version to confirm. This is separate from Claude.ai — it runs in your terminal and writes code with you.","m":"20"},
    {"t":"Get a Claude API key (separate from Gemini — Claude Code needs this for development tooling): go to console.anthropic.com → API Keys → Create Key. Store in 1Password as 'Claude Code API Key'. This is NOT the same as Gemini — Claude Code is your dev assistant, Gemini is your app's AI engine.","m":"15"},
    {"t":"Install GStack: run claude install garrytan/gstack in terminal. Confirm: type claude in your vaulty project folder → you should see gstack slash commands available. Run /gstack to see the full skill list.","m":"20"},
    {"t":"Claim GitHub Student Pack at education.github.com/pack. Claim: Sentry (enhanced), Datadog Pro (2 years), BrowserStack, Namecheap domain, 1Password. Store all credentials in 1Password immediately.","m":"45"},
    {"t":"Create accounts: Supabase (supabase.com), Posthog (posthog.com), Resend (resend.com), Vercel (vercel.com), aistudio.google.com (Gemini API key). Store every key in 1Password.","m":"30"}],
   "gstack":[
    {"t":"[GSTACK FIRST RUN] In your terminal, navigate to any folder and type: claude. You are now in Claude Code. Type /gstack to see all available skills. Read the description of each one. Spend 20 minutes just reading what each skill does — this investment pays back every day.","m":"20"}],
    "security":[
     {"t":"[SECURITY SETUP] In 1Password: create a Vault called 'Vaulty Secrets'. Store every API key here. Rule: no API key ever goes in code, .env files committed to GitHub, Notion notes, or chat messages. Every key lives in 1Password. This is non-negotiable.","m":"15"}],
   "learn":[
    {"t":"Watch: 'What is Claude Code?' — search on YouTube or anthropic.com/claude-code. 10 minutes. Understand: Claude Code is an agentic coding assistant that runs in your terminal, reads your files, writes code, runs tests, and uses GStack skills to review and ship your work.","m":"15"},
    {"t":"Read: github.com/garrytan/gstack README fully. 30 minutes. This is the most important reading of this entire plan — GStack shapes how you build everything. Read it like a user manual, not skimming.","m":"30"}]},

  {"d":2,"name":"Day 2","title":"Understand GStack Skills + Run Office Hours",
   "dev":[
    {"t":"Create your GitHub repository: go to github.com → New repository → name: vaulty → Private → Create. Clone it locally. Create a CLAUDE.md file in the root — this is where GStack stores project context and skill routing rules. Copy the template from the GStack README.","m":"25"},
    {"t":"Create your project root structure: vaulty/ with folders: supabase/ (for edge functions and migrations), app/ (for Expo app, created later), docs/ (for architecture decisions). Initialize git: git add . && git commit -m 'project init'","m":"20"}],
   "gstack":[
    {"t":"[GSTACK /office-hours] In Claude Code terminal type: /office-hours. When prompted, describe Vaulty: 'I am building a career intelligence mobile app for university students. Users add achievements to a vault, then paste a job description and get a tailored resume. Also generates LinkedIn posts from achievements.' The skill will ask 6 forcing questions that challenge your product assumptions. Answer every question honestly. This output shapes your entire architecture.","m":"60"},
    {"t":"[GSTACK /plan-ceo-review] After office-hours, run: /plan-ceo-review. Share the Vaulty context file we created earlier. This skill reviews your product strategy like a CEO — it will challenge your scope, target user definition, and business model. Take notes on every critique. Update your product spec based on the output.","m":"45"}],
   "security":[
    {"t":"[SECURITY PLANNING] Based on your /office-hours output: list the 5 most sensitive data types in Vaulty (career achievements, job applications, email, university info, LinkedIn profile). For each: write who should access it (only the owner), how it could leak (auth bypass, API exploit, storage), and how you will prevent it. This is your threat model draft.","m":"30"}],
   "learn":[
    {"t":"Read: owasp.org/www-project-mobile-top-10 — all 10 mobile security risks. 45 minutes. This is the industry standard for mobile app security. Highlight the ones most relevant to Vaulty: M1 (credential storage), M4 (input validation), M6 (privacy), M9 (data storage). You will test against these explicitly in Phase 9.","m":"45"},
    {"t":"Watch: 'STRIDE Threat Modeling Explained' on YouTube (15 min). STRIDE = Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege. The /cso skill uses STRIDE. Understanding it before using /cso means you get more value from the output.","m":"15"}]},

  {"d":3,"name":"Day 3","title":"Architecture Planning with GStack",
   "dev":[
    {"t":"Install VS Code + GitHub Copilot (from Student Pack). Install Node.js LTS. Install Git. Install Expo Go on phone. Run: node --version → should show v20+. Run: git --version → should show 2.x+. These are your daily tools.","m":"30"},
    {"t":"Set up 1Password Teams (Student Pack) for secrets management. Install the 1Password CLI: 1password.com/downloads/command-line. This lets you inject secrets from 1Password into your terminal without ever hardcoding them.","m":"20"}],
   "gstack":[
    {"t":"[GSTACK /autoplan] Run: /autoplan in Claude Code. This chains /plan-ceo-review → /plan-eng-review → /plan-design-review automatically. Input: the Vaulty build spec document we created earlier. This gives you a fully reviewed architecture plan before you touch code. The output will have specific findings and required fixes. This is the most valuable session of Phase 0.","m":"90"},
    {"t":"[GSTACK /plan-eng-review] After /autoplan, run: /plan-eng-review specifically on your database schema design (the SQL from the build spec). The skill will flag: missing indexes, RLS policy gaps, data normalization issues, missing audit trails. Fix every HIGH and CRITICAL finding before Phase 2.","m":"45"}],
   "security":[
    {"t":"[SECURITY] From /plan-eng-review output: create a 'Security Decisions' doc in Notion. For each architectural decision: record the security implication. Example: 'Achievement data stored in Supabase → encrypted at rest by default → additionally protected by RLS → user can only SELECT/INSERT/UPDATE/DELETE their own rows.' This doc becomes your security audit trail.","m":"25"}],
   "learn":[
    {"t":"Read: supabase.com/docs/guides/database/row-level-security (full guide, 30 min). Then read: supabase.com/docs/guides/auth/auth-deep-dive/auth-deep-dive-jwts (20 min). You need to understand JWTs deeply before building auth — every Supabase RLS policy depends on auth.uid() which comes from the JWT.","m":"50"},
    {"t":"Read: docs.expo.dev/guides/security (15 min). Understand: what data to store in SecureStore vs AsyncStorage vs memory. SecureStore = sensitive (tokens, keys). AsyncStorage = non-sensitive (preferences, cache). Memory = temporary (component state). This decision affects every storage call you make.","m":"15"}]}
 ]},


{"ph":1,"title":"Backend Core — Database + Auth + AI","duration":"5 days",
 "goal":"Full backend working. Schema live with RLS. Gemini generates real resumes. Every operation tested via Postman.",
 "days":[
  {"d":4,"name":"Day 4","title":"Database Schema",
   "dev":[
    {"t":"Open Supabase → your vaulty project → SQL Editor. Run: CREATE EXTENSION IF NOT EXISTS 'uuid-ossp'; to enable UUIDs. Then run the complete schema SQL from the Vaulty Build Spec (profiles, achievements, resume_requests, linkedin_posts tables). Confirm: 4 tables created, zero errors.","m":"60"},
    {"t":"Enable pgvector extension for Phase 2 semantic matching: run CREATE EXTENSION IF NOT EXISTS vector; in SQL Editor. Add embedding column to achievements: ALTER TABLE achievements ADD COLUMN embedding vector(768); This costs nothing now but saves a migration later.","m":"15"},
    {"t":"Run all RLS policies: ALTER TABLE public.profiles ENABLE ROW LEVEL SECURITY — repeat for achievements, resume_requests, linkedin_posts. Then run all CREATE POLICY statements from the build spec. These are your primary data security layer.","m":"30"},
    {"t":"Run the auto-create profile trigger from the build spec. Test it: Supabase Auth → Add user manually → check profiles table → a row should appear automatically. If it does not, debug the trigger before proceeding.","m":"20"}],
   "gstack":[
    {"t":"[GSTACK /review] After writing the SQL schema file: save it as supabase/migrations/001_initial_schema.sql in your repo. Then in Claude Code type: /review and point it at this file. The skill will catch: missing indexes on frequently queried columns (user_id), missing CASCADE rules, potential RLS bypass patterns, inefficient query patterns. Fix every issue it flags before deploying.","m":"30"}],
   "security":[
    {"t":"[SECURITY] Verify every table has RLS enabled by running: SELECT tablename, rowsecurity FROM pg_tables WHERE schemaname = 'public'; in Supabase SQL Editor. Every table must show rowsecurity = true. Any table showing false is a critical security gap.","m":"10"},
    {"t":"[SECURITY] Test RLS isolation: create two test users in Supabase Auth. Insert a row in achievements as User A. Then try to SELECT it as User B. You should get 0 rows — not an error, not the data. If User B can see User A's data, your RLS policy has a bug. Fix this before any frontend work.","m":"20"}],
   "learn":[
    {"t":"Read: supabase.com/docs/guides/database/postgres/row-level-security (the advanced section, 20 min). Then read: supabase.com/docs/guides/database/postgres/indexes (15 min). Run: CREATE INDEX idx_achievements_user_id ON achievements(user_id); in Supabase. Every query against achievements filters by user_id — without this index it does a full table scan, getting slower as data grows.","m":"35"},
    {"t":"Read: postgresql.org/docs/current/datatype.html — specifically the UUID, TEXT, BOOLEAN, TIMESTAMP WITH TIME ZONE, and ARRAY types. 20 minutes. You used all of these in your schema. Understanding why each type was chosen (TIMESTAMPTZ not TIMESTAMP for timezone safety, UUID not INTEGER for distributed safety) makes you a better engineer.","m":"20"}]},

  {"d":5,"name":"Day 5","title":"Auth + Edge Function Scaffold",
   "dev":[
    {"t":"Enable Email/Password auth in Supabase: Dashboard → Authentication → Providers → Email → Enable. Disable email confirmation for development (re-enable before beta). Test via Supabase Auth API directly: POST to {SUPABASE_URL}/auth/v1/signup with email and password. Should return a user object and JWT.","m":"20"},
    {"t":"Install Supabase CLI: npm install -g supabase. Initialize: supabase init in your project folder. Create the generate function: supabase functions new generate. This creates supabase/functions/generate/index.ts. Do not deploy yet.","m":"20"},
    {"t":"Write the complete Gemini edge function from the build spec. Key imports for Deno: import { GoogleGenerativeAI } from 'npm:@google/generative-ai'. Model: 'gemini-1.5-flash'. Handlers: type === 'resume', type === 'linkedin', type === 'extract_pdf'. The PDF handler uses Gemini's native PDF reading: pass {inlineData:{data:base64Pdf, mimeType:'application/pdf'}} as content.","m":"90"},
    {"t":"Add GEMINI_API_KEY to Supabase secrets: supabase secrets set GEMINI_API_KEY=your-key-here. NEVER put this in code or .env files. Deploy: supabase functions deploy generate. Test with Postman: POST to the function URL with a hardcoded test body. You should get a response within 5 seconds.","m":"30"}],
   "gstack":[
    {"t":"[GSTACK /review] After writing the edge function: run /review on supabase/functions/generate/index.ts. The skill checks for: unhandled promise rejections (crash the function), missing input validation (security risk), API key exposure (critical security), error messages that leak internal details (security), missing CORS headers (blocks mobile app). Fix everything flagged as HIGH before deploying.","m":"30"}],
   "security":[
    {"t":"[SECURITY] Edge function authentication: every call to your generate function must include the Supabase JWT in the Authorization header. Add auth verification at the top of your edge function: const authHeader = req.headers.get('Authorization'); if (!authHeader) return new Response(JSON.stringify({error:'Unauthorized'}), {status:401}). Without this, anyone on the internet can call your Gemini endpoint.","m":"25"},
    {"t":"[SECURITY] Rate limiting: add a simple rate limit to prevent abuse. Track calls per user per hour. After 10 generations in an hour: return 429 Too Many Requests. This prevents both accidental loops and malicious abuse that would drain your Gemini API credits.","m":"20"}],
   "learn":[
    {"t":"Read: deno.land/manual/runtime/workers (10 min). Read: deno.land/manual/examples/fetch_data (10 min). Understand: Supabase Edge Functions run on Deno (not Node.js). The key differences: import from 'npm:' prefix for npm packages, no require(), top-level await is fine, built-in fetch. These differences will confuse you if you don't know them.","m":"25"},
    {"t":"Read: ai.google.dev/gemini-api/docs/quickstart?lang=node (20 min). Then in AI Studio (aistudio.google.com): test your resume prompt with a real JD and fake achievements. Does it follow your resume quality checklist from Week 0? If not, refine the prompt NOW before wiring it to the app. Prompt quality is your product quality.","m":"30"}]},

  {"d":6,"name":"Day 6","title":"Test Backend End-to-End",
   "dev":[
    {"t":"Test the complete resume generation pipeline via Postman: (1) Signup → get JWT. (2) Insert 5 test achievements directly in Supabase Table Editor. (3) POST to generate function with those achievement IDs + a real job description + the JWT in Authorization header. (4) Verify: you get a JSON object with resume, match_score, keywords_covered, keywords_missing.","m":"60"},
    {"t":"Test the PDF extraction: encode a real PDF (your own CV) as base64 in Postman. POST to generate function with type:'extract_pdf' and the base64 data. Verify: you get back a JSON array of achievement objects. Test with an Arabic CV too. Document: what extracts correctly and what does not.","m":"45"},
    {"t":"Test RLS via API: use two different JWTs (from two different test users). Try to GET achievements from user A while authenticated as user B. Should return empty array. Try to INSERT an achievement with a hardcoded user_id of user A while authenticated as user B. Should fail. If either test passes, your RLS has a critical bug.","m":"30"}],
   "gstack":[
    {"t":"[GSTACK /investigate] If any test fails unexpectedly: run /investigate in Claude Code and describe the exact failing behavior. The skill systematically works through potential causes, tests each hypothesis, and proposes fixes. Do not spend more than 30 minutes debugging alone — use /investigate after 30 minutes of being stuck.","m":"0"}],
   "security":[
    {"t":"[SECURITY] Test for SQL injection: try sending a job description containing: '; DROP TABLE achievements; -- in the JD field. The edge function should sanitize this and NOT crash. Supabase's parameterized queries prevent SQL injection by default, but you should verify your edge function does not build raw SQL strings anywhere.","m":"15"},
    {"t":"[SECURITY] Check error messages: what does the API return when auth fails? It should say 'Unauthorized' — not reveal anything about your database structure. What does it return when a resume generation fails? Should say 'Generation failed' — not expose Gemini API error details.","m":"10"}],
   "learn":[
    {"t":"Read: portswigger.net/web-security/sql-injection (25 min). Even though Supabase prevents SQL injection by default, understanding how it works makes you write safer code. Also read: portswigger.net/web-security/authentication (25 min). These are the two most common web vulnerabilities — knowing them makes you a better developer.","m":"50"},
    {"t":"Practice: open Postman and write a test collection for your edge function. Add 5 tests: (1) resume generation with valid data, (2) resume generation with no auth, (3) PDF extraction with valid PDF, (4) invalid type parameter, (5) empty achievements array. Save this collection — you will rerun it after every schema change.","m":"30"}]},

  {"d":7,"name":"Day 7","title":"LinkedIn Service + Achievement CRUD Services",
   "dev":[
    {"t":"Create src/services/achievements.service.ts with 5 functions: getAchievements(userId), addAchievement(data), updateAchievement(id,updates), deleteAchievement(id), getAchievementById(id). Each wraps a Supabase query with error handling. Add TypeScript types for all parameters and return values.","m":"60"},
    {"t":"Create src/services/resume.service.ts: generateResume({userId,jobDescription,jobTitle,companyName}) — fetches achievements, calls edge function, saves to DB, returns result. Create src/services/linkedin.service.ts: generateLinkedInPost({userId,achievementId}) — same pattern. Create src/services/pdf.service.ts: exportResumeToPDF(text, name) — converts to HTML then PDF.","m":"60"},
    {"t":"Create src/lib/supabase.ts using the build spec. The SecureStore adapter is critical: on native platforms it uses Expo SecureStore (encrypted device storage) for session tokens. On web it uses localStorage. Test: import the client in a test file and run a simple SELECT — should return data.","m":"30"}],
   "gstack":[
    {"t":"[GSTACK /review] Run /review on all 3 service files (achievements, resume, linkedin). Key things the skill checks: uncaught promise rejections that crash the app, type safety gaps, functions that do too many things (should be split), missing error codes, inconsistent error handling patterns. Fix every issue before building UI on top of these services.","m":"35"}],
   "security":[
    {"t":"[SECURITY] In every service function: validate that userId matches the authenticated user before any database operation. Example in addAchievement: verify data.user_id === supabase.auth.getUser().id before inserting. This is a defense-in-depth layer on top of RLS — even if RLS has a bug, your service layer rejects unauthorized operations.","m":"20"}],
   "learn":[
    {"t":"Read: supabase.com/docs/reference/javascript/typescript-support (15 min). Supabase can auto-generate TypeScript types from your schema. Run: supabase gen types typescript --project-id your-id > src/types/database.types.ts. This gives you fully typed database operations — no more guessing column names.","m":"30"},
    {"t":"YouTube: search 'TypeScript generics explained simply' → watch 20 min video. Your service functions use generics: function getAchievements<T extends Achievement>. Understanding generics lets you write reusable, type-safe service patterns instead of copy-pasting code.","m":"20"}]},

  {"d":8,"name":"Day 8","title":"Backend Security Hardening + First /cso",
   "dev":[
    {"t":"Add input validation to ALL edge function inputs. Install a validation library in Deno: import { z } from 'npm:zod'. Define schemas: resumeSchema = z.object({achievements:z.array(achievementSchema), jobDescription:z.string().min(50).max(5000), profile:profileSchema}). Validate every incoming request body. Invalid data returns 400 with specific error messages.","m":"45"},
    {"t":"Add database indexes for performance and security: CREATE INDEX idx_achievements_user_id ON achievements(user_id); CREATE INDEX idx_achievements_type ON achievements(type); CREATE INDEX idx_resume_requests_user_id ON resume_requests(user_id); CREATE INDEX idx_resume_requests_created_at ON resume_requests(created_at DESC). These make RLS policies execute faster.","m":"20"},
    {"t":"Set up Supabase project settings: Dashboard → Settings → General → disable 'Allow new users to sign up' (you will re-enable for beta). Dashboard → Settings → Auth → increase JWT expiry from 1 hour to 24 hours for better UX. Dashboard → Settings → API → note your project rate limits.","m":"15"}],
   "gstack":[
    {"t":"[GSTACK /cso] Run /cso in Claude Code and describe your Vaulty backend: auth implementation, data storage, API endpoints, user data types. This skill performs an OWASP Top 10 + STRIDE threat model analysis. It will generate a security findings report with Critical, High, Medium, Low issues. STOP — do not move to Phase 2 until every Critical and High finding is resolved.","m":"90"},
    {"t":"[GSTACK /review] After fixing /cso findings: run /review one more time on the entire supabase/ folder. The skill verifies your fixes are complete and did not introduce new issues. Only proceed to mobile development when /review shows no HIGH or CRITICAL issues.","m":"30"}],
   "security":[
    {"t":"[SECURITY] Implement the STRIDE mitigations identified by /cso. The 6 STRIDE threats for Vaulty: Spoofing → RLS policies (done). Tampering → input validation + ownership checks (add today). Repudiation → created_at timestamps on all tables (verify exists). Information Disclosure → error sanitization (verify edge function). Denial of Service → rate limiting (add today). Elevation of Privilege → no admin endpoints exposed (verify).","m":"45"},
    {"t":"[SECURITY] Create a security-headers.ts utility file. It adds: X-Content-Type-Options: nosniff, X-Frame-Options: DENY, X-XSS-Protection: 1; mode=block to all edge function responses. Apply it to every edge function response using a wrapper function. 15 lines of code that prevent 3 common web attacks.","m":"20"}],
   "learn":[
    {"t":"Read: cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html (30 min). Read: cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html (20 min). These are the two most important security cheat sheets for what you are building. After reading: check your edge function against every relevant recommendation.","m":"50"},
    {"t":"Watch: 'JWT Security Best Practices' on YouTube (15 min). Understand: never store JWTs in localStorage on web (use HttpOnly cookies or memory), check expiry before using, validate signature server-side. For mobile (SecureStore) these risks are lower, but understanding JWT security makes you build better auth.","m":"15"}]}
 ]},


{"ph":2,"title":"Mobile Foundation — Expo + Auth Screens","duration":"4 days",
 "goal":"App running on phone. Signup creates real Supabase data. Auth flow tested end-to-end with GStack /qa.",
 "days":[
  {"d":9,"name":"Day 9","title":"Expo Init + Dependencies + Theme",
   "dev":[
    {"t":"Run: npx create-expo-app@latest vaulty --template blank-typescript → cd vaulty → npm install. Install all dependencies from the build spec in two commands. Change package.json main to 'expo-router/entry'. Create the full folder structure from the build spec.","m":"45"},
    {"t":"Create src/theme/index.ts with ALL design tokens from the build spec. Create src/lib/supabase.ts with SecureStore adapter. Create src/lib/constants.ts with ACHIEVEMENT_TYPES (14 types) and CAREER_TAGS (60 tags). Create src/types/index.ts with every TypeScript interface. These 4 files are the foundation everything builds on.","m":"60"},
    {"t":"Run npx expo start → scan QR with Expo Go on your phone → confirm white screen appears. Commit: git add . && git commit -m 'expo foundation — theme, types, constants, supabase client'","m":"15"}],
   "gstack":[
    {"t":"[GSTACK /plan-design-review] Before building any UI: run /plan-design-review and describe your 3 auth screens (welcome, login, onboarding). The skill checks for: missing loading states, missing error states, empty state definitions, mobile-specific UX problems. It will rate each screen 0-10 and explain what a 10 looks like. Fix every issue before coding — UI changes are expensive after the fact.","m":"45"}],
   "security":[
    {"t":"[SECURITY] In src/lib/supabase.ts: verify your SecureStore adapter uses expo-secure-store (not AsyncStorage) for the session. SecureStore uses the device's secure enclave (iOS Keychain, Android Keystore) — it is hardware-encrypted. AsyncStorage is plain text. If you accidentally use AsyncStorage for JWT tokens, they are readable by any app on a rooted device.","m":"15"}],
   "learn":[
    {"t":"FrontendMasters (Student Pack): watch 'Complete Intro to React Native v3' Chapters 1-3. 90 minutes total. Do not just watch — type every example they write. Understanding StyleSheet.create, View, Text, TouchableOpacity, and flexbox from practice (not reading) is the difference between getting stuck and building fast.","m":"90"},
    {"t":"Read: docs.expo.dev/router/introduction (20 min). Then: docs.expo.dev/router/layouts (20 min). Draw a diagram of your app's navigation tree on paper: (auth)/welcome, (auth)/login, (auth)/onboarding, (app)/vault/index, (app)/vault/add, (app)/generate/index, (app)/generate/result, (app)/linkedin/index, (app)/profile/index. This diagram prevents navigation bugs.","m":"40"}]},

  {"d":10,"name":"Day 10","title":"Auth Hook + Welcome + Login Screens",
   "dev":[
    {"t":"Create src/hooks/useAuth.ts: full React Context providing user, profile, session, loading, error, signIn, signUp, signOut. Use supabase.auth.onAuthStateChange as the reactive listener. When user logs in: fetch their profile from profiles table. Export both the context and a useAuth() hook. This is the central state for your entire app.","m":"75"},
    {"t":"Create app/_layout.tsx: wrap Stack navigator with AuthProvider. Load Syne Bold and DM Sans fonts. Show splash screen until both fonts loaded AND auth state resolved. This prevents the flash of unstyled content on first load.","m":"30"},
    {"t":"Create app/(auth)/welcome.tsx: navy full-screen background, V logo (gold circle 80px), 'Vaulty' in Syne ExtraBold 40px white, tagline in gold 16px, Get Started button (full width, gold bg, navy text), Sign In text link. Run on phone — it should look exactly like a real app.","m":"45"},
    {"t":"Create app/(auth)/login.tsx: React Hook Form + Zod. Fields: email (valid email), password (min 8 chars), confirm password (signup mode only, must match). Show/hide toggle on password. Connect to Supabase: signInWithPassword for login, signUp for registration. Inline error messages below each field. router.replace navigation after success.","m":"75"}],
   "gstack":[
    {"t":"[GSTACK /review] After creating useAuth.ts and login.tsx: run /review on both files. The auth hook is the most security-sensitive file in your codebase. The skill will check: session persistence across app restarts, race conditions in the auth state listener, missing loading states that cause navigation flickers, profile fetch error handling.","m":"30"}],
   "security":[
    {"t":"[SECURITY] In useAuth.ts: never log the user object or JWT to console. Add: if(__DEV__) console.log only for non-sensitive auth events like 'Auth state changed: signed_in'. Production builds should have zero auth-related console logs. Console logs in React Native are visible to anyone with the device.","m":"10"},
    {"t":"[SECURITY] In login.tsx: implement a simple brute force protection: track failed login attempts in local state. After 5 failures: disable the login button for 30 seconds. Show: 'Too many attempts. Try again in 30s.' This prevents automated credential stuffing attacks.","m":"20"}],
   "learn":[
    {"t":"YouTube: search 'React Context API complete tutorial' → watch 25-minute comprehensive video. Then practice: build a simple ThemeContext from scratch in a test file (toggles between dark/light, provides colors to child components). When you can build a context from memory without looking at examples, you understand it.","m":"45"},
    {"t":"Read: reactnative.dev/docs/security (full page, 30 min). This is the official React Native security guide. It covers: secure storage, authentication, network security, SSL pinning, and obfuscation. Read it fully — it directly applies to Vaulty.","m":"30"}]},

  {"d":11,"name":"Day 11","title":"Onboarding + LinkedIn OAuth",
   "dev":[
    {"t":"Create app/(auth)/onboarding.tsx: 3 steps with animated progress dots. Step 1: name input (autofocus, min 2 chars). Step 2: university input + year picker (horizontal chips). Step 3: target field grid (2 columns). Animate between steps with a left-to-right slide. On Step 3 confirm: update Supabase profile, set onboarding_completed=true, router.replace to vault.","m":"90"},
    {"t":"Set up LinkedIn OAuth: create LinkedIn Developer App at developer.linkedin.com. Enable 'Sign In with LinkedIn using OpenID Connect'. Configure in Supabase Auth → Providers → LinkedIn OIDC. Add 'Continue with LinkedIn' button to login.tsx. Handler: supabase.auth.signInWithOAuth({provider:'linkedin_oidc'}). Handle redirect with expo-linking. Test on Android.","m":"90"}],
   "gstack":[
    {"t":"[GSTACK /design-review] Run the Expo web version of your app: npx expo start --web. Then run: /design-review with the local URL. The skill opens a browser, evaluates your auth screens visually, flags: spacing inconsistencies, color contrast issues (accessibility), typography hierarchy problems, AI-generated-looking generic UI. Fix every HIGH visual issue before proceeding.","m":"45"}],
   "security":[
    {"t":"[SECURITY] LinkedIn OAuth security: verify your LinkedIn app has the correct redirect URI (your Supabase auth callback URL). Wrong redirect URIs are a common OAuth misconfiguration that enables redirect attacks. In LinkedIn Developer Portal → Auth → OAuth 2.0 settings → verify redirect URL exactly matches what Supabase expects.","m":"15"},
    {"t":"[SECURITY] Add app.json scheme: 'vaulty' as a deep link scheme. This is used for OAuth redirects. Verify no other app on the device uses the same scheme (common scheme collisions are a security risk). Also set android.intentFilters correctly so only your app handles vaulty:// links.","m":"10"}],
   "learn":[
    {"t":"YouTube: search 'OAuth 2.0 and OpenID Connect full tutorial' → watch 30-minute complete video (not the 7-minute overview). The difference: OAuth 2.0 = authorization (what you can access), OpenID Connect = authentication (who you are). LinkedIn Sign In uses OIDC. Understanding this prevents auth security bugs.","m":"30"},
    {"t":"Read: docs.expo.dev/guides/linking (20 min). Deep links in Expo (the vaulty:// scheme) power your LinkedIn OAuth callback. If you do not configure them correctly, users who tap 'Sign in with LinkedIn' on iOS will get stuck in the browser. Read this before testing OAuth.","m":"20"}]},

  {"d":12,"name":"Day 12","title":"Test Auth + Navigation + QA",
   "dev":[
    {"t":"Test the complete auth flow 5 times on your phone: welcome → sign up → onboarding 3 steps → arrive at empty vault. Each run: verify in Supabase that the profiles table shows the new user with all 3 onboarding fields. Fix any run that fails before proceeding.","m":"45"},
    {"t":"Create the tab navigator in app/(app)/_layout.tsx: 4 tabs (Vault, Generate, LinkedIn, Profile). Add placeholder screens for Generate, LinkedIn, and Profile. Style the tab bar with Vaulty colors (navy active color, gold indicator). The app should now look like a complete app shell even with empty tabs.","m":"45"},
    {"t":"Create app/index.tsx: checks auth state → if logged in and onboarding_completed: router.replace vault → if logged in and not onboarding_completed: router.replace onboarding → if not logged in: router.replace welcome. This is the app's entry point. Test: close and reopen the app while logged in — it should go straight to vault.","m":"20"}],
   "gstack":[
    {"t":"[GSTACK /qa] Run the Expo web version: npx expo start --web. Then run: /qa. The skill opens a real Chromium browser, goes to your app URL, and tests: landing on welcome screen, tapping Get Started, filling the signup form, completing onboarding, arriving at vault. It catches: forms that don't submit, navigation that breaks, error states that don't show, console errors during auth. Fix everything before the Vault phase.","m":"45"},
    {"t":"[GSTACK /retro] After completing auth: run /retro and describe Phase 1 + 2 progress. The skill asks you structured questions: what went slower than expected, what security assumptions turned out to be wrong, what technical debt was introduced. The retro output becomes your improvement plan for Phase 3.","m":"20"}],
   "security":[
    {"t":"[SECURITY] Test session persistence: log in → force-close the app → reopen → you should still be logged in without entering credentials again. Then: log out → verify supabase.auth.signOut() cleared the SecureStore session token (check by running supabase.auth.getSession() — should return null). Any session that survives a logout is a security bug.","m":"20"}],
   "learn":[
    {"t":"FrontendMasters React Native: watch Chapters 4 and 5. Focus on: flexbox in React Native (number-based flex values, not CSS percentages), StyleSheet.create vs inline styles (performance), Platform.OS for conditional styling. After watching: make one screen in your app look correctly on both iPhone SE (375px wide) and a large Android (430px wide).","m":"90"},
    {"t":"Read: reactnative.dev/docs/navigation (20 min). Specifically understand: why expo-router uses file-based navigation (less configuration, better TypeScript), the difference between Stack and Tab navigators, how to pass parameters between screens using useLocalSearchParams. Draw your navigation tree and verify every route is correct.","m":"20"}]}
 ]},


{"ph":3,"title":"The Vault — Achievement Database + PDF Import","duration":"5 days",
 "goal":"Add an achievement on phone. Import a real CV via PDF. Vault shows real data. /qa passes all vault flows.",
 "days":[
  {"d":13,"name":"Day 13","title":"Achievement Service + Plan Review",
   "dev":[
    {"t":"Create src/hooks/useAchievements.ts: wraps achievements.service.ts with React state (achievements array, loading, error). add/update/delete functions update local state optimistically — no re-fetch after mutations. This makes the UI feel instant even on slow connections.","m":"45"},
    {"t":"Create all reusable UI components needed for the vault: src/components/ui/Button.tsx (5 variants: primary/secondary/outlined/ghost/danger), src/components/ui/Card.tsx, src/components/ui/Input.tsx (with error state), src/components/ui/EmptyState.tsx (icon + title + subtitle + optional CTA), src/components/ui/LoadingSkeleton.tsx (grey animated placeholder cards).","m":"90"}],
   "gstack":[
    {"t":"[GSTACK /plan-eng-review] Before building the vault screens: run /plan-eng-review and describe your achievement data model and the vault UI flow. The skill will verify: is the useAchievements hook correctly handling optimistic updates, are there race conditions when add and delete are called simultaneously, is the FlatList using correct key extraction to prevent rendering bugs. Take notes on every concern raised.","m":"35"},
    {"t":"[GSTACK /plan-design-review] Run /plan-design-review on your vault screen wireframe (describe it verbally: FlatList of achievement cards, filter chips, stat cards, FAB button). The skill checks: empty state when vault is empty (what does the user see?), loading state during fetch (skeleton or spinner?), error state if fetch fails, what happens when achievements list is very long (100+ items).","m":"30"}],
   "security":[
    {"t":"[SECURITY] In useAchievements.ts: add an ownership check before every mutation. Example: before updateAchievement(id), first fetch the achievement and verify its user_id matches the current user. This is redundant with RLS but necessary — defense in depth means multiple layers, not trust in a single layer.","m":"15"}],
   "learn":[
    {"t":"Read: reactnative.dev/docs/optimistic-updates-with-zustand (if using Zustand) OR read the general concept: medium.com search 'optimistic UI updates React'. Optimistic updates show the result before the server confirms it (then roll back on error). Your vault should feel instant — an achievement should appear immediately when added, not wait for the Supabase round-trip.","m":"25"},
    {"t":"Read: reactnative.dev/docs/flatlist (complete page, 25 min). Focus on: windowSize prop (render only visible items for performance), removeClippedSubviews (memory optimization for long lists), getItemLayout (pre-calculate item heights for instant scroll). Apply all 3 props to your vault FlatList.","m":"25"}]},

  {"d":14,"name":"Day 14","title":"Add Achievement Form",
   "dev":[
    {"t":"Create app/(app)/vault/add.tsx. Section 1: Title text input (autofocus, placeholder 'e.g. Led marketing for TEDx event'). Section 2: 14-type picker as 2-column card grid (emoji + label + colored border on selected). This is the most important UI in the app — the easier it is to add an achievement, the more users will actually use the vault.","m":"90"},
    {"t":"Add form sections: organization input, date pickers (month+year chips), is_current toggle, description textarea (500 char limit + counter), impact input ('Quantify if possible'). Add skills tag input: type → Enter/comma → removable chip. Same for tools. Add career tags multi-select (CAREER_TAGS in searchable modal). Save button in header (disabled until title + type filled).","m":"90"}],
   "gstack":[
    {"t":"[GSTACK /review] After building the add form: run /review on app/(app)/vault/add.tsx. This is a complex form with many interactions. The skill checks: forms that could submit with empty data (validation bypass), uncontrolled inputs that lose state on re-render, scroll behavior that hides the focused input behind the keyboard, modal state that persists when the user navigates away.","m":"30"}],
   "security":[
    {"t":"[SECURITY] Input sanitization in the add form: strip HTML tags from all text inputs before saving to Supabase. A user entering '<script>alert(1)</script>' as an achievement title should store the plain text, not executable HTML. Install: npm install dompurify OR write a simple stripHtml(text) function that removes < and > characters.","m":"20"}],
   "learn":[
    {"t":"YouTube: search 'React Hook Form advanced patterns' → watch 25-minute video. Specifically learn: watch() for reactive form values (used for the char counter), setValue() for programmatic field updates (used when importing from PDF), reset() for clearing the form after save, Controller component for custom inputs like your chip selectors.","m":"25"},
    {"t":"Read: reactnative.dev/docs/keyboard (15 min). Read: reactnative.dev/docs/keyboardavoidingview (10 min). Your add achievement form has 8+ inputs. Without KeyboardAvoidingView configured correctly, the keyboard will cover the focused field. Test every input by tapping it and verifying the field is visible above the keyboard. On iPhone and Android separately.","m":"25"}]},

  {"d":15,"name":"Day 15","title":"Vault Dashboard",
   "dev":[
    {"t":"Create app/(app)/vault/index.tsx. States: loading (LoadingSkeleton cards), empty (EmptyState with 'Add Your First Achievement' CTA), data (FlatList of AchievementCard). Pull-to-refresh. Type filter chips (horizontal ScrollView, 'All' + one per type user has). Stats bar (horizontal scroll: 4 stat cards fetched from Supabase count queries).","m":"60"},
    {"t":"Create src/components/achievement/AchievementCard.tsx: 3px left border (achievement type color from theme), title (2-line max, Syne Medium), org + date range (gray, DM Sans), skill chips (max 3 visible + '+X more'). Press → bottom sheet with full details. Long press → quick actions (Edit, Delete). The card is the most-seen component in the app — polish it.","m":"60"},
    {"t":"Create the bottom sheet for achievement details: shows all fields, Edit and Delete buttons. Delete triggers a confirmation alert before calling deleteAchievement. After deletion: achievement disappears from FlatList immediately (optimistic update) then Supabase delete confirms asynchronously.","m":"30"}],
   "gstack":[
    {"t":"[GSTACK /design-review] Run the web version and use /design-review on the vault dashboard. The skill evaluates: is the empty state compelling enough to make users want to add their first achievement, do the stat cards tell a meaningful story, is the filter chip behavior intuitive, do achievement cards communicate enough information at a glance. Fix every HIGH visual issue.","m":"35"}],
   "security":[],
   "learn":[
    {"t":"Read: supabase.com/docs/reference/javascript/count (10 min). Your stats bar uses 4 count queries. Instead of 4 separate queries (4 round trips), learn to combine them with a single RPC call or multiple columns in one query. This reduces your API calls from 4 to 1 on every vault load — significant on mobile.","m":"20"},
    {"t":"Watch: 'React Native performance profiling' on YouTube → 20-minute tutorial on using the Flipper performance profiler or React DevTools profiler. After watching: profile your vault screen load. How long does it take from navigation to first meaningful content? Target: under 500ms. If slower, find the bottleneck.","m":"20"}]},

  {"d":16,"name":"Day 16","title":"PDF Extraction Backend + Frontend",
   "dev":[
    {"t":"Verify your edge function's extract_pdf handler works correctly with Gemini's native PDF reading. The Gemini call uses: model.generateContent([{inlineData:{data:base64Pdf, mimeType:'application/pdf'}}, extractionPrompt]). The extraction prompt must end with: 'Respond ONLY with the JSON array. No other text.' Test: send your own CV encoded as base64. Verify: clean JSON array returned.","m":"45"},
    {"t":"Add expo-document-picker and expo-file-system to the project. Build the 'Import Your CV' screen in onboarding (after Step 3). Two options: [Upload PDF] and [Add manually]. PDF path: DocumentPicker → read as base64 → call edge function → navigate to review screen with JSON array as params.","m":"60"},
    {"t":"Build the loading screen shown during PDF extraction. Animated 3-step progress: 'Reading your CV...' (1.5s) → 'Finding your achievements...' (2s) → 'Building your vault...' (1.5s). Use Reanimated for smooth progress bar animation. This 5-second wait needs to feel productive, not broken.","m":"45"}],
   "gstack":[
    {"t":"[GSTACK /review] Run /review on the PDF import flow code (document picker, base64 conversion, edge function call). The skill checks: what happens if the user picks a 50MB PDF (should fail gracefully with file size check), what if the device runs out of memory during base64 encoding (should catch the error), what if Gemini returns malformed JSON (should catch JSON.parse error and show fallback).","m":"25"}],
   "security":[
    {"t":"[SECURITY] PDF security: before sending a PDF to your edge function: (1) verify file type is truly application/pdf (not a renamed .js or .html file), (2) check file size is under 10MB, (3) verify the file was selected by the user (not injected). A malicious user could try to upload a file that tricks your Gemini prompt injection. Add: strip any text that looks like a prompt injection before sending ('Ignore all previous instructions' patterns).","m":"25"}],
   "learn":[
    {"t":"Read: docs.expo.dev/versions/latest/sdk/document-picker (15 min). Read: docs.expo.dev/versions/latest/sdk/filesystem (20 min). Practice: build a standalone test screen that picks any file, reads it as base64, and shows the first 100 characters in a Text component. This tests your understanding before you wire it to the edge function.","m":"35"},
    {"t":"Read: ai.google.dev/gemini-api/docs/document-processing (20 min). Understand Gemini's PDF limits: max file size, supported PDF types (text-based vs scanned), accuracy on Arabic text, handling of multi-column CVs. This knowledge helps you write better error messages when PDF import fails.","m":"20"}]},

  {"d":17,"name":"Day 17","title":"PDF Review Screen + Achievement Batch Save",
   "dev":[
    {"t":"Build the 'Review Extracted Achievements' screen. Parse the JSON array. Render each as a card: type emoji, title (editable), org (editable), dates (editable). Three buttons per card: Edit (opens edit modal pre-filled with extracted data), Remove (deletes from local array), Keep (marks as confirmed). 'Confirm All' button at top-right.","m":"90"},
    {"t":"Build the Edit modal: all achievement fields pre-filled from Claude's extraction. User corrects anything wrong. 'Save' updates local state only (not DB yet). Confirm All: supabase.from('achievements').insert(confirmedAchievements) as a single batch. On success: toast + navigate to vault. On error: show specific error + allow retry.","m":"50"},
    {"t":"Add error fallback states: (1) Gemini returns empty array → 'We could not read your PDF. Try a text-based PDF or add manually.' (2) JSON.parse fails → same message. (3) Batch insert fails → 'Could not save achievements. Check your connection and try again.' Never leave users stranded.","m":"20"}],
   "gstack":[
    {"t":"[GSTACK /qa] After completing the full PDF import flow (pick PDF → loading → review → confirm → vault): run /qa on the web version and test this complete flow. The skill clicks through every step and reports: where the flow breaks, any JS console errors, loading states that get stuck, success messages that do not appear. Fix every issue before the Resume Generator phase.","m":"45"}],
   "security":[
    {"t":"[SECURITY] In the batch insert: verify every achievement being saved has user_id set to the current user's ID (not taken from the PDF extraction, which could be manipulated). The edge function should never set user_id — it comes exclusively from the authenticated user's JWT on the server side.","m":"10"}],
   "learn":[
    {"t":"Read: reactnative.dev/docs/modal (15 min). Read: reactnative.dev/docs/pressable (10 min). Then practice: build a reusable ConfirmModal component that accepts title, message, onConfirm, onCancel props. You will use this pattern for Delete confirmation, Sign Out confirmation, and Delete Account confirmation. Build it once, use it everywhere.","m":"35"},
    {"t":"FrontendMasters React Native: watch Chapters 6 and 7. Focus on controlled vs uncontrolled inputs, form state management in modals, and how to pre-fill inputs from external data (the PDF extraction pre-fill pattern). After watching: can you build a pre-filled edit form from memory?","m":"90"}]}
 ]},


{"ph":4,"title":"Resume Generator — AI-Powered Tailoring","duration":"3 days",
 "goal":"Paste a job description, get a real resume from vault data, export as PDF. /review and /qa pass all generation flows.",
 "days":[
  {"d":18,"name":"Day 18","title":"Resume Service + Generate Screen",
   "dev":[
    {"t":"Create app/(app)/generate/index.tsx. Inputs: optional job title, optional company name, large JD textarea (min height 200px, character count shown). Vault summary widget: 'X achievements ready' with type badges. Gate: disable generate if <3 achievements OR JD <100 chars with specific helper text. 'Generate Resume' button full width.","m":"60"},
    {"t":"Wire the generate button: tap → disable button + show loading state → call resume.service.ts generateResume() → on success navigate to result screen with resume_request_id → on failure show error toast with specific message + stay on screen (preserving the JD the user typed).","m":"30"},
    {"t":"Build the 3-step loading animation. useState(0) for step. useEffect with setInterval(1800ms) to advance. Messages: 'Analyzing your vault...' → 'Matching to the role...' → 'Writing your resume...'. A subtle progress indicator below. Reanimated FadeIn/FadeOut between messages.","m":"35"}],
   "gstack":[
    {"t":"[GSTACK /plan-eng-review] Before wiring the AI: run /plan-eng-review on the resume generation flow. Describe: how achievements are fetched, how the prompt is built, how the JSON is parsed, how errors from Gemini are handled. The skill checks: what happens if Gemini times out (Supabase edge functions have a 150s limit), what if the JSON response is malformed, what if the user has 100+ achievements (prompt token limit).","m":"30"}],
   "security":[
    {"t":"[SECURITY] The JD input is sent to Gemini. Add prompt injection detection: check the JD for common injection patterns ('ignore previous instructions', 'system:', 'you are now'). If detected: sanitize by treating the entire JD as literal text (wrap in triple quotes and instruct Gemini to treat it as user data only). This prevents users from hijacking your resume generation prompt.","m":"25"}],
   "learn":[
    {"t":"Read your resume generation prompt from the build spec end-to-end. Then search: 'resume ATS optimization guide 2024' and read the top result. Ask: does your prompt enforce everything the guide recommends? Add any missing rules to the prompt. Your prompt quality IS your product quality — spend 45 minutes improving it.","m":"45"},
    {"t":"Read: supabase.com/docs/guides/functions/limits (10 min). Supabase Edge Functions have limits: 150-second timeout, 512MB memory, 500KB request size. With large achievement lists and long JDs, you could hit these. Plan: limit achievements sent to Gemini to the 15 most recent (not all), truncate JD at 3000 characters if longer.","m":"15"}]},

  {"d":19,"name":"Day 19","title":"Resume Result Screen + PDF Export",
   "dev":[
    {"t":"Create app/(app)/generate/result.tsx. Fetch resume_request by ID. Match score circle (filled arc, green 8-10/gold 5-7/red 0-4). Keywords covered (green horizontal chips). Keywords missing (red chips). Improvement suggestion (amber callout). Full resume text (white card, formatted: ALL CAPS → bold headers, bullets indented). Copy button (full width outlined).","m":"75"},
    {"t":"Create src/services/pdf.service.ts. exportResumeToPDF(text, name): convert to A4 HTML with professional CSS (18mm margins, navy headings, Georgia 10pt body, consistent line-height). Use Print.printToFileAsync({html}) to generate PDF. Use Sharing.shareAsync(uri) to open share sheet. Test: generate → export → open PDF → verify it looks like a real professional resume.","m":"60"},
    {"t":"Add 'Recent Resumes' section to generate/index.tsx: last 3 resume_requests as compact cards (job title, match score badge, date). Tap → navigate to that result screen. Add upgrade prompt after 2nd generation: modal with 80 EGP/month offer, track upgrade_clicked in Posthog.","m":"30"}],
   "gstack":[
    {"t":"[GSTACK /review] After result.tsx and pdf.service.ts are complete: run /review on both. The skill specifically checks the PDF CSS for: content that breaks across pages awkwardly, fonts that don't render in PDF context, margins that produce unprintable areas. It also checks the result screen for: circular match score rendering across screen sizes, chip overflow handling when there are 20+ keywords.","m":"35"},
    {"t":"[GSTACK /design-review] Run /design-review on the resume result screen (web version). The skill evaluates this as a designer would: is the match score visually prominent enough, does the resume text maintain adequate line spacing for readability, is the PDF export button clear enough. This screen is the 'aha moment' of Vaulty — it must look and feel great.","m":"30"}],
   "security":[],
   "learn":[
    {"t":"Read: developer.mozilla.org/en-US/docs/Web/CSS/CSS_Paged_Media (20 min). This is the CSS specification for print/PDF styling. Key properties: @page for margins, page-break-before/after/inside for controlling page breaks, orphans/widows for preventing single-line paragraphs at page boundaries. Apply these to your PDF HTML template.","m":"20"},
    {"t":"Watch: 'Understanding JSON Web Tokens' on YouTube → 15-minute thorough explanation. After watching: trace the JWT through your Vaulty app: created on signup → stored in SecureStore → attached to every Supabase request → verified server-side by RLS → expired after 24 hours → refreshed by Supabase client automatically. Can you trace this path without notes?","m":"15"}]},

  {"d":20,"name":"Day 20","title":"Test + Polish Resume Feature",
   "dev":[
    {"t":"Test resume generation with 5 different real job descriptions across 5 different fields: tech, marketing, business, engineering, consulting. For each: evaluate the output against your Resume Quality Checklist from Phase 0. How many criteria does each pass? If any fails fewer than 10/15 criteria: update the Gemini prompt and retest. Do not move to LinkedIn generator until the output consistently passes your checklist.","m":"90"},
    {"t":"Add robustness to the generate flow: (1) if Gemini response has no 'resume' key → fallback message. (2) if match_score is missing or NaN → show score as '--/10'. (3) if keywords arrays are empty → hide those sections gracefully. (4) if PDF generation fails → show 'PDF export unavailable. Use Copy instead.' Never crash on an unexpected Gemini response format.","m":"45"}],
   "gstack":[
    {"t":"[GSTACK /qa] Run /qa on the complete resume generation flow on the web version. The skill tests: (1) entering a JD with fewer than 100 characters (button should stay disabled), (2) entering a valid JD and generating (should complete within 30 seconds), (3) clicking Export PDF (should trigger download on web), (4) clicking Copy (should copy text to clipboard), (5) navigating back and viewing recent resumes. Fix every failure.","m":"45"}],
   "security":[
    {"t":"[SECURITY] The generated resume is stored in resume_requests table. Verify via SQL that a user cannot SELECT another user's resumes: use two test accounts, generate resumes with Account A, try to fetch them authenticated as Account B. Should return empty. The resume contains career achievements — a data leak here exposes private career information.","m":"15"}],
   "learn":[
    {"t":"Deep practice: take your 5 test resume outputs and manually critique each one. For every weakness you find: trace it back to a specific instruction in your prompt that is missing or unclear. Add that instruction. This prompt iteration process IS the core product engineering of Vaulty — the better your prompt, the better your product.","m":"60"}]}
 ]},


{"ph":5,"title":"LinkedIn Generator + Profile + Analytics","duration":"4 days",
 "goal":"All 3 MVP features working. Posthog tracking 6 events. Profile screen complete.",
 "days":[
  {"d":21,"name":"Day 21","title":"LinkedIn Generator",
   "dev":[
    {"t":"LinkedIn generator screen: achievement picker (horizontal scroll, compact cards, selected gets gold border), Generate Post button, loading state, post preview card (LinkedIn-style, character count), Copy Post button, Regenerate button, Recent Posts section (last 5). Wire to linkedin.service.ts which calls the edge function 'linkedin' handler.","m":"90"},
    {"t":"Profile screen app/(app)/profile/index.tsx: avatar circle (first letter, navy bg, gold text, 60px), name Syne Bold, university + year gray, target field badge. Stats grid 2x2 (achievements, resumes, posts, skills). Sign Out with confirmation. 'Import from LinkedIn' secondary option. Settings section with Delete Account (leads to Phase 7 implementation).","m":"60"},
    {"t":"Add 'linkedin' CSV import: instructions screen (step-by-step LinkedIn export path), DocumentPicker for ZIP, CSV parser for Positions.csv + Education.csv + Skills.csv, map to achievement schema, show same review screen. This reuses the review screen component built for PDF import.","m":"45"}],
   "gstack":[
    {"t":"[GSTACK /review] Run /review on linkedin.service.ts and the LinkedIn generator screen. The skill checks: what happens when a user generates a post for an achievement with very little data (empty description, no impact, no skills) — the output quality should degrade gracefully with a message rather than generate a poor post. Fix this edge case.","m":"25"},
    {"t":"[GSTACK /design-review] Run /design-review on both the LinkedIn generator and profile screens. The LinkedIn post preview card is particularly important — it must look like a real LinkedIn post. The skill flags any UI that looks generic or AI-generated. Fix all HIGH visual issues.","m":"30"}],
   "security":[],
   "learn":[
    {"t":"Read the LinkedIn post prompt from the build spec end-to-end. Search: 'LinkedIn algorithm 2025 what gets reach' and read the top article. Ask: does your prompt encode these principles? Specifically: hooks that generate comments (not just likes), length that maximizes dwell time (100-180 words), ending with a specific call to engagement. Update the prompt accordingly.","m":"30"},
    {"t":"FrontendMasters: watch final chapters of React Native course. Focus on: complex FlatList patterns (nested horizontal FlatLists for the achievement picker), Modal animations, tab bar customization. After each chapter: verify you could implement it from memory.","m":"75"}]},

  {"d":22,"name":"Day 22","title":"Posthog Integration + Analytics",
   "dev":[
    {"t":"Install posthog-react-native. Add PostHogProvider to app/_layout.tsx with your project key. Track exactly 6 events: achievement_added (with type + source), resume_generated (with match_score + count), linkedin_post_generated (with achievement_type), upgrade_prompt_shown, upgrade_clicked, pdf_exported. Use posthog.identify() on login to link events to users.","m":"45"},
    {"t":"In Posthog dashboard: create a Funnel: achievement_added → resume_generated → pdf_exported. Create a Retention chart starting with achievement_added. Create a Dashboard showing: DAU, weekly active users, most-used feature (events count by type), upgrade click rate. Save these — they are your weekly health metrics.","m":"30"},
    {"t":"Add app performance tracking: log resume generation time (start timer on button press, stop on result screen load), PDF extraction time, edge function response time. Track these as Posthog properties on each event. Slow generation is your #1 user experience risk.","m":"25"}],
   "gstack":[],
   "security":[
    {"t":"[SECURITY] Posthog data privacy: verify you are NOT sending personally identifiable information in event properties. Acceptable: achievement_type, match_score, count, duration. Not acceptable: achievement_title, user email, university name. In the Posthog dashboard, review every captured property and remove any that are PII.","m":"15"}],
   "learn":[
    {"t":"Read: posthog.com/docs/product-analytics/funnels (20 min). Read: posthog.com/docs/product-analytics/retention (20 min). Read: posthog.com/docs/surveys (10 min). The surveys feature lets you ask in-app questions to users — use this in beta to ask 'How useful was this resume? 1-5' immediately after generation. This automated feedback collection replaces manual WhatsApp questions.","m":"50"},
    {"t":"Read: posthog.com/docs/privacy (15 min). Understand: GDPR compliance requirements for analytics, how to anonymize user IDs in Posthog, how to handle data deletion requests (when a user deletes their account, their Posthog data should also be deleted via the Posthog API). Implement delete_user_data() in your delete account flow.","m":"15"}]},

  {"d":23,"name":"Day 23","title":"Full Polish Pass — Loading, Error, Empty States",
   "dev":[
    {"t":"Audit every screen systematically: for each screen, identify every async operation. For every async operation: add loading state (spinner on button press, skeleton on fetch). For every failure mode: add error state (specific message, retry option). For every empty list: add EmptyState component. Never show a blank white screen. Never show a generic 'Something went wrong'.","m":"90"},
    {"t":"Add KeyboardAvoidingView to all form screens (behavior='padding' iOS, 'height' Android). Test every input by tapping it — zero inputs should be hidden behind the keyboard. Add expo-haptics: impactAsync(Heavy) when achievement saves, notificationAsync(Success) when resume generates. These micro-interactions signal success to users with tactile feedback.","m":"30"},
    {"t":"Add pull-to-refresh to vault screen and recent resumes list. Add ScrollView keyboardDismissMode='on-drag' to all scrollable screens (tapping off a keyboard should dismiss it). Add accessibility labels to all interactive elements (accessibilityLabel prop on every Button and TouchableOpacity). These improve app store rating.","m":"25"}],
   "gstack":[
    {"t":"[GSTACK /design-review] Run /design-review on the complete app (all screens) after polish. This is the final visual quality gate before beta. The skill checks everything: consistent spacing (8px grid), consistent border radius, color contrast ratios for accessibility, typography scale consistency, interaction states (pressed, disabled, loading) on every button. Treat this like a senior designer's review before launch.","m":"60"}],
   "security":[],
   "learn":[
    {"t":"Read: nngroup.com/articles/response-times-3-important-limits (10 min). The 3 important response time limits: 0.1 second = feels instant, 1 second = noticeable but OK, 10 seconds = loses attention. Categorize your app's operations by these limits. Resume generation (5-10s) needs the loading animation to bridge the gap. Achievement save (<0.5s) should feel instant via optimistic updates.","m":"15"},
    {"t":"Read: docs.expo.dev/guides/accessibility (25 min). Accessibility is an App Store rating factor and affects real users. Implement: accessibilityLabel on all interactive elements, accessibilityHint for non-obvious actions, accessibilityRole for custom components. Use the Expo Go accessibility inspector to verify your implementation.","m":"25"}]},

  {"d":24,"name":"Day 24","title":"Performance + QA Pass",
   "dev":[
    {"t":"Performance audit: use React DevTools profiler to identify components that re-render unnecessarily. Add React.memo() to AchievementCard (it renders in a FlatList — unnecessary re-renders here lag the entire scroll). Add useMemo() for expensive computations (filtering the achievements list). Add useCallback() for event handlers passed to child components.","m":"45"},
    {"t":"Cross-device test: BrowserStack (Student Pack) → upload APK → test on Samsung Galaxy S23 (Android 13), Samsung A34 (Android 12), older phone with Android 10. For each: run the complete flow (signup → add achievement → generate resume → export PDF). Document every visual issue in Notion Bug Tracker. Fix all Critical and High issues.","m":"60"}],
   "gstack":[
    {"t":"[GSTACK /benchmark] Run /benchmark to establish your app's performance baseline. The skill measures: FlatList scroll performance (target: 60fps), screen navigation time, edge function cold start time. Record these numbers as your baseline. Every future update should be checked against this baseline — performance regressions get caught before users feel them.","m":"30"},
    {"t":"[GSTACK /qa] Final QA run on all 3 MVP features simultaneously. The skill tests the complete user journey: sign up → complete onboarding → add 5 achievements manually → import a PDF → generate a resume → export PDF → generate LinkedIn post → view profile → sign out → sign in again → verify data persists. This is your acceptance test.","m":"45"}],
   "security":[],
   "learn":[
    {"t":"Read: reactnative.dev/docs/performance (full page, 30 min). The two most important concepts: the JS thread (where your React code runs) vs UI thread (where animations render). Heavy JS operations on the main thread drop frames. Solutions: move calculations to useMemo, use InteractionManager.runAfterInteractions for non-urgent work, use native driver for animations.","m":"30"},
    {"t":"Watch: 'React Native debugging tools' YouTube tutorial → 20 min. Learn to use: Flipper (performance profiler, network inspector, log viewer), Expo DevTools, React DevTools Chrome extension. Being able to profile your app means you find performance issues before your users do.","m":"20"}]}
 ]},


{"ph":6,"title":"Security Hardening + Full Audit","duration":"4 days",
 "goal":"OWASP Top 10 compliance verified. /cso report shows zero Critical or High issues. Data privacy checklist complete.",
 "days":[
  {"d":25,"name":"Day 25","title":"OWASP Mobile Audit with /cso",
   "dev":[
    {"t":"Before running /cso: prepare a security audit document in Notion with sections for each OWASP Mobile Top 10 item (M1-M10). For each: write what your current implementation does. Example: M1 (Credential Handling) → 'JWTs stored in expo-secure-store (hardware-encrypted)'. This self-audit prepares you to understand and act on /cso findings.","m":"45"},
    {"t":"Review your complete authentication implementation against the OWASP Authentication Cheat Sheet: password hashing (Supabase handles this), brute force protection (you added in Phase 2), session expiry (24hr JWT + refresh), account enumeration prevention (error messages should say 'Invalid credentials', not 'Email not found' — fix this if needed).","m":"30"}],
   "gstack":[
    {"t":"[GSTACK /cso] Run the full /cso audit. Describe your complete tech stack: React Native + Expo, Supabase (auth + DB + edge functions), Gemini API, Expo SecureStore, PDF processing. The skill runs OWASP + STRIDE analysis. It will generate a prioritized findings report. READ EVERY FINDING. You will spend the next 2 days fixing Critical and High findings. This is not optional.","m":"120"},
    {"t":"[GSTACK /plan-eng-review] After /cso: run /plan-eng-review specifically focused on the security fixes you need to implement. This validates that your planned fixes actually address the vulnerabilities identified by /cso — not just appear to address them.","m":"30"}],
   "security":[
    {"t":"[SECURITY AUDIT] Manually test each OWASP Mobile Top 10 item on your running app: M1: try accessing another user's achievement via direct API call with your JWT → should get empty. M4: try submitting a 100,000 character achievement description → should be rejected. M5: check all network calls go to HTTPS (no HTTP) in the network inspector. M9: try reading the Expo SecureStore on a rooted Android emulator.","m":"60"}],
   "learn":[
    {"t":"Read: cheatsheetseries.owasp.org/cheatsheets/Mobile_Application_Security_Cheat_Sheet.html (45 min). This is the comprehensive mobile security reference. After reading: compare every item to your current implementation. Create a checklist in Notion with your compliance status for each item.","m":"45"},
    {"t":"Read: gdpr.eu/checklist (20 min). Vaulty stores personal data about EU students (including Egyptian students studying abroad). Understanding GDPR basics — lawful basis for processing, right to erasure (you have this via delete account), data minimization — protects you from legal exposure. Your privacy policy must reflect these principles.","m":"20"}]},

  {"d":26,"name":"Day 26","title":"Fix Critical + High Security Findings",
   "dev":[
    {"t":"Work through every Critical and High finding from /cso in priority order. Common findings for this stack: (1) Missing authentication on edge function (add JWT verification — done in Phase 1), (2) No rate limiting on generation endpoint (add per-user rate limit), (3) Insufficient input validation length limits (add max lengths to all text inputs), (4) Missing Content-Security-Policy on web version (add headers).","m":"120"},
    {"t":"Implement any missing security headers in your edge function wrapper. Required headers: Strict-Transport-Security: max-age=31536000 (force HTTPS), X-Content-Type-Options: nosniff (prevent MIME sniffing), Referrer-Policy: strict-origin-when-cross-origin (control referrer data). Apply to every edge function response.","m":"30"}],
   "gstack":[
    {"t":"[GSTACK /review] After implementing security fixes: run /review on all modified files. Security fixes often introduce new bugs — a rate limiting implementation could accidentally block legitimate users, a validation fix could reject valid achievement descriptions. The review catches these regressions.","m":"30"}],
   "security":[
    {"t":"[SECURITY] Implement data minimization: audit every field you store. Do you actually need to store the full PDF in the achievements table? (No — extract and delete). Do you need to store the full job description in resume_requests? (Yes — for history). Do you need to store the full prompt sent to Gemini? (No — never store prompts). Delete any data you do not need.","m":"20"},
    {"t":"[SECURITY] Implement the Right to Erasure completely: your delete account function must (1) delete all achievements, (2) delete all resume_requests, (3) delete all linkedin_posts, (4) delete the profile, (5) delete the auth user, (6) call the Posthog API to delete user's analytics data, (7) sign out the device. Test with a throwaway account to verify all data is gone.","m":"30"}],
   "learn":[
    {"t":"Read: cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html (20 min). CSP prevents XSS attacks on your web version. Even though your app is primarily mobile, the web version (expo start --web) is accessible and should be secured. Add a CSP header to your Vercel deployment.","m":"20"},
    {"t":"Read: supabase.com/docs/guides/auth/row-level-security (advanced section — policies with functions, 25 min). Learn to create more sophisticated RLS policies: a policy that checks if a user's account is suspended (future feature), a policy that limits achievements to 500 per user (rate limiting at the database level), a policy that prevents users from modifying created_at timestamps.","m":"25"}]},

  {"d":27,"name":"Day 27","title":"Privacy Compliance + Security Documentation",
   "dev":[
    {"t":"Write the complete Privacy Policy at termly.io (free): data collected (email, name, university, career achievements, generated resumes), purpose of processing (career management), data storage (Supabase, encrypted at rest), data sharing (none — Gemini API processes but does not store), right to erasure (delete account feature), contact email. Publish at vaulty.me/privacy.","m":"45"},
    {"t":"Implement in-app privacy consent: on first signup, before profile creation, show a modal: 'By creating an account, you agree to our Privacy Policy [link] and Terms of Service [link]. Your career data is private and encrypted.' User must explicitly tap 'I Agree' to proceed. Log the consent timestamp to the profiles table (consent_given_at column).","m":"30"}],
   "gstack":[
    {"t":"[GSTACK /cso] Run /cso a second time, specifically focused on the fixes you implemented. The skill verifies: are the Critical and High issues resolved, did the fixes introduce new issues, are Medium issues still acceptable for beta launch. Get a clean /cso report showing zero Critical and zero High issues before proceeding to beta.","m":"45"},
    {"t":"[GSTACK /document-generate] Run /document-generate to create a Security Documentation file for your project. This documents: your threat model, the security controls implemented, known residual risks, and your security review history. Professional teams do this — it also helps when career centers or companies ask about data security.","m":"20"}],
   "security":[
    {"t":"[SECURITY] Create a responsible disclosure document: docs/SECURITY.md in your GitHub repo. Content: 'If you discover a security vulnerability in Vaulty, please email [your email]. We will respond within 48 hours. Please do not publicly disclose before we have a chance to fix it.' This is a professional security practice that also provides legal protection.","m":"15"}],
   "learn":[
    {"t":"Read: owasp.org/www-project-api-security/editions/2023/en/0x11-t10 (OWASP API Security Top 10, 30 min). Your edge functions are REST APIs. Common API security issues: Broken Object Level Authorization (prevented by your RLS + ownership checks), Unrestricted Resource Consumption (prevented by your rate limiting), Security Misconfiguration (review your Supabase settings). Check your implementation against each.","m":"30"},
    {"t":"Practice: write a security checklist in Notion that you will run before every APK release. Items: /cso shows no Critical/High, all inputs validated, all secrets in 1Password (not code), RLS tests pass, delete account works, privacy policy accessible. Run this checklist before beta and before production submission.","m":"20"}],
   "d":27},

  {"d":28,"name":"Day 28","title":"Security Retro + Final Pre-Beta Checklist",
   "dev":[
    {"t":"Run your pre-beta security checklist from yesterday. Each item: verify manually. Example: open your GitHub repo and search for 'sk-' or 'key' or 'password' — should find zero matches in code. Check Supabase settings: confirm RLS enabled on all tables, confirm email confirmation is on for new users, confirm Supabase project password is strong.","m":"30"},
    {"t":"Final integration test: delete a test user and verify ALL their data is gone from: profiles table, achievements table, resume_requests table, linkedin_posts table, Supabase Auth users. If any data remains: your delete function has a bug. Fix before beta — a data leak on account deletion is a severe privacy violation.","m":"30"}],
   "gstack":[
    {"t":"[GSTACK /retro] Run /retro on the security phase. Questions the skill asks: what security issues did /cso find that you would not have caught manually, what security decision did you make that you are uncertain about, what security work are you deferring to Phase 2. The retro output becomes your security roadmap for post-launch.","m":"20"}],
   "security":[
    {"t":"[SECURITY] Dependency audit: run npm audit in your Expo project. Fix all Critical and High severity vulnerabilities in your dependencies. Many security breaches come from outdated packages, not custom code. Run: npm audit fix for auto-fixable issues. For manual fixes: review the advisory and update the specific package.","m":"25"},
    {"t":"[SECURITY] Data retention policy: decide how long you keep resume_requests (generated resumes). Storing indefinitely creates a growing liability of user career data. Decision: delete resume_requests older than 90 days (users can regenerate). Create a Supabase scheduled function to run this cleanup weekly. Document this policy in your Privacy Policy.","m":"20"}],
   "learn":[
    {"t":"Read: 'The Security Development Lifecycle' introduction — microsoft.com/en-us/securityengineering/sdl/about (20 min). SDL is the practice of building security into every phase of development (which is exactly what you did in this plan). Understanding the framework helps you maintain this discipline in Phase 2 and beyond.","m":"20"},
    {"t":"Watch: 'OWASP ZAP Tutorial' on YouTube (15 min). ZAP is a free security scanner. Install and run it against your Expo web version URL. It will find issues automatically. Fix any HIGH severity findings. This is the same tool professional security teams use — you now know how to use it.","m":"15"}]}
 ]},


{"ph":7,"title":"Beta Testing — 30 Real Users","duration":"7 days",
 "goal":"APK in hands of 30 users. Day 7 retention measured. All 3 validation questions answered with real data.",
 "days":[
  {"d":29,"name":"Day 29","title":"EAS Build + Beta Distribution",
   "dev":[
    {"t":"Install EAS CLI: npm install -g eas-cli. Login: eas login. Configure: eas build:configure (select Android, preview profile). Build: eas build --platform android --profile preview. This builds in Expo's cloud — your laptop just waits. Takes 15-20 minutes. Download the APK and test install on 3 different Android phones before distributing.","m":"60"},
    {"t":"For iOS beta users: run npx expo start --tunnel. The QR code works with Expo Go over the internet (not just local WiFi). Share the QR screenshot with iOS users. Document in Notion Beta Users database: which of your 30 users are iOS vs Android.","m":"15"}],
   "gstack":[
    {"t":"[GSTACK /document-release] Before distributing the APK: run /document-release. This generates release notes that describe what is in this beta build, what has been tested, known limitations, and how to report bugs. Share these release notes with beta users — it sets expectations and reduces confused bug reports.","m":"20"}],
   "security":[
    {"t":"[SECURITY] Before distributing the APK: verify the APK is built with production keys (not debug keys). Debug APKs are less secure and should never be distributed to non-developers. In your EAS build configuration, confirm profile: preview uses appropriate signing. Also: verify your edge function URL in the app points to production (not localhost or staging).","m":"15"}],
   "learn":[
    {"t":"Read: docs.expo.dev/build/introduction (20 min). Understand the difference between development (internal testing with your phone), preview (APK for beta testers), and production (AAB for Google Play). You are in preview now, production comes in Phase 9. The key difference: production builds require a signed AAB and Play Store submission, preview is direct APK install.","m":"20"}]},

  {"d":30,"name":"Day 30","title":"Monitor Day 1 + First Bug Fixes",
   "dev":[
    {"t":"Check Sentry every 2 hours on Day 1 of beta. Any unhandled crash: read the full stack trace (Sentry shows you file + line number), fix the root cause, rebuild APK (eas build --platform android --profile preview), share updated link in beta WhatsApp group with a specific note: 'Updated — fixed [what you fixed].'","m":"60"},
    {"t":"Check Posthog Live Events: are you seeing achievement_added, resume_generated events from users who are not you? That confirms real users are inside the app. Note which events fire most (engagement) and which do not fire at all (features users are skipping).","m":"20"}],
   "gstack":[
    {"t":"[GSTACK /investigate] When a Sentry crash appears that you cannot diagnose quickly: run /investigate and describe the stack trace. The skill systematically works through possible causes and proposes specific fixes. Use this after 30 minutes of being stuck — not immediately, but do not spend more than 30 minutes alone on a crash.","m":"0"}],
   "security":[],
   "learn":[
    {"t":"Read: docs.sentry.io/platforms/react-native/configuration/options (20 min). Configure Sentry properly for beta: set environment='beta', release=your-app-version, beforeSend hook to strip PII from error reports (remove user email from breadcrumbs). Proper Sentry configuration means your error reports are useful without containing user privacy data.","m":"20"}]},

  {"d":31,"name":"Day 31","title":"Day 3 Retention Check",
   "dev":[
    {"t":"Open Posthog → Retention chart. Check the cohort from Day 1 of beta — what percentage came back on Day 3? Record in Notion Weekly Metrics. This is your most important product health metric. Target: 40%+. If below 20%: something fundamental is broken. Message every user who has not returned: 'Hey [name] — hope the install went smoothly. Did anything feel broken or confusing?'","m":"30"},
    {"t":"Message every beta user personally (not a broadcast) with 3 specific questions: (1) Does the resume feel like it was written about YOU specifically? Rate 1-5. (2) Would you submit it to a real company? (3) What was the most confusing part of the app? Record every answer in Notion Beta Users database.","m":"30"}],
   "gstack":[
    {"t":"[GSTACK /qa] After collecting first feedback: use /qa to specifically test the flows that users report as confusing. If users say 'I couldn't figure out how to add an achievement': run /qa on the vault add flow. The skill finds the UX gap — the place where a real user would get lost. Fix it and rebuild.","m":"30"}],
   "security":[],
   "learn":[
    {"t":"Read: andrewchen.com/new-data-on-mobile-app-retention (20 min). Industry mobile app retention benchmarks: Day 1: 25%, Day 7: 10%, Day 30: 5%. Vaulty's career use case should be above average because users have a strong motivation (job applications). If your Day 3 is below 25%, research what other career apps do differently for retention.","m":"20"}]},

  {"d":32,"name":"Day 32","title":"Critical Bug Fixes",
   "dev":[
    {"t":"Fix every Critical bug from Sentry and user reports. Fix every High severity bug that more than one user reported. Skip Medium and Low — they go in the backlog for Phase 8 polish. Rebuild and redistribute after every batch of fixes.","m":"120"},
    {"t":"Update Notion Bug Tracker: for each fixed bug, record the root cause and the fix. This builds institutional knowledge — 'why did we change this?' answers are critical when you add features that interact with fixed bugs later.","m":"20"}],
   "gstack":[
    {"t":"[GSTACK /review] After each batch of bug fixes: run /review on the changed files. Bug fixes are where new bugs get introduced (you fix one thing, break another). The review catches regressions before you redistribute the APK. A broken APK redistribution wastes beta users' time and damages trust.","m":"25"}],
   "security":[],
   "learn":[
    {"t":"Read: sentry.io/for/react-native (15 min). Explore Sentry features you may not be using: Performance Monitoring (tracks app startup time, navigation transitions), Session Replay (records user sessions that led to a crash — shows exactly what the user did), Release Health (tracks crash-free session rate by version). Enable these for more beta insights.","m":"15"}]},

  {"d":33,"name":"Day 33","title":"Set Up Datadog + Performance Monitoring",
   "dev":[
    {"t":"Claim Datadog Student Pack (2 years free Pro). Create account. Set up Synthetic Monitoring: API Test → enter your Supabase edge function URL → verify it responds in under 3 seconds → set alert if it goes down. Set up a second test: API Test → POST a test resume generation → verify response includes 'resume' key in under 10 seconds.","m":"45"},
    {"t":"Connect Posthog and Datadog: create a dashboard in Datadog showing: edge function average response time, error rate, and uptime alongside Posthog's DAU and resume_generated count. Seeing infrastructure health and user behavior together helps you correlate: slow edge function → fewer resumes generated.","m":"30"}],
   "gstack":[],
   "security":[],
   "learn":[
    {"t":"Read: docs.datadoghq.com/synthetics (20 min). Synthetic monitoring runs automated tests against your API from Datadog's global network — it simulates real user requests every 5 minutes. If your edge function goes down at 3am, Datadog pages you (via email or Slack). Set up at least one alert so production outages wake you up.","m":"20"}]},

  {"d":34,"name":"Day 34","title":"BrowserStack Device Testing",
   "dev":[
    {"t":"Login to BrowserStack Real Devices. Upload your APK. Test systematically on: Samsung Galaxy S23 (Android 13, high-end), Samsung Galaxy A34 (Android 13, mid-range, common in Egypt), Samsung Galaxy A12 (Android 11, older, very common in Egypt), old device with Android 10. For each: complete the full flow. Screenshot every visual issue.","m":"90"},
    {"t":"Fix the top 5 most impactful layout issues found in BrowserStack. Typical issues: text truncation on small screens, buttons below safe area on old Android, FlatList scroll performance on older hardware. These fixes make Vaulty work for the majority of Egyptian university students.","m":"60"}],
   "gstack":[
    {"t":"[GSTACK /design-review] After BrowserStack fixes: run /design-review one more time. BrowserStack testing often reveals visual issues that /design-review missed (because /design-review uses a standard browser, not old Android WebViews). The second review is faster and focused only on the fixes made.","m":"20"}],
   "security":[],
   "learn":[
    {"t":"Read: developer.android.com/guide/practices/security (25 min). Android-specific security practices: how Android's permission model works, why you should request only necessary permissions (Vaulty needs: INTERNET, READ_EXTERNAL_STORAGE for PDF picking — nothing else), how to configure network security config to prevent cleartext traffic.","m":"25"}]},

  {"d":35,"name":"Day 35","title":"Beta Retro + Feedback Synthesis",
   "dev":[
    {"t":"Compile all beta feedback from: Notion Beta Users database, WhatsApp group messages, Posthog event data, Sentry error counts, Datadog performance data. Create a synthesis document: top 5 positive reactions, top 5 negative reactions, top 5 feature requests, top 3 technical issues. This document guides what you build next.","m":"60"},
    {"t":"Answer the 3 validation questions in Notion Validation Scorecard with real numbers: (1) Day 7 retention % — actual number from Posthog. (2) Average resume quality rating — from direct user messages. (3) Upgrade click rate % — from Posthog upgrade_clicked events. These are your product PMF indicators.","m":"20"}],
   "gstack":[
    {"t":"[GSTACK /retro] Run a comprehensive /retro on the entire beta phase. The skill asks: what did users struggle with that you did not expect, what feature was ignored (and why), what technical decision caused the most bugs, what security issue came up that /cso did not catch. The retro output is your Phase 2 roadmap.","m":"30"}],
   "security":[],
   "learn":[
    {"t":"Read: leanstartup.co/principles (20 min) — specifically the Build-Measure-Learn cycle. You just completed one full cycle: Build (the app) → Measure (beta data) → Learn (retention, ratings, usage patterns). Your next cycle starts with what you learned. The key discipline: do not build based on what you think users want — build based on what the data says.","m":"20"}]}
 ]},


{"ph":8,"title":"App Store Preparation + Launch","duration":"5 days",
 "goal":"Privacy policy live. Delete account built. Production AAB submitted to Google Play.",
 "days":[
  {"d":36,"name":"Day 36","title":"App Icon + Screenshots + Store Listing",
   "dev":[
    {"t":"Create all app store assets: app icon (1024x1024 PNG, V+arrow on navy from Canva), splash screen (2048x2732 PNG, navy bg + centered logo), Android adaptive icon (1024x1024 foreground only, transparent bg). Verify all are at correct dimensions before setting up app.json. Run npx expo start to confirm icon appears correctly in Expo Go.","m":"45"},
    {"t":"Build 'Delete Account' fully in the app (required by Apple, good practice for Google): Profile → Settings → 'Delete my account and all data' → confirmation dialog → delete all user data from all tables → sign out → navigate to welcome. Also add the consent tracking column (consent_given_at) and the in-app consent modal before this phase.","m":"60"},
    {"t":"Take screenshots on phone via Expo Go on the 5 key screens. In Canva: add phone frames + benefit caption on each. Write Google Play short description (80 chars) and full description (4000 chars, keyword-rich). Create the feature graphic (1024x500 navy banner with logo + tagline).","m":"60"}],
   "gstack":[
    {"t":"[GSTACK /qa] Final QA pass before store submission. This is your acceptance test. The skill tests: the complete user journey from install to first generated resume, all error states, all empty states, the delete account flow, performance on web. No failures allowed before submitting to Google Play.","m":"60"}],
   "security":[
    {"t":"[SECURITY] Pre-submission security checklist: run npm audit → 0 Critical/High vulnerabilities, /cso report → 0 Critical/High findings, RLS test → users cannot access each other's data, delete account → all data removed, API keys → none in code or git history, input validation → all fields have max length limits. ALL must pass before submission.","m":"30"}],
   "learn":[
    {"t":"Read: play.google.com/about/developer-content-policy (20 min). Specific sections relevant to Vaulty: Personal and Sensitive User Data (your privacy policy must match actual data practices), User Data (explain exactly what you collect and why), Deceptive Behavior (your match score and resume quality claims must be accurate). Review your store listing against these policies.","m":"20"}]},

  {"d":37,"name":"Day 37","title":"Google Play Submission",
   "dev":[
    {"t":"Pay $25 Google Play registration. Create developer account. Create app listing. Fill Dashboard checklist: App access (all features accessible to reviewers, provide test credentials), Ads (none), Content rating questionnaire, Target audience (13+, Education category), Data safety (declare all data types you collect — be thorough, Google audits this).","m":"60"},
    {"t":"Build production AAB: eas build --platform android --profile production. Upload to Play Console → Internal Testing → create release → submit. Add 5 internal testers. Let them test for 48 hours minimum. Watch Sentry for production-specific crashes (production builds behave slightly differently from preview APKs).","m":"30"},
    {"t":"After 48-hour internal test: Play Console → Production → Create new release → upload AAB → review → Start rollout. Google review: 3-7 days typically. You cannot speed this up. Prepare launch content while waiting.","m":"20"}],
   "gstack":[
    {"t":"[GSTACK /document-release] Create the official v1.0 release document: what features are in this release, what is explicitly not in v1.0, known limitations, how to report bugs, what is coming in v1.1. This is published as CHANGELOG.md in your GitHub repo. Professional practice that also helps users understand what to expect.","m":"20"},
    {"t":"[GSTACK /ship] Run /ship to create a proper PR, run final checks, and document the release. The skill ensures: tests pass, no uncommitted changes, branch is merged cleanly, release tag is created. After /ship: your GitHub shows a clean v1.0.0 tag with the production-ready code.","m":"20"}],
   "security":[
    {"t":"[SECURITY] Before production submission: verify your app.json android.permissions list includes ONLY what you need (INTERNET for API calls, likely nothing else). Every extra permission triggers user suspicion and App Store review scrutiny. Remove CAMERA, LOCATION, MICROPHONE, CONTACTS if they appear — Vaulty does not need them.","m":"10"}],
   "learn":[
    {"t":"Read: developer.android.com/distribute/best-practices/launch (15 min). Read: support.google.com/googleplay/android-developer/answer/9999779 (data safety section, 15 min). The Data Safety form in Google Play Console requires you to declare every data type you collect. If your declaration does not match your actual behavior, Google can suspend your app. Fill it accurately.","m":"30"}]},

  {"d":38,"name":"Day 38","title":"Apple App Store (If Available)",
   "dev":[
    {"t":"If your university has an Apple Developer membership: request student access. If not: continue iOS distribution via Expo Go QR until you have revenue for the $99/year fee. iOS is secondary to Android for your Egyptian university target market. Do not delay Google Play submission for iOS readiness.","m":"15"},
    {"t":"If Apple access available: eas build --platform ios --profile production → eas submit --platform ios. Apple review: 24-48 hours typically. Apple requirements beyond Google: no external payment prompts without in-app purchase integration (your upgrade prompt showing 80 EGP may trigger review — phrase it as 'Premium coming soon' to avoid this issue).","m":"0"}],
   "gstack":[],
   "security":[],
   "learn":[
    {"t":"Read: developer.apple.com/app-store/review/guidelines (skim the relevant sections, 30 min). Key sections for Vaulty: 1.4 Physical Harm (n/a), 3.1 Payments (the upgrade prompt edge case), 5.1 Privacy (data handling). Most rejections come from 5.1 Privacy (missing delete account) and 3.1 (monetization language). You have addressed both.","m":"30"}]},

  {"d":39,"name":"Day 39","title":"Launch Day",
   "dev":[
    {"t":"When Google Play approval email arrives: download Vaulty from Google Play on your own device. Test the production version completely — every screen, every feature. Confirm it is identical to the beta APK in functionality. Check Sentry for any immediate production errors. Monitor Posthog for first real public users.","m":"30"},
    {"t":"Set up your post-launch monitoring routine: check Sentry every morning, check Posthog DAU and retention weekly, check Datadog edge function uptime daily. Create a Notion page 'Launch Metrics' and record: Day 1 downloads, Day 2 retention, first week active users, upgrade click rate. These numbers become your investor pitch data.","m":"20"}],
   "gstack":[
    {"t":"[GSTACK /retro] After the first week of production: run /retro on the launch. Questions: what was different about production users vs beta users, what monitoring alert fired that you did not expect, what feature usage pattern surprised you, what would you do differently if launching again. The retro shapes your Month 2 roadmap.","m":"20"}],
   "security":[
    {"t":"[SECURITY] Post-launch security monitoring: set up a Datadog alert for unusual API call patterns (e.g. same IP calling generate endpoint 50+ times in an hour — rate limiting bypass attempt). Set up a Sentry alert for auth-related errors. Security incidents do not announce themselves — you have to watch for them.","m":"15"}],
   "learn":[
    {"t":"Read: andrewchen.com/how-to-build-a-product-roadmap (20 min). After launch, you have real user data for the first time. Understanding how to prioritize your roadmap based on retention data (fix what causes churn first), engagement data (double down on most-used features), and user feedback (weight by frequency and severity) is the skill that determines Vaulty's trajectory.","m":"20"}]},

  {"d":40,"name":"Day 40","title":"Phase 2 Planning",
   "dev":[
    {"t":"Open Notion Task Backlog → create Phase 2 features based on: beta feedback, launch data, /retro outputs. Likely top Phase 2 features: (1) embedding-based achievement matching (pgvector + Gemini text-embedding-004 — the column already exists), (2) career advisory gap analysis, (3) chat-style achievement input, (4) achievement reminder notifications via Resend. Prioritize by impact on Day 7 retention.","m":"45"},
    {"t":"Plan the embedding implementation for Phase 2: when a user adds an achievement → call Gemini text-embedding-004 model → store 768-dimension vector in achievements.embedding column. When generating a resume → embed the JD → SELECT achievements ORDER BY embedding <=> jd_embedding LIMIT 15. This gives you semantic matching (finds relevant achievements even with different vocabulary).","m":"25"}],
   "gstack":[
    {"t":"[GSTACK /office-hours] Run /office-hours for Phase 2 planning. Describe what you learned from beta and launch. The skill will challenge: are you building the right Phase 2 features, is the embedding matching feature actually the highest leverage improvement, what assumptions from Phase 1 turned out to be wrong. Start Phase 2 from the right foundation.","m":"30"},
    {"t":"[GSTACK /autoplan] Run /autoplan on the Phase 2 feature set. This chains CEO review (is this the right strategy) + eng review (is this the right architecture) + design review (are the screens planned correctly). Invest this planning time before Phase 2 code — you will build faster and make fewer architectural mistakes.","m":"45"}],
   "security":[
    {"t":"[SECURITY] Phase 2 security planning: the embedding feature stores AI-generated vectors alongside achievement text. Threat: could vectors leak information about the original text? (Technically possible but practically negligible for this use case.) Plan: when a user deletes an achievement, also null out the embedding column. When a user deletes their account, all embedding data is deleted with the achievement rows (CASCADE DELETE).","m":"15"}],
   "learn":[
    {"t":"Read: supabase.com/blog/pgvector-vs-pinecone (20 min). This explains when to use pgvector (your use case: moderate scale, existing Postgres database) vs dedicated vector databases like Pinecone (large scale, billions of vectors). You are in pgvector territory for Phase 2. Also read: supabase.com/docs/guides/ai/vector-columns (15 min) for the exact implementation you planned above.","m":"35"},
    {"t":"This is the end of the core development plan. Review everything you built: a production mobile app with enterprise-grade security (/cso verified), real AI features (Gemini), analytics (Posthog), monitoring (Datadog + Sentry), and GStack-reviewed code quality throughout. The journey from Day 1 to Day 40 is the foundation. Phase 2 is where you grow it.","m":"0"}]}
 ]}

]

# ─── OUTPUT DIR ──────────────────────────────────────────────────────────────
OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ─── CSS ─────────────────────────────────────────────────────────────────────
CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:-apple-system,BlinkMacSystemFont,'DM Sans',sans-serif;background:#F8F5EE;color:#111827;line-height:1.5;font-size:14px}
.hdr{background:#0D1F4E;padding:16px 16px 0;position:sticky;top:0;z-index:100;box-shadow:0 2px 12px rgba(13,31,78,0.3)}
.hdr-top{display:flex;align-items:center;justify-content:space-between;margin-bottom:10px}
.hdr-title{font-size:15px;font-weight:700;color:#fff}
.hdr-pct{font-size:12px;color:rgba(255,255,255,0.55);font-weight:600}
.pbar{height:3px;background:rgba(255,255,255,0.12);border-radius:2px;margin-bottom:10px}
.pbar-fill{height:100%;background:#C9A84C;border-radius:2px;transition:width .4s}
.ptabs{display:flex;gap:0;overflow-x:auto;scrollbar-width:none}
.ptabs::-webkit-scrollbar{display:none}
.ptab{flex-shrink:0;padding:8px 11px;font-size:11px;font-weight:700;color:rgba(255,255,255,0.45);cursor:pointer;border:none;background:none;border-bottom:2px solid transparent;transition:all .2s;text-transform:uppercase;letter-spacing:.06em;white-space:nowrap}
.ptab.on{color:#C9A84C;border-bottom-color:#C9A84C}
.ptab:hover:not(.on){color:rgba(255,255,255,.75)}
.main{max-width:760px;margin:0 auto;padding:18px 14px 80px}
.psec{display:none}.psec.on{display:block}
.phdr{background:#0D1F4E;border-radius:12px;padding:16px 18px;margin-bottom:14px}
.pbadge{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:#C9A84C;margin-bottom:3px}
.ptitle{font-size:17px;font-weight:700;color:#fff;margin-bottom:3px}
.pdur{font-size:11px;color:rgba(255,255,255,.4);margin-bottom:4px}
.pgoal{font-size:12px;color:rgba(255,255,255,.6);line-height:1.5}
.pbar2{height:3px;background:rgba(201,168,76,.2);border-radius:2px;margin-top:10px}
.pbar2-fill{height:100%;background:#C9A84C;border-radius:2px;transition:width .4s}
.ppct{font-size:10px;color:rgba(255,255,255,.4);margin-top:5px;text-align:right}
.dcard{background:#fff;border-radius:12px;margin-bottom:8px;overflow:hidden;border:1px solid #E5E7EB}
.dcard.done-all{border-color:#A7F3D0}
.dhdr{padding:12px 14px;cursor:pointer;display:flex;align-items:center;gap:10px;user-select:none}
.dhdr:hover{background:#F9FAFB}
.dnum{width:30px;height:30px;border-radius:8px;background:#0D1F4E;color:#C9A84C;font-size:12px;font-weight:700;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.dcard.done-all .dnum{background:#059669;color:#fff}
.dinfo{flex:1;min-width:0}
.dday{font-size:10px;font-weight:700;color:#9CA3AF;text-transform:uppercase;letter-spacing:.06em}
.dtitle{font-size:13px;font-weight:600;color:#111827}
.dtag{font-size:10px;font-weight:700;color:#059669;background:#D1FAE5;padding:2px 8px;border-radius:20px}
.dchev{font-size:18px;color:#D1D5DB;transition:transform .2s;margin-left:4px}
.dcard.open .dchev{transform:rotate(180deg)}
.dbody{display:none;padding:0 14px 14px;border-top:1px solid #F3F4F6}
.dcard.open .dbody{display:block}
.sec-lbl{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.1em;padding:3px 10px;border-radius:20px;display:inline-block;margin:10px 0 6px}
.lbl-d{background:#DBEAFE;color:#1E40AF}
.lbl-l{background:#D1FAE5;color:#065F46}
.lbl-g{background:#EDE9FE;color:#5B21B6}
.lbl-s{background:#FEE2E2;color:#991B1B}
.titem{display:flex;align-items:flex-start;gap:9px;padding:7px 0;border-bottom:1px solid #F9FAFB}
.titem:last-child{border-bottom:none}
.tcheck{width:17px;height:17px;border-radius:4px;border:1.5px solid #D1D5DB;cursor:pointer;flex-shrink:0;margin-top:1px;appearance:none;-webkit-appearance:none;background:#fff;transition:all .15s;position:relative}
.tcheck:checked{background:#0D1F4E;border-color:#0D1F4E}
.tcheck:checked::after{content:'\\2713';position:absolute;top:0;left:0;right:0;bottom:0;display:flex;align-items:center;justify-content:center;font-size:10px;font-weight:700;color:#C9A84C}
.ttxt{flex:1;font-size:12.5px;color:#374151;line-height:1.55}
.titem.ck .ttxt{text-decoration:line-through;color:#9CA3AF}
.tmin{font-size:10px;color:#9CA3AF;flex-shrink:0;margin-top:2px}
.dact{display:flex;justify-content:space-between;align-items:center;margin-top:10px;padding-top:8px;border-top:1px solid #F3F4F6}
.dact-pct{font-size:11px;color:#6B7280}
.btn-all{font-size:11px;font-weight:600;padding:4px 12px;border-radius:6px;cursor:pointer;border:1px solid #E5E7EB;background:#F9FAFB;color:#374151}
.btn-all:hover{background:#E5E7EB}
.rest{text-align:center;padding:16px;color:#9CA3AF;font-size:12px;font-style:italic}
.today-btn{position:fixed;bottom:18px;right:14px;background:#C9A84C;color:#0D1F4E;border:none;border-radius:20px;padding:9px 16px;font-size:12px;font-weight:700;cursor:pointer;box-shadow:0 4px 14px rgba(201,168,76,0.4);z-index:200}
.legend{display:flex;gap:10px;padding:10px 14px;background:#fff;border-bottom:1px solid #E5E7EB;flex-wrap:wrap}
.leg{display:flex;align-items:center;gap:5px;font-size:11px;font-weight:600}
.leg-dot{width:9px;height:9px;border-radius:3px}
"""

# ─── JS RENDERER (not a template literal — clean string) ──────────────────
RENDERER_JS = r"""

var C = {}, startDay = null;
var SK = 'vp-dev-v1', STK = 'vp-dev-start';
var planData = null;
var STORE = (function() {
  try {
    if (window.storage) return window.storage;
  } catch (e) {}
  try {
    if (typeof localStorage !== 'undefined') {
      return {
        get: async function(key) {
          var value = localStorage.getItem(key);
          return value === null ? null : { value: value };
        },
        set: async function(key, value) {
          localStorage.setItem(key, value);
        }
      };
    }
  } catch (e) {}
  return null;
})();

function init(data) {
  planData = data;
  load().then(render);
}

async function load(){
  try{
    if(STORE){
      const r=await STORE.get(SK);
      if(r)C=JSON.parse(r.value);
      const s=await STORE.get(STK);
      if(s)startDay=new Date(s.value);
    }
  }catch(e){}
}

async function save(id,val){
  C[id]=val;
  try{if(STORE)await STORE.set(SK,JSON.stringify(C));}catch(e){}
  updateProgress();
}

function getId(ph,d,type,i){return 'p'+ph+'d'+d+type+i;}

function countPhase(ph){
  var total=0,done=0;
  ph.days.forEach(function(day){
    ['dev','gstack','security','learn'].forEach(function(t){
      (day[t]||[]).forEach(function(_,i){total++;if(C[getId(ph.ph,day.d,t,i)])done++;});
    });
  });
  return{total:total,done:done};
}

function countAll(){
  var total=0,done=0;
  planData.forEach(function(ph){var c=countPhase(ph);total+=c.total;done+=c.done;});
  return{total:total,done:done};
}

function updateProgress(){
  var all=countAll();
  var pct=all.total?Math.round(all.done/all.total*100):0;
  document.getElementById('total-pct').textContent=pct+'% done';
  document.getElementById('total-bar').style.width=pct+'%';
  planData.forEach(function(ph){
    var w=countPhase(ph);
    var wp=w.total?Math.round(w.done/w.total*100):0;
    var bf=document.getElementById('pbar2-'+ph.ph);
    var pt=document.getElementById('ppct-'+ph.ph);
    if(bf)bf.style.width=wp+'%';
    if(pt)pt.textContent=wp+'% complete';
    ph.days.forEach(function(day){
      var arr=['dev','gstack','security','learn'];
      var dayIds=[];
      arr.forEach(function(t){(day[t]||[]).forEach(function(_,i){dayIds.push(getId(ph.ph,day.d,t,i));});});
      var allDone=dayIds.length>0&&dayIds.every(function(id){return C[id];});
      var dc=document.getElementById('dcard-'+ph.ph+'-'+day.d);
      var db=document.getElementById('dbadge-'+ph.ph+'-'+day.d);
      var da=document.getElementById('dact-'+ph.ph+'-'+day.d);
      var done=dayIds.filter(function(id){return C[id];}).length;
      if(dc)dc.classList.toggle('done-all',allDone);
      if(db)db.style.display=allDone?'':'none';
      if(da)da.textContent=done+' / '+dayIds.length+' tasks done';
    });
  });
}

function switchPhase(ph){
  document.querySelectorAll('.psec').forEach(function(s){s.classList.remove('on');});
  document.querySelectorAll('.ptab').forEach(function(t){t.classList.remove('on');});
  document.getElementById('psec-'+ph).classList.add('on');
  document.getElementById('ptab-'+ph).classList.add('on');
  document.getElementById('psec-'+ph).scrollIntoView({behavior:'smooth',block:'start'});
}

function toggleDay(ph,d){
  document.getElementById('dcard-'+ph+'-'+d).classList.toggle('open');
}

async function markAllDay(ph,d,day){
  var arr=['dev','gstack','security','learn'];
  var ids=[];
  arr.forEach(function(t){(day[t]||[]).forEach(function(_,i){ids.push(getId(ph,d,t,i));});});
  var allDone=ids.every(function(id){return C[id];});
  ids.forEach(function(id){
    C[id]=!allDone;
    var cb=document.getElementById('cb-'+id);
    var item=document.getElementById('item-'+id);
    if(cb)cb.checked=!allDone;
    if(item)item.classList.toggle('ck',!allDone);
  });
  try{if(STORE)await STORE.set(SK,JSON.stringify(C));}catch(e){}
  updateProgress();
}

function goToday(){
  if(!startDay){
    if(confirm('Set today as Day 1 of your Vaulty build journey?')){
      startDay=new Date();
      try{if(STORE)STORE.set(STK,startDay.toISOString());}catch(e){}
    }else return;
  }
  var now=new Date();
  var diff=Math.floor((now-startDay)/(1000*60*60*24));
  var dayNum=Math.min(Math.max(diff+1,1),999);
  var cumDays=0,targetPh=0;
  for(var i=0;i<planData.length;i++){
    var phDays=planData[i].days.length;
    if(dayNum<=cumDays+phDays){targetPh=planData[i].ph;break;}
    cumDays+=phDays;
  }
  switchPhase(targetPh);
  setTimeout(function(){
    var dc=document.getElementById('dcard-'+targetPh+'-'+dayNum);
    if(dc){dc.classList.add('open');dc.scrollIntoView({behavior:'smooth',block:'start'});}
  },300);
}

function render(){
  var tabs=document.getElementById('ptabs');
  var main=document.getElementById('main');
  tabs.innerHTML='';main.innerHTML='';
  var LABELS=['Setup','Backend','Mobile','Vault','Resume','LinkedIn','Security','Beta','Launch'];
  planData.forEach(function(ph,pi){
    var lbl=LABELS[pi]||('P'+ph.ph);
    var tab=document.createElement('button');
    tab.className='ptab'+(pi===0?' on':'');
    tab.id='ptab-'+ph.ph;
    tab.textContent='P'+ph.ph+' '+lbl;
    tab.onclick=function(){switchPhase(ph.ph);};
    tabs.appendChild(tab);
    var sec=document.createElement('div');
    sec.className='psec'+(pi===0?' on':'');
    sec.id='psec-'+ph.ph;
    var h='<div class="phdr">'
      + '<div class="pbadge">Phase '+ph.ph+' \u00b7 '+ph.duration+'</div>'
      + '<div class="ptitle">'+esc(ph.title)+'</div>'
      + '<div class="pgoal">'+esc(ph.goal)+'</div>'
      + '<div class="pbar2"><div class="pbar2-fill" id="pbar2-'+ph.ph+'" style="width:0%"></div></div>'
      + '<div class="ppct" id="ppct-'+ph.ph+'">0% complete</div>'
      + '</div>';
    ph.days.forEach(function(day){
      var allIds=[];
      ['dev','gstack','security','learn'].forEach(function(t){(day[t]||[]).forEach(function(_,i){allIds.push(getId(ph.ph,day.d,t,i));});});
      var hasTasks=allIds.length>0;
      h+='<div class="dcard" id="dcard-'+ph.ph+'-'+day.d+'">'
        + '<div class="dhdr" onclick="toggleDay('+ph.ph+','+day.d+')">'
        + '<div class="dnum">'+day.d+'</div>'
        + '<div class="dinfo">'
        + '<div class="dday">'+esc(day.name)+'</div>'
        + '<div class="dtitle">'+esc(day.title)+'</div>'
        + '</div>'
        + '<div class="dtag" id="dbadge-'+ph.ph+'-'+day.d+'" style="display:none">\u2713 Done</div>'
        + '<div class="dchev">\u203a</div>'
        + '</div>'
        + '<div class="dbody">';
      if(!hasTasks){
        h+='<div class="rest">Rest or catch-up day.</div>';
      }else{
        var secs=[
          {key:'dev',label:'Development',cls:'lbl-d'},
          {key:'gstack',label:'GStack Skill',cls:'lbl-g'},
          {key:'security',label:'Security',cls:'lbl-s'},
          {key:'learn',label:'Learning',cls:'lbl-l'}
        ];
        secs.forEach(function(s){
          var tasks=day[s.key]||[];
          if(!tasks.length)return;
          h+='<div class="sec-lbl '+s.cls+'">'+s.label+'</div><div>';
          tasks.forEach(function(task,i){
            var id=getId(ph.ph,day.d,s.key,i);
            var ck=!!C[id];
            h+='<div class="titem'+(ck?' ck':'')+'" id="item-'+id+'">'
              + '<input type="checkbox" class="tcheck" id="cb-'+id+'"'+(ck?' checked':'')+' onchange="(function(el,id){C[id]=el.checked;document.getElementById(\'item-\'+id).classList.toggle(\'ck\',el.checked);save(id,el.checked);})(this,\''+id+'\')">'
              + '<div class="ttxt">'+esc(task.t)+'</div>'
              +(task.m&&task.m!='0'?'<div class="tmin">'+task.m+'m</div>':'')
              + '</div>';
          });
          h+='</div>';
        });
        h+='<div class="dact">'
          + '<span class="dact-pct" id="dact-'+ph.ph+'-'+day.d+'">0 / '+allIds.length+' tasks done</span>'
          + '<button class="btn-all" onclick="markAllDay('+ph.ph+','+day.d+',planData['+pi+'].days['+ph.days.indexOf(day)+'])">Mark all done</button>'
          + '</div>';
      }
      h+='</div></div>';
    });
    sec.innerHTML=h;
    main.appendChild(sec);
  });
  updateProgress();
}

function esc(s){
  var d=document.createElement('div');
  d.appendChild(document.createTextNode(s));
  return d.innerHTML;
}

"""

# ─── WRITE DATA JSON ────────────────────────────────────────────────────────
def write_data_json(phases):
    data_path = os.path.join(OUT_DIR, 'vaulty-data.json')
    with open(data_path, 'w', encoding='utf-8') as f:
        json.dump(phases, f, ensure_ascii=False, indent=2)
    return data_path

# ─── BUILD HTML ─────────────────────────────────────────────────────────────
def build_html(phases):
    plan_json = json.dumps(phases, ensure_ascii=False)
    plan_safe = plan_json.replace('</script>', '<\\/script>')

    return ('<!DOCTYPE html>\n<html lang="en">\n<head>\n'
        + '<meta charset="UTF-8">\n'
        + '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        + '<title>Vaulty — Development Plan</title>\n'
        + '<style>' + CSS + '</style>\n'
        + '</head>\n<body>\n'
        + '<div class="hdr">\n'
        + '  <div class="hdr-top">\n'
        + '    <div class="hdr-title">Vaulty — Dev Plan \u00b7 GStack \u00b7 Security</div>\n'
        + '    <div class="hdr-pct" id="total-pct">0% done</div>\n'
        + '  </div>\n'
        + '  <div class="pbar"><div class="pbar-fill" id="total-bar" style="width:0%"></div></div>\n'
        + '  <div class="ptabs" id="ptabs"></div>\n'
        + '</div>\n'
        + '<div class="legend">\n'
        + '  <div class="leg"><div class="leg-dot" style="background:#DBEAFE;border:1px solid #93C5FD"></div>Development</div>\n'
        + '  <div class="leg"><div class="leg-dot" style="background:#EDE9FE;border:1px solid #C4B5FD"></div>GStack Skill</div>\n'
        + '  <div class="leg"><div class="leg-dot" style="background:#FEE2E2;border:1px solid #FCA5A5"></div>Security</div>\n'
        + '  <div class="leg"><div class="leg-dot" style="background:#D1FAE5;border:1px solid #6EE7B7"></div>Learning</div>\n'
        + '</div>\n'
        + '<div class="main" id="main"></div>\n'
        + '<button class="today-btn" onclick="goToday()">Today</button>\n'
        + '<script>\n'
        + 'var PLAN_FALLBACK = ' + plan_safe + ';\n'
        + RENDERER_JS + '\n'
        + '(async function boot() {\n'
        + '  try {\n'
        + '    var res = await fetch("./vaulty-data.json");\n'
        + '    var data = await res.json();\n'
        + '    init(data);\n'
        + '  } catch(e) {\n'
        + '    console.warn("fetch failed, using inline fallback", e);\n'
        + '    init(PLAN_FALLBACK);\n'
        + '  }\n'
        + '})();\n'
        + '</script>\n'
        + '</body>\n</html>')

# ─── MAIN ────────────────────────────────────────────────────────────────────
def main():
    json_path = write_data_json(PHASES)
    html_code = build_html(PHASES)

    html_path = os.path.join(OUT_DIR, 'vaulty-dev-plan.html')
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_code)

    json_size = os.path.getsize(json_path)
    html_size = os.path.getsize(html_path)

    print("Written: " + html_path)
    print("Written: " + json_path)
    print("HTML size: " + str(html_size) + " bytes (" + str(html_size // 1024) + " KB)")
    print("JSON size: " + str(json_size) + " bytes (" + str(json_size // 1024) + " KB)")
    print("Phases: " + str(len(PHASES)))
    total_days = sum(len(p['days']) for p in PHASES)
    print("Total days: " + str(total_days))
    total_tasks = sum(
        len(day.get(t, []))
        for p in PHASES for day in p['days']
        for t in ['dev', 'gstack', 'security', 'learn']
    )
    print("Total tasks: " + str(total_tasks))

if __name__ == '__main__':
    main()
