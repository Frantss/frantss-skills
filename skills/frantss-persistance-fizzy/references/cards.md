# Card mapping and writes

Store one current task/report per card on the configured board. Use the supplied title; a card's number addresses CLI operations, its native ID is separate, and neither replaces the logical UUID/key.
Store the complete caller record in one HTML `<pre>` block whose text is `FRANTSS_RECORD_V1` followed by a newline and compact JSON. HTML-escape JSON when writing; parse text/entities once when reading. JSON strings escape embedded newlines.
Decode from `description_html` using an HTML parser, or the plain-text `description` with the same marker and JSON. Require one block, valid schema/version, common fields (`record_type`, UUID `id`, stable `key`, `title`, integer `revision`, `created_at`, `updated_at`), and caller domain schema. Accept only task/report; unsupported/malformed marked cards remain unchanged and make coverage incomplete.
Preserve JSON types, nulls, date precision, unknown fields, human content outside the block, and supplied relationship IDs/project strings. Source URLs stay direct links. Native columns, tags, assignment, and closed state never override logical fields.
Read native title edits alongside the stored title; reconcile differences before replacing either. Patch only the managed block and requested title, preserving surrounding HTML; updates require `description_html` if human formatting/attachments would otherwise be lost.
Use `card list --board <board> --indexed-by all --all` for all pages and lanes, including closed/postponed cards; then `card show <number>` for complete records. Verify each card's board ID before use.
Filter decoded records by exact type, UUID/key, and caller fields; titles, tags, and full-text search are discovery aids. Scan to completion before declaring absence or creating; inaccessible pages/cards mean incomplete coverage. Apply caller result limits after filtering and report truncation.
Ignore unrelated unmarked cards. Duplicate UUIDs/keys or inconsistent identity matches are conflicts; never choose one silently. Settings/project/source records and archived revisions are unsupported.

## Save and recovery

1. Find by both UUID and key across the board; require one consistent match or verified absence. Reuse identities and the discovered card number on retries.
2. Read the current card, logical revision, and full description. Compare the caller's expected revision; reconcile changed content and preserve human edits. An identical retry changes neither card nor revision.
3. Start revision at 1; increment once per logical change, retaining original creation time. Verify parent task identities/ancestors; reject dangling references/cycles and save parents before children.
4. Serialize writers for this backend. Immediately reread the card and compare title, full description, and revision before replacement; return conflict on change. The CLI provides no atomic compare-and-swap or unique-key enforcement; strict concurrent writes are unsupported, and checks cannot exclude races with other writers.
5. Write UTF-8 HTML to a private temporary file; pass its absolute path with `--description_file`. Create with `card create --board <board> --title <title> --description_file <path>`; update with `card update <number> --title <title> --description_file <path>`. Use scoped CLI flags on both.
6. Read back with `card show <number>` and repeat identity lookup; verify board, title, every decoded field, revision, surrounding human content, and related references. A successful mutation response alone never establishes a verified save.
7. After uncertain creation, scan by UUID/key before retrying; after uncertain update, compare current and intended payloads. Reuse a verified result and retry only missing work with the same identities/revisions.
Related saves form one logical operation without transactions. Return each persisted part, missing step, and recoverable unsaved payload/location; keep recovery files private and remove them after verified completion. Stop after a repeated unresolved conflict/access failure.
Keep one current card, without revision cards/comments. Ordinary saves never close, move, publish, delete, or otherwise modify unrelated native card state.
