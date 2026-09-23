# Dorrigo Heritage Gateway — project brief

## Purpose and users

Explore the prominently situated Dorrigo Museum as a Heritage Gateway: an
interactive outdoor display in the existing central noticeboard position,
a museum website and a small trail of QR markers at selected historic places.
The present website is a concept for committee members, local partners and
potential funders. A public visitor experience is a longer-term goal.
Use clear Australian English, accessible layouts and mobile-first QR journeys.

## Visitor journey

Encounter a story at the museum, follow it to a historic place, then discover
related objects and records in the museum collection. The first release
illustrates this journey; it does not provide an approved installation or an
official published history trail. No markers or display have been installed.

## First release and acceptance

- Homepage explains the gateway and shows the display in the central noticeboard
  position, distinguishing the original photograph from the artist's rendering.
- Heritage Hotel Dorrigo demonstration opens directly and through navigation.
- Its QR image decodes to https://stu2454.github.io/Dorrigo-heritage-gateway/places/dorrigo-hotel/.
- Both deployed pages, internal links, images and styles work on desktop and mobile.
- Historical claims have visible sources and concept material is clearly labelled.
- Existing GitHub Actions workflow publishes site/ from main; verify the actual
  live homepage and hotel page after deployment.
- Durable working instructions, brief, status, log and operating guide support
  future sessions without access to the original conversation.

## Technical context

Repository: https://github.com/stu2454/Dorrigo-heritage-gateway.git
Public base: https://stu2454.github.io/Dorrigo-heritage-gateway/
Static HTML/CSS in site/; .github/workflows/pages.yml uploads that directory.
No build, backend, accounts, database or user-generated data. CSS uses Google
Fonts with local font fallbacks. Python 3 is only a local preview convenience.
The starter ZIP supplied the initial site because the remote repository was empty.

## Assets and content permissions

- site/assets/museum-current.png: supplied museum photograph; retain unchanged.
  Photographer, date, attribution and documented licence are not yet recorded.
- site/assets/museum-concept.png: supplied illustrative rendering based on the
  photograph, showing a display in the central noticeboard position. It is not a
  construction design; pictured content and landscaping are illustrative.
- site/assets/hotel-qr.png: demonstration QR to the live hotel page. Keep its
  destination and displayed address consistent. Prefer a stable museum-controlled
  route in future; domain control and redirect policy remain undecided.
- Initial publication of supplied concept assets is authorised by the requester.
  Do not infer broader reuse rights. Review museum records, donor conditions,
  copyright, privacy and site-owner permission before new public material is final.
- Verify dimensions, wall suitability, access, power, weather protection and
  permissions before producing an installation specification.
- First Nations cultural content requires development with appropriate
  Gumbayngirr representatives and permissions.
- Cite primary sources. The hotel demonstration uses the NSW Government's
  14 May 2026 heritage announcement; location comes from the hotel's contact page.
  Interpretation, proposed markers, routes and collection connections remain examples.

## Milestones and deferred work

1. Publish and verify this two-page concept and establish durable documentation.
2. Seek committee feedback on the concept and record asset credits/permissions.
3. Only following a separate decision, scope an approved visitor pilot.

Deferred: installation specifications, physical markers, additional researched
stories, archival media, oral histories, collection links/database, digitisation
workflows, grant budget, display procurement and a production visitor route.
These are discussion topics, not automatic implementation instructions.

## Open decisions

Committee endorsement, hotel/site-owner review, asset credits and documented
permissions, museum-controlled domain/ownership, content review responsibility,
physical feasibility and funding are unresolved. Resolve relevant permissions
before expanding or presenting the concept as an official visitor service.

## Hotel photograph addition — 23 September 2026

Requested scope: add sourced photographs of the hotel and Michael Feros to the
existing hotel demonstration. Use dated captions, accessible alternative text
and visible credits; retain the concept status. Asset sources and reuse evidence
are recorded once in [docs/IMAGE_CREDITS.md](docs/IMAGE_CREDITS.md). The requester
confirmed hotel/family permission for website use of the booklet photographs.
