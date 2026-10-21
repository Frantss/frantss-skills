# Shared configuration directory

Create or reuse the selected `.frantss` directory; preserve unselected configuration files and reject escaping paths or symlinks.
Preserve the workspace's existing `.gitignore` content and unrelated files.
Inside Git, run `git ls-files -- .frantss` before writing configuration.
If entries are tracked, stop config writes; ignoring does not untrack them. Request explicit index cleanup separately.
Ensure a local effective `/.frantss/` rule exists, even when global ignores apply; append it only when needed.
Insert a separator newline if existing content has no final newline; reruns must not keep appending effective rules.
In Git, verify with `git check-ignore --no-index --quiet -- .frantss/.ignore-check`; create no probe file.
Outside Git, retain the local rule and report Git verification as unavailable.
