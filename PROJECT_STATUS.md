# Dorrigo Heritage Gateway — current status

Last verified: 2026-09-23 (Australia/Sydney).
Site/deployment revision: `a7f9df2fe57af55e7226214e34073e58a99fb769`.
This snapshot is carried by a subsequent documentation-only commit; use
`git log a7f9df2..HEAD` to identify later changes. No site files changed in that
handover commit, which skips CI to retain the verified deployment revision.

## Verified state

- Repository: https://github.com/stu2454/Dorrigo-heritage-gateway.git
- Branch: main, tracking origin/main. Image update committed and pushed.
- [Deployment 35822217941](https://github.com/stu2454/Dorrigo-heritage-gateway/actions/runs/35822217941)
  succeeded using the supplied workflow. Pages source is GitHub Actions;
  HTTPS is enforced. No user settings changes are needed.
- [Homepage](https://stu2454.github.io/Dorrigo-heritage-gateway/) and
  [hotel demonstration](https://stu2454.github.io/Dorrigo-heritage-gateway/places/dorrigo-hotel/)
  are publicly live and verified. Concept labels and source links are visible.
- The hotel page now includes the 2006 exterior, 2012 verandah and Michael/Elene’s
  1929 wedding portrait, with captions and credits. Permission and licence
  evidence is in [docs/IMAGE_CREDITS.md](docs/IMAGE_CREDITS.md). No feature
  work is in progress. Recheck Git status at the start of the next session.

## Validation of the revision above

Local and live Chrome checks at 320, 390, 768 and 1440 pixels passed both pages:
HTTP 200, images loaded, no horizontal overflow, one h1 per page and en-AU
language. Homepage-to-hotel and return navigation passed at every width.
Keyboard Tab reached the skip link. Axe WCAG 2 A/AA and 2.1 AA checks reported
zero violations. Local desktop and mobile hotel screenshots were visually
inspected, including the wedding portrait framing.

All 14 distinct internal URLs, assets and fragment targets passed. Live HTML,
CSS and image response bytes matched the committed local site. The unchanged QR was previously independently decoded by Apple Vision; it
decoded hotel-qr.png to the exact live hotel URL above; that URL
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
