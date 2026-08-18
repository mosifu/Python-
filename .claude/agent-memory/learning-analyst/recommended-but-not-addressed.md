---
name: recommended-but-not-addressed
description: Topics recommended in prior reports but not yet addressed in subsequent sessions
metadata:
  type: project
---

Topics recommended as consolidation/next steps that have NOT yet appeared in later sessions. Check these when analyzing new content.

**From 2026-07-27 report (Stage 2 finale)**:
- `__lt__` and sorting linkage - not yet revisited in Stage 3
- Class attribute vs instance attribute shadowing - not yet revisited
- `except` ordering (specific before Exception catch-all) - not yet revisited
- `__all__` role difference in `__init__.py` vs module level - not yet revisited
- `if __name__ == '__main__':` guard habit - **partially addressed**: Stage 3 code files do NOT use this guard (they run top-level code directly)

**From 2026-07-29 analysis (this session)**:
- ChatSession sliding window implementation - recommended as practice exercise, not yet completed
- stream=True response parsing - knowledge gap flagged, to be filled by Streamlit lessons (eps 100-119)
- Summary memory scheme - pseudo-code in notes but never implemented
- Type hints in Stage 3 code - habit dropped, needs conscious restoration
- ask() function error handling - flagged, not yet fixed

**Why:** Tracking recommendations prevents them from being forgotten. If a topic keeps appearing as "recommended but not addressed" across multiple sessions, it may need a dedicated consolidation session.

**How to apply:** At the start of each analysis, check this list against new content. If the learner addressed a previously-recommended topic, acknowledge the follow-through. If still unaddressed after 2+ sessions, escalate the recommendation priority.

See [[learning-progress]] for current stage positioning and [[code-quality-patterns]] for related code issues.
