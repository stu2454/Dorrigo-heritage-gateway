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

## 2026-09-23 — publication verified and handover

Committed and pushed initial release `1a9556fa2036759c551cf7b3d9def1a83c8c6987`
to main. GitHub Actions run 35820783708 completed successfully:
https://github.com/stu2454/Dorrigo-heritage-gateway/actions/runs/35820783708
Pages uses GitHub Actions with HTTPS enforced; no user setting change remains.

Verified both live pages with headless Chrome/Playwright at 320, 390, 768 and
1440 pixels: HTTP 200, no missing images, no horizontal overflow, navigation
in both directions and skip-link keyboard focus passed. Axe WCAG A/AA checks
reported zero violations. Inspected local desktop/mobile screenshots of both
pages and live mobile hotel/desktop homepage screenshots. All 11 internal
URLs/assets/fragments passed and deployed response bytes matched the release.
The supplied QR decoded to the live hotel route (including project prefix),
which browser checks opened successfully. Compared all supplied PNG bytes to
the ZIP: unchanged. Diff whitespace check passed.

Temporary validation commands were `node /private/tmp/dorrigo-browser-check/check.cjs
BASE_URL` and `node /private/tmp/dorrigo-browser-check/links.cjs BASE_URL` with
local and live base URLs; QR decoding used Apple's Vision barcode request.
These temporary tools are not project dependencies. Physical device scanning
and a full screen-reader audit remain unperformed.

The workflow emitted non-blocking action-runtime deprecation and upcoming
Ubuntu runner migration notices. Retained the user's existing workflow for this
release; review action versions separately. Asset permissions/credits and
committee/site-owner review remain open as documented in the brief.

Handover: site committed, pushed and verified deployed at the revision above.
Status/log updates follow in a documentation-only commit with [skip ci], keeping
the verified site deployment unchanged. Next recommendation is committee review
of these two live pages and recording content/asset permission decisions.
