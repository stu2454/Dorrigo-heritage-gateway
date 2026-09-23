# Dorrigo Heritage Gateway — current status

Last verified: 2026-09-23 (Australia/Sydney).
Site/deployment revision: `1a9556fa2036759c551cf7b3d9def1a83c8c6987`.
This snapshot is carried by a subsequent documentation-only commit; use
`git log 1a9556f..HEAD` to identify later changes. No site files changed in that
handover commit, which skips CI to retain the verified deployment revision.

## Verified state

- Repository: https://github.com/stu2454/Dorrigo-heritage-gateway.git
- Branch: main, tracking origin/main. Initial site committed and pushed.
- [Deployment 35820783708](https://github.com/stu2454/Dorrigo-heritage-gateway/actions/runs/35820783708)
  succeeded using the supplied workflow. Pages source is GitHub Actions;
  HTTPS is enforced. No user settings changes are needed.
- [Homepage](https://stu2454.github.io/Dorrigo-heritage-gateway/) and
  [hotel demonstration](https://stu2454.github.io/Dorrigo-heritage-gateway/places/dorrigo-hotel/)
  are publicly live and verified. Concept labels and source links are visible.
- Documentation, preview helper and a mobile layout fix are complete. No feature
  work is in progress. Recheck Git status at the start of the next session.

## Validation of the revision above

Local and live Chrome checks at 320, 390, 768 and 1440 pixels passed both pages:
HTTP 200, images loaded, no horizontal overflow, one h1 per page and en-AU
language. Homepage-to-hotel and return navigation passed at every width.
Keyboard Tab reached the skip link. Axe WCAG 2 A/AA and 2.1 AA checks reported
zero violations. Desktop and mobile screenshots were visually inspected.

All 11 distinct internal URLs, assets and fragment targets passed. Live HTML,
CSS and PNG response bytes matched the committed local site. Apple Vision
independently decoded hotel-qr.png to the exact live hotel URL above; that URL
was opened in the browser checks. All three PNGs match the starter ZIP bytes.
`git diff --check` passed. Validation tools were temporary and add no runtime
or npm dependencies to the project. See README.md for repeatable manual checks.

## Known limitations

- A physical phone-camera scan and full screen-reader audit were not performed.
- Workflow succeeded with a Node.js 20 action-runtime deprecation warning;
  GitHub ran those actions on Node.js 24. Runner image migration was also noted.
  Review upstream action versions in a separate maintenance change.
- Committee/site-owner endorsement, asset credit/licence records and future
  museum-controlled domain arrangements remain unresolved; see PROJECT_BRIEF.md.
- No installation feasibility assessment or physical trail exists.

## One next recommended task

Review the two live pages with the museum committee and record requested edits,
asset credits and permission decisions before expanding the public content.
Complete when the review outcome and unresolved permissions are documented.
Status: recommended only; not authorised implementation work.
