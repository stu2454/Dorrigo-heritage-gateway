# Dorrigo Heritage Gateway

A small static concept website for discussion of an outdoor museum display and
QR heritage trail. The rendering and trail are illustrative, not an approved
installation or official history trail.

- [Public concept](https://stu2454.github.io/Dorrigo-heritage-gateway/)
- [Hotel demonstration](https://stu2454.github.io/Dorrigo-heritage-gateway/places/dorrigo-hotel/)
- [Current verified status](PROJECT_STATUS.md)
- [Requirements and content permissions](PROJECT_BRIEF.md)
- [Working instructions](AGENTS.md) · [History](DEVLOG.md)

## Run locally in VS Code

Open this repository folder in VS Code. No npm install or build is required.
With Python 3 installed, run in the integrated terminal:

```sh
python3 scripts/serve.py
```

Open http://127.0.0.1:8000/Dorrigo-heritage-gateway/ and test the hotel page at
http://127.0.0.1:8000/Dorrigo-heritage-gateway/places/dorrigo-hotel/.
Stop with Ctrl+C. The helper mounts site/ at the production project path;
opening HTML as a file or serving site/ at the domain root breaks its absolute
asset paths. The QR deliberately opens the public site, even during preview.

## Update and check

Edit site/index.html, site/places/dorrigo-hotel/index.html or site/assets/site.css.
Store cleared assets in site/assets/. Preserve the supplied photograph and
rendering; consult the brief for sourcing and permission rules. Keep concept
labels visible and add source links beside historical claims.

Check both pages directly and through navigation at narrow phone and desktop
widths. Check image loading, no sideways scrolling, keyboard focus/skip link,
headings, contrast and source links. Decode any changed QR image and open the
result; update the displayed full address at the same time. Retain the project
prefix in every internal absolute path. Run `git diff --check`, inspect the diff
and update status/log before committing related changes.

## Deploy and verify

GitHub repository: stu2454/Dorrigo-heritage-gateway. GitHub Settings → Pages →
Source must be **GitHub Actions**. The workflow .github/workflows/pages.yml runs
on main pushes or manual dispatch, uploads site/ without a build and deploys to
the github-pages environment. No project secrets or application environment
variables are required; the workflow uses GitHub's supplied token and OIDC.

```sh
git push origin main
gh run list --workflow pages.yml --limit 5
gh run view RUN_ID
```

Wait for the matching commit's deployment to succeed, then open both public
URLs above, follow navigation, inspect desktop/mobile layouts and load assets.
Compare live bytes to the checked-out site when identifying the deployed
revision. Record the commit and workflow URL in PROJECT_STATUS.md. A successful
push is not deployment verification. Only site/ is uploaded; root docs remain
in the repository. GitHub Pages and Google Fonts are external dependencies;
fallback fonts allow reading if Google Fonts is unavailable.

For rollback, revert the specific faulty commit with `git revert COMMIT`, review,
push main and verify the new deployment. Preserve history; never force-push.
