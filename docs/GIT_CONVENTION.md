# Git Commit & Branch Convention

All projects under this workspace follow this convention.

## Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Header (required)

`<type>(<scope>): <subject>`

- **type**: required, see table below
- **scope**: optional, the module or area affected
- **subject**: 使用中文，必填项，使用祈使语气，全部小写，不加句点，最多 70 个字符

| type       | When to use                              |
|------------|------------------------------------------|
| `feat`     | New feature                              |
| `fix`      | Bug fix                                  |
| `refactor` | Code restructure without behavior change |
| `perf`     | Performance improvement                  |
| `chore`    | Dependencies, CI, config, tooling        |
| `docs`     | Documentation only                       |
| `test`     | Add or update tests                      |
| `style`    | Formatting, whitespace (no logic change) |

### Body (optional)

- Separated from header by a blank line
- Explain **why** the change is needed, not just what changed
- Wrap at 72 characters per line

### Footer (optional)

- `Closes: #<issue>` — auto-close a GitHub issue
- `Refs: #<issue>` — reference without closing
- `BREAKING CHANGE: <description>` — flag incompatible changes

### Examples

```
fix(wechat): 在创建草稿时处理过期的访问令牌

Token cache was not checking expiry correctly, causing 401 errors
when publishing after 2+ hours of idle time.

Closes: #8
```

```
feat(source): 添加 Twitter/X 作为新闻源

Integrate Twitter API v2 to fetch AI-related tweets from curated
accounts. Includes rate limiting and dedup against existing items.

Refs: #12
```

```
chore(deploy): upgrade httpx to 0.28
```

## Branch Naming

```
<type>/<short-description>
```

| type       | Purpose             | Example                      |
|------------|---------------------|------------------------------|
| `feat/`    | New feature         | `feat/add-twitter-source`    |
| `fix/`     | Bug fix             | `fix/json-parse-error`       |
| `refactor/`| Refactoring         | `refactor/split-pipeline`    |
| `chore/`   | Tooling, CI, config | `chore/add-dockerfile`       |
| `docs/`    | Documentation       | `docs/update-readme`         |
| `perf/`    | Performance         | `perf/batch-api-requests`    |

**Rules:**
- All lowercase
- Use `-` to separate words
- Keep it short and descriptive

## Workflow

```bash
# 1. Create branch from main
git checkout -b feat/add-twitter-source

# 2. Develop and commit
git commit -m "feat(source): 添加 Twitter/X 采集器"

# 3. Push
git push -u origin feat/add-twitter-source

# 4. Create PR
gh pr create --title "feat(source): 添加 Twitter/X 采集器" --body "..."

# 5. After merge, clean up
git checkout main && git pull
git branch -d feat/add-twitter-source
```
