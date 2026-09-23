# Development log

## 2026-09-23 — establish the initial concept release

Inspected the empty workspace and remote: no existing commits or working site;
Pages API returned 404. Cloned the authorised remote and unpacked the supplied
Dorrigo_Heritage_Gateway_GitHub_Pages.zip without overwriting files. Adapted the
supplied PROJECT_STARTER_TEMPLATE.md principles to this small static project.

Established shared instructions, Claude entry point, brief, status and operating
guide. Kept the HTML/CSS stack and supplied workflow. Added a standard-library
preview server to reproduce the GitHub project path. Retained all supplied PNGs.
Corrected the displayed QR address to include the host and project prefix,
clarified the planned Great Walk route and the heritage announcement date,
and linked the hotel's contact page for the address.

Verified primary sources on 2026-09-23: NSW heritage announcement (14 May 2026),
NSW Great Walk route description and hotel contact page. Visually compared the
museum photograph and rendering: central noticeboard position is retained.
Initial state: local only; remaining browser/QR/deployment checks are recorded
in the subsequent handover entry when complete.

Local release checks: decoded supplied QR with Apple Vision to the exact live
hotel URL. Chrome checks at 320, 390, 768 and 1440 pixels found a starter CSS
percentage row-gap that overlapped the hotel footer on mobile. Replaced it with
32px row spacing, kept article-before-aside reading order and added explicit
focus outlines/anchor clearance. Rerun passed both pages at all four widths:
HTTP 200, images loaded, no horizontal overflow, navigation and keyboard skip
focus worked, and axe WCAG A/AA checks reported zero violations. Visually
reviewed desktop homepage and mobile hotel screenshots. Automated checks do
not replace a physical phone scan or full screen-reader audit.

Enabled GitHub Pages with build_type=workflow and HTTPS enforced under the
requester's initial publication authorisation. Public deployment remains pending.
