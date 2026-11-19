# Daily Instagram poster brief

Every morning, make one poster for each brand below and show both to the owner for approval. Post only after they reply "ok".

## Brand 1: The Top Tickets (@thetoptickets)
- Business: online tickets for attractions and museums, similar to GetYourGuide or Viator.
- Instagram account id (Windsor.ai `instagram` connector): `17841434441137123`
- Website: thetoptickets.com
- WhatsApp: +33 7 51 13 64 73
- Email: contact@thetoptickets.com
- Logo: `templates/assets/toptickets-logo.png` (coral "T")
- Brand look (keep): logo, navy #14213a + coral #ff6b52 + gold #d9b56a, contact details. Layout A (`templates/toptickets-template.html`, the Musée d'Orsay poster): It has a white header with the big logo and "THE TOP TICKETS", a navy scene with an SVG illustration, the attraction name, 2 benefit badges, a coral "BOOK NOW" button and a coral contact strip at the bottom.
- Products (confirmed by owner): all excursions across Europe, plus guided walking tours. So any well-known European attraction ticket, day trip/excursion or guided walking tour is fair to feature. Examples already confirmed by name: Musée d'Orsay Entry Ticket (instant confirmation, free cancellation), Musée de l'Orangerie tickets.
- Vary the topics: museums, landmarks, day trips, river cruises and guided walking tours, across different European cities.
- Prices: the site shows prices in euros, but they are not known here. Do not put a price unless the owner gives it.

## Brand 2: Z Ocean Tours (@z.ocean_tours)
- Business: complete Europe holiday packages (Asia planned later).
- Instagram account id: `17841452250476808`
- Website: www.z-oceantours.com
- WhatsApp: +33 7 51 13 64 73
- Email: info@zoceantours.com
- Logo: `templates/assets/zocean-logo.jpg`
- Brand look (keep): logo, blue #0a4fd6 + orange #ff6a1a/#ffb000 + yellow #ffd23f, contact details. Layout A (`templates/zocean-template.html`, the Paris + Switzerland poster): The owner liked it because it shows a specific package, duration and an inclusions list. It has a white logo header, a hero illustration with a big package title and a days/nights ribbon, a white "WHAT'S INCLUDED" card with 8 emoji-icon inclusions, a "Perfect for..." line, an orange "GET YOUR QUOTE ON WHATSAPP" button and a blue contact strip.
- The owner said a plain "Europe holiday" poster was boring. Always feature a specific multi-country package with inclusions.

## Design variety and information (owner feedback 2026-11-19: "design or information exact same ban rahe ho, different design, different layout aur more information chahiye, formality mat karo")
- NEVER use the same layout as the previous post of that brand (check the Layout column in posts-log.md). Brand colours, logo and contact strip stay; the composition must clearly change.
- 2026-11-19: owner saw the layout B samples (samples/ folder) and approved: "ye wale theek lag rahe, more informative hai, aise hi alag alag daily daalne hai". This informative, varied style is now the standard; the daily task prompt's old "same layout and style" wording is superseded by this section.
- Layouts so far (rotate, and add new ones):
  - Top Tickets A: centered circle illustration on navy, big title, 2 badges (`toptickets-template.html`).
  - Top Tickets B: header bar, full-width panorama illustration, cream info area with "Tour highlights" (4 numbered) + "Insider tips" (4) cards, badges + CTA row, navy footer (`toptickets-layout-b-split.html`).
  - Z Ocean A: hero skyline + title + days ribbon, 8-inclusion card (`zocean-template.html`).
  - Z Ocean B: blue top with logo + days/nights, route map of the cities with train/flight links and nights per city, day-by-day itinerary card, 8 inclusion chips, best-season note + CTA (`zocean-layout-b-itinerary.html`).
  - When A and B have both been used recently, design a NEW layout C, D... (e.g. ticket-stub shape, magazine cover, "Top 5 things to do in <city>" list, before/after map, FAQ card, price-from card once owner gives prices), save it to templates/ as `<brand>-layout-<letter>-<name>.html` and add it to this list.
- More information on every poster, not just a title: Top Tickets → what you will see/do (highlights), practical tips (best time, what to bring, how long to plan), why book with us. Z Ocean → day-by-day route, nights per city, 8 inclusions, best season, who it suits. Use well-known general facts only; anything about our product (duration, language, inclusions, cancellation) goes in the "please verify" list.
- Vary fonts too (installed: Inter, DM Sans, Poppins, Montserrat, Bitter, Anton, Archivo Black, Lora, Crimson Text) and the illustration style.
- Captions should also carry more information (highlights, itinerary, tips), not only the poster text.

## LinkedIn (B2B, different from Instagram)
- Pages (Windsor.ai connector `linkedin_organic`): The Top Tickets = `105064529`, Z-Ocean Tours = `90948921`.
- Audience: B2B travel agents, tour operators, DMCs and corporate travel planners, not end travellers. Content must differ from the Instagram post of the day.
- Goal: get agents to partner with us (resell our tickets/tours or packages, ask for agent rates, WhatsApp/email us). The tone is professional and warm, with few emojis and short paragraphs, and it ends with a question or a clear call to action for agents.
- Rotate formats day to day, one LinkedIn post per company per day:
  1. **B2B poster** (1200x1200 JPEG, brand style): e.g. "Partner with The Top Tickets: Europe-wide attraction tickets & guided walking tours for your clients", "Ready-made Paris + Swiss packages for your agency". Post with action `create_image_post` and the raw GitHub image_url.
  2. **Quote card** (1200x1200 JPEG): a short original line about travel or the travel trade (never a copied or attributed quote from a real person), with the logo, plus commentary explaining why it matters for agents. Post with `create_image_post`.
  3. **Story post** (text only, `create_post`): a short, engaging story or insight such as a behind-the-scenes moment, a peak-season tip for agents, a destination trend or a lesson from handling a group booking. Write it as the company's voice, keep it plausible and general, and never invent specific clients, numbers or events as if they really happened.
- Never state commission %, net rates, B2B discounts or partner names unless the owner confirms them. Use "agent rates available on request" instead, and flag anything unconfirmed in the preview.
- Save LinkedIn images under `linkedin/` with the date in the file name and log each LinkedIn post in posts-log.md with the brand "LinkedIn – <company>".

## Stories
- Every approved feed post also goes up as a story. Make the story image with `python3 templates/make_story.py <poster.jpg> stories/<date>-<topic>-story.jpg <topcolor> <bottomcolor>` (Top Tickets: "#24365a" "#ff6b52"; Z Ocean: "#ffb000" "#0a4fd6"), commit it, and publish with action `create_story` and its raw GitHub `image_url` right after the feed post.

## Rules
- Size 1080x1350 JPEG. Render the HTML with Playwright using /usr/bin/google-chrome, then look at the result and fix overlaps before showing it.
- Hosting: commit the JPEG to this repo (`toptickets/` or `zocean/` folder, file name with the date), push to main, and use `https://raw.githubusercontent.com/alizaidiparis/toptickets-posters/main/<path>` as the image_url.
- Never repeat a topic listed in `posts-log.md` until every option has been used.
- Log the layout used in the Layout column of posts-log.md.
- Inclusions, durations and attractions that the owner has not confirmed must be flagged in the preview message as "please verify", so customers are never promised something that is not sold.
- No real photos (photo sites are blocked); use SVG illustrations and emoji.
- Captions are in English, with emojis, contact details, "link in bio" and about 12 hashtags.
- Talk to the owner in Hinglish.
