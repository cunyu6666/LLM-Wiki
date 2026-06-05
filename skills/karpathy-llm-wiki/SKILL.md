---
name: karpathy-llm-wiki
description: "Use when building or maintaining a personal LLM-powered knowledge base. Triggers: ingesting sources into a wiki, querying wiki knowledge, linting wiki quality, farming data sources, scheduling wiki tasks, 'add to wiki', 'what do I know about', or any mention of 'LLM wiki' or 'Karpathy wiki'."
---

# Karpathy LLM Wiki

Build and maintain a personal knowledge base using LLMs. You manage two directories: `raw/` (immutable source material) and `wiki/` (compiled knowledge articles). Sources go into raw/, you compile them into wiki articles, and the wiki compounds over time.

Core ideas from Karpathy:
- "The LLM writes and maintains the wiki; the human reads and asks questions."
- "The wiki is a persistent, compounding artifact."

## Architecture

Four layers, all under the user's project root:

**raw/** — Immutable source material. You read, never modify. Organized by topic subdirectories (e.g., `raw/machine-learning/`).

**wiki/** — Compiled knowledge articles. You have full ownership. Organized by topic subdirectories, one level only: `wiki/<topic>/<article>.md`. Contains two special files:
- `wiki/index.md` — Global index. One row per article, grouped by topic, with link + summary + Updated date.
- `wiki/log.md` — Append-only operation log.

**SKILL.md** (this file) — Schema layer. Defines structure and workflow rules.

**MCP integration** (optional) — External data sources connected via MCP servers. When configured, Farmer agents use MCP tools to fetch data from APIs, websites, YouTube, RSS feeds, and other platforms. MCP server configurations live in the project's MCP settings (e.g., `.mcp.json` or Claude Code MCP config).

Templates live in `references/` relative to this file. Read them when you need the exact format for raw files, articles, archive pages, or the index.

---

## Setup

Interactive initialization wizard. Triggers on first use or when the user says "setup wiki" / "init wiki". Two modes:

### Quick Build

Create directory structure only. Skip the interview.

- `raw/` directory (with `.gitkeep`)
- `wiki/` directory (with `.gitkeep`)
- `wiki/index.md` — heading `# Knowledge Base Index`, empty body
- `wiki/log.md` — heading `# Wiki Log`, empty body

### Full Build (recommended)

Interview the user one question at a time, then generate the full project scaffold.

**Interview questions (ask sequentially, one at a time):**

1. **Topic / Domain** — "What is this wiki about? Describe your domain or field of interest."
   - Examples: AI research, content creation, competitive analysis, personal learning, academic papers

2. **Data Sources** — "Where will you get your sources from?"
   - Options: web URLs, local files, YouTube channels, RSS feeds, API endpoints, MCP-connected services, pasted text
   - If MCP sources are mentioned, ask which MCP servers to configure

3. **Directory Buckets** — "How do you want to organize topics?"
   - Suggest subdirectories based on their domain answer
   - Example for content creation: `competitors/`, `trending/`, `my-channel/`, `synthesis/`
   - Example for research: `papers/`, `tools/`, `concepts/`, `people/`
   - User can customize; one level deep only

4. **Page Types** — "What kinds of wiki pages do you expect?"
   - Suggest page types based on domain
   - Example: overview pages, deep-dive analysis, comparison tables, trend reports, weekly summaries

5. **Scheduling** — "Do you want automated data farming? If yes, how often?"
   - Options: manual only, daily, weekly, custom cron
   - If automated: ask which sources to farm on schedule

6. **Git Tracking** — "Do you want automatic git commits after each wiki operation?"
   - If yes: auto-commit with structured messages after ingest/lint/farm operations

**After the interview:**

1. Create all directories from question 3 under both `raw/` and `wiki/`
2. Create `wiki/index.md` with topic sections from question 3
3. Create `wiki/log.md`
4. If scheduling was requested, set up cron tasks (see Schedule section)
5. If git tracking was requested, initialize git if needed and enable auto-commit
6. Present the full structure to the user for approval before proceeding

### Domain Presets

When the user's domain matches a preset, offer it as a starting template:

**Content Creation / YouTube Research:**
- Buckets: `competitors/`, `trending/`, `my-channel/`, `synthesis/`
- Page types: channel overview, video deep-dive, trend analysis, weekly synthesis
- Typical sources: YouTube URLs, VidIQ MCP, social media APIs

**Technical Research:**
- Buckets: `papers/`, `tools/`, `concepts/`, `people/`
- Page types: paper summary, tool comparison, concept explainer, researcher profile
- Typical sources: arXiv, GitHub, blog posts, documentation

**Academic / Literature Review:**
- Buckets: `papers/`, `methods/`, `datasets/`, `findings/`
- Page types: paper review, methodology comparison, dataset catalog, literature synthesis
- Typical sources: PDFs, journal articles, conference proceedings

**Personal Knowledge / Learning:**
- Buckets: `books/`, `courses/`, `articles/`, `reflections/`
- Page types: book notes, course summary, article digest, learning journal
- Typical sources: Kindle highlights, course notes, bookmarks, blog posts

Presets are starting points — the user can always customize during the interview.

---

## Farm

Automated batch fetching of content from configured data sources into `raw/`. Runs Farmer sub-agents in parallel, each responsible for one source type.

### Triggers
- `/wiki farm` or `/wiki farm all` — farm all configured sources
- `/wiki farm <source-name>` — farm a specific source (e.g., `/wiki farm my-channel`)
- `/wiki farm --last N days` — limit to content from the last N days

### Farmer Agents

Each data source gets its own Farmer agent. Define Farmers in `wiki/farmers.md` (created during Setup if Farm is enabled):

```markdown
# Farmer Agents

## my-channel
- Source type: youtube (via MCP)
- MCP server: vidiq
- Target: raw/my-channel/
- Fetch: channel videos, metadata, analytics

## competitors
- Source type: youtube (via MCP)
- MCP server: vidiq
- Target: raw/competitors/
- Fetch: channel list from competitors.txt, split into parallel batches

## tech-news
- Source type: web
- URLs: [RSS feed URLs or website URLs]
- Target: raw/tech-news/
- Fetch: latest articles, full text extraction
```

### Execution Flow

1. Read `wiki/farmers.md` to identify which Farmers to run
2. For each active Farmer, spawn a sub-agent with the Farmer's configuration
3. Sub-agents run in parallel, each fetching data into its assigned `raw/` subdirectory
4. Each sub-agent saves fetched content following raw-template.md format
5. After all Farmers complete, automatically trigger **Ingest** on all new raw files
6. Log the farm operation to `wiki/log.md`:

```
## [YYYY-MM-DD] farm | <source-name>
- Fetched: N new files into raw/<topic>/
- Ingested: M articles compiled to wiki/
```

### Batch Processing

When a source has many items (e.g., 50+ YouTube channels):
- Split into batches of ~15 items each
- Distribute batches across parallel sub-agents
- Each sub-agent processes its batch independently
- Results merge into the same raw/ subdirectory

### MCP Integration

When a Farmer requires MCP tools (e.g., VidIQ for YouTube data):
- Verify the MCP server is connected before starting
- If not connected, report which MCP server is needed and how to configure it
- Use MCP tools for data fetching; fall back to web fetch if MCP is unavailable

---

## Ingest

Fetch a source into raw/, then compile it into wiki/. Always both steps, no exceptions.

### Fetch (raw/)

1. Get the source content using whatever web or file tools your environment provides. If nothing can reach the source, ask the user to paste it directly.

2. Pick a topic directory. Check existing `raw/` subdirectories first; reuse one if the topic is close enough. Create a new subdirectory only for genuinely distinct topics.

3. Save as `raw/<topic>/YYYY-MM-DD-descriptive-slug.md`.
   - Slug from source title, kebab-case, max 60 characters.
   - Published date unknown → omit the date prefix from the file name (e.g., `descriptive-slug.md`). The metadata Published field still appears; set it to `Unknown`.
   - If a file with the same name already exists, append a numeric suffix (e.g., `descriptive-slug-2.md`).
   - Include metadata header: source URL, collected date, published date.
   - Preserve original text. Clean formatting noise. Do not rewrite opinions.

   See `references/raw-template.md` for the exact format.

### Batch Ingest

When multiple new files exist in raw/ (e.g., after a Farm operation):
- Process all un-ingested files in one pass
- For each file: Compile → Cascade Updates → move to next
- Run Post-Ingest once at the end (consolidated index and log update)
- `--dry-run`: preview which files would be ingested and what wiki pages would be affected, without writing anything

### Compile (wiki/)

Determine where the new content belongs:

- **Same core thesis as existing article** → Merge into that article. Add the new source to Sources/Raw. Update affected sections.
- **New concept** → Create a new article in the most relevant topic directory. Name the file after the concept, not the raw file.
- **Spans multiple topics** → Place in the most relevant directory. Add See Also cross-references to related articles elsewhere.

These are not mutually exclusive. A single source may warrant merging into one article while also creating a separate article for a distinct concept it introduces. In all cases, check for factual conflicts: if the new source contradicts existing content, annotate the disagreement with source attribution. When merging, note the conflict within the merged article. When the conflicting content lives in separate articles, note it in both and cross-link them.

See `references/article-template.md` for article format. Key points:
- Sources field: author, organization, or publication name + date, semicolon-separated.
- Raw field: markdown links to raw/ files, semicolon-separated.
- Relative paths from `wiki/<topic>/` use `../../raw/<topic>/<file>.md` (two levels up to project root).

### Cascade Updates

After the primary article, check for ripple effects:

1. Scan articles in the same topic directory for content affected by the new source.
2. Scan `wiki/index.md` entries in other topics for articles covering related concepts.
3. Update every article whose content is materially affected. Each updated file gets its Updated date refreshed.

Archive pages are never cascade-updated (they are point-in-time snapshots).

### Post-Ingest

Update `wiki/index.md`: add or update entries for every touched article. When adding a new topic section, include a one-line description. The Updated date reflects when the article's knowledge content last changed, not the file system timestamp. See `references/index-template.md` for format.

Append to `wiki/log.md`:

```
## [YYYY-MM-DD] ingest | <primary article title>
- Updated: <cascade-updated article title>
- Updated: <another cascade-updated article title>
```

Omit `- Updated:` lines when no cascade updates occur.

### Auto-Commit

If git tracking is enabled, after Post-Ingest:
- Stage all changed files (raw/, wiki/)
- Commit with message: `[wiki] ingest: <primary article title>`
- If cascade updates occurred: `[wiki] ingest: <primary article title> (+N cascade updates)`

---

## Query

Search the wiki and answer questions. Examples of triggers:
- "What do I know about X?"
- "Summarize everything related to Y"
- "Compare A and B based on my wiki"

### Steps

1. Read `wiki/index.md` to locate relevant articles.
2. Read those articles and synthesize an answer.
3. Prefer wiki content over your own training knowledge. Cite sources with markdown links: `[Article Title](wiki/topic/article.md)` (project-root-relative paths for in-conversation citations; within wiki/ files, use paths relative to the current file).
4. Output the answer in the conversation. Do not write files unless asked.

### Archiving

When the user explicitly asks to archive or save the answer to the wiki:

1. Write the answer as a new wiki page. See `references/archive-template.md`. When converting conversation citations to the archive page, rewrite project-root-relative paths (e.g., `wiki/topic/article.md`) to file-relative paths (e.g., `../topic/article.md` or `article.md` for same-directory).
   - Sources: markdown links to the wiki articles cited in the answer.
   - No Raw field (content does not come from raw/).
   - File name reflects the query topic, e.g., `transformer-architectures-overview.md`.
   - Place in the most relevant topic directory.
2. Always create a new page. Never merge into existing articles (archive content is a synthesized answer, not raw material).
3. Update `wiki/index.md`. Prefix the Summary with `[Archived]`.
4. Append to `wiki/log.md`:
   ```
   ## [YYYY-MM-DD] query | Archived: <page title>
   ```

---

## Lint

Quality checks on the wiki. Two categories with different authority levels.

### Deterministic Checks (auto-fix)

Fix these automatically:

**Index consistency** — compare `wiki/index.md` against actual wiki/ files (excluding index.md and log.md):
- File exists but missing from index → add entry with `(no summary)` placeholder. For Updated, use the article's metadata Updated date if present; otherwise fall back to file's last modified date.
- Index entry points to nonexistent file → mark as `[MISSING]` in the index. Do not delete the entry; let the user decide.

**Internal links** — for every markdown link in wiki/ article files (body text and Sources metadata), excluding Raw field links (validated by Raw references below) and excluding index.md/log.md (handled above):
- Target does not exist → search wiki/ for a file with the same name elsewhere.
  - Exactly one match → fix the path.
  - Zero or multiple matches → report to the user.

**Raw references** — every link in a Raw field must point to an existing raw/ file:
- Target does not exist → search raw/ for a file with the same name elsewhere.
  - Exactly one match → fix the path.
  - Zero or multiple matches → report to the user.

**See Also** — within each topic directory:
- Add obviously missing cross-references between related articles.
- Remove links to deleted files.

### Heuristic Checks (report only)

These rely on your judgment. Report findings without auto-fixing:

- Factual contradictions across articles
- Outdated claims superseded by newer sources
- Missing conflict annotations where sources disagree
- Orphan pages with no inbound links from other wiki articles
- Missing cross-topic references
- Concepts frequently mentioned but lacking a dedicated page
- Archive pages whose cited source articles have been substantially updated since archival

### Post-Lint

Append to `wiki/log.md`:

```
## [YYYY-MM-DD] lint | <N> issues found, <M> auto-fixed
```

If git tracking is enabled:
- Stage all changed files
- Commit with message: `[wiki] lint: <N> issues found, <M> auto-fixed`

---

## Schedule

Automated recurring tasks using cron scheduling. Manages Farm and Ingest operations on a schedule.

### Triggers
- "Schedule wiki farm every Monday at 2am"
- "Set up daily ingest"
- "List my wiki schedules"
- "Remove the weekly farm schedule"

### Adding a Schedule

When the user requests a recurring task:

1. Determine the operation (farm, ingest, lint) and cron expression
2. Use the CronCreate tool to register the task
3. Log the schedule to `wiki/log.md`:
   ```
   ## [YYYY-MM-DD] schedule | Added: <description> (<cron expression>)
   ```

### Common Schedules

| Use Case | Cron Expression | Description |
|----------|----------------|-------------|
| Daily morning ingest | `3 8 * * *` | Farm + ingest every day at 8:03am |
| Weekly Monday summary | `0 2 * * 1` | Full farm every Monday at 2am |
| Weekday check | `30 9 * * 1-5` | Farm news sources on weekdays at 9:30am |

### Managing Schedules

- **List**: Show all active wiki-related cron tasks
- **Remove**: Delete a specific schedule by ID or description
- **Pause**: Temporarily disable without deleting (if supported by the cron tool)

### Schedule + Farm Integration

When a scheduled farm runs:
1. Execute the Farm operation for the configured sources
2. Auto-ingest all new raw files
3. Auto-commit if git tracking is enabled
4. Log the complete operation to `wiki/log.md`

---

## Conventions

- Standard markdown with relative links throughout.
- wiki/ supports one level of topic subdirectories only. No deeper nesting.
- Today's date for log entries, Collected dates, and Archived dates. Updated dates reflect when the article's knowledge content last changed. Published dates come from the source (use `Unknown` when unavailable).
- Inside wiki/ files, all markdown links use paths relative to the current file. In conversation output, use project-root-relative paths (e.g., `wiki/topic/article.md`).
- Ingest updates both `wiki/index.md` and `wiki/log.md`. Archive (from Query) updates both. Lint updates `wiki/log.md` (and `wiki/index.md` only when auto-fixing index entries). Farm updates `wiki/log.md`. Plain queries do not write any files.
- Git commit messages follow the format: `[wiki] <action>: <description>`
- Farmer configurations are defined in `wiki/farmers.md`, created during Setup.
- Schedule configurations are managed via cron tasks and logged to `wiki/log.md`.
