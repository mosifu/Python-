---
name: code-quality-patterns
description: Recurring code quality issues observed across the learner's example files
metadata:
  type: feedback
---

Recurring code quality patterns observed in the learner's example .py files:

1. **Missing type hints in Stage 3 code**: Despite learning type annotations in Stage 2.5 (07-27), both Stage 3 code files (07-28/07-29) have zero type hints. New stage = dropped habits.
   - **Why:** Learner focuses on new domain concepts and drops syntax-level conventions from prior stages.
   - **How to apply:** Flag missing type hints in every Stage 3+ code review. Remind learner to maintain 2.5 habits.

2. **Note-to-code gap**: Notes sometimes contain more complete implementations than the example code. Example: 3.1 note has full ChatSession with sliding window + token counting, but the .py file only has basic message appending.
   - **Why:** Notes may be written from course content (complete) while code is written from memory/practice (incomplete).
   - **How to apply:** Compare note code blocks against example .py files. Flag gaps as consolidation exercises.

3. **Inconsistent error handling across files**: File 1 (01_调用大模型API.py) has thorough try/except + status code handling (9/10). File 2 (01_提示词工程示例.py) ask() function has zero error handling (5/10). Same day, same learner, big variance.
   - **Why:** Error handling has not yet become "muscle memory" - it's applied when specifically thinking about it.
   - **How to apply:** Check every function that makes network/API calls for exception handling. Note the inconsistency.

4. **Unused imports and PEP 8 violations**: import json/time unused (file 1); import os placed mid-file instead of top (file 1).
   - **Why:** Minor oversights during incremental coding.
   - **How to apply:** Scan imports in every file. Quick check, easy fix.

5. **Redundant conditions**: `if not API_KEY or API_KEY == "":` where `not API_KEY` already covers empty string.
   - **Why:** Over-cautious boolean logic, common in early-stage developers.
   - **How to apply:** Flag redundant boolean conditions when found.

**Positive patterns to reinforce**: Security awareness (env vars for keys from day one), clear code sectioning with `# ===== N. xxx =====` headers, docstrings on all functions, commenting out actual API calls for safe standalone execution.

See [[user-profile]] and [[learning-progress]] for context.
